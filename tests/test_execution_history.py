"""Tests for append-only workflow execution history."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.execution_history import HistoryWriteError, append_history


class ExecutionHistoryTests(unittest.TestCase):
    def test_appends_one_json_record_per_line(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = root / "workflow.json"
            workflow.write_text(json.dumps({"manifest_path":"manifest.json","rules_path":"rules.json","context_path":"context.json"}), encoding="utf-8")
            for name in ("manifest.json", "rules.json", "context.json"):
                (root / name).write_text("{}", encoding="utf-8")
            history = root / "history.jsonl"
            append_history(workflow, "history.jsonl", {"run_id":"one", "status":"completed"})
            append_history(workflow, "history.jsonl", {"run_id":"two", "status":"blocked"})
            records = [json.loads(line) for line in history.read_text(encoding="utf-8").splitlines()]
        self.assertEqual([record["run_id"] for record in records], ["one", "two"])

    def test_rejects_unsafe_and_protected_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = root / "workflow.json"
            workflow.write_text(json.dumps({"manifest_path":"manifest.json"}), encoding="utf-8")
            (root / "manifest.json").write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(HistoryWriteError, "inside"):
                append_history(workflow, "../history.jsonl", {"run_id":"x"})
            with self.assertRaisesRegex(HistoryWriteError, "overwrite"):
                append_history(workflow, "manifest.json", {"run_id":"x"})


if __name__ == "__main__":
    unittest.main()
