"""Tests for independent-branch recovery after workflow step failures."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.multi_step_workflow import run_multi_step


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


class WorkflowRecoveryTests(unittest.TestCase):
    def test_failure_skips_dependents_but_independent_step_runs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_json(root / "manifest.json", {
                "schema_version": "1.0.0", "authority_state": "proposed",
                "source_document": "synthetic-recovery-fixture.md",
                "artifacts": [{
                    "artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0",
                    "path": None, "record_state": "explicit", "source_location": "Fixture",
                    "notes": ["recovery test"],
                }],
            })
            write_json(root / "rules.json", {"schema_version": "1.0", "rules": []})
            write_json(root / "context.json", {})
            write_json(root / "workflow.json", {
                "schema_version": "1.0", "workflow_id": "WF-RECOVERY-TEST",
                "manifest_path": "manifest.json", "rules_path": "rules.json",
                "context_path": "context.json",
                "steps": [
                    {"step_id": "failed_branch", "depends_on": [],
                     "operation": {"type": "registry.list"}},
                    {"step_id": "dependent_step", "depends_on": ["failed_branch"],
                     "operation": {"type": "registry.list"}},
                    {"step_id": "independent_step", "depends_on": [],
                     "operation": {"type": "registry.list"}},
                ],
            })
            with patch("tools.multi_step_workflow._dispatch", side_effect=[
                OSError("temporary read issue"), ("completed", [{"artifact_id": "DEMO-001"}])
            ]) as dispatch:
                result = run_multi_step(root / "workflow.json")

        steps = {item["step_id"]: item for item in result["steps"]}
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(steps["failed_branch"]["outcome"], "failed")
        self.assertEqual(steps["dependent_step"]["outcome"], "skipped")
        self.assertEqual(steps["dependent_step"]["reason"], "dependency_not_completed")
        self.assertEqual(steps["independent_step"]["status"], "completed")
        self.assertEqual(steps["independent_step"]["result"], [{"artifact_id": "DEMO-001"}])
        self.assertEqual(dispatch.call_count, 2)

    def test_not_found_does_not_prevent_later_independent_step(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_json(root / "manifest.json", {
                "schema_version": "1.0.0", "authority_state": "proposed",
                "source_document": "synthetic-recovery-fixture.md",
                "artifacts": [{
                    "artifact_id": "DEMO-001", "status": "Frozen", "version": "1.0",
                    "path": None, "record_state": "explicit", "source_location": "Fixture",
                    "notes": ["recovery test"],
                }],
            })
            write_json(root / "rules.json", {"schema_version": "1.0", "rules": []})
            write_json(root / "context.json", {})
            write_json(root / "workflow.json", {
                "schema_version": "1.0", "workflow_id": "WF-NOT-FOUND-RECOVERY",
                "manifest_path": "manifest.json", "rules_path": "rules.json",
                "context_path": "context.json",
                "steps": [
                    {"step_id": "missing", "depends_on": [],
                     "operation": {"type": "registry.get", "artifact_id": "MISSING"}},
                    {"step_id": "still_runs", "depends_on": [],
                     "operation": {"type": "registry.list"}},
                ],
            })
            result = run_multi_step(root / "workflow.json")
        steps = {item["step_id"]: item for item in result["steps"]}
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(steps["missing"]["outcome"], "not_found")
        self.assertEqual(steps["still_runs"]["status"], "completed")


if __name__ == "__main__":
    unittest.main()
