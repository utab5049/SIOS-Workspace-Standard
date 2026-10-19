"""Tests for bounded, explicitly configured workflow retries."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.multi_step_workflow import MultiStepWorkflowError, run_multi_step


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def fixture(root, *, retry=None, operation=None):
    write_json(root / "manifest.json", {
        "schema_version": "1.0.0", "authority_state": "proposed",
        "source_document": "synthetic-retry-fixture.md",
        "artifacts": [{
            "artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0",
            "path": None, "record_state": "explicit", "source_location": "Fixture",
            "notes": ["retry test"],
        }],
    })
    write_json(root / "rules.json", {"schema_version": "1.0", "rules": []})
    write_json(root / "context.json", {})
    step = {
        "step_id": "read", "depends_on": [],
        "operation": operation or {"type": "registry.list"},
    }
    if retry is not None:
        step["retry"] = retry
    write_json(root / "workflow.json", {
        "schema_version": "1.0", "workflow_id": "WF-RETRY-TEST",
        "manifest_path": "manifest.json", "rules_path": "rules.json",
        "context_path": "context.json", "steps": [step],
    })
    return root / "workflow.json"


class ControlledRetryTests(unittest.TestCase):
    def test_default_is_one_attempt(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = fixture(Path(temp))
            with patch("tools.multi_step_workflow._dispatch", side_effect=OSError("temporary read issue")) as dispatch:
                result = run_multi_step(workflow)
        self.assertEqual(dispatch.call_count, 1)
        self.assertEqual(result["steps"][0]["error_detail"]["code"], "TRANSIENT_IO_ERROR")
        self.assertEqual(result["steps"][0]["attempts"], 1)

    def test_retries_transient_io_error_then_succeeds(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = fixture(Path(temp), retry={"max_attempts": 3})
            with patch("tools.multi_step_workflow._dispatch", side_effect=[
                OSError("temporary read issue"), [{"artifact_id": "DEMO-001"}]
            ]) as dispatch:
                result = run_multi_step(workflow)
        step = result["steps"][0]
        self.assertEqual(dispatch.call_count, 2)
        self.assertEqual(step["status"], "completed")
        self.assertEqual(step["attempts"], 2)
        self.assertEqual(step["result"], [{"artifact_id": "DEMO-001"}])
        self.assertEqual(step["retry_history"][0]["code"], "TRANSIENT_IO_ERROR")

    def test_retry_attempts_are_bounded(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = fixture(Path(temp), retry={"max_attempts": 2})
            with patch("tools.multi_step_workflow._dispatch", side_effect=OSError("still unavailable")) as dispatch:
                result = run_multi_step(workflow)
        self.assertEqual(dispatch.call_count, 2)
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(result["steps"][0]["attempts"], 2)
        self.assertTrue(result["steps"][0]["error_detail"]["retryable"])

    def test_retry_policy_rejects_out_of_range_or_boolean(self):
        for value in (0, 4, True, 1.5, "2"):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as temp:
                workflow = fixture(Path(temp), retry={"max_attempts": value})
                with self.assertRaisesRegex(MultiStepWorkflowError, "from 1 to 3"):
                    run_multi_step(workflow)

    def test_non_retryable_not_found_is_not_retried(self):
        with tempfile.TemporaryDirectory() as temp:
            workflow = fixture(
                Path(temp), retry={"max_attempts": 3},
                operation={"type": "registry.get", "artifact_id": "MISSING"},
            )
            result = run_multi_step(workflow)
        step = result["steps"][0]
        self.assertEqual(step["outcome"], "not_found")
        self.assertFalse(step["error_detail"]["retryable"])
        self.assertEqual(step["attempts"], 1)


if __name__ == "__main__":
    unittest.main()
