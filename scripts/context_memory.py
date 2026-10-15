"""Sparse personal memory, explicit lifecycle transitions and guarded transactions.

Semantic decisions belong to the current user-authorized Observer/Reflector.
This module validates their sources and owns the bounded file-writing path.
"""
from __future__ import annotations

import argparse
import base64
import copy
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import uuid

KEY = re.compile(r"^[a-z0-9][a-z0-9._-]{2,100}$")
ACTIVE = "active"
RETIRED = {"merged", "superseded", "archived", "discarded"}
KINDS = {"memory", "rule", "skill", "core"}
SECRET = re.compile(r"(?i)(?:\bBearer\s+[A-Za-z0-9._~+/=-]{12,}|\b(?:sk-|ghp_|github_pat_)[A-Za-z0-9_-]{15,}|-----BEGIN [^-]+PRIVATE KEY-----)")
PUBLIC = "contexts/memory/registry.json"
PRIVATE = ".local/context-memory/registry.json"
TRANSACTIONS = ".local/context-memory/transactions"


def now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def read(path, default=None):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else copy.deepcopy(default)


def source_lines(path, raw):
    if path.suffix == ".zst":
        try:
            import zstandard
        except ImportError as exc:
            raise ValueError("zstandard is required to read compressed Codex evidence") from exc
        with zstandard.ZstdDecompressor().stream_reader(io.BytesIO(raw)) as reader:
            raw = reader.read()
    # JSONL offsets count LF bytes; splitlines() also splits legal U+2028 text.
    return raw.decode("utf-8").split("\n")


def safe_path(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()) or Path(relative).is_absolute():
        raise ValueError("path escapes repository")
    return path


def writable(name):
    return name in {PUBLIC, PRIVATE, "habits/learned.json", "habits/learned.md",
                    "notes/candidate-dispositions.md", "notes/candidates.md"} or bool(re.fullmatch(
                        r"(?:contexts/memory/items|\.local/context-memory/items|notes/candidates)/[a-zA-Z0-9._-]+\.md", name))


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name("." + path.name + "." + uuid.uuid4().hex + ".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def registries(root):
    return {visibility: read(root / path, {"schema_version": 1, "items": [], "decisions": []})
            for visibility, path in (("public", PUBLIC), ("local", PRIVATE))}


def all_items(data):
    result = {}
    for visibility, registry in data.items():
        for item in registry["items"]:
            if item["id"] in result:
                raise ValueError("duplicate memory ID across stores")
            result[item["id"]] = item
            if item.get("visibility") != visibility:
                raise ValueError("memory visibility does not match store")
    return result


def managed_paths(root):
    fixed = [PUBLIC, PRIVATE, "habits/learned.json", "habits/learned.md",
             "notes/candidate-dispositions.md", "notes/candidates.md"]
    discovered = [p.relative_to(root).as_posix() for folder in
                  ("contexts/memory/items", ".local/context-memory/items", "notes/candidates")
                  for p in (root / folder).glob("*.md")]
    return sorted(set(fixed + discovered))


def snapshot(root):
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest() if (root / name).exists() else None
            for name in managed_paths(root)}


def base_hash(root):
    return digest(snapshot(root))


def entry_path(item):
    prefix = "contexts/memory" if item["visibility"] == "public" else ".local/context-memory"
    return f"{prefix}/items/{item['id']}.md"


def due(item, today):
    return bool(item.get("review_after") and item["review_after"] <= today.isoformat())


def usable(item, today):
    # Only temporary, explicitly dated memories expire automatically.
    return item["status"] == ACTIVE and not (
        item.get("validity") == "temporary" and item.get("expires_after") and
        item["expires_after"] <= today.isoformat())


def render_entry(item):
    lines = [f"# {item['title']}", "", f"- id: `{item['id']}`", f"- kind: {item['kind']}",
             f"- status: {item['status']}", f"- scope: {item['scope']}",
             f"- verification: {item['verification']}", f"- validity: {item['validity']}",
             f"- updated_at: {item['updated_at']}", "", item["claim"], "", "## Boundaries", ""]
    lines += ["- " + value for value in item["exceptions"]]
    for field in ("review_after", "expires_after", "target", "replaced_by", "merged_into", "retirement_reason"):
        if item.get(field):
            lines.append(f"- {field}: {item[field]}")
    lines += ["", "## Evidence pointers", ""]
    lines += [f"- {ev['ref']}: `{ev['thread_id']}` / `{ev['location']}` — {ev['support']}" for ev in item["evidence"]]
    lines += ["", "- candidates: " + ", ".join(item.get("source_candidates", [])), ""]
    if item["status"] in RETIRED:
        lines.insert(2, "> Historical record. Excluded from active retrieval; do not apply as an instruction.\n")
    return "\n".join(lines).encode("utf-8")


def projections(root, data):
    items = all_items(data)
    outputs = {PUBLIC: encoded(data["public"]), PRIVATE: encoded(data["local"])}
    for item in items.values():
        outputs[entry_path(item)] = render_entry(item)
    rules = [x for x in data["public"]["items"] if x["kind"] == "rule" and x["status"] == ACTIVE]
    learned = [{"key": x["id"], "claim": x["claim"], "scope": x["scope"], "exceptions": x["exceptions"],
                "confidence": "high", "sensitivity": "non_sensitive", "status": "auto_applied",
                "candidate_audit": {"action": "refine", "related_ids": x.get("source_candidates", [])},
                "evidence": x["evidence"], "updated_at": x["updated_at"], "source_run": "memory-lifecycle"} for x in rules]
    outputs["habits/learned.json"] = encoded({"schema_version": "0.1", "items": learned})
    lines = ["# Learned Context", "", "仅在条目范围内使用；当前用户指令优先。正文按需读取，不加载全部历史。", ""]
    lines += [f"- [{x['title']}](../{entry_path(x)})：{x['scope']}" for x in rules]
    lines += ["", "项目约定、Skill 去向和维护命令见 [记忆入口](../contexts/memory/INDEX.md)。", ""]
    outputs["habits/learned.md"] = "\n".join(lines).encode("utf-8")
    decisions = data["public"].get("decisions", [])
    if decisions:
        labels = {"memory": "可用记忆", "skill": "Skill", "rule": "长期规则", "discard": "舍弃"}
        lines = ["# 46 条历史候选的最终去向", "", "原候选是历史提炼文本；实际使用以目标条目的范围、状态和例外为准。已有覆盖与本次新增分开记录。", "",
                 "| 编号 | 去向 | 处理方式 | 目标 | 理由 |", "|---|---|---|---|---|"]
        for row in sorted(decisions, key=lambda x: x["candidate_id"]):
            targets = []
            for key in row["targets"]:
                item = items.get(key)
                if item is None and row.get("local_only"):
                    targets.append(f"`{key}`（仅本地，当前机器未提供）")
                    continue
                if item is None:
                    raise ValueError("candidate destination is missing")
                targets.append(f"`{key}`（仅本地）" if item["visibility"] == "local" else f"[{item['title']}](../{entry_path(item)})")
            lines.append(f"| {row['candidate_id'][-3:]} | {labels[row['bucket']]} | {row['action']} | {'; '.join(targets) or '—'} | {row['reason'].replace('|', '/')} |")
        outputs["notes/candidate-dispositions.md"] = ("\n".join(lines) + "\n").encode("utf-8")
        by_id = {x["candidate_id"]: x for x in decisions}
        for path in sorted((root / "notes/candidates").glob("*.md")):
            text = path.read_text(encoding="utf-8").replace("历史候选，不因拆分而晋升。", "历史候选原文；已逐条裁决。按 disposition 和目标记忆使用，不能把旧 claim 整条当成生效规则。")
            chunks = re.split(r"(?=^## C-20261014-[0-9]{3})", text, flags=re.M)
            for index, chunk in enumerate(chunks):
                match = re.match(r"## (C-20261014-[0-9]{3})", chunk)
                if match and match[1] in by_id:
                    row = by_id[match[1]]
                    chunk = re.sub(r"^- (?:status|disposition|destination):.*\n?", "", chunk, flags=re.M).rstrip()
                    chunks[index] = chunk + f"\n- status: resolved\n- disposition: {row['bucket']} / {row['action']}\n- destination: {', '.join(row['targets']) or 'discarded'}\n\n"
            outputs[path.relative_to(root).as_posix()] = ("".join(chunks).rstrip() + "\n").encode("utf-8")
    return outputs


def source_checker(root, manifest_name):
    manifest = read(safe_path(root, manifest_name), {}) if manifest_name else {}
    cache = {}

    def check(ev):
        if not all(isinstance(ev.get(field), str) and ev[field] for field in ("ref", "thread_id", "location", "support", "family_id")):
            raise ValueError("evidence requires ref, thread, exact location, support and family")
        proof = manifest.get(ev["ref"])
        if not proof or ev.get("source_kind") != "user_authored" or proof.get("origin") != "human_parent":
            raise ValueError("evidence is not a verified direct human-parent source")
        path = Path(proof["path"])
        if str(path) not in cache:
            raw = path.read_bytes()
            cache[str(path)] = (hashlib.sha256(raw).hexdigest(), source_lines(path, raw))
        actual_hash, lines = cache[str(path)]
        if actual_hash != proof["sha256"]:
            raise ValueError("source file changed after evidence freeze")
        expected = f"{path.name.removesuffix('.zst')}:L{proof['line']}"
        if expected != ev["location"] or proof["thread_id"] != ev["thread_id"]:
            raise ValueError("source filename, line or thread mismatch")
        record = json.loads(lines[proof["line"] - 1])
        payload = record.get("payload", {})
        if ev.get("message_timestamp") and ev["message_timestamp"] != record.get("timestamp"):
            raise ValueError("source message timestamp does not match")
        direct = (record.get("type") == "response_item" and payload.get("role") == "user") or (
            record.get("type") == "event_msg" and payload.get("type") == "user_message")
        if not direct:
            raise ValueError("source does not resolve to a user message")
        text_hash = hashlib.sha256(json.dumps(payload.get("content", payload.get("message", "")), ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if ev.get("text_sha256") != text_hash:
            raise ValueError("source expression hash does not match")
        metadata = json.loads(lines[0]).get("payload", {})
        if metadata.get("id") != ev["thread_id"] or metadata.get("source") == "exec" or isinstance(metadata.get("source"), dict):
            raise ValueError("automated or different source session")
    return check


def validate_entry(root, item, check_source, known_evidence):
    for field in ("id", "title", "claim", "scope", "verification", "validity", "visibility", "sensitivity"):
        if not isinstance(item.get(field), str) or not item[field].strip():
            raise ValueError("missing memory field: " + field)
    if not KEY.fullmatch(item["id"]) or item.get("kind") not in KINDS:
        raise ValueError("invalid memory ID or kind")
    if item["visibility"] not in {"public", "local"} or item["validity"] not in {"stable", "project", "temporary"}:
        raise ValueError("invalid memory visibility or validity")
    if item["visibility"] == "public" and item["sensitivity"] != "non_sensitive":
        raise ValueError("sensitive memory must stay local")
    if SECRET.search(json.dumps(item)):
        raise ValueError("secret-like material is not memory")
    if not isinstance(item.get("exceptions"), list) or not item["exceptions"] or not isinstance(item.get("tags"), list):
        raise ValueError("memory requires explicit exceptions and tags")
    for field in ("review_after", "expires_after"):
        if item.get(field):
            dt.date.fromisoformat(item[field])
    if item.get("expires_after") and item["validity"] != "temporary":
        raise ValueError("only explicitly temporary memory may expire by date")
    if item["validity"] == "temporary" and not item.get("expires_after"):
        raise ValueError("temporary memory requires an explicit expiry")
    if item["kind"] in {"skill", "core"}:
        target = safe_path(root, item.get("target", ""))
        if not target.is_file():
            raise ValueError("Skill/core target does not exist")
    evidence = item.get("evidence", [])
    if not evidence:
        raise ValueError("usable memory requires evidence")
    for ev in evidence:
        if digest(ev) not in known_evidence:
            try:
                check_source(ev)
            except ValueError as exc:
                raise ValueError(f"{item['id']} / {ev.get('ref')}: {exc}") from exc
    if item["kind"] == "rule":
        if len({x["thread_id"] for x in evidence}) < 2 or len({x["family_id"] for x in evidence}) < 2 or len({x.get("text_sha256") for x in evidence}) < 2:
            raise ValueError("general rule needs independent parent conversations and families")


def prepare_plan(root, plan):
    if not isinstance(plan, dict):
        raise ValueError("memory plan is missing or is not an object")
    if plan.get("base_sha256") != base_hash(root):
        raise ValueError("memory base changed; refresh and reconcile the plan")
    if not isinstance(plan.get("reason"), str) or not plan["reason"].strip():
        raise ValueError("plan requires a reason")
    if SECRET.search(json.dumps(plan)):
        raise ValueError("plan contains secret-like material")
    data = registries(root)
    items = all_items(data)
    known_evidence = {digest(ev) for item in items.values() for ev in item.get("evidence", [])}
    check_source = source_checker(root, plan.get("source_manifest"))
    timestamp = now()

    def add(record):
        item = copy.deepcopy(record)
        if item.get("id") in items:
            raise ValueError("memory ID already exists; merge, replace or review it explicitly")
        validate_entry(root, item, check_source, known_evidence)
        item.update(status=ACTIVE, updated_at=timestamp, revision=1, history=[])
        items[item["id"]] = item
        data[item["visibility"]]["items"].append(item)
        return item

    def change(item, values, reason):
        if item["status"] != ACTIVE:
            raise ValueError("cannot transition an inactive memory")
        previous = {key: value for key, value in item.items() if key != "history"}
        item["history"].append(previous)
        item.update(values, updated_at=timestamp, revision=item["revision"] + 1, last_reason=reason)

    for operation in plan.get("operations", []):
        action = operation.get("op")
        reason = operation.get("reason", "").strip()
        if not reason:
            raise ValueError("each operation requires a reason")
        if action == "add":
            add(operation["record"])
        elif action in {"merge", "replace"}:
            source_ids = operation.get("from", [])
            if not source_ids or len(source_ids) != len(set(source_ids)):
                raise ValueError("merge/replace requires distinct source IDs")
            target = add(operation["record"]) if "record" in operation else items[operation["into"]]
            if target["id"] in source_ids or target["status"] != ACTIVE:
                raise ValueError("invalid merge/replace destination")
            sources = [items[key] for key in source_ids]
            if any(x["visibility"] == "local" for x in sources) and target["visibility"] != "local":
                raise ValueError("local memory cannot be moved into public memory")
            if action == "merge":
                evidence = {digest(ev): ev for x in [target] + sources for ev in x["evidence"]}
                candidates = sorted({v for x in [target] + sources for v in x.get("source_candidates", [])})
                change(target, {"evidence": list(evidence.values()), "source_candidates": candidates}, reason)
            for item in sources:
                change(item, {"status": "merged" if action == "merge" else "superseded",
                              "merged_into" if action == "merge" else "replaced_by": target["id"]}, reason)
            for row in data["public"].get("decisions", []):
                row["targets"] = list(dict.fromkeys(target["id"] if key in source_ids else key for key in row["targets"]))
        elif action in {"archive", "discard"}:
            for key in operation["ids"]:
                change(items[key], {"status": "archived" if action == "archive" else "discarded", "retirement_reason": reason}, reason)
        elif action == "review":
            item = items[operation["id"]]
            dt.date.fromisoformat(operation["review_after"])
            change(item, {"review_after": operation["review_after"]}, reason)
        else:
            raise ValueError("unsupported lifecycle operation")
    if "decisions" in plan:
        decisions = plan["decisions"]
        expected = {value for path in (root / "notes/candidates").glob("*.md")
                    for value in re.findall(r"^## (C-20261014-[0-9]{3})", path.read_text(encoding="utf-8"), re.M)}
        ids = [x["candidate_id"] for x in decisions]
        if len(ids) != len(set(ids)) or set(ids) != expected or len(ids) != 46:
            raise ValueError("candidate dispositions must cover exactly the 46 historical IDs")
        for row in decisions:
            if row["bucket"] not in {"memory", "skill", "rule", "discard"} or not row.get("reason"):
                raise ValueError("invalid candidate disposition")
            if row["bucket"] != "discard" and not row["targets"]:
                raise ValueError("accepted candidate has no destination")
            for key in row["targets"]:
                if key not in items and row.get("local_only"):
                    continue
                if key not in items:
                    raise ValueError("candidate target is missing")
                item = items[key]
                expected_kind = {"memory": {"memory"}, "skill": {"skill"}, "rule": {"rule", "core"}, "discard": KINDS}[row["bucket"]]
                if item["status"] != ACTIVE or item["kind"] not in expected_kind:
                    raise ValueError("candidate target is inactive or of the wrong kind")
        data["public"]["decisions"] = decisions
    for registry in data.values():
        registry["updated_at"] = timestamp
    return data, projections(root, data)


def apply_plan(root, plan):
    before_snapshot = snapshot(root)
    data, outputs = prepare_plan(root, plan)
    if snapshot(root) != before_snapshot:
        raise ValueError("memory base changed during validation")
    transaction_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:8]
    folder = root / TRANSACTIONS / transaction_id
    before = {name: base64.b64encode((root / name).read_bytes()).decode() if (root / name).exists() else None for name in outputs}
    write(folder / "before.json", encoded(before))
    write(folder / "plan.json", encoded(plan))
    try:
        for name, payload in outputs.items():
            if not writable(name):
                raise ValueError("write target is outside the memory allowlist")
            write(safe_path(root, name), payload)
    except Exception:
        restore(root, before)
        raise
    after = {name: hashlib.sha256(payload).hexdigest() for name, payload in outputs.items()}
    receipt = {"transaction_id": transaction_id, "status": "applied", "created_at": now(), "after": after,
               "operations": len(plan.get("operations", [])), "decisions": len(data["public"].get("decisions", []))}
    write(folder / "receipt.json", encoded(receipt))
    return receipt


def restore(root, before):
    for name, payload in before.items():
        if not writable(name):
            raise ValueError("rollback target is outside the memory allowlist")
        path = safe_path(root, name)
        if payload is None:
            path.unlink(missing_ok=True)
        else:
            write(path, base64.b64decode(payload))


def rollback(root, transaction_id):
    if not re.fullmatch(r"[0-9]{8}T[0-9]{6}-[a-f0-9]{8}", transaction_id):
        raise ValueError("invalid transaction ID")
    folder = root / TRANSACTIONS / transaction_id
    receipt = read(folder / "receipt.json")
    if not receipt or receipt["status"] != "applied":
        raise ValueError("transaction is not applied")
    for name, expected in receipt["after"].items():
        path = safe_path(root, name)
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("newer changes exist; refusing stale rollback")
    restore(root, read(folder / "before.json"))
    receipt["status"] = "rolled_back"
    write(folder / "receipt.json", encoded(receipt))
    return {"status": "rolled_back", "transaction_id": transaction_id}


def search(root, query, project=None, include_local=False, limit=5, today=None):
    today = today or dt.date.today()
    data = registries(root)
    items = all_items(data)
    words = re.findall(r"[a-z0-9_.-]+|[\u4e00-\u9fff]+", query.lower())
    terms = set(words + [word[i:i+2] for word in words if re.search(r"[\u4e00-\u9fff]", word) for i in range(len(word)-1)])
    matches = []
    for item in items.values():
        if not usable(item, today) or (item["visibility"] == "local" and not include_local):
            continue
        if project and item.get("project") != project:
            continue
        text = " ".join([item["title"], item["scope"], item.get("project", "")] + item["tags"]).lower()
        score = sum(1 for term in terms if term in text)
        if score or (project and not query):
            matches.append((score, item))
    matches.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    return {"matches": [{"id": x["id"], "title": x["title"], "kind": x["kind"], "scope": x["scope"],
                         "review_due": due(x, today), "visibility": x["visibility"], "path": entry_path(x),
                         **({"target": x["target"]} if x.get("target") else {})} for _, x in matches[:limit]],
            "omitted_matches": max(0, len(matches)-limit), "as_of": today.isoformat(),
            "usage": "Use show for the selected entry, including its boundaries; search results are routing metadata."}


def maintenance(root, today):
    items = all_items(registries(root)).values()
    expired = [x["id"] for x in items if x["status"] == ACTIVE and not usable(x, today)]
    review = [x["id"] for x in items if usable(x, today) and due(x, today)]
    return {"base_sha256": base_hash(root), "reason": "Explicitly temporary records reached their expiry.",
            "operations": [{"op": "archive", "ids": expired, "reason": "Explicit temporary expiry reached on " + today.isoformat()}] if expired else [],
            "review_due": review, "as_of": today.isoformat()}


def main():
    # Codex captures UTF-8 tool output even on legacy Windows code pages.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("snapshot")
    for name in ("validate", "apply"):
        sub.add_parser(name).add_argument("--plan", type=Path, required=True)
    query = sub.add_parser("search")
    query.add_argument("--query", default="")
    query.add_argument("--project")
    query.add_argument("--include-local", action="store_true")
    query.add_argument("--limit", type=int, choices=range(1, 11), default=5)
    for name in ("show", "history"):
        view = sub.add_parser(name)
        view.add_argument("--id", required=True)
        view.add_argument("--include-local", action="store_true")
        view.add_argument("--include-retired", action="store_true")
        view.add_argument("--evidence", action="store_true", help="include full source metadata for maintenance")
    maintain = sub.add_parser("maintain")
    maintain.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.date.today())
    maintain.add_argument("--apply", action="store_true")
    sub.add_parser("rollback").add_argument("--transaction", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "snapshot":
            result = {"base_sha256": base_hash(root)}
        elif args.command in {"validate", "apply"}:
            plan = read(args.plan)
            if args.command == "validate":
                prepare_plan(root, plan)
                result = {"status": "passed"}
            else:
                result = apply_plan(root, plan)
                result = {key: value for key, value in result.items() if key != "after"}
        elif args.command == "search":
            if not args.query and not args.project:
                raise ValueError("search requires query or project; do not load the whole memory pool")
            result = search(root, args.query, args.project, args.include_local, args.limit)
        elif args.command in {"show", "history"}:
            item = all_items(registries(root))[args.id]
            if item["visibility"] == "local" and not args.include_local:
                raise ValueError("local entry requires --include-local")
            if args.command == "show" and not usable(item, dt.date.today()) and not args.include_retired:
                raise ValueError("entry is retired or expired; use history or --include-retired for audit only")
            result = item if args.command == "history" else {k: v for k, v in item.items() if k != "history"}
            if args.command == "show":
                if not args.evidence:
                    fields = {"id", "kind", "title", "claim", "scope", "exceptions", "status", "verification", "project", "target", "review_after", "expires_after"}
                    result = {key: value for key, value in result.items() if key in fields}
                    result["evidence_count"] = len(item["evidence"])
                    result["source"] = entry_path(item)
                result = {**result, "review_due": due(item, dt.date.today()),
                          "usage": "Historical project agreement: check current scope/state before reuse." if item["validity"] == "project" else "Apply only within scope and exceptions; current user instructions take priority."}
        elif args.command == "maintain":
            result = maintenance(root, args.as_of)
            if args.apply and result["operations"]:
                result = {**result, "applied": apply_plan(root, result)["transaction_id"]}
        else:
            result = rollback(root, args.transaction)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, IndexError) as exc:
        parser.exit(2, str(exc) + "\n")


if __name__ == "__main__":
    main()
