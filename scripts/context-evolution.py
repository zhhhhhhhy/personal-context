#!/usr/bin/env python3
"""Evidence-bounded, reversible Context evolution for the personal-context repo.

The semantic Observer and Reflector are the current Codex session.  This
script owns the deterministic boundary: cohort selection, train/eval split,
source validation, secret checks, base-version checks, atomic application and
rollback.  It never reads raw logs unless ``prepare`` invokes the existing
redacting extractor, and it never writes core rules automatically.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from typing import Any


SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
EXTRACTOR = SCRIPT_DIR / "extract-conversation-evidence.py"
LOCAL_TZ = dt.timezone(dt.timedelta(hours=8))
SCHEMA_VERSION = "0.1"
SECRET_PATTERNS = (
    re.compile(r"(?i)(?:sk|ghp|github_pat)-[A-Za-z0-9_-]{10,}"),
    re.compile(r"(?i)f3b_[^\s,，;；。]+"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}\b"),
    re.compile(r"-----BEGIN [^-]+-----"),
)
KEY_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{2,100}$")
FORBIDDEN_TARGETS = {
    "rules/SOUL.md",
    "profile.md",
    "habits/communication.md",
    "INDEX.md",
    "AGENTS.md",
}
ALLOWED_SOURCE_KINDS = {"user_authored"}
MESSAGE_DATE_COUNTS = (
    "input_messages", "retained_messages", "retained_unknown_timestamp",
    "filtered_messages", "filtered_missing_timestamp", "filtered_out_of_window",
)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def die(message: str) -> None:
    raise SystemExit(message)


def load_json(path: pathlib.Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        die(f"missing JSON file: {path}")
    except json.JSONDecodeError as exc:
        die(f"invalid JSON {path}: {exc}")


def write_json(path: pathlib.Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def write_text(path: pathlib.Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    tmp.write_text(value, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


def sha256_file(path: pathlib.Path) -> str | None:
    if not path.exists():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_json(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def parse_date(value: Any) -> dt.date:
    if isinstance(value, (int, float)):
        return dt.datetime.fromtimestamp(value, LOCAL_TZ).date()
    text = str(value or "").strip()
    if not text:
        die("a conversation is missing created_at")
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        try:
            return dt.date.fromisoformat(text[:10])
        except ValueError as exc:
            die(f"cannot parse conversation date {value!r}: {exc}")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=LOCAL_TZ)
    return parsed.astimezone(LOCAL_TZ).date()


def thread_date_bounds(row: dict[str, Any], start: dt.date, end: dt.date) -> dict[str, Any]:
    """Describe metadata bounds without substituting a date for any message."""
    result = {"created_at": row.get("created_at"), "updated_at": row.get("updated_at")}
    parsed = []
    for field in ("created_at", "updated_at"):
        value = row.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            return {**result, "status": "missing", "invalid_field": field}
        try:
            if isinstance(value, bool):
                raise ValueError("boolean is not a timestamp")
            if isinstance(value, (int, float)):
                timestamp = dt.datetime.fromtimestamp(value, LOCAL_TZ)
            elif isinstance(value, str):
                text = value.strip()
                timestamp = dt.datetime.fromisoformat(text[:-1] + "+00:00" if text.endswith("Z") else text)
                if timestamp.tzinfo is None:
                    timestamp = timestamp.replace(tzinfo=LOCAL_TZ)
                timestamp = timestamp.astimezone(LOCAL_TZ)
            else:
                raise ValueError("unsupported timestamp type")
        except (ValueError, TypeError, OverflowError, OSError):
            return {**result, "status": "invalid", "invalid_field": field}
        parsed.append(timestamp)
        result[field + "_local"] = timestamp.isoformat()
    created, updated = parsed
    if created > updated:
        result["status"] = "reversed"
    elif not (start <= created.date() <= updated.date() < end):
        result["status"] = "out_of_window"
    else:
        result["status"] = "within_window"
    return result


def load_index(path: pathlib.Path) -> list[dict[str, Any]]:
    rows = jsonl(path)
    return [row for row in rows if row.get("kind") == "root_conversation"]


def selection_ids(paths: list[pathlib.Path]) -> set[str]:
    ids: set[str] = set()
    for path in paths:
        if not path.exists():
            die(f"exclude selection does not exist: {path}")
        raw = load_json(path)
        items = raw if isinstance(raw, list) else raw.get("threads", raw.get("selection", []))
        ids.update(str(item["thread_id"]) for item in items if item.get("thread_id"))
    return ids


def snapshot_paths() -> list[pathlib.Path]:
    return [
        REPO_ROOT / "rules" / "SOUL.md",
        REPO_ROOT / "profile.md",
        REPO_ROOT / "habits" / "communication.md",
        REPO_ROOT / "INDEX.md",
        REPO_ROOT / "habits" / "learned.json",
        REPO_ROOT / "habits" / "learned.md",
    ]


def base_snapshot() -> dict[str, Any]:
    files = {str(path.relative_to(REPO_ROOT)): sha256_file(path) for path in snapshot_paths()}
    return {"schema_version": SCHEMA_VERSION, "created_at": utc_now(), "files": files, "sha256": sha256_json(files)}


def current_base_hash() -> str:
    return sha256_json({str(path.relative_to(REPO_ROOT)): sha256_file(path) for path in snapshot_paths()})


def candidate_paths() -> list[pathlib.Path]:
    paths = [REPO_ROOT / "notes" / "candidates.md"]
    paths.extend(sorted((REPO_ROOT / "notes" / "candidates").glob("*.md")))
    return [path for path in paths if path.is_file()]


def candidate_ids() -> set[str]:
    # Scan IDs mechanically; the model reads only the relevant topic pages.
    ids: set[str] = set()
    for path in candidate_paths():
        ids.update(re.findall(r"^## (C-[0-9-]+)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE))
    return ids


def lookup_candidate(candidate_id: str) -> dict[str, Any]:
    if not re.fullmatch(r"C-\d{8}-\d{3}", candidate_id):
        die("candidate ID must use C-YYYYMMDD-NNN")
    matches: list[dict[str, Any]] = []
    for path in candidate_paths():
        lines = path.read_text(encoding="utf-8").splitlines()
        for start, line in enumerate(lines):
            if line.strip() != f"## {candidate_id}":
                continue
            end = next((index for index in range(start + 1, len(lines)) if lines[index].startswith("## ")), len(lines))
            matches.append({"id": candidate_id, "file": path.relative_to(REPO_ROOT).as_posix(), "start_line": start + 1, "end_line": end, "text": "\n".join(lines[start:end]).rstrip()})
    if len(matches) != 1:
        die(f"expected one candidate record, found {len(matches)} for {candidate_id}")
    return matches[0]


def cmd_show_candidate(args: argparse.Namespace) -> None:
    print(json.dumps(lookup_candidate(args.candidate_id), ensure_ascii=False, indent=2))


def run_extractor(index: pathlib.Path, selection: pathlib.Path, output: pathlib.Path, codex_home: pathlib.Path, max_chars: int) -> None:
    command = [
        sys.executable,
        str(EXTRACTOR),
        "--index",
        str(index),
        "--selection",
        str(selection),
        "--output",
        str(output),
        "--max-message-chars",
        str(max_chars),
    ]
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    result = subprocess.run(command, cwd=REPO_ROOT, env=env, text=True, capture_output=True)
    if result.returncode != 0:
        die(f"conversation extraction failed:\n{result.stdout}\n{result.stderr}")


def cmd_prepare(args: argparse.Namespace) -> None:
    index = args.index.resolve()
    output = args.output.resolve()
    rows = load_index(index)
    excluded = selection_ids([path.resolve() for path in args.exclude_selection])
    start = dt.date.fromisoformat(args.start)
    end = dt.date.fromisoformat(args.end)
    date_policy = getattr(args, "message_date_policy", "strict")
    if date_policy not in {"strict", "thread-bounded"}:
        die("message date policy must be strict or thread-bounded")
    eligible = [
        row
        for row in rows
        if row["thread_id"] not in excluded
        and start <= parse_date(row.get("created_at")) < end
    ]
    eligible.sort(key=lambda row: (str(row.get("created_at")), row["thread_id"]))
    selection_meta: dict[str, dict[str, Any]] = {}
    if args.partition_manifest:
        manifest = load_json(args.partition_manifest)
        if not isinstance(manifest, list) or not manifest:
            die("partition manifest must be a nonempty list")
        by_id = {row["thread_id"]: row for row in eligible}
        families: dict[str, str] = {}
        for item in manifest:
            thread_id = item.get("thread_id")
            if thread_id not in by_id or thread_id in selection_meta:
                die("partition manifest contains an excluded, unknown or duplicate root")
            if item.get("partition") not in {"train", "eval"} or not item.get("category"):
                die("partition manifest requires category and train/eval partition")
            family = item.get("family_id", thread_id)
            if family in families and families[family] != item["partition"]:
                die("related conversation family crosses train/eval partitions")
            families[family] = item["partition"]
            selection_meta[thread_id] = item
        train_rows = [by_id[x["thread_id"]] for x in manifest if x["partition"] == "train"]
        eval_rows = [by_id[x["thread_id"]] for x in manifest if x["partition"] == "eval"]
        if not train_rows or not eval_rows:
            die("both train and eval partitions must be nonempty")
        if {selection_meta[x["thread_id"]]["category"] for x in train_rows} != {selection_meta[x["thread_id"]]["category"] for x in eval_rows}:
            die("each selected category requires train and eval roots")
    else:
        if args.eval_count < 1 or len(eligible) <= args.eval_count:
            die(f"need a positive evaluation count below eligible roots, found {len(eligible)}")
        eval_rows = eligible[-args.eval_count :]
        train_rows = eligible[: -args.eval_count]
    output.mkdir(parents=True, exist_ok=False)

    def public_row(row: dict[str, Any], partition: str) -> dict[str, Any]:
        return {
            "thread_id": row["thread_id"],
            "category": selection_meta.get(row["thread_id"], {}).get("category", "context_evolution"),
            "family_id": selection_meta.get(row["thread_id"], {}).get("family_id", row["thread_id"]),
            "reason": f"bounded historical cohort; partition={partition}",
            "created_at": row.get("created_at"),
            "updated_at": row.get("updated_at"),
            "message_date_policy": date_policy,
            "thread_date_bounds": thread_date_bounds(row, start, end),
            "message_date_counts": {field: 0 for field in MESSAGE_DATE_COUNTS},
            "archived": row.get("archived"),
            "title": row.get("title", ""),
            "source_kind": row.get("thread_source") or row.get("source"),
        }

    train = [public_row(row, "train") for row in train_rows]
    evaluation = [public_row(row, "eval") for row in eval_rows]
    write_json(output / "train.selection.json", train)
    write_json(output / "eval.selection.json", evaluation)
    cohort = {
        "schema_version": SCHEMA_VERSION,
        "run_id": output.name,
        "created_at": utc_now(),
        "index": str(index),
        "start": args.start,
        "end_exclusive": args.end,
        "excluded_thread_count": len(excluded),
        "eligible_thread_count": len(eligible),
        "selected_thread_count": len(train) + len(evaluation),
        "selection_mode": "explicit_stratified" if selection_meta else "chronological",
        "train_thread_count": len(train),
        "eval_thread_count": len(evaluation),
        "train_thread_ids": [item["thread_id"] for item in train],
        "eval_thread_ids": [item["thread_id"] for item in evaluation],
        "raw_evidence_policy": "local_only_redacted_extract",
        "coverage_required": True,
        "message_date_policy": date_policy,
        "thread_date_bounds": {item["thread_id"]: item["thread_date_bounds"] for item in train + evaluation},
    }
    write_json(output / "cohort.json", cohort)
    write_json(output / "base_snapshot.json", base_snapshot())
    run_extractor(index, output / "train.selection.json", output / "evidence.train.jsonl", args.codex_home.resolve(), args.max_message_chars)
    run_extractor(index, output / "eval.selection.json", output / "evidence.eval.jsonl", args.codex_home.resolve(), args.max_message_chars)
    # Strict remains the default. The explicit fallback preserves null message
    # timestamps only when the complete parent-thread interval is in-window.
    partition_counts = {}
    thread_audit = []
    for partition, selected in (("train", train), ("eval", evaluation)):
        name = f"evidence.{partition}.jsonl"
        selected_by_id = {item["thread_id"]: item for item in selected}
        records = jsonl(output / name)
        for record in records:
            metadata = selected_by_id.get(record.get("thread_id"))
            if metadata is None:
                die(f"extracted {partition} evidence contains a thread outside its selection")
            counts = metadata["message_date_counts"]
            bounds = metadata["thread_date_bounds"]
            kept = []
            for message in record.get("messages", []):
                counts["input_messages"] += 1
                timestamp = message.get("timestamp")
                missing = timestamp is None or (isinstance(timestamp, str) and not timestamp.strip())
                if missing:
                    if date_policy == "thread-bounded" and message.get("source_kind") == "user_authored":
                        if bounds["status"] != "within_window":
                            die(f"thread-bounded cannot retain untimed direct messages for thread {metadata['thread_id']}: {bounds['status']} thread date bounds")
                        message["timestamp"] = None
                        message["timestamp_precision"] = "thread_bounded"
                        counts["retained_unknown_timestamp"] += 1
                    else:
                        counts["filtered_missing_timestamp"] += 1
                        counts["filtered_messages"] += 1
                        continue
                elif not start <= parse_date(timestamp) < end:
                    counts["filtered_out_of_window"] += 1
                    counts["filtered_messages"] += 1
                    continue
                else:
                    message["timestamp_precision"] = "message_timestamp"
                counts["retained_messages"] += 1
                kept.append(message)
            record["messages"] = kept
            record["message_date_policy"] = date_policy
            record["thread_date_bounds"] = bounds
        write_text(output / name, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in records))
        write_json(output / f"{partition}.selection.json", selected)
        partition_counts[partition] = {field: sum(item["message_date_counts"][field] for item in selected) for field in MESSAGE_DATE_COUNTS}
        for item in selected:
            bounds = item["thread_date_bounds"]
            counts = item["message_date_counts"]
            thread_audit.append(f"- `{item['thread_id']}` ({partition}): created_at={bounds['created_at']}; updated_at={bounds['updated_at']}; bounds={bounds['status']}; retained_unknown_timestamp={counts['retained_unknown_timestamp']}; filtered_messages={counts['filtered_messages']}")
    totals = {field: sum(counts[field] for counts in partition_counts.values()) for field in MESSAGE_DATE_COUNTS}
    cohort["message_date_counts"] = {**partition_counts, "total": totals}
    write_json(output / "cohort.json", cohort)
    frozen = ("train.selection.json", "eval.selection.json", "cohort.json", "evidence.train.jsonl", "evidence.eval.jsonl")
    write_json(output / "input_hashes.json", {name: sha256_file(output / name) for name in frozen})
    write_text(output / "README.md", f"""# Context evolution run {output.name}

- Date window: {args.start} <= local date < {args.end}
- Message date policy: {date_policy}
- Retained messages with unknown timestamp: {totals['retained_unknown_timestamp']}
- Filtered messages: {totals['filtered_messages']} (missing timestamp: {totals['filtered_missing_timestamp']}; outside message date window: {totals['filtered_out_of_window']})
- Training roots: {len(train)}
- Evaluation roots: {len(evaluation)}
- Excluded previously processed roots: {len(excluded)}
- Raw logs are read-only. Evidence packs are local and redacted.
- `evidence.train.jsonl` is for Observer/Reflector only.
- `observations.json` must use coverage/1 and map every direct training message to units.
- Every observation must map to exactly one reflection outcome. Structural checks do not replace independent semantic review.
- `evidence.eval.jsonl` must not be used to draft or tune promotions.
- `thread-bounded` admits only untimed direct user messages whose complete parent-thread bounds are within the window; their timestamp remains null and timestamp_precision is thread_bounded.
- Thread bounds and message counts are frozen in cohort/selection/evidence files; thread bounds do not establish an exact message date.

## Thread date audit

{chr(10).join(thread_audit)}
""")
    print(json.dumps({"run_dir": str(output), "train": len(train), "eval": len(evaluation), "eligible": len(eligible)}, ensure_ascii=False))


def read_reflection(run_dir: pathlib.Path) -> tuple[dict[str, Any], dict[str, Any]]:
    cohort = load_json(run_dir / "cohort.json")
    reflection = load_json(run_dir / "reflection.json")
    return cohort, reflection


def contains_secret(value: Any) -> bool:
    text = json.dumps(value, ensure_ascii=False)
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def evidence_locations(run_dir: pathlib.Path) -> dict[str, dict[tuple[int, str], dict[str, str]]]:
    path = run_dir / "evidence.train.jsonl"
    if not path.exists():
        return {}
    locations: dict[str, dict[tuple[int, str], dict[str, str]]] = {}
    for row in jsonl(path):
        thread_id = str(row.get("thread_id"))
        for message in row.get("messages", []):
            evidence = message.get("evidence") or {}
            line = evidence.get("line")
            kind = message.get("source_kind")
            if isinstance(line, int) and isinstance(kind, str) and message.get("text", "").strip():
                locations.setdefault(thread_id, {})[(line, kind)] = {
                    "file": pathlib.Path(evidence.get("file", "")).name,
                    "text": " ".join(message["text"].split()),
                }
    return locations


def validate_reflection(run_dir: pathlib.Path) -> dict[str, Any]:
    cohort, reflection = read_reflection(run_dir)
    errors: list[str] = []
    frozen_path = run_dir / "input_hashes.json"
    if frozen_path.exists():
        for name, expected in load_json(frozen_path).items():
            if sha256_file(run_dir / name) != expected:
                errors.append(f"prepared input changed: {name}")
    coverage_result = None
    if "coverage_required" in cohort:
        if cohort["coverage_required"] is not True:
            errors.append("cohort.coverage_required must be true when present")
        else:
            spec = importlib.util.spec_from_file_location("context_coverage", SCRIPT_DIR / "context-coverage.py")
            coverage = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(coverage)
            coverage_result = coverage.validate_coverage(run_dir, run_dir / "observations.json", reflection)
            errors.extend(f"coverage: {error}" for error in coverage_result["errors"])
    if reflection.get("schema_version") != SCHEMA_VERSION:
        errors.append("reflection schema_version must be 0.1")
    if reflection.get("run_id") != run_dir.name:
        errors.append("reflection run_id does not match run directory")
    snapshot = load_json(run_dir / "base_snapshot.json")
    expected_base = snapshot.get("sha256")
    if reflection.get("base_snapshot_sha256") != expected_base:
        errors.append("reflection base_snapshot_sha256 does not match prepared snapshot")
    conflict_check = reflection.get("conflict_check")
    if not isinstance(conflict_check, dict) or not all(conflict_check.get(name) is True for name in ("core_checked", "learned_checked", "candidate_ledger_checked")):
        errors.append("reflection must record core, learned and candidate-ledger conflict checks")
    train_ids = set(cohort.get("train_thread_ids", []))
    eval_ids = set(cohort.get("eval_thread_ids", []))
    if train_ids & eval_ids:
        errors.append("training and evaluation roots overlap")
    locations = evidence_locations(run_dir)
    selection_path = run_dir / "train.selection.json"
    families = {x["thread_id"]: x.get("family_id", x["thread_id"]) for x in load_json(selection_path)} if selection_path.exists() else {}
    if not locations:
        errors.append("evidence.train.jsonl is missing or contains no readable messages")
    promotions = reflection.get("promotions", [])
    if not isinstance(promotions, list):
        errors.append("promotions must be a list")
        promotions = []
    existing: set[str] = set()
    learned_path = REPO_ROOT / "habits" / "learned.json"
    if learned_path.exists():
        existing = {str(item.get("key")) for item in load_json(learned_path).get("items", [])}
    known_candidates = candidate_ids()
    keys: set[str] = set()
    for index, item in enumerate(promotions, start=1):
        prefix = f"promotion[{index}]"
        key = item.get("key")
        if not isinstance(key, str) or not KEY_PATTERN.fullmatch(key):
            errors.append(f"{prefix}: invalid key")
        elif key in keys:
            errors.append(f"{prefix}: duplicate key in batch: {key}")
        elif key in existing:
            errors.append(f"{prefix}: key already exists; use reinforce/defer instead: {key}")
        else:
            keys.add(key)
        audit = item.get("candidate_audit")
        if not isinstance(audit, dict):
            errors.append(f"{prefix}: candidate_audit is required")
        else:
            action = audit.get("action")
            related = audit.get("related_ids", [])
            if action not in {"new", "refine"}:
                errors.append(f"{prefix}: candidate_audit.action must be new or refine")
            if not isinstance(related, list):
                errors.append(f"{prefix}: candidate_audit.related_ids must be a list")
                related = []
            if action == "new" and related:
                errors.append(f"{prefix}: new promotion cannot list related candidates")
            if action == "refine" and not related:
                errors.append(f"{prefix}: refine promotion must identify related candidates")
            for candidate in related:
                if candidate not in known_candidates:
                    errors.append(f"{prefix}: unknown related candidate {candidate}")
        for field in ("claim", "scope", "confidence", "sensitivity"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}: missing {field}")
        if item.get("sensitivity") != "non_sensitive":
            errors.append(f"{prefix}: only non_sensitive items may be auto-applied")
        if not isinstance(item.get("exceptions"), list):
            errors.append(f"{prefix}: exceptions must be a list")
        evidence = item.get("evidence")
        if not isinstance(evidence, list) or len(evidence) < 2:
            errors.append(f"{prefix}: at least two evidence records are required")
            evidence = []
        evidence_threads: set[str] = set()
        evidence_texts: set[str] = set()
        evidence_families: set[str] = set()
        for ev in evidence:
            if not isinstance(ev, dict):
                errors.append(f"{prefix}: evidence record is not an object")
                continue
            thread_id = ev.get("thread_id")
            if thread_id in eval_ids:
                errors.append(f"{prefix}: evaluation thread used as training evidence: {thread_id}")
            if thread_id not in train_ids:
                errors.append(f"{prefix}: evidence thread is outside training cohort: {thread_id}")
            if ev.get("source_kind") not in ALLOWED_SOURCE_KINDS:
                errors.append(f"{prefix}: evidence must be direct user authored text")
            if not isinstance(ev.get("location"), str) or not ev["location"].strip():
                errors.append(f"{prefix}: evidence location is required")
            if not isinstance(ev.get("support"), str) or not ev["support"].strip():
                errors.append(f"{prefix}: evidence support summary is required")
            location_match = re.search(r":L(\d+)$", str(ev.get("location", "")))
            if not location_match:
                errors.append(f"{prefix}: evidence location must end with :L<line>")
            elif (int(location_match.group(1)), ev.get("source_kind")) not in locations.get(str(thread_id), set()):
                errors.append(f"{prefix}: evidence location does not resolve to a direct user message: {thread_id} {ev.get('location')}")
            else:
                source = locations[str(thread_id)][(int(location_match.group(1)), ev.get("source_kind"))]
                filename = pathlib.Path(ev["location"].rsplit(":L", 1)[0]).name
                if filename != source["file"]:
                    errors.append(f"{prefix}: evidence filename does not match prepared source")
                evidence_texts.add(source["text"])
                evidence_families.add(families.get(str(thread_id), str(thread_id)))
            evidence_threads.add(str(thread_id))
        if len(evidence_threads) < 2:
            errors.append(f"{prefix}: evidence must span two distinct parent conversations")
        if len(evidence_texts) < 2 or len(evidence_families) < 2:
            errors.append(f"{prefix}: evidence must contain distinct user expressions from independent conversation families")
        if any(fragment in str(item).lower() for fragment in ("permission", "password", "token", "private key", "health", "financial")):
            errors.append(f"{prefix}: possible permission or sensitive claim; manual review required")
    if contains_secret(reflection):
        errors.append("reflection contains a secret-like value")
    for field in ("deferred", "rejected", "reinforced"):
        entries = reflection.get(field, [])
        if not isinstance(entries, list):
            errors.append(f"{field} must be a list")
            continue
        for index, entry in enumerate(entries, start=1):
            if field != "reinforced" and isinstance(entry, str) and entry.strip():
                continue  # Older runs may use plain-text deferred/rejected entries.
            if not isinstance(entry, dict) or not all(isinstance(entry.get(key), str) and entry[key].strip() for key in ("claim", "reason")):
                errors.append(f"{field}[{index}] must contain nonempty claim and reason")
    result = {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_dir.name,
        "validated_at": utc_now(),
        "status": "passed" if not errors else "rejected",
        "promotion_count": len(promotions),
        "errors": errors,
        "train_thread_count": len(train_ids),
        "eval_thread_count": len(eval_ids),
    }
    if coverage_result is not None:
        result["coverage"] = coverage_result
    return result


def cmd_validate(args: argparse.Namespace) -> None:
    run_dir = args.run_dir.resolve()
    result = validate_reflection(run_dir)
    write_json(run_dir / "validation.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] != "passed":
        raise SystemExit(2)


def backup_file(run_dir: pathlib.Path, path: pathlib.Path) -> dict[str, Any]:
    relative = path.relative_to(REPO_ROOT).as_posix()
    destination = run_dir / "backup" / relative
    existed = path.exists()
    if existed:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
    return {"target": relative, "backup": destination.relative_to(run_dir).as_posix(), "existed": existed}


def render_learned(items: list[dict[str, Any]]) -> str:
    lines = ["# Learned Context", "", "规则由证据约束的 Context 进化流程自动应用；`auto_applied` 不等于用户最终认可。", ""]
    for item in items:
        lines.extend([
            f"## {item['key']}",
            "",
            f"- claim: {item['claim']}",
            f"- scope: {item['scope']}",
            f"- exceptions: {', '.join(item.get('exceptions', [])) or 'none recorded'}",
            f"- confidence: {item['confidence']}",
            f"- candidate_audit: {item['candidate_audit']['action']} ({', '.join(item['candidate_audit'].get('related_ids', [])) or 'none'})",
            f"- status: {item['status']}",
            f"- source_run: {item['source_run']}",
            f"- updated_at: {item['updated_at']}",
            "- evidence:",
        ])
        for evidence in item.get("evidence", []):
            lines.append(f"  - {evidence['thread_id']} @ {evidence['location']}: {evidence['support']}")
        lines.append("")
    return "\n".join(lines)


def cmd_apply(args: argparse.Namespace) -> None:
    run_dir = args.run_dir.resolve()
    validation = load_json(run_dir / "validation.json")
    if validation.get("status") != "passed":
        die("apply requires validation.status=passed")
    validation = validate_reflection(run_dir)
    if validation["status"] != "passed":
        die("reflection or input changed after validation: " + "; ".join(validation["errors"]))
    snapshot = load_json(run_dir / "base_snapshot.json")
    if current_base_hash() != snapshot.get("sha256"):
        die("repository base changed after prepare; re-run prepare and reflection")
    cohort, reflection = read_reflection(run_dir)
    if contains_secret(reflection):
        die("refusing to apply secret-like reflection")
    promotions = reflection.get("promotions", [])
    backup_manifest = [backup_file(run_dir, path) for path in snapshot_paths() if path.name in {"learned.json", "learned.md"}]
    learned_path = REPO_ROOT / "habits" / "learned.json"
    existing = load_json(learned_path) if learned_path.exists() else {"schema_version": SCHEMA_VERSION, "items": []}
    items = list(existing.get("items", []))
    now = utc_now()
    for promotion in promotions:
        items.append({
            "key": promotion["key"],
            "claim": promotion["claim"],
            "scope": promotion["scope"],
            "exceptions": promotion.get("exceptions", []),
            "confidence": promotion["confidence"],
            "sensitivity": promotion["sensitivity"],
            "candidate_audit": promotion["candidate_audit"],
            "evidence": promotion["evidence"],
            "source_run": run_dir.name,
            "updated_at": now,
            "status": "auto_applied",
        })
    write_json(learned_path, {"schema_version": SCHEMA_VERSION, "updated_at": now, "items": items})
    write_text(REPO_ROOT / "habits" / "learned.md", render_learned(items))
    decision_path = REPO_ROOT / "notes" / "evolution" / f"{run_dir.name}.md"
    decision_lines = [
        f"# Context evolution {run_dir.name}",
        "",
        f"- applied_at: {now}",
        f"- train_threads: {len(cohort.get('train_thread_ids', []))}",
        f"- eval_threads: {len(cohort.get('eval_thread_ids', []))}",
        f"- promotions: {len(promotions)}",
        "- raw evidence: local only",
        "- human acceptance: pending",
        "",
        "## Applied rules",
        "",
    ]
    for item in promotions:
        audit = item["candidate_audit"]
        related = ", ".join(audit.get("related_ids", [])) or "none"
        decision_lines.append(f"- `{item['key']}`: {item['claim']} (scope: {item['scope']}; confidence: {item['confidence']}; candidate audit: {audit['action']} [{related}])")
    decision_lines.extend(["", "## Reinforced existing rules", ""])
    for item in reflection.get("reinforced", []):
        decision_lines.append(f"- {item['claim']} — {item['reason']}")
    decision_lines.extend(["", "## Deferred / rejected", ""])
    for item in reflection.get("deferred", []) + reflection.get("rejected", []):
        decision_lines.append(f"- {item['claim']}: {item['reason']}" if isinstance(item, dict) else f"- {item}")
    write_text(decision_path, "\n".join(decision_lines) + "\n")
    observation_path = REPO_ROOT / "notes" / "observations.md"
    prior = observation_path.read_text(encoding="utf-8") if observation_path.exists() else "# Observations\n"
    marker = f"- Context evolution `{run_dir.name}` applied {len(promotions)} low-risk rule(s); human acceptance pending; detailed evidence is local."
    if marker not in prior:
        write_text(observation_path, prior.rstrip() + "\n" + marker + "\n")
    result = {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_dir.name,
        "applied_at": now,
        "status": "applied",
        "keys": [item["key"] for item in promotions],
        "backup_manifest": backup_manifest,
        "decision_log": str(decision_path.relative_to(REPO_ROOT)),
        "base_snapshot_sha256": snapshot.get("sha256"),
    }
    write_json(run_dir / "apply.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_rollback(args: argparse.Namespace) -> None:
    run_dir = args.run_dir.resolve()
    applied = load_json(run_dir / "apply.json")
    if applied.get("status") != "applied":
        die("run is not marked applied")
    restored: list[str] = []
    for item in applied.get("backup_manifest", []):
        target = REPO_ROOT / item["target"]
        backup = run_dir / item["backup"]
        if item.get("existed"):
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(backup, target)
        elif target.exists():
            target.unlink()
        restored.append(item["target"])
    result = {"schema_version": SCHEMA_VERSION, "run_id": run_dir.name, "rolled_back_at": utc_now(), "status": "rolled_back", "restored": restored}
    write_json(run_dir / "rollback.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_status(args: argparse.Namespace) -> None:
    run_dir = args.run_dir.resolve()
    fields = {}
    for name in ("cohort.json", "reflection.json", "validation.json", "apply.json", "rollback.json"):
        path = run_dir / name
        if path.exists():
            data = load_json(path)
            fields[name] = {key: data.get(key) for key in ("status", "promotion_count", "errors", "keys", "rolled_back_at") if key in data}
    print(json.dumps({"run_dir": str(run_dir), "files": fields}, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)
    candidate = sub.add_parser("show-candidate", help="read exactly one historical candidate; no rule changes")
    candidate.add_argument("--id", dest="candidate_id", required=True)
    candidate.set_defaults(func=cmd_show_candidate)
    prepare = sub.add_parser("prepare")
    prepare.add_argument("--index", type=pathlib.Path, required=True)
    prepare.add_argument("--start", required=True, help="inclusive local date YYYY-MM-DD")
    prepare.add_argument("--end", required=True, help="exclusive local date YYYY-MM-DD")
    prepare.add_argument("--output", type=pathlib.Path, required=True)
    prepare.add_argument("--exclude-selection", type=pathlib.Path, action="append", default=[])
    prepare.add_argument("--partition-manifest", type=pathlib.Path, help="local list of thread_id/category/family_id/partition records frozen before semantic reading")
    prepare.add_argument("--eval-count", type=int, default=3)
    prepare.add_argument("--max-message-chars", type=int, default=6000)
    prepare.add_argument("--message-date-policy", choices=("strict", "thread-bounded"), default="strict", help="strict requires message timestamps; thread-bounded explicitly admits untimed direct messages only inside complete parent-thread date bounds")
    prepare.add_argument("--codex-home", type=pathlib.Path, default=pathlib.Path(os.environ.get("CODEX_HOME", pathlib.Path.home() / ".codex")))
    prepare.set_defaults(func=cmd_prepare)
    for name, func in (("validate", cmd_validate), ("apply", cmd_apply), ("rollback", cmd_rollback), ("status", cmd_status)):
        command = sub.add_parser(name)
        command.add_argument("--run-dir", type=pathlib.Path, required=True)
        command.set_defaults(func=func)
    return root


def main() -> None:
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
