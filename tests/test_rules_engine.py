"""Tests for the deterministic SIOS rules engine."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.rules_engine import RulesConfigurationError, RulesEngine, main


def sample_rules():
    return {
        "schema_version": "1.0",
        "rules": [
            {
                "rule_id": "PRE-001", "field": "request.approved",
                "operator": "equals", "value": True,
                "message": "Request must be approved",
            },
            {
                "rule_id": "PRE-002", "field": "request.owner",
                "operator": "exists", "message": "Request owner is required",
            },
            {
                "rule_id": "PRE-003", "field": "request.tags",
                "operator": "contains", "value": "reviewed",
                "severity": "warning", "message": "Request should be reviewed",
            },
            {
                "rule_id": "PRE-004", "field": "request.legacy",
                "operator": "truthy", "enabled": False,
            },
        ],
    }


class RulesEngineTests(unittest.TestCase):
    def test_all_preconditions_pass(self):
        result = RulesEngine(sample_rules()).evaluate({
            "request": {"approved": True, "owner": "team", "tags": ["reviewed"]}
        })
        self.assertEqual(result["decision"], "allow")
        self.assertEqual(result["blocking_failures"], [])
        self.assertEqual([r["status"] for r in result["results"]],
                         ["passed", "passed", "passed", "skipped"])

    def test_blocking_failure_denies_but_warning_does_not(self):
        result = RulesEngine(sample_rules()).evaluate({
            "request": {"approved": False, "owner": "team", "tags": []}
        })
        self.assertEqual(result["decision"], "deny")
        self.assertEqual(result["blocking_failures"], ["PRE-001"])
        self.assertEqual(result["warnings"], ["PRE-003"])

    def test_missing_nested_field_fails_closed(self):
        result = RulesEngine(sample_rules()).evaluate({"request": {"approved": True}})
        self.assertEqual(result["decision"], "deny")
        self.assertIn("PRE-002", result["blocking_failures"])

    def test_exists_can_check_absence(self):
        engine = RulesEngine({"schema_version": "1.0", "rules": [{
            "rule_id": "PRE-ABSENT", "field": "token", "operator": "exists", "value": False,
        }]})
        self.assertEqual(engine.evaluate({})["decision"], "allow")
        self.assertEqual(engine.evaluate({"token": None})["decision"], "deny")

    def test_equals_not_equals_in_and_contains(self):
        rules = {"schema_version": "1.0", "rules": [
            {"rule_id": "R1", "field": "state", "operator": "not_equals", "value": "blocked"},
            {"rule_id": "R2", "field": "role", "operator": "in", "value": ["admin", "reviewer"]},
            {"rule_id": "R3", "field": "labels", "operator": "contains", "value": "ready"},
        ]}
        result = RulesEngine(rules).evaluate({
            "state": "ready", "role": "reviewer", "labels": ["ready", "safe"]
        })
        self.assertEqual(result["decision"], "allow")

    def test_duplicate_rule_ids_rejected(self):
        rules = {"schema_version": "1.0", "rules": [
            {"rule_id": "DUP", "field": "x", "operator": "truthy"},
            {"rule_id": "DUP", "field": "y", "operator": "truthy"},
        ]}
        with self.assertRaisesRegex(RulesConfigurationError, "duplicate"):
            RulesEngine(rules)

    def test_unknown_operator_and_keys_rejected(self):
        with self.assertRaisesRegex(RulesConfigurationError, "unsupported"):
            RulesEngine({"schema_version": "1.0", "rules": [
                {"rule_id": "R", "field": "x", "operator": "eval", "value": "1"}
            ]})
        with self.assertRaisesRegex(RulesConfigurationError, "unsupported keys"):
            RulesEngine({"schema_version": "1.0", "rules": [
                {"rule_id": "R", "field": "x", "operator": "truthy", "python": "danger"}
            ]})

    def test_invalid_severity_and_missing_value_rejected(self):
        with self.assertRaises(RulesConfigurationError):
            RulesEngine({"schema_version": "1.0", "rules": [
                {"rule_id": "R", "field": "x", "operator": "equals"}
            ]})
        with self.assertRaises(RulesConfigurationError):
            RulesEngine({"schema_version": "1.0", "rules": [
                {"rule_id": "R", "field": "x", "operator": "truthy", "severity": "critical"}
            ]})

    def test_input_context_is_not_mutated(self):
        context = {"nested": {"items": ["original"]}}
        before = json.loads(json.dumps(context))
        RulesEngine({"schema_version": "1.0", "rules": [
            {"rule_id": "R", "field": "nested.items", "operator": "contains", "value": "original"}
        ]}).evaluate(context)
        self.assertEqual(context, before)

    def test_cli_returns_two_when_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rules = root / "rules.json"
            context = root / "context.json"
            rules.write_text(json.dumps({"schema_version": "1.0", "rules": [
                {"rule_id": "R", "field": "approved", "operator": "equals", "value": True}
            ]}), encoding="utf-8")
            context.write_text(json.dumps({"approved": False}), encoding="utf-8")
            with patch("sys.stdout"), patch("sys.stderr"):
                self.assertEqual(main([str(rules), str(context)]), 2)


if __name__ == "__main__":
    unittest.main()
