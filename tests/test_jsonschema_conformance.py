"""Conformance smoke tests using a standards-compliant Draft 2020-12 validator."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "registry-manifest.schema.json"


class JSONSchemaConformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)

    def valid_manifest(self) -> dict:
        return {
            "schema_version": "1.0.0",
            "authority_state": "proposed",
            "source_document": None,
            "artifacts": [
                {
                    "artifact_id": "MAI-001",
                    "status": None,
                    "version": None,
                    "path": None,
                    "record_state": "unverified",
                    "source_location": None,
                    "notes": ["Example fixture only; not a registry record."],
                }
            ],
        }

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(self.schema)

    def test_representative_valid_manifest_is_accepted(self) -> None:
        self.validator.validate(self.valid_manifest())

    def test_nullable_unknown_values_are_accepted(self) -> None:
        self.validator.validate(self.valid_manifest())

    def test_invalid_manifests_are_rejected(self) -> None:
        cases = {
            "wrong schema version": lambda d: d.update(schema_version="2.0.0"),
            "authority cannot be changed": lambda d: d.update(authority_state="ratified"),
            "unknown top-level field": lambda d: d.update(unexpected=True),
            "invalid artifact identifier": lambda d: d["artifacts"][0].update(artifact_id="../escape"),
            "invalid record state": lambda d: d["artifacts"][0].update(record_state="approved"),
            "unknown artifact field": lambda d: d["artifacts"][0].update(extra="no"),
            "empty non-null status": lambda d: d["artifacts"][0].update(status=""),
            "notes must be strings": lambda d: d["artifacts"][0].update(notes=[1]),
            "missing required field": lambda d: d["artifacts"][0].pop("path"),
        }
        for label, mutate in cases.items():
            with self.subTest(case=label):
                data = self.valid_manifest()
                mutate(data)
                with self.assertRaises(ValidationError):
                    self.validator.validate(data)


if __name__ == "__main__":
    unittest.main()
