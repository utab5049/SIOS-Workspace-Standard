"""Tests for workflow history inspection."""
import json
from pathlib import Path
import tempfile
import unittest
from datetime import datetime, timezone

from tools.workflow_inspector import HistoryReadError, inspect_history, load_history, main


def entry(run_id, timestamp, status="completed", duration=12):
    return {
        "history_schema_version": "1.0",
        "run_id": run_id,
        "timestamp": timestamp,
        "workflow_id": "WF-DEMO",
        "status": status,
        "duration_ms": duration,
        "operation_type": "registry.list",
        "operation_status": "completed",
        "error": None,
    }


class WorkflowInspectorTests(unittest.TestCase):
    def test_loads_jsonl_and_skips_blank_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.jsonl"
            path.write_text(json.dumps(entry("a", "2026-10-18T10:00:00+00:00")) + "\n\n" + json.dumps(entry("b", "2026-10-19T10:00:00Z")) + "\n", encoding="utf-8")
            self.assertEqual([item["run_id"] for item in load_history(path)], ["a", "b"])

    def test_rejects_malformed_json_and_missing_required_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.jsonl"
            path.write_text('{"run_id":\n', encoding="utf-8")
            with self.assertRaisesRegex(HistoryReadError, "line 1"):
                load_history(path)
            path.write_text(json.dumps({"run_id": "a", "timestamp": "2026-10-18T10:00:00+00:00"}), encoding="utf-8")
            with self.assertRaisesRegex(HistoryReadError, "status"):
                load_history(path)

    def test_filters_by_run_status_and_time_range_newest_first(self):
        records = [
            entry("older", "2026-10-17T10:00:00+00:00", "completed", 10),
            entry("blocked", "2026-10-18T10:00:00+00:00", "blocked", 20),
            entry("newer", "2026-10-19T10:00:00+00:00", "completed", 30),
        ]
        result = inspect_history(
            records,
            status="completed",
            since=datetime(2026, 10, 17, tzinfo=timezone.utc),
            until=datetime(2026, 10, 19, tzinfo=timezone.utc),
        )
        self.assertEqual([item["run_id"] for item in result["runs"]], ["older"])
        result = inspect_history(records, status="completed")
        self.assertEqual([item["run_id"] for item in result["runs"]], ["newer", "older"])
        self.assertEqual(result["matched_runs"], 2)
        self.assertEqual(result["average_duration_ms"], 20)

    def test_limit_does_not_change_total_match_count(self):
        result = inspect_history([
            entry("a", "2026-10-17T10:00:00+00:00"),
            entry("b", "2026-10-18T10:00:00+00:00"),
        ], limit=1)
        self.assertEqual(result["matched_runs"], 2)
        self.assertEqual(result["returned_runs"], 1)
        self.assertEqual(result["runs"][0]["run_id"], "b")

    def test_cli_json_output(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "history.jsonl"
            path.write_text(json.dumps(entry("target", "2026-10-18T10:00:00+00:00", "blocked")), encoding="utf-8")
            from unittest.mock import patch
            from io import StringIO
            output = StringIO()
            with patch("sys.stdout", output):
                code = main([str(path), "--status", "blocked", "--json"])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(output.getvalue())["runs"][0]["run_id"], "target")


if __name__ == "__main__":
    unittest.main()
