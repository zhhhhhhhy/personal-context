"""Minimal synthetic prepare checks for the explicit thread-bounded date policy."""

import contextlib
import copy
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest
from unittest import mock


spec = importlib.util.spec_from_file_location("evolution_dates", pathlib.Path(__file__).with_name("context-evolution.py"))
evolution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evolution)


class DatePolicyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp.name)
        self.old_root = evolution.REPO_ROOT
        evolution.REPO_ROOT = self.root
        self.index = self.root / "index.jsonl"
        self.rows = [{
            "thread_id": name, "kind": "root_conversation",
            "created_at": "2026-10-01T08:00:00+08:00", "updated_at": "2026-10-01T20:00:00+08:00",
        } for name in ("a", "b")]
        self.messages = [
            {"source_kind": "user_authored", "timestamp": None, "text": "Keep this untimed direct request."},
            {"source_kind": "user_authored", "timestamp": "2026-10-01T10:00:00+08:00", "text": "An in-window request."},
            {"source_kind": "user_authored", "timestamp": "2026-10-02T00:00:00+08:00", "text": "An out-of-window request."},
            {"source_kind": "assistant", "timestamp": None, "text": "An untimed assistant suggestion."},
        ]
        self.sequence = 0

    def tearDown(self):
        evolution.REPO_ROOT = self.old_root
        self.temp.cleanup()

    def prepare(self, policy=None):
        self.sequence += 1
        self.output = self.root / f"prepared-{self.sequence}"
        evolution.write_text(self.index, "".join(json.dumps(row) + "\n" for row in self.rows))
        argv = ["prepare", "--index", str(self.index), "--output", str(self.output), "--start", "2026-10-01", "--end", "2026-10-02", "--eval-count", "1", "--codex-home", str(self.root)]
        if policy is not None:
            argv.extend(["--message-date-policy", policy])
        args = evolution.parser().parse_args(argv)

        def extract(_index, selection, output, _codex_home, _max_chars):
            records = []
            for selected in evolution.load_json(selection):
                messages = copy.deepcopy(self.messages)
                for index, message in enumerate(messages, start=1):
                    message["evidence"] = {"file": selected["thread_id"] + ".jsonl", "line": index}
                records.append({"thread_id": selected["thread_id"], "messages": messages})
            evolution.write_text(output, "".join(json.dumps(row) + "\n" for row in records))

        with mock.patch.object(evolution, "run_extractor", side_effect=extract), contextlib.redirect_stdout(io.StringIO()):
            evolution.cmd_prepare(args)
        return evolution.jsonl(self.output / "evidence.train.jsonl")[0]

    def test_default_strict_excludes_unknown_timestamps(self):
        # Missing updated_at does not change the existing strict policy.
        self.rows[0].pop("updated_at")
        record = self.prepare()
        self.assertEqual(record["message_date_policy"], "strict")
        self.assertEqual([message["text"] for message in record["messages"]], ["An in-window request."])
        selection = evolution.load_json(self.output / "train.selection.json")[0]
        self.assertEqual(selection["message_date_counts"], {
            "input_messages": 4, "retained_messages": 1, "retained_unknown_timestamp": 0,
            "filtered_messages": 3, "filtered_missing_timestamp": 2, "filtered_out_of_window": 1,
        })

    def test_explicit_bounded_policy_preserves_null_and_freezes_audit(self):
        record = self.prepare("thread-bounded")
        self.assertEqual(len(record["messages"]), 2)
        unknown, known = record["messages"]
        self.assertIsNone(unknown["timestamp"])
        self.assertEqual(unknown["timestamp_precision"], "thread_bounded")
        self.assertEqual(known["timestamp_precision"], "message_timestamp")
        selection = evolution.load_json(self.output / "train.selection.json")[0]
        self.assertEqual(selection["thread_date_bounds"]["status"], "within_window")
        self.assertEqual(selection["message_date_counts"]["retained_unknown_timestamp"], 1)
        self.assertEqual(selection["message_date_counts"]["filtered_messages"], 2)
        cohort = evolution.load_json(self.output / "cohort.json")
        self.assertEqual(cohort["message_date_policy"], "thread-bounded")
        self.assertEqual(cohort["message_date_counts"]["total"]["retained_unknown_timestamp"], 2)
        self.assertEqual(cohort["thread_date_bounds"]["a"], selection["thread_date_bounds"])
        frozen = evolution.load_json(self.output / "input_hashes.json")
        for name in ("cohort.json", "train.selection.json", "evidence.train.jsonl"):
            self.assertEqual(frozen[name], evolution.sha256_file(self.output / name))
        readme = (self.output / "README.md").read_text(encoding="utf-8")
        self.assertIn("Message date policy: thread-bounded", readme)
        self.assertIn("retained_unknown_timestamp=1; filtered_messages=2", readme)

    def test_incomplete_invalid_reversed_and_outside_bounds_fail_closed(self):
        original = copy.deepcopy(self.rows)
        for status, updated in (("missing", None), ("invalid", "not a timestamp"), ("reversed", "2026-10-01T07:59:00+08:00"), ("out_of_window", "2026-10-02T00:00:00+08:00")):
            with self.subTest(status=status):
                self.rows = copy.deepcopy(original)
                self.rows[0]["updated_at"] = updated
                with self.assertRaisesRegex(SystemExit, f"thread-bounded cannot retain.*{status} thread date bounds"):
                    self.prepare("thread-bounded")
                self.assertFalse((self.output / "input_hashes.json").exists())

    def test_known_messages_still_use_message_window(self):
        # No fallback is requested by these timestamped messages, so incomplete
        # thread metadata cannot substitute for or override their actual dates.
        self.rows[0]["updated_at"] = None
        self.messages = [message for message in self.messages if message["timestamp"] is not None]
        record = self.prepare("thread-bounded")
        self.assertEqual([message["text"] for message in record["messages"]], ["An in-window request."])
        counts = evolution.load_json(self.output / "train.selection.json")[0]["message_date_counts"]
        self.assertEqual(counts["retained_unknown_timestamp"], 0)
        self.assertEqual(counts["filtered_out_of_window"], 1)


if __name__ == "__main__":
    unittest.main()
