"""Read-only structural and safety checks for the proposed registry manifest.

This is a standard-library checker for the current proposed contract, not a
full JSON Schema implementation and not an authority/governance decision.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


ARTIFACT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
RECORD_STATES = {"explicit", "grouped", "ambiguous", "unverified"}
TOP_LEVEL_FIELDS = {"schema_version", "authority_state", "source_document", "artifacts"}
ARTIFACT_FIELDS = {
    "artifact_id", "status", "version", "path", "record_state",
    "source_location", "notes",
}
REQUIRED_TOP_LEVEL = {"schema_version", "authority_state", "artifacts"}
REQUIRED_ARTIFACT = {"artifact_id", "status", "version", "path", "record_state"}


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    location: str
    message: str

    def render(self) -> str:
        return f"{self.severity.upper()} {self.code} at {self.location}: {self.message}"


def _finding(code: str, severity: str, location: str, message: str) -> Finding:
    return Finding(code, severity, location, message)


def validate_manifest(data: Any, repo_root: Path | None = None) -> list[Finding]:
    """Return deterministic findings without modifying the manifest or repository."""
    findings: list[Finding] = []

    if not isinstance(data, dict):
        return [_finding("ROOT_TYPE", "error", "$", "manifest root must be an object")]

    for key in sorted(REQUIRED_TOP_LEVEL - data.keys()):
        findings.append(_finding("FIELD_REQUIRED", "error", f"$.{key}", "required field is missing"))
    for key in sorted(data.keys() - TOP_LEVEL_FIELDS):
        findings.append(_finding("FIELD_UNKNOWN", "error", f"$.{key}", "field is not defined by the proposed contract"))

    if "schema_version" in data and data["schema_version"] != "1.0.0":
        findings.append(_finding("SCHEMA_VERSION", "error", "$.schema_version", "expected the proposed contract version '1.0.0'"))
    if "authority_state" in data and data["authority_state"] != "proposed":
        findings.append(_finding("AUTHORITY_STATE", "error", "$.authority_state", "must remain 'proposed'; this validator cannot ratify authority"))

    if "source_document" in data and data["source_document"] is not None and not isinstance(data["source_document"], str):
        findings.append(_finding("FIELD_TYPE", "error", "$.source_document", "must be a string or null"))

    artifacts = data.get("artifacts")
    if "artifacts" not in data:
        return findings
    if not isinstance(artifacts, list):
        findings.append(_finding("FIELD_TYPE", "error", "$.artifacts", "must be an array"))
        return findings

    seen_ids: dict[str, int] = {}
    for index, item in enumerate(artifacts):
        base = f"$.artifacts[{index}]"
        if not isinstance(item, dict):
            findings.append(_finding("RECORD_TYPE", "error", base, "artifact record must be an object"))
            continue

        for key in sorted(REQUIRED_ARTIFACT - item.keys()):
            findings.append(_finding("FIELD_REQUIRED", "error", f"{base}.{key}", "required field is missing"))
        for key in sorted(item.keys() - ARTIFACT_FIELDS):
            findings.append(_finding("FIELD_UNKNOWN", "error", f"{base}.{key}", "field is not defined by the proposed contract"))

        artifact_id = item.get("artifact_id")
        if "artifact_id" in item:
            if not isinstance(artifact_id, str) or not ARTIFACT_ID_RE.fullmatch(artifact_id):
                findings.append(_finding("ARTIFACT_ID_INVALID", "error", f"{base}.artifact_id", "must match ^[A-Za-z0-9][A-Za-z0-9._-]*$"))
            elif artifact_id in seen_ids:
                findings.append(_finding("ARTIFACT_ID_DUPLICATE", "error", f"{base}.artifact_id", f"duplicate ID; first seen at artifacts[{seen_ids[artifact_id]}]"))
            else:
                seen_ids[artifact_id] = index

        status = item.get("status")
        if "status" in item and status is not None and (not isinstance(status, str) or len(status) < 1):
            findings.append(_finding("FIELD_TYPE", "error", f"{base}.status", "must be a non-empty string or null"))

        for field in ("version", "path", "source_location"):
            value = item.get(field)
            if field in item and value is not None and not isinstance(value, str):
                findings.append(_finding("FIELD_TYPE", "error", f"{base}.{field}", "must be a string or null"))

        record_state = item.get("record_state")
        if "record_state" in item and record_state not in RECORD_STATES:
            findings.append(_finding("RECORD_STATE_INVALID", "error", f"{base}.record_state", f"must be one of: {', '.join(sorted(RECORD_STATES))}"))

        notes = item.get("notes")
        if "notes" in item and (
            not isinstance(notes, list) or any(not isinstance(note, str) for note in notes)
        ):
            findings.append(_finding("FIELD_TYPE", "error", f"{base}.notes", "must be an array of strings"))

        path_value = item.get("path")
        if isinstance(path_value, str):
            path = PurePosixPath(path_value)
            if (
                not path_value
                or path.is_absolute()
                or "\\" in path_value
                or any(part in {".", ".."} for part in path.parts)
                or (path.parts and ":" in path.parts[0])
            ):
                findings.append(_finding("PATH_UNSAFE", "error", f"{base}.path", "must be a safe repository-relative POSIX path without traversal"))
            elif repo_root is not None and not (repo_root / Path(*path.parts)).exists():
                findings.append(_finding("PATH_NOT_FOUND", "warning", f"{base}.path", "path does not currently exist in the supplied repository root"))

    return findings


def validate_manifest_file(manifest_path: Path, repo_root: Path | None = None) -> list[Finding]:
    """Read and validate one JSON file; report parse/read failures as findings."""
    try:
        text = manifest_path.read_text(encoding="utf-8")
    except OSError as exc:
        return [_finding("FILE_READ_ERROR", "error", str(manifest_path), str(exc))]
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return [_finding("JSON_INVALID", "error", f"{manifest_path}:{exc.lineno}:{exc.colno}", exc.msg)]
    return validate_manifest(data, repo_root=repo_root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check a proposed SIOS registry manifest without modifying files."
    )
    parser.add_argument("manifest", type=Path, help="path to the JSON manifest")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="optional repository root used to warn about paths that do not exist",
    )
    args = parser.parse_args(argv)

    findings = validate_manifest_file(args.manifest, repo_root=args.repo_root)
    if not findings:
        print("Manifest checks passed (limited proposed-contract checks; no authority inferred).")
        return 0

    for finding in findings:
        print(finding.render())
    errors = sum(f.severity == "error" for f in findings)
    warnings = sum(f.severity == "warning" for f in findings)
    print(f"Summary: {errors} error(s), {warnings} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
