#!/usr/bin/env python3
"""Extract a bounded, redacted evidence pack from selected Codex threads.

The source JSONL files are never modified.  The output is a local review
artifact: it keeps direct user messages, assistant summaries, message line
references, and tool-call counts while excluding runtime wrappers and tool
payload bodies by default.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
from collections import Counter
from typing import Any, Iterable


WRAPPER_PREFIXES = (
    "<environment_context>",
    "<external_codex_apps_open_page>",
    "<send_user_message_question_reply>",
    "<turn_aborted>",
    "<system>",
    "<in-app-browser-context",
    "<subagent_notification>",
    "<realtime_delegation>",
    "<heartbeat>",
    "<recommended_plugins>",
    "<codex_internal_context",
)

REDACTION_PATTERNS = (
    (
        re.compile(
            r"(?i)(password|passwd|密码|口令)\s*[:：=]?\s*[^\s,，;；。]+"
        ),
        "[REDACTED_CREDENTIAL]",
    ),
    (
        re.compile(r"(?i)(api[_ -]?key|access[_ -]?token|secret)\s*[:：=]?\s*[^\s,，;；。]+"),
        "[REDACTED_SECRET]",
    ),
    (
        re.compile(r"(?i)(?<![A-Za-z0-9_])(?:sk|ghp|github_pat)-[A-Za-z0-9_-]{10,}(?![A-Za-z0-9_])"),
        "[REDACTED_TOKEN]",
    ),
    # Some older prompts placed a credential directly after an SSH/API
    # connection line without a password label.  These prefixes are kept
    # deliberately narrow to avoid masking ordinary prose.
    (
        re.compile(r"(?i)(?<![A-Za-z0-9_])f3b_[^\s,，;；。]+"),
        "[REDACTED_CREDENTIAL]",
    ),
    (
        re.compile(r"(?i)(?<![A-Za-z0-9_])sk-[^\s,，;；。]+"),
        "[REDACTED_TOKEN]",
    ),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}\b"), "Bearer [REDACTED_TOKEN]"),
    (
        re.compile(r"-----BEGIN [^-]+-----.*?-----END [^-]+-----", re.S),
        "[REDACTED_PRIVATE_KEY]",
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=pathlib.Path, required=True)
    parser.add_argument("--selection", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    parser.add_argument("--max-message-chars", type=int, default=6000)
    return parser.parse_args()


def load_jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def extract_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for block in content:
        if not isinstance(block, dict):
            continue
        value = block.get("text")
        if isinstance(value, str):
            parts.append(value)
    return "\n".join(parts)


def is_wrapper(text: str) -> bool:
    stripped = text.lstrip()
    return any(stripped.startswith(prefix) for prefix in WRAPPER_PREFIXES)


def redact(text: str) -> tuple[str, int]:
    redaction_count = 0
    result = text
    for pattern, replacement in REDACTION_PATTERNS:
        result, count = pattern.subn(replacement, result)
        redaction_count += count
    return result, redaction_count


def resolve_session_file(raw_path: str, codex_home: pathlib.Path) -> pathlib.Path | None:
    candidate = pathlib.Path(raw_path)
    if candidate.exists():
        return candidate
    cleaned = raw_path.replace("\\\\?\\", "")
    candidate = pathlib.Path(cleaned)
    if candidate.exists():
        return candidate
    name = pathlib.Path(raw_path).name
    matches = list((codex_home / "sessions").rglob(name)) + list(
        (codex_home / "archived_sessions").rglob(name)
    )
    return matches[0] if matches else None


def iterate_records(path: pathlib.Path) -> Iterable[tuple[int, dict[str, Any]]]:
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            yield line_number, record


def classify_message(payload: dict[str, Any], text: str) -> tuple[str, str | None]:
    item_type = payload.get("type")
    role = payload.get("role")
    if item_type == "agent_message":
        return "agent", "agent_message"
    if role == "user":
        return ("runtime_wrapper" if is_wrapper(text) else "user_authored"), item_type
    if role == "assistant":
        return "assistant_summary", item_type
    if role == "developer":
        return "developer_context", item_type
    return "other_message", item_type


def collect_thread(
    item: dict[str, Any],
    all_rows: list[dict[str, Any]],
    codex_home: pathlib.Path,
    max_chars: int,
) -> dict[str, Any]:
    thread_id = item["thread_id"]
    files = sorted(item.get("session_files", []), key=lambda x: (x.get("mtime_ns", 0), x.get("path", "")))
    messages: list[dict[str, Any]] = []
    seen_content: set[str] = set()
    role_counts: Counter[str] = Counter()
    item_counts: Counter[str] = Counter()
    tool_names: Counter[str] = Counter()
    redactions = 0
    unreadable_files: list[str] = []

    for file_meta in files:
        path = resolve_session_file(file_meta["path"], codex_home)
        if path is None:
            unreadable_files.append(file_meta["path"])
            continue
        for line_number, record in iterate_records(path):
            if record.get("type") != "response_item":
                continue
            payload = record.get("payload") or {}
            item_type = payload.get("type") or "unknown"
            item_counts[item_type] += 1
            if item_type in {
                "function_call",
                "function_call_output",
                "custom_tool_call",
                "custom_tool_call_output",
                "web_search_call",
                "computer_call",
            }:
                name = payload.get("name") or item_type
                tool_names[str(name)] += 1
                continue
            text = extract_text(payload.get("content"))
            if not text:
                continue
            kind, classified_type = classify_message(payload, text)
            role_counts[kind] += 1
            if kind == "developer_context" or kind == "runtime_wrapper":
                continue
            redacted, count = redact(text)
            redactions += count
            fingerprint = hashlib.sha256(
                (kind + "\n" + redacted).encode("utf-8", errors="replace")
            ).hexdigest()
            if fingerprint in seen_content:
                continue
            seen_content.add(fingerprint)
            truncated = len(redacted) > max_chars
            if truncated:
                redacted = redacted[:max_chars] + "\n[TRUNCATED]"
            messages.append(
                {
                    "ordinal": len(messages) + 1,
                    "source_kind": kind,
                    "item_type": classified_type,
                    "role": payload.get("role") or payload.get("author"),
                    "text": redacted,
                    "text_chars": len(text),
                    "truncated": truncated,
                    "evidence": {
                        "thread_id": thread_id,
                        "file": str(path),
                        "line": line_number,
                    },
                }
            )

    linked_children = [
        {
            "thread_id": row["thread_id"],
            "archived": row["archived"],
            "thread_source": row["thread_source"],
            "agent_path": row.get("agent_path"),
            "file_bytes": row.get("file_bytes", 0),
        }
        for row in all_rows
        if row["kind"] == "child_or_agent"
        and (
            row.get("parent_thread_id") == thread_id
            or row.get("forked_from_id") == thread_id
        )
    ]
    return {
        "schema_version": "0.1",
        "thread_id": thread_id,
        "category": item.get("category"),
        "selection_reason": item.get("reason"),
        "metadata": {
            key: item.get(key)
            for key in (
                "archived",
                "kind",
                "title",
                "thread_source",
                "source",
                "cwd",
                "created_at",
                "updated_at",
                "file_count",
                "file_bytes",
            )
        },
        "stats": {
            "message_count": len(messages),
            "role_counts": dict(role_counts),
            "item_counts": dict(item_counts),
            "tool_names": dict(tool_names),
            "redaction_count": redactions,
            "unreadable_files": unreadable_files,
        },
        "linked_children": linked_children,
        "messages": messages,
    }


def main() -> None:
    args = parse_args()
    index_rows = load_jsonl(args.index)
    by_id = {row["thread_id"]: row for row in index_rows}
    selection = load_jsonl(args.selection) if args.selection.suffix == ".jsonl" else json.loads(args.selection.read_text(encoding="utf-8"))
    missing = [item["thread_id"] for item in selection if item["thread_id"] not in by_id]
    nonroots = [item["thread_id"] for item in selection if item["thread_id"] in by_id and by_id[item["thread_id"]]["kind"] != "root_conversation"]
    if missing or nonroots:
        raise SystemExit(f"invalid selection: missing={missing}, nonroots={nonroots}")
    codex_home = pathlib.Path.home() / ".codex"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as output:
        for selected in selection:
            selected_row = dict(by_id[selected["thread_id"]])
            selected_row["category"] = selected.get("category")
            selected_row["reason"] = selected.get("reason")
            row = collect_thread(selected_row, index_rows, codex_home, args.max_message_chars)
            output.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps({"threads": len(selection), "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
