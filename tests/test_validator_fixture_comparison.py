"""Compare schema and application-validator results on shared synthetic fixtures.

These fixtures are test examples only, not extracted registry records.
Expected differences are intentional: JSON Schema does not enforce cross-record
artifact_id uniqueness or repository path traversal safety.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from tools.manifest_validator import validate_manifest


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "registry-manifest.schema.json"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "manifests"


class ValidatorFixtureComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        cls.schema_validator = Draft202012Validator(schema)

    def load_fixture(self, name: str) -> dict:
        return json.loads((FIXTURE_DIR / name).read_text(encoding="utf-8"))

    def outcomes(self, name: str) -> tuple[bool, bool, set[str]]:
        data = self.load_fixture(name)
        schema_valid = not list(self.schema_validator.iter_errors(data))
        findings = validate_manifest(data)
        app_valid = not any(item.severity == "error" for item in findings)
        codes = {item.code for item in findings if item.severity == "error"}
        return schema_valid, app_valid, codes

    def test_valid_fixture_passes_both_validators(self) -> None:
        schema_valid, app_valid, codes = self.outcomes("valid-unknowns.json")
        self.assertTrue(schema_valid)
        self.assertTrue(app_valid, codes)

    def test_schema_invalid_fixture_fails_both_validators(self) -> None:
        schema_valid, app_valid, codes = self.outcomes("invalid-schema-record-state.json")
        self.assertFalse(schema_valid)
        self.assertFalse(app_valid)
        self.assertIn("RECORD_STATE_INVALID", codes)

    def test_duplicate_ids_are_an_intentional_application_only_rule(self) -> None:
        schema_valid, app_valid, codes = self.outcomes("app-rule-duplicate-ids.json")
        self.assertTrue(schema_valid, "JSON Schema does not enforce unique artifact_id across records")
        self.assertFalse(app_valid)
        self.assertIn("ARTIFACT_ID_DUPLICATE", codes)

    def test_unsafe_paths_are_an_intentional_application_only_rule(self) -> None:
        schema_valid, app_valid, codes = self.outcomes("app-rule-unsafe-path.json")
        self.assertTrue(schema_valid, "Path traversal safety is not encoded in the current schema")
        self.assertFalse(app_valid)
        self.assertIn("PATH_UNSAFE", codes)


if __name__ == "__main__":
    unittest.main()
