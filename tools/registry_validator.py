#!/usr/bin/env python3
"""Read-only checks for explicit contradictions in SIOS registry status claims.

This first version intentionally checks only a narrow, known invariant:
MAI-001 contains status-bearing artifact entries, while secondary registry
documents may claim that no artifacts are registered. It does not decide
which document has governance authority and never edits repository files.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    paths: tuple[str, ...]

    def format(self) -> str:
        return f"ERROR [{self.code}] {self.message} (files: {', '.join(self.paths)})"


STATUS_ENTRY = re.compile(
    r"\|\s*(?:\*\*)?(?:Frozen|Approved|Registered|Failed)(?:\*\*)?"
    r"(?:\s|\|)",
    re.IGNORECASE,
)
EMPTY_REGISTRY_CLAIM = re.compile(
    r"no artifacts currently registered", re.IGNORECASE
)


def validate(root: Path) -> list[Finding]:
    """Return findings without changing any files."""
    mai_path = Path("01-Foundation/Registry/MAI-001.md")
    secondary_paths = (
        Path("12-Registry/README.md"),
        Path("12-Registry/INDEX.md"),
    )
    mai_file = root / mai_path

    if not mai_file.is_file():
        return [
            Finding(
                "MAI_MISSING",
                "The expected master index file does not exist.",
                (mai_path.as_posix(),),
            )
        ]

    mai_text = mai_file.read_text(encoding="utf-8")
    has_status_entries = bool(STATUS_ENTRY.search(mai_text))
    if not has_status_entries:
        return []

    findings: list[Finding] = []
    for relative_path in secondary_paths:
        file_path = root / relative_path
        if not file_path.is_file():
            continue
        content = file_path.read_text(encoding="utf-8")
        if EMPTY_REGISTRY_CLAIM.search(content):
            findings.append(
                Finding(
                    "MAI_REGISTRY_CONFLICT",
                    "MAI-001 contains status-bearing artifact entries, but this "
                    "secondary registry document says no artifacts are registered. "
                    "Resolve the authority/status discrepancy manually; no source "
                    "is automatically preferred.",
                    (mai_path.as_posix(), relative_path.as_posix()),
                )
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Workspace root to inspect (defaults to current directory).",
    )
    args = parser.parse_args(argv)

    findings = validate(args.root.resolve())
    if findings:
        for finding in findings:
            print(finding.format())
        print(f"Validation failed: {len(findings)} finding(s).")
        return 1

    print("Validation passed: no contradictions covered by this validator were found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
