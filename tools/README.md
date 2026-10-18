# SIOS Repository Tools

## Registry consistency validator

`registry_validator.py` is a read-only, deliberately narrow first check for a
known contradiction between the Master Artifact Index (MAI-001) and the
secondary `12-Registry` status documents.

Run from the repository root:

```sh
python tools/registry_validator.py
python -m unittest discover -s tests -v
```

The validator exits with code `1` when it finds a covered contradiction and
code `0` when no covered contradiction is found. A passing result is **not**
proof that the complete registry is correct: this first version does not yet
validate every artifact ID, version, metadata field, dependency, or link.

It never edits files and does not automatically choose which conflicting
document is authoritative. Governance owners must resolve findings explicitly.
The validator is not the SIOS Runner and does not claim to execute the research
pipeline.

## Continuous integration

The GitHub Actions workflow at `.github/workflows/registry-validator.yml` installs
the development test dependencies, compiles the Python sources, and runs the
unit-test suite on relevant pushes and pull requests. It does not gate merges on
the repository-wide validator result yet, because the current workspace contains
a known registry status contradiction that requires an explicit governance
resolution. This keeps CI failures actionable and avoids silently treating a
disputed source as authoritative.

## Proposed manifest validator

`manifest_validator.py` checks one JSON manifest against a limited
implementation of the proposed contract in
`schemas/registry-manifest.schema.json`. It checks required/unknown fields,
basic field types, artifact ID syntax and duplicates, record-state values, and
unsafe repository-relative paths. When `--repo-root` is supplied, missing
paths are warnings rather than errors because a path may be unverified or
refer to content not present in the current checkout.

Run it by passing a manifest explicitly:

```sh
python tools/manifest_validator.py path/to/manifest.json --repo-root .
```

This command uses only the Python standard library and remains dependency-free.
It is **not** a full JSON Schema validator, does not generate a manifest, does
not resolve source conflicts, and does not grant authority to the proposed
contract. A structurally valid manifest is not evidence that its records are
factually correct. Errors return exit code `1`; warnings alone return `0`.
The validator never edits files.

## Schema compatibility, fixture comparison, and coverage

`tests/test_schema_compatibility.py` compares the schema's field sets,
required fields, version and proposed-authority constants, artifact ID pattern,
record-state enum, and selected field types against the Python validator.

`tests/test_jsonschema_conformance.py` uses the `jsonschema` package's
Draft 2020-12 implementation to validate the schema itself and representative
valid/invalid data. The dependency is installed only for CI/development tests;
it is not required to run `tools/manifest_validator.py`.

`tests/test_validator_fixture_comparison.py` runs the same synthetic fixtures
through both validators and asserts the expected outcome for each. Fixtures in
`tests/fixtures/manifests/` are explicitly illustrative and are **not** records
extracted from MAI-001 or any other project source. The tests document two
intentional differences: JSON Schema alone does not enforce unique
`artifact_id` values across records, and the current schema does not encode
repository path traversal safety. The application validator rejects both cases.

See `02-Research/Audit/VALIDATION-COVERAGE-MATRIX.md` for the rule-by-rule
coverage audit, test gaps, and issues that require governance or source review.
The matrix is an engineering assessment, not an approval of the proposed
contract.

These tests cover representative cases, not every possible input or every
semantic/governance rule. Neither validator proves source accuracy, path
correctness, or governance authority. The manifest schema remains a proposal.
