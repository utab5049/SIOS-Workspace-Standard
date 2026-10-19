"""Deterministic, side-effect-free SIOS precondition rules engine."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


_MISSING = object()
_ALLOWED_RULE_KEYS = {
    "rule_id", "description", "enabled", "severity", "field",
    "operator", "value", "message",
}
_ALLOWED_OPERATORS = {"exists", "equals", "not_equals", "in", "contains", "truthy"}
_ALLOWED_SEVERITIES = {"block", "warning"}


class RulesConfigurationError(ValueError):
    """Raised when a rules document is malformed or uses unsupported logic."""


def _field_value(context: dict[str, Any], field: str) -> Any:
    """Resolve a dot-separated path through dictionaries only."""
    value: Any = context
    for segment in field.split("."):
        if not isinstance(value, dict) or segment not in value:
            return _MISSING
        value = value[segment]
    return value


def _validate_rules(document: Any) -> tuple[dict[str, Any], ...]:
    if not isinstance(document, dict) or set(document) != {"schema_version", "rules"}:
        raise RulesConfigurationError("Rules document must contain only schema_version and rules")
    if document["schema_version"] != "1.0":
        raise RulesConfigurationError("schema_version must be '1.0'")
    if not isinstance(document["rules"], list):
        raise RulesConfigurationError("rules must be a list")

    validated: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, rule in enumerate(document["rules"]):
        prefix = f"rules[{index}]"
        if not isinstance(rule, dict):
            raise RulesConfigurationError(f"{prefix} must be an object")
        unknown = set(rule) - _ALLOWED_RULE_KEYS
        if unknown:
            raise RulesConfigurationError(f"{prefix} has unsupported keys: {', '.join(sorted(unknown))}")
        for key in ("rule_id", "field", "operator"):
            if key not in rule:
                raise RulesConfigurationError(f"{prefix}.{key} is required")
            if not isinstance(rule[key], str) or not rule[key].strip():
                raise RulesConfigurationError(f"{prefix}.{key} must be a non-empty string")
        rule_id = rule["rule_id"]
        if rule_id in seen_ids:
            raise RulesConfigurationError(f"duplicate rule_id: {rule_id}")
        seen_ids.add(rule_id)
        if not all(part.strip() for part in rule["field"].split(".")):
            raise RulesConfigurationError(f"{prefix}.field contains an empty path segment")
        if rule["operator"] not in _ALLOWED_OPERATORS:
            raise RulesConfigurationError(f"{prefix}.operator is unsupported: {rule['operator']}")
        severity = rule.get("severity", "block")
        if not isinstance(severity, str) or severity not in _ALLOWED_SEVERITIES:
            raise RulesConfigurationError(f"{prefix}.severity must be 'block' or 'warning'")
        if "enabled" in rule and not isinstance(rule["enabled"], bool):
            raise RulesConfigurationError(f"{prefix}.enabled must be a boolean")
        if "description" in rule and not isinstance(rule["description"], str):
            raise RulesConfigurationError(f"{prefix}.description must be a string")
        if "message" in rule and not isinstance(rule["message"], str):
            raise RulesConfigurationError(f"{prefix}.message must be a string")
        operator = rule["operator"]
        if operator not in {"exists", "truthy"} and "value" not in rule:
            raise RulesConfigurationError(f"{prefix}.value is required for operator {operator}")
        if operator == "exists" and "value" in rule and not isinstance(rule["value"], bool):
            raise RulesConfigurationError(f"{prefix}.value must be a boolean for operator exists")
        normalized = dict(rule)
        normalized["enabled"] = rule.get("enabled", True)
        normalized["severity"] = severity
        normalized["message"] = rule.get("message", rule.get("description", rule_id))
        validated.append(normalized)
    return tuple(validated)


def _matches(rule: dict[str, Any], context: dict[str, Any]) -> bool:
    actual = _field_value(context, rule["field"])
    operator = rule["operator"]
    expected = rule.get("value")

    if operator == "exists":
        exists = actual is not _MISSING
        return exists is expected if "value" in rule else exists
    if operator == "truthy":
        return actual is not _MISSING and bool(actual)
    if actual is _MISSING:
        return False
    if operator == "equals":
        return actual == expected
    if operator == "not_equals":
        return actual != expected
    if operator == "in":
        return isinstance(expected, list) and actual in expected
    if operator == "contains":
        if isinstance(actual, (str, list, tuple, dict)):
            try:
                return expected in actual
            except (TypeError, ValueError):
                return False
        return False
    return False


class RulesEngine:
    """Evaluate declarative preconditions without executing operations or side effects."""

    def __init__(self, document: Any):
        self._rules = _validate_rules(document)

    @classmethod
    def from_file(cls, path: Path) -> "RulesEngine":
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RulesConfigurationError(f"could not read rules JSON: {exc}") from exc
        return cls(document)

    def evaluate(self, context: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(context, dict):
            raise TypeError("context must be a dictionary")

        results: list[dict[str, Any]] = []
        for rule in self._rules:
            if not rule["enabled"]:
                results.append({
                    "rule_id": rule["rule_id"], "status": "skipped",
                    "severity": rule["severity"], "message": rule["message"],
                })
                continue
            passed = _matches(rule, context)
            results.append({
                "rule_id": rule["rule_id"],
                "status": "passed" if passed else "failed",
                "severity": rule["severity"],
                "message": rule["message"],
            })

        blocking_failures = [
            result["rule_id"] for result in results
            if result["status"] == "failed" and result["severity"] == "block"
        ]
        warnings = [
            result["rule_id"] for result in results
            if result["status"] == "failed" and result["severity"] == "warning"
        ]
        return {
            "decision": "allow" if not blocking_failures else "deny",
            "blocking_failures": blocking_failures,
            "warnings": warnings,
            "results": results,
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate SIOS rules against JSON context (no side effects).")
    parser.add_argument("rules", type=Path, help="path to rules JSON")
    parser.add_argument("context", type=Path, help="path to context JSON")
    args = parser.parse_args(argv)
    try:
        engine = RulesEngine.from_file(args.rules)
        context = json.loads(args.context.read_text(encoding="utf-8"))
        result = engine.evaluate(context)
    except (RulesConfigurationError, OSError, json.JSONDecodeError, TypeError) as exc:
        print(f"ERROR RULES_EVALUATION: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["decision"] == "allow" else 2


if __name__ == "__main__":
    sys.exit(main())
