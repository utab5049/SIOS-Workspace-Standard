"""Read-only query runtime for validated SIOS registry manifests."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from tools.manifest_validator import Finding, validate_manifest, validate_manifest_file


class ManifestValidationError(ValueError):
    """Raised when a manifest cannot safely be loaded into the runtime."""

    def __init__(self, findings: Iterable[Finding]):
        self.findings = tuple(findings)
        super().__init__("; ".join(f.render() for f in self.findings))


class RegistryRuntime:
    """In-memory, read-only registry index built from a validated manifest."""

    def __init__(self, manifest: dict[str, Any]):
        findings = validate_manifest(manifest)
        if findings:
            raise ManifestValidationError(findings)

        self.schema_version = manifest["schema_version"]
        self.authority_state = manifest["authority_state"]
        self.source_document = manifest.get("source_document")
        # Copy records so callers cannot mutate the source object through this runtime.
        self._records = tuple(json.loads(json.dumps(record)) for record in manifest["artifacts"])
        self._by_id = {record["artifact_id"]: record for record in self._records}

    @classmethod
    def from_file(cls, manifest_path: Path, schema_path: Path | None = None) -> "RegistryRuntime":
        """Load a JSON manifest from disk, validating before exposing records."""
        findings = validate_manifest_file(manifest_path, schema_path=schema_path)
        if findings:
            raise ManifestValidationError(findings)
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            # Protect against the file changing between validation and the read.
            raise ManifestValidationError(()) from exc
        return cls(manifest)

    def list_records(self) -> list[dict[str, Any]]:
        """Return records in manifest order, as detached copies."""
        return [json.loads(json.dumps(record)) for record in self._records]

    def get_by_id(self, artifact_id: str) -> dict[str, Any] | None:
        """Get one record by its exact artifact ID, or None when absent."""
        record = self._by_id.get(artifact_id)
        return json.loads(json.dumps(record)) if record is not None else None

    def search(self, query: str) -> list[dict[str, Any]]:
        """Case-insensitive substring search across user-facing record values."""
        needle = query.strip().casefold()
        if not needle:
            return self.list_records()

        matches = []
        for record in self._records:
            searchable = [
                record.get("artifact_id"), record.get("status"), record.get("version"),
                record.get("path"), record.get("source_location"),
                *record.get("notes", []),
            ]
            if any(needle in value.casefold() for value in searchable if isinstance(value, str)):
                matches.append(record)
        return [json.loads(json.dumps(record)) for record in matches]

    def filter_records(
        self, *, status: str | None = None, record_state: str | None = None
    ) -> list[dict[str, Any]]:
        """Filter by exact status and/or record_state, case-insensitively."""
        result = self._records
        if status is not None:
            wanted = status.strip().casefold()
            result = tuple(r for r in result if isinstance(r.get("status"), str)
                           and r["status"].strip().casefold() == wanted)
        if record_state is not None:
            wanted_state = record_state.strip().casefold()
            result = tuple(r for r in result if r.get("record_state", "").casefold() == wanted_state)
        return [json.loads(json.dumps(record)) for record in result]


def _emit(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query a validated SIOS registry manifest (read-only).")
    parser.add_argument("manifest", type=Path, help="path to registry manifest JSON")
    parser.add_argument("--schema", type=Path, default=None, help="optional JSON Schema override")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("list", help="list all registry records")
    get_parser = commands.add_parser("get", help="get one record by exact artifact ID")
    get_parser.add_argument("artifact_id")
    search_parser = commands.add_parser("search", help="search record fields by substring")
    search_parser.add_argument("query")
    filter_parser = commands.add_parser("filter", help="filter records by exact status or record state")
    filter_parser.add_argument("--status")
    filter_parser.add_argument("--record-state", choices=("explicit", "grouped", "ambiguous", "unverified"))

    args = parser.parse_args(argv)
    try:
        runtime = RegistryRuntime.from_file(args.manifest, schema_path=args.schema)
    except ManifestValidationError as exc:
        for finding in exc.findings:
            print(finding.render(), file=sys.stderr)
        if not exc.findings:
            print("ERROR MANIFEST_LOAD: manifest changed or could not be read after validation", file=sys.stderr)
        return 1

    if args.command == "list":
        _emit(runtime.list_records())
    elif args.command == "get":
        record = runtime.get_by_id(args.artifact_id)
        if record is None:
            print(f"Artifact not found: {args.artifact_id}", file=sys.stderr)
            return 2
        _emit(record)
    elif args.command == "search":
        _emit(runtime.search(args.query))
    elif args.command == "filter":
        _emit(runtime.filter_records(status=args.status, record_state=args.record_state))
    return 0


if __name__ == "__main__":
    sys.exit(main())
