#!/usr/bin/env python3
"""Build a deduplicated, metadata-only index of local Codex conversations.

The Codex runtime keeps session JSONL files in two trees and can write more
than one file for a single thread.  This script joins those files to the
read-only state database by thread id.  It deliberately does not copy message
body text into the output, so the generated index can be inspected locally
before any candidate is promoted to the personal-context repository.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sqlite3
from collections import Counter
from typing import Any


CHILD_THREAD_SOURCES = {
    "subagent",
    "agent_forked_thread",
    "agent_created_thread",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--codex-home",
        type=pathlib.Path,
        default=pathlib.Path.home() / ".codex",
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        required=True,
        help="Local JSONL output path; no raw message bodies are written.",
    )
    parser.add_argument("--summary", type=pathlib.Path, required=True)
    return parser.parse_args()


def read_session_headers(codex_home: pathlib.Path) -> dict[str, list[dict[str, Any]]]:
    by_id: dict[str, list[dict[str, Any]]] = {}
    for tree_name in ("sessions", "archived_sessions"):
        tree = codex_home / tree_name
        if not tree.exists():
            continue
        for path in tree.rglob("*.jsonl"):
            try:
                with path.open("r", encoding="utf-8") as handle:
                    first_line = handle.readline()
                record = json.loads(first_line)
                if record.get("type") != "session_meta":
                    continue
                payload = record.get("payload") or {}
                session_id = payload.get("id") or payload.get("session_id")
                if not session_id:
                    continue
                stat = path.stat()
                by_id.setdefault(session_id, []).append(
                    {
                        "path": str(path),
                        "tree": tree_name,
                        "bytes": stat.st_size,
                        "mtime_ns": stat.st_mtime_ns,
                        "parent_thread_id": payload.get("parent_thread_id"),
                        "forked_from_id": payload.get("forked_from_id"),
                        "agent_path": payload.get("agent_path"),
                        "agent_nickname": payload.get("agent_nickname"),
                    }
                )
            except (OSError, UnicodeError, json.JSONDecodeError):
                continue
    return by_id


def classify(
    *,
    thread_source: str | None,
    source: str | None,
    headers: list[dict[str, Any]],
) -> tuple[str, str | None, str | None, str | None]:
    parent = next(
        (h.get("parent_thread_id") for h in headers if h.get("parent_thread_id")),
        None,
    )
    fork = next(
        (h.get("forked_from_id") for h in headers if h.get("forked_from_id")),
        None,
    )
    agent_path = next(
        (h.get("agent_path") for h in headers if h.get("agent_path")),
        None,
    )
    if thread_source in CHILD_THREAD_SOURCES or parent or fork:
        return "child_or_agent", parent, fork, agent_path
    if thread_source == "voice_chat" or source == "voice_chat":
        return "voice_or_other", parent, fork, agent_path
    if thread_source == "guardian_review":
        return "system_review", parent, fork, agent_path
    # Older local VS Code sessions have no explicit thread_source.  If they
    # have no parent/fork relation, they are still root conversation records.
    return "root_conversation", parent, fork, agent_path


def main() -> None:
    args = parse_args()
    codex_home = args.codex_home.expanduser().resolve()
    db_path = codex_home / "state_5.sqlite"
    headers = read_session_headers(codex_home)

    connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT id, archived, title, thread_source, source, cwd,
               rollout_path, created_at, updated_at, project_id,
               agent_path, agent_nickname, history_mode
        FROM threads
        ORDER BY created_at, id
        """
    ).fetchall()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    archive_counts = Counter()
    header_file_count = 0
    duplicate_id_count = 0
    missing_header_count = 0

    with args.output.open("w", encoding="utf-8", newline="\n") as output:
        for row in rows:
            thread_id = row["id"]
            files = headers.get(thread_id, [])
            if not files:
                missing_header_count += 1
            if len(files) > 1:
                duplicate_id_count += 1
            header_file_count += len(files)
            kind, parent, fork, header_agent_path = classify(
                thread_source=row["thread_source"],
                source=row["source"],
                headers=files,
            )
            file_bytes = sum(int(item.get("bytes", 0)) for item in files)
            record = {
                "schema_version": "0.1",
                "thread_id": thread_id,
                "archived": bool(row["archived"]),
                "kind": kind,
                "title": row["title"] or "",
                "thread_source": row["thread_source"],
                "source": row["source"],
                "cwd": row["cwd"],
                "project_id": row["project_id"],
                "agent_path": header_agent_path or row["agent_path"],
                "agent_nickname": row["agent_nickname"],
                "parent_thread_id": parent,
                "forked_from_id": fork,
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "history_mode": row["history_mode"],
                "file_count": len(files),
                "file_bytes": file_bytes,
                # These are local evidence pointers.  The output contains no
                # message body and is intentionally kept outside the repo.
                "session_files": [
                    {
                        "path": item["path"],
                        "tree": item["tree"],
                        "bytes": item["bytes"],
                        "mtime_ns": item["mtime_ns"],
                    }
                    for item in files
                ],
            }
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
            counts[kind] += 1
            archive_counts[(bool(row["archived"]), kind)] += 1
    connection.close()

    summary = {
        "schema_version": "0.1",
        "database": str(db_path),
        "thread_count": len(rows),
        "session_header_file_count": header_file_count,
        "unique_thread_ids_with_headers": len(headers),
        "thread_ids_with_multiple_files": duplicate_id_count,
        "threads_missing_headers": missing_header_count,
        "kind_counts": dict(counts),
        "archive_kind_counts": {
            f"{'archived' if archived else 'active'}:{kind}": count
            for (archived, kind), count in sorted(archive_counts.items(), key=str)
        },
        "policy": {
            "primary_source": "root_conversation",
            "child_source": "workflow_and_failure_evidence_only",
            "raw_bodies_in_output": False,
        },
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
