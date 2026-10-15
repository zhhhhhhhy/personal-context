#!/usr/bin/env python3
"""Check local source -> observation -> reflection bookkeeping.

This is a structural check, not proof of semantic completeness. An independent
review must still examine whether units preserve every useful source meaning.
``inventory`` prints counts by default; ``--include-text`` explicitly returns
the local source bodies. Validation diagnostics never include source bodies.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import pathlib
from typing import Any


SCHEMA_VERSION = "coverage/1"
KINDS = {
    "preference_signal", "task_requirement", "correction", "exception",
    "project_fact", "question", "non_substantive", "permission_scope", "sensitive",
}
USEFUL_KINDS = {"preference_signal", "task_requirement", "correction", "exception"}
FROZEN_NAMES = {
    "cohort.json", "train.selection.json", "eval.selection.json",
    "evidence.train.jsonl", "evidence.eval.jsonl",
}
SOURCE_NAMES = {"cohort.json", "train.selection.json", "evidence.train.jsonl"}


class CoverageError(ValueError):
    """A source/pack error whose message is safe to include in diagnostics."""


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _read_json(path: pathlib.Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise CoverageError(f"{label} is missing, unreadable or invalid JSON") from None


def _digest(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def source_inventory(run_dir: pathlib.Path | str) -> dict[str, Any]:
    """Return only direct user-authored training messages, with stable identities.

    IDs hash thread_id, basename:Lline and exact text. The source digest hashes
    sorted IDs, so record/array order cannot change identity. Duplicate source
    identities are rejected rather than assigned order-dependent suffixes.
    Source body text stays local; callers decide whether to return it to a model.
    """
    run_dir = pathlib.Path(run_dir)
    selection = _read_json(run_dir / "train.selection.json", "training selection")
    if not isinstance(selection, list):
        raise CoverageError("training selection must be a list")
    metadata: dict[str, dict[str, Any]] = {}
    for item in selection:
        if not isinstance(item, dict) or not _nonempty(item.get("thread_id")):
            raise CoverageError("training selection contains an invalid thread")
        if item["thread_id"] in metadata:
            raise CoverageError("training selection contains duplicate threads")
        metadata[item["thread_id"]] = item
    try:
        lines = (run_dir / "evidence.train.jsonl").read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        raise CoverageError("training evidence is missing or unreadable") from None
    messages: dict[str, dict[str, Any]] = {}
    for row_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            raise CoverageError(f"training evidence row {row_number} is invalid JSON") from None
        if not isinstance(row, dict) or not _nonempty(row.get("thread_id")):
            raise CoverageError(f"training evidence row {row_number} has no valid thread_id")
        thread_id = row["thread_id"]
        if thread_id not in metadata:
            raise CoverageError(f"training evidence row {row_number} is outside the training selection")
        if not isinstance(row.get("messages"), list):
            raise CoverageError(f"training evidence row {row_number} must contain a messages list")
        meta = metadata[thread_id]
        for message_number, message in enumerate(row["messages"], start=1):
            label = f"training evidence row {row_number} message {message_number}"
            if not isinstance(message, dict):
                raise CoverageError(f"{label} must be an object")
            if message.get("source_kind") != "user_authored":
                continue
            evidence = message.get("evidence")
            if not isinstance(evidence, dict):
                raise CoverageError(f"{label} has no evidence location")
            source_line = evidence.get("line")
            source_file = evidence.get("file")
            if type(source_line) is not int or source_line < 1 or not _nonempty(source_file):
                raise CoverageError(f"{label} has an invalid evidence location")
            text = message.get("text")
            if not _nonempty(text):
                raise CoverageError(f"{label} has no text")
            truncated = message.get("truncated", False)
            if not isinstance(truncated, bool):
                raise CoverageError(f"{label} has an invalid truncated flag")
            # Normalize both Windows and POSIX source paths on either platform.
            basename = source_file.replace("\\", "/").rsplit("/", 1)[-1]
            if not basename:
                raise CoverageError(f"{label} has an invalid source filename")
            location = f"{basename}:L{source_line}"
            message_id = "msg-" + _digest({"thread_id": thread_id, "location": location, "text": text})
            if message_id in messages:
                raise CoverageError("training evidence contains duplicate direct source identities")
            messages[message_id] = {
                "message_id": message_id,
                "thread_id": thread_id,
                "category": meta.get("category") or row.get("category") or "context_evolution",
                "family_id": meta.get("family_id") or thread_id,
                "location": location,
                "text": text,
                "truncated": truncated,
            }
    return {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_dir.name,
        "source_digest": _digest(sorted(messages)),
        # Preserve conversation chronology for readers; only identity/digest
        # are independent of source array order.
        "messages": list(messages.values()),
    }


def _frozen_errors(run_dir: pathlib.Path) -> list[str]:
    try:
        hashes = _read_json(run_dir / "input_hashes.json", "input_hashes.json")
    except CoverageError as exc:
        return [str(exc)]
    if not isinstance(hashes, dict):
        return ["input_hashes.json must be an object"]
    errors = []
    if not SOURCE_NAMES.issubset(hashes):
        errors.append("input_hashes.json must freeze cohort, training selection and training evidence")
    for name, expected in hashes.items():
        if name not in FROZEN_NAMES:
            errors.append("input_hashes.json contains an unsupported file")
            continue
        try:
            actual = hashlib.sha256((run_dir / name).read_bytes()).hexdigest()
        except OSError:
            actual = None
        if not isinstance(expected, str) or actual != expected:
            errors.append(f"prepared input changed: {name}")
    return errors


def _references(value: Any, label: str, errors: list[str], *, required: bool) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a list")
        return []
    if required and not value:
        errors.append(f"{label} must not be empty")
    valid = [item for item in value if _nonempty(item)]
    if len(valid) != len(value):
        errors.append(f"{label} must contain nonempty string IDs")
    if len(set(valid)) != len(valid):
        errors.append(f"{label} contains duplicate IDs")
    return valid


def validate_coverage(
    run_dir: pathlib.Path | str,
    observations_path: pathlib.Path | str,
    reflection: dict[str, Any] | pathlib.Path | str | None = None,
) -> dict[str, Any]:
    """Validate bookkeeping without returning quotes, unit claims or source text.

    ``reflection`` accepts a decoded object or a JSON path for per-arm checks.
    ``reviewed_messages`` counts distinct source messages represented by a
    nonempty unit list; it does not assert a semantic review was sufficient.
    """
    run_dir = pathlib.Path(run_dir)
    errors = _frozen_errors(run_dir)
    result = {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_dir.name,
        "status": "rejected",
        "structural_only": True,
        "message_count": 0,
        "reviewed_messages": 0,
        "unit_count": 0,
        "observation_count": 0,
        "errors": errors,
    }
    try:
        inventory = source_inventory(run_dir)
    except CoverageError as exc:
        errors.append(str(exc))
        return result
    sources = {item["message_id"]: item for item in inventory["messages"]}
    result["message_count"] = len(sources)
    if not sources:
        errors.append("training source inventory contains no direct user messages")
    truncated_count = sum(item["truncated"] for item in sources.values())
    if truncated_count:
        errors.append(f"truncated direct sources fail coverage: {truncated_count}")
    try:
        pack = _read_json(pathlib.Path(observations_path), "observations")
    except CoverageError as exc:
        errors.append(str(exc))
        return result
    if not isinstance(pack, dict):
        errors.append("observations must be an object")
        return result
    if pack.get("schema_version") != SCHEMA_VERSION:
        errors.append("observations schema_version must be coverage/1")
    if pack.get("run_id") != run_dir.name:
        errors.append("observations run_id does not match run directory")
    if pack.get("source_digest") != inventory["source_digest"]:
        errors.append("observations source_digest does not match training source inventory")
    review = pack.get("review")
    if not isinstance(review, dict) or review.get("completeness_reviewed") is not True or not _nonempty(review.get("method")):
        errors.append("observations review must record completeness_reviewed=true and a nonempty method")
    entries = pack.get("messages")
    if not isinstance(entries, list):
        errors.append("observations messages must be a list")
        entries = []
    seen_messages: Counter[str] = Counter()
    reviewed: set[str] = set()
    units: set[str] = set()
    unit_edges: set[tuple[str, str]] = set()
    for index, entry in enumerate(entries, start=1):
        prefix = f"messages[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} must be an object")
            continue
        message_id = entry.get("message_id")
        source = sources.get(message_id) if isinstance(message_id, str) else None
        if source is None:
            errors.append(f"{prefix} has an unknown message_id")
        else:
            seen_messages[message_id] += 1
        entries_units = entry.get("units")
        if not isinstance(entries_units, list) or not entries_units:
            errors.append(f"{prefix} must contain at least one unit")
            continue
        if source is not None:
            reviewed.add(message_id)
        result["unit_count"] += len(entries_units)
        for unit_index, unit in enumerate(entries_units, start=1):
            label = f"{prefix}.units[{unit_index}]"
            if not isinstance(unit, dict):
                errors.append(f"{label} must be an object")
                continue
            unit_id = unit.get("id")
            if not _nonempty(unit_id):
                errors.append(f"{label} must have a nonempty id")
            elif unit_id in units:
                errors.append(f"{label} has a duplicate unit id")
            else:
                units.add(unit_id)
            quote = unit.get("quote")
            if not _nonempty(quote) or (source is not None and quote not in source["text"]):
                errors.append(f"{label} quote must be a nonempty exact substring of its source message")
            if not isinstance(unit.get("kind"), str) or unit["kind"] not in KINDS:
                errors.append(f"{label} has an unsupported kind")
            for field in ("claim", "reason"):
                if not _nonempty(unit.get(field)):
                    errors.append(f"{label} must have a nonempty {field}")
            useful = isinstance(unit.get("kind"), str) and unit["kind"] in USEFUL_KINDS
            references = _references(unit.get("observation_ids"), f"{label}.observation_ids", errors, required=useful)
            if _nonempty(unit_id):
                unit_edges.update((unit_id, observation_id) for observation_id in references)
    result["reviewed_messages"] = len(reviewed)
    missing = set(sources) - set(seen_messages)
    if missing:
        errors.append(f"direct source messages missing from observations: {len(missing)}")
    duplicate_count = sum(count > 1 for count in seen_messages.values())
    if duplicate_count:
        errors.append(f"direct source messages represented multiple times: {duplicate_count}")
    observation_entries = pack.get("observations")
    if not isinstance(observation_entries, list):
        errors.append("observations observations must be a list")
        observation_entries = []
    result["observation_count"] = len(observation_entries)
    observations: set[str] = set()
    observation_edges: set[tuple[str, str]] = set()
    for index, observation in enumerate(observation_entries, start=1):
        prefix = f"observations[{index}]"
        if not isinstance(observation, dict):
            errors.append(f"{prefix} must be an object")
            continue
        observation_id = observation.get("id")
        if not _nonempty(observation_id):
            errors.append(f"{prefix} must have a nonempty id")
        elif observation_id in observations:
            errors.append(f"{prefix} has a duplicate observation id")
        else:
            observations.add(observation_id)
        for field in ("claim", "scope"):
            if not _nonempty(observation.get(field)):
                errors.append(f"{prefix} must have a nonempty {field}")
        references = _references(observation.get("source_units"), f"{prefix}.source_units", errors, required=True)
        if _nonempty(observation_id):
            observation_edges.update((unit_id, observation_id) for unit_id in references)
    if any(observation_id not in observations for _, observation_id in unit_edges):
        errors.append("units reference unknown observation IDs")
    if any(unit_id not in units for unit_id, _ in observation_edges):
        errors.append("observations reference unknown unit IDs")
    if unit_edges != observation_edges:
        errors.append("unit and observation edges must match in both directions")
    if reflection is not None:
        if isinstance(reflection, (str, pathlib.Path)):
            try:
                reflection = _read_json(pathlib.Path(reflection), "reflection")
            except CoverageError as exc:
                errors.append(str(exc))
                reflection = None
        if not isinstance(reflection, dict):
            errors.append("reflection must be an object")
        else:
            mapped: Counter[str] = Counter()
            for field in ("promotions", "reinforced", "deferred", "rejected"):
                decisions = reflection.get(field, [])
                if not isinstance(decisions, list):
                    errors.append(f"reflection {field} must be a list")
                    continue
                for index, decision in enumerate(decisions, start=1):
                    label = f"reflection {field}[{index}]"
                    if not isinstance(decision, dict):
                        errors.append(f"{label} must be an object with observation_ids")
                        continue
                    references = _references(decision.get("observation_ids"), f"{label}.observation_ids", errors, required=True)
                    mapped.update(references)
            if set(mapped) - observations:
                errors.append("reflection maps unknown observation IDs")
            if observations - set(mapped):
                errors.append(f"observations missing from reflection outcomes: {len(observations - set(mapped))}")
            if any(count > 1 for count in mapped.values()):
                errors.append("reflection maps observation IDs multiple times")
    result["status"] = "passed" if not errors else "rejected"
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inventory_parser = commands.add_parser("inventory", help="show counts; source bodies require --include-text")
    inventory_parser.add_argument("--run-dir", type=pathlib.Path, required=True)
    inventory_parser.add_argument("--include-text", action="store_true", help="explicitly return local direct source bodies")
    validate_parser = commands.add_parser("validate", help="check a local observation pack and optional reflection")
    validate_parser.add_argument("--run-dir", type=pathlib.Path, required=True)
    validate_parser.add_argument("--observations", type=pathlib.Path, required=True)
    validate_parser.add_argument("--reflection", type=pathlib.Path)
    args = parser.parse_args()
    if args.command == "validate":
        result = validate_coverage(args.run_dir, args.observations, args.reflection)
    else:
        try:
            result = source_inventory(args.run_dir)
            if not args.include_text:
                messages = result.pop("messages")
                result.update(message_count=len(messages), truncated_messages=sum(item["truncated"] for item in messages))
        except CoverageError as exc:
            result = {"schema_version": SCHEMA_VERSION, "status": "rejected", "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("status") == "rejected":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
