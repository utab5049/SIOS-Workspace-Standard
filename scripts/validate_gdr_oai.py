#!/usr/bin/env python3
"""Validate the staged GDR/OAI migration package without changing repository files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
MIGRATION = ROOT / "02-Research/Registry/migration/phase-20-migration-map.json"
GDR_SCHEMA = ROOT / "02-Research/Registry/schemas/gdr.schema.json"
OAI_SCHEMA = ROOT / "02-Research/Registry/schemas/oai.schema.json"
STAGED_GDR = ROOT / "02-Research/Registry/migration/staged/gdr"
STAGED_OAI = ROOT / "02-Research/Registry/migration/staged/oai"
PROPOSED_OAI = ROOT / "02-Research/Registry/migration/proposals"


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: cannot load valid JSON: {exc}") from exc


def validate_package():
    migration = load_json(MIGRATION)
    gdr_schema = load_json(GDR_SCHEMA)
    oai_schema = load_json(OAI_SCHEMA)

    Draft202012Validator.check_schema(gdr_schema)
    Draft202012Validator.check_schema(oai_schema)

    gdr_validator = Draft202012Validator(gdr_schema, format_checker=FormatChecker())
    oai_validator = Draft202012Validator(oai_schema, format_checker=FormatChecker())
    errors = []

    decisions = migration.get("governance_decisions", [])
    artifacts = migration.get("operational_inventory", [])
    for index, record in enumerate(decisions):
        errors.extend(
            f"governance_decisions[{index}]: {error.message}"
            for error in sorted(gdr_validator.iter_errors(record), key=lambda e: list(map(str, e.path)))
        )
    for index, record in enumerate(artifacts):
        errors.extend(
            f"operational_inventory[{index}]: {error.message}"
            for error in sorted(oai_validator.iter_errors(record), key=lambda e: list(map(str, e.path)))
        )

    # Each staged JSON record must match the corresponding migration-map entry.
    expected_sets = [
        (STAGED_GDR, decisions, "decision_id", gdr_validator, "GDR"),
        (STAGED_OAI, artifacts, "artifact_id", oai_validator, "OAI"),
    ]
    for directory, records, id_key, validator, label in expected_sets:
        expected = {record.get(id_key): record for record in records}
        staged_paths = sorted(directory.glob("*.json")) if directory.is_dir() else []
        actual_names = {path.stem for path in staged_paths}
        expected_names = {str(record_id) for record_id in expected}
        for missing in sorted(expected_names - actual_names):
            errors.append(f"{label} staged record is missing: {missing}.json")
        for extra in sorted(actual_names - expected_names):
            errors.append(f"{label} staged record is not present in migration map: {extra}.json")
        for staged_path in staged_paths:
            record_id = staged_path.stem
            try:
                staged_record = load_json(staged_path)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            for error in sorted(validator.iter_errors(staged_record), key=lambda e: list(map(str, e.path))):
                errors.append(f"{label} staged {record_id}: {error.message}")
            if record_id in expected and staged_record != expected[record_id]:
                errors.append(f"{label} staged record differs from migration map: {record_id}.json")

    # Phase 27 proposals are schema-validated separately and never counted as staged/canonical records.
    proposed_paths = sorted(PROPOSED_OAI.glob("phase-*-oai-candidates/*.json")) if PROPOSED_OAI.is_dir() else []
    proposed_records = []
    proposed_ids = []
    for proposed_path in proposed_paths:
        try:
            record = load_json(proposed_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        proposed_records.append((proposed_path, record))
        proposed_ids.append(record.get("artifact_id"))
        for error in sorted(oai_validator.iter_errors(record), key=lambda e: list(map(str, e.path))):
            errors.append(f"proposed OAI {proposed_path.name}: {error.message}")
        if proposed_path.stem != record.get("artifact_id"):
            errors.append(f"Phase 27 proposed OAI filename does not match artifact_id: {proposed_path.name}")
        for provenance in record.get("provenance", []):
            source_path = provenance.get("source_path")
            if source_path and not (ROOT / source_path).is_file():
                errors.append(
                    f"Phase 27 proposed OAI {record.get('artifact_id')} provenance source does not exist: {source_path}"
                )

    if len(proposed_ids) != len(set(proposed_ids)):
        errors.append("duplicate artifact_id in Phase 27 proposed OAI records")

    decision_ids = [record.get("decision_id") for record in decisions]
    artifact_ids = [record.get("artifact_id") for record in artifacts]
    if len(decision_ids) != len(set(decision_ids)):
        errors.append("duplicate decision_id in governance_decisions")
    if len(artifact_ids) != len(set(artifact_ids)):
        errors.append("duplicate artifact_id in operational_inventory")

    known_decisions = set(decision_ids)
    for index, artifact in enumerate(artifacts):
        for decision_id in artifact.get("source_decision_ids", []):
            if decision_id not in known_decisions:
                errors.append(
                    f"operational_inventory[{index}] references unknown decision_id {decision_id!r}"
                )

    for proposed_path, artifact in proposed_records:
        for decision_id in artifact.get("source_decision_ids", []):
            if decision_id not in known_decisions:
                errors.append(
                    f"Phase 27 proposed OAI {artifact.get('artifact_id')} references unknown decision_id {decision_id!r}"
                )

    for index, artifact in enumerate(artifacts):
        for provenance in artifact.get("provenance", []):
            source_path = provenance.get("source_path")
            if source_path and not (ROOT / source_path).is_file():
                errors.append(
                    f"operational_inventory[{index}] provenance source does not exist in checkout: {source_path}"
                )

    for index, decision in enumerate(decisions):
        for evidence in decision.get("evidence", []):
            reference = evidence.get("reference", "")
            # References may be external identifiers, but repository-relative paths must resolve.
            if reference.startswith(("02-", "01-", "12-", "13-")) and not (ROOT / reference).is_file():
                errors.append(
                    f"governance_decisions[{index}] repository evidence path does not exist: {reference}"
                )

    if migration.get("status") != "staged_not_applied":
        errors.append("migration status must remain 'staged_not_applied' until a separate migration is approved")
    c1 = next((d for d in decisions if d.get("decision_id") == "GOV-DEC-C1"), None)
    if c1 is None or c1.get("status") != "unresolved":
        errors.append("C1 must remain explicitly unresolved in this staged migration package")

    if errors:
        return errors
    return []


def main() -> int:
    try:
        errors = validate_package()
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("GDR/OAI validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("GDR/OAI schemas, migration map, and individual staged records passed validation.")
    print("No source registry files were modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
