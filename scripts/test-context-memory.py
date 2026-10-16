"""Focused lifecycle and source-integrity checks in isolated temporary stores."""
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import importlib.util
import os
import subprocess
import sys

import context_memory as m


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manifest = {}
        self.evidence = []
        for key in ("alpha", "beta"):
            path = self.root / (key + ".jsonl")
            payload = {"role": "user", "content": [{"type": "input_text", "text": key + " direct instruction"}]}
            records = [{"type": "session_meta", "payload": {"id": key, "source": "vscode"}},
                       {"type": "event_msg", "payload": {"message": "legal separator: \u2028 remains on one JSONL line"}},
                       {"type": "response_item", "payload": payload}]
            path.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in records) + "\n", encoding="utf-8")
            self.manifest[key] = {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                                  "line": 3, "thread_id": key, "origin": "human_parent"}
            expression = hashlib.sha256(json.dumps(payload["content"], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
            self.evidence.append({"ref": key, "thread_id": key, "location": key + ".jsonl:L3", "source_kind": "user_authored",
                                  "support": "Direct scoped request", "family_id": key, "text_sha256": expression})
        m.write(self.root / ".local/sources.json", m.encoded(self.manifest))
        m.write(self.root / "habits/communication.md", b"pre-existing user edit\n")

    def tearDown(self):
        self.temp.cleanup()

    def record(self, key, **changes):
        value = {"id": key, "kind": "memory", "title": "Scoped test", "claim": "Check the specified inputs.",
                 "scope": "test project only", "exceptions": ["Current instruction takes priority"], "tags": ["focused"],
                 "visibility": "public", "sensitivity": "non_sensitive", "validity": "project", "verification": "historical_user_instruction",
                 "evidence": [self.evidence[0]], "review_after": "2026-01-01"}
        value.update(changes)
        return value

    def plan(self, operations):
        return {"base_sha256": m.base_hash(self.root), "source_manifest": ".local/sources.json", "reason": "Focused validation", "operations": operations}

    def add(self, record):
        return {"op": "add", "record": record, "reason": "Explicit scoped agreement"}

    def test_merge_replace_expiry_review_and_rollback(self):
        records = [self.record("project.original"), self.record("project.duplicate", evidence=[self.evidence[1]]),
                   self.record("temporary.todo", validity="temporary", expires_after="2026-10-01"),
                   self.record("rule.stable", kind="rule", validity="stable", evidence=self.evidence)]
        m.apply_plan(self.root, self.plan([self.add(x) for x in records]))
        before = m.base_hash(self.root)
        operations = [{"op": "merge", "from": ["project.duplicate"], "into": "project.original", "reason": "Same topic"},
                      {"op": "replace", "from": ["project.original"], "record": self.record("project.current", evidence=self.evidence), "reason": "Later user correction"}]
        receipt = m.apply_plan(self.root, self.plan(operations))
        items = m.all_items(m.registries(self.root))
        self.assertEqual(items["project.original"]["status"], "superseded")
        self.assertEqual(len(items["project.original"]["evidence"]), 2)
        self.assertEqual(items["project.duplicate"]["merged_into"], "project.original")
        self.assertTrue(items["project.original"]["history"])
        results = m.search(self.root, "focused", today=dt.date(2026, 10, 15))
        self.assertEqual({x["id"] for x in results["matches"]}, {"project.current", "rule.stable"})
        self.assertTrue(all(x["review_due"] for x in results["matches"]))
        m.rollback(self.root, receipt["transaction_id"])
        self.assertEqual(m.base_hash(self.root), before)
        maintenance = m.maintenance(self.root, dt.date(2026, 10, 15))
        self.assertEqual(maintenance["operations"][0]["ids"], ["temporary.todo"])
        m.apply_plan(self.root, maintenance)
        self.assertEqual(m.all_items(m.registries(self.root))["temporary.todo"]["status"], "archived")
        m.apply_plan(self.root, self.plan([{"op": "discard", "ids": ["project.duplicate"], "reason": "No remaining reuse value"}]))
        self.assertEqual(m.all_items(m.registries(self.root))["project.duplicate"]["status"], "discarded")
        self.assertEqual((self.root / "habits/communication.md").read_bytes(), b"pre-existing user edit\n")

    def test_stale_plan_and_stale_rollback_preserve_newer_changes(self):
        plan = self.plan([self.add(self.record("project.first"))])
        receipt = m.apply_plan(self.root, plan)
        with self.assertRaisesRegex(ValueError, "base changed"):
            m.apply_plan(self.root, plan)
        m.write(self.root / "contexts/memory/items/project.first.md", b"newer user edit")
        with self.assertRaisesRegex(ValueError, "newer changes"):
            m.rollback(self.root, receipt["transaction_id"])
        self.assertEqual((self.root / "contexts/memory/items/project.first.md").read_bytes(), b"newer user edit")

    def test_project_material_requires_identity_and_explicit_project_search(self):
        target = self.root / "references/projects/alpha.md"
        target.parent.mkdir(parents=True)
        target.write_text("Version-specific project conditions\n", encoding="utf-8")
        record = self.record("project.scoped", kind="project", project="alpha",
                             target="references/projects/alpha.md")
        m.apply_plan(self.root, self.plan([self.add(record)]))
        self.assertEqual(m.search(self.root, "focused")["matches"], [])
        self.assertEqual(m.search(self.root, "focused", project="beta")["matches"], [])
        self.assertEqual(m.search(self.root, "focused", project="alpha")["matches"][0]["id"], "project.scoped")
        m.apply_plan(self.root, self.plan([self.add(self.record("common.preference", validity="stable"))]))
        self.assertEqual({x["id"] for x in m.search(self.root, "focused", project="alpha")["matches"]},
                         {"project.scoped", "common.preference"})
        self.assertEqual([x["id"] for x in m.search(self.root, "", project="alpha")["matches"]],
                         ["project.scoped"])
        before = m.base_hash(self.root)
        with self.assertRaisesRegex(ValueError, "explicit project"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("project.invalid", kind="project"))]))
        self.assertEqual(m.base_hash(self.root), before)

    def test_private_memory_cannot_be_published_or_found_by_default(self):
        private = self.record("local.context", visibility="local", sensitivity="sensitive")
        m.apply_plan(self.root, self.plan([self.add(private)]))
        self.assertEqual(m.search(self.root, "focused")["matches"], [])
        self.assertEqual(len(m.search(self.root, "focused", include_local=True)["matches"]), 1)
        with self.assertRaisesRegex(ValueError, "stay local"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("public.invalid", sensitivity="sensitive"))]))
        with self.assertRaisesRegex(ValueError, "cannot be moved"):
            m.prepare_plan(self.root, self.plan([{"op": "merge", "from": ["local.context"],
                "record": self.record("public.context"), "reason": "Unsafe publication attempt"}]))
        self.assertNotIn(b"local.context", (self.root / m.PUBLIC).read_bytes())

    def test_sources_and_generalization_require_actual_support(self):
        false = copy.deepcopy(self.evidence)
        false[1]["family_id"] = false[0]["family_id"]
        with self.assertRaisesRegex(ValueError, "independent"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("rule.invalid", kind="rule", validity="stable", evidence=false))]))
        bad = copy.deepcopy(self.evidence[0]); bad["location"] = "alpha.jsonl:L2"
        with self.assertRaisesRegex(ValueError, "mismatch"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("source.invalid", evidence=[bad]))]))
        wrong_date = copy.deepcopy(self.evidence[0]); wrong_date["message_timestamp"] = "2020-01-01T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "timestamp"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("source.wrong-date", evidence=[wrong_date]))]))
        self.manifest["alpha"]["origin"] = "automatic"
        m.write(self.root / ".local/sources.json", m.encoded(self.manifest))
        with self.assertRaisesRegex(ValueError, "human-parent"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("source.automatic"))]))

    def test_source_offsets_survive_unicode_and_compression(self):
        import zstandard
        path = Path(self.manifest["alpha"]["path"])
        compressed = path.with_suffix(".jsonl.zst")
        compressed.write_bytes(zstandard.ZstdCompressor().compress(path.read_bytes()))
        self.manifest["alpha"].update(path=str(compressed), sha256=hashlib.sha256(compressed.read_bytes()).hexdigest())
        m.write(self.root / ".local/sources.json", m.encoded(self.manifest))
        m.prepare_plan(self.root, self.plan([self.add(self.record("source.compressed"))]))

    def test_path_escape_and_incomplete_dispositions_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid memory ID"):
            m.prepare_plan(self.root, self.plan([self.add(self.record("../../escape"))]))
        plan = self.plan([]); plan["decisions"] = []
        with self.assertRaisesRegex(ValueError, "exactly the 46"):
            m.prepare_plan(self.root, plan)
        with self.assertRaisesRegex(ValueError, "allowlist"):
            m.restore(self.root, {"rules/SOUL.md": None})

    def test_legacy_writer_cannot_diverge_from_initialized_store(self):
        spec = importlib.util.spec_from_file_location("legacy_memory_boundary", Path(__file__).with_name("context-evolution.py"))
        legacy = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(legacy)
        legacy.REPO_ROOT = self.root
        m.write(self.root / m.PUBLIC, m.encoded({"schema_version": 1, "items": [], "decisions": []}))
        for action in (legacy.cmd_apply, legacy.cmd_rollback):
            with self.subTest(action=action.__name__), self.assertRaisesRegex(SystemExit, "memory store initialized"):
                action(type("Args", (), {"run_dir": self.root / ".local/run"})())

    def test_plain_windows_command_returns_utf8(self):
        record = self.record("project.chinese", title="中文检索", tags=["中文"])
        m.apply_plan(self.root, self.plan([self.add(record)]))
        result = subprocess.run([sys.executable, str(Path(__file__).with_name("context-memory.py")), "--root", str(self.root),
                                 "search", "--query", "中文"], capture_output=True,
                                env={**os.environ, "PYTHONIOENCODING": "cp936"}, check=True)
        output = json.loads(result.stdout.decode("utf-8"))
        self.assertEqual(output["matches"][0]["title"], "中文检索")


if __name__ == "__main__":
    unittest.main()
