"""Focused coverage regressions. All evidence and writes use synthetic temp files."""

import argparse
import contextlib
import copy
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest
from unittest import mock


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(filename))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


coverage = module("coverage_controls", "context-coverage.py")
evolution = module("evolution_coverage", "context-evolution.py")


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp.name)
        self.old_root = evolution.REPO_ROOT
        evolution.REPO_ROOT = self.root
        self.run = self.root / ".local/run"
        self.run.mkdir(parents=True)
        self.observations_path = self.run / "observations.json"
        self.cohort = {"train_thread_ids": ["a", "b"], "eval_thread_ids": ["c"], "coverage_required": True}
        self.selection = [{"thread_id": name, "category": "research", "family_id": name} for name in ("a", "b")]
        self.rows = [
            {"thread_id": "a", "messages": [
                {"source_kind": "user_authored", "text": "Start with the evidence.", "evidence": {"file": "C:\\local\\a.jsonl", "line": 6}},
                {"source_kind": "assistant", "text": "An assistant suggestion is not a source."},
                {"source_kind": "user_plan_confirmation", "text": "PLEASE IMPLEMENT THIS PLAN: a copied plan"},
            ]},
            {"thread_id": "b", "messages": [
                {"source_kind": "user_authored", "text": "For this figure, deliver the editable SVG and a rendered PNG.", "evidence": {"file": "/local/b.jsonl", "line": 11}},
            ]},
        ]
        evolution.write_json(self.root / "habits/learned.json", {"items": []})
        evolution.write_json(self.run / "base_snapshot.json", evolution.base_snapshot())
        self.write_sources()
        self.inventory = coverage.source_inventory(self.run)
        self.pack = {
            "schema_version": "coverage/1", "run_id": "run", "source_digest": self.inventory["source_digest"],
            "messages": [], "observations": [],
            "review": {"completeness_reviewed": True, "method": "Enumerated the synthetic direct source requirements."},
        }
        for index, source in enumerate(self.inventory["messages"], start=1):
            unit_id, observation_id = f"U-{index}", f"O-{index}"
            self.pack["messages"].append({"message_id": source["message_id"], "units": [{
                "id": unit_id, "quote": source["text"], "kind": "task_requirement",
                "claim": "Retain the explicit task requirement", "reason": "Direct request for the current task",
                "observation_ids": [observation_id],
            }]})
            self.pack["observations"].append({
                "id": observation_id, "claim": "Retain the task requirement locally",
                "scope": "The source task only", "source_units": [unit_id],
            })
        self.reflection = {
            "schema_version": "0.1", "run_id": "run", "base_snapshot_sha256": evolution.current_base_hash(),
            "conflict_check": {"core_checked": True, "learned_checked": True, "candidate_ledger_checked": True},
            "promotions": [], "reinforced": [], "rejected": [],
            "deferred": [{"claim": "Retained task requirement", "reason": "A single task is not a general preference", "observation_ids": [item["id"]]} for item in self.pack["observations"]],
        }
        self.write_pack()

    def tearDown(self):
        evolution.REPO_ROOT = self.old_root
        self.temp.cleanup()

    def write_sources(self):
        evolution.write_json(self.run / "cohort.json", self.cohort)
        evolution.write_json(self.run / "train.selection.json", self.selection)
        evolution.write_json(self.run / "eval.selection.json", [{"thread_id": "c"}])
        evolution.write_text(self.run / "evidence.train.jsonl", "".join(json.dumps(row) + "\n" for row in self.rows))
        evolution.write_text(self.run / "evidence.eval.jsonl", "")
        evolution.write_json(self.run / "input_hashes.json", {name: evolution.sha256_file(self.run / name) for name in coverage.FROZEN_NAMES})

    def write_pack(self):
        evolution.write_json(self.observations_path, self.pack)
        evolution.write_json(self.run / "reflection.json", self.reflection)

    def validate(self):
        self.write_pack()
        return coverage.validate_coverage(self.run, self.observations_path, self.reflection)

    def test_complete_chain_and_legacy_compatibility(self):
        result = self.validate()
        self.assertEqual(result["status"], "passed", result["errors"])
        self.assertTrue(result["structural_only"])
        self.assertEqual([result[name] for name in ("message_count", "reviewed_messages", "unit_count", "observation_count")], [2, 2, 2, 2])
        self.assertEqual({item["location"] for item in self.inventory["messages"]}, {"a.jsonl:L6", "b.jsonl:L11"})
        self.assertEqual(evolution.validate_reflection(self.run)["status"], "passed")
        del self.cohort["coverage_required"]
        self.write_sources()
        self.observations_path.unlink()
        for item in self.reflection["deferred"]:
            del item["observation_ids"]
        evolution.write_json(self.run / "reflection.json", self.reflection)
        legacy = evolution.validate_reflection(self.run)
        self.assertEqual(legacy["status"], "passed", legacy["errors"])
        self.assertNotIn("coverage", legacy)

    def test_inventory_stable_across_array_order_but_frozen_inputs_stay_immutable(self):
        self.rows.reverse()
        for row in self.rows:
            row["messages"].reverse()
        evolution.write_text(self.run / "evidence.train.jsonl", "".join(json.dumps(row) + "\n" for row in self.rows))
        reordered = coverage.source_inventory(self.run)
        self.assertEqual(reordered["source_digest"], self.inventory["source_digest"])
        self.assertEqual({item["message_id"] for item in reordered["messages"]}, {item["message_id"] for item in self.inventory["messages"]})
        self.assertEqual([item["thread_id"] for item in reordered["messages"]], ["b", "a"])
        result = self.validate()
        self.assertIn("prepared input changed: evidence.train.jsonl", result["errors"])

    def test_omitted_single_task_requirement_is_rejected(self):
        target = next(item["message_id"] for item in self.inventory["messages"] if item["thread_id"] == "b")
        self.pack["messages"] = [entry for entry in self.pack["messages"] if entry["message_id"] != target]
        result = self.validate()
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(result["reviewed_messages"], 1)
        self.assertIn("direct source messages missing from observations: 1", result["errors"])

    def test_reflection_dropped_unknown_and_duplicate_mappings(self):
        original = copy.deepcopy(self.reflection)
        for field in ("promotions", "reinforced", "deferred", "rejected"):
            with self.subTest(outcome=field):
                self.reflection = copy.deepcopy(original)
                decisions = self.reflection.pop("deferred")
                self.reflection[field] = decisions
                self.assertEqual(self.validate()["status"], "passed")
        for fault in ("missing", "unknown", "duplicate"):
            with self.subTest(fault=fault):
                self.reflection = copy.deepcopy(original)
                if fault == "missing":
                    self.reflection["deferred"].pop()
                elif fault == "unknown":
                    self.reflection["deferred"][0]["observation_ids"] = ["unknown"]
                else:
                    self.reflection["rejected"] = [copy.deepcopy(self.reflection["deferred"][0])]
                result = self.validate()
                self.assertEqual(result["status"], "rejected")
                self.assertTrue(any({"missing": "missing from reflection", "unknown": "unknown observation", "duplicate": "multiple times"}[fault] in error for error in result["errors"]))
                if fault == "missing":
                    self.assertEqual(evolution.validate_reflection(self.run)["status"], "rejected")

    def test_forged_quote_and_truncated_source_fail_without_text_in_diagnostics(self):
        original_quote = self.pack["messages"][0]["units"][0]["quote"]
        self.pack["messages"][0]["units"][0]["quote"] = "PRIVATE FORGED QUOTE"
        result = self.validate()
        self.assertEqual(result["status"], "rejected")
        self.assertIn("exact substring", " ".join(result["errors"]))
        self.assertNotIn("PRIVATE FORGED QUOTE", json.dumps(result))
        self.assertNotIn(original_quote, json.dumps(result))
        self.pack["messages"][0]["units"][0]["quote"] = original_quote
        self.rows[0]["messages"][0]["truncated"] = True
        self.write_sources()
        self.assertIn("truncated direct sources fail coverage: 1", self.validate()["errors"])

    def test_useful_units_and_bidirectional_edges(self):
        original = copy.deepcopy(self.pack)
        unit = self.pack["messages"][0]["units"][0]
        unit["observation_ids"] = []
        result = self.validate()
        self.assertEqual(result["status"], "rejected")
        self.assertTrue(any("observation_ids must not be empty" in error for error in result["errors"]))
        self.assertIn("unit and observation edges must match in both directions", result["errors"])
        self.pack = copy.deepcopy(original)
        self.pack["observations"][0]["source_units"] = ["unknown"]
        self.assertIn("observations reference unknown unit IDs", self.validate()["errors"])
        self.pack = copy.deepcopy(original)
        self.pack["messages"][0]["units"][0]["kind"] = "non_substantive"
        self.pack["messages"][0]["units"][0]["observation_ids"] = []
        self.pack["observations"].pop(0)
        self.reflection["deferred"].pop(0)
        self.assertEqual(self.validate()["status"], "passed")

    def test_duplicate_message_unit_and_observation_ids_are_rejected(self):
        original = copy.deepcopy(self.pack)
        for field in ("message", "unit", "observation"):
            with self.subTest(field=field):
                self.pack = copy.deepcopy(original)
                if field == "message":
                    self.pack["messages"].append(copy.deepcopy(self.pack["messages"][0]))
                elif field == "unit":
                    self.pack["messages"][1]["units"][0]["id"] = self.pack["messages"][0]["units"][0]["id"]
                else:
                    self.pack["observations"][1]["id"] = self.pack["observations"][0]["id"]
                self.assertEqual(self.validate()["status"], "rejected")

    def test_missing_or_invalid_observations_return_rejected(self):
        for invalid in (None, "{broken JSON", "[]"):
            with self.subTest(invalid=invalid):
                if invalid is None:
                    self.observations_path.unlink()
                else:
                    self.observations_path.write_text(invalid, encoding="utf-8")
                result = coverage.validate_coverage(self.run, self.observations_path, self.reflection)
                self.assertEqual(result["status"], "rejected")
                self.assertTrue(result["errors"])
                self.assertEqual(evolution.validate_reflection(self.run)["status"], "rejected")

    def test_empty_direct_inventory_cannot_pass_zero_coverage(self):
        for row in self.rows:
            row["messages"] = [message for message in row["messages"] if message["source_kind"] != "user_authored"]
        self.write_sources()
        self.pack.update(source_digest=coverage.source_inventory(self.run)["source_digest"], messages=[], observations=[])
        self.reflection["deferred"] = []
        result = self.validate()
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(result["message_count"], 0)
        self.assertIn("training source inventory contains no direct user messages", result["errors"])

    def test_prepare_requires_coverage_before_freezing_cohort(self):
        index = self.root / "index.jsonl"
        evolution.write_text(index, "".join(json.dumps({"thread_id": name, "kind": "root_conversation", "created_at": "2026-10-01"}) + "\n" for name in ("a", "b")))
        args = argparse.Namespace(index=index, output=self.root / ".local/prepared", exclude_selection=[], start="2026-10-01", end="2026-10-02", partition_manifest=None, eval_count=1, codex_home=self.root, max_message_chars=6000)

        def extract(_index, selection, output, _codex_home, _max_chars):
            rows = [{"thread_id": item["thread_id"], "messages": [{"source_kind": "user_authored", "timestamp": "2026-10-01T00:00:00Z", "text": "A bounded request", "evidence": {"file": item["thread_id"] + ".jsonl", "line": 1}}]} for item in evolution.load_json(selection)]
            evolution.write_text(output, "".join(json.dumps(row) + "\n" for row in rows))

        with mock.patch.object(evolution, "run_extractor", side_effect=extract), contextlib.redirect_stdout(io.StringIO()):
            evolution.cmd_prepare(args)
        self.assertIs(evolution.load_json(args.output / "cohort.json")["coverage_required"], True)
        self.assertEqual(evolution.load_json(args.output / "input_hashes.json")["cohort.json"], evolution.sha256_file(args.output / "cohort.json"))
        self.assertEqual(len(coverage.source_inventory(args.output)["messages"]), 1)


if __name__ == "__main__":
    unittest.main()
