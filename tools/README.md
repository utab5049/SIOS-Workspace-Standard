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

## Registry runtime

`registry_runtime.py` loads a manifest only after it passes the canonical schema and application-level validation. It builds an in-memory, read-only index and exposes exact-ID lookup, case-insensitive substring search, and exact status/record-state filters. Returned records are detached copies so callers cannot mutate the runtime index.

Examples from the repository root:

```sh
python tools/registry_runtime.py path/to/manifest.json list
python tools/registry_runtime.py path/to/manifest.json get SIOS-001
python tools/registry_runtime.py path/to/manifest.json search baseline
python tools/registry_runtime.py path/to/manifest.json filter --status Frozen --record-state explicit
```

The runtime does not create or infer artifact records, write back to the manifest, resolve source conflicts, or grant governance approval. It operates on a manifest supplied by the caller; this repository does not yet claim to have a reconciled production manifest. A missing ID returns exit code `2`; invalid manifest input returns `1`.

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

`tests/test_manifest_validator.py` also covers malformed JSON, missing files,
invalid root and artifact shapes, wrong nullable-field types, repository path
warnings, CLI error codes, and the read-only guarantee.

See `02-Research/Audit/VALIDATION-COVERAGE-MATRIX.md` for the rule-by-rule
coverage audit, test gaps, and issues that require governance or source review.
The matrix is an engineering assessment, not an approval of the proposed
contract.

These tests cover representative cases, not every possible input or every
semantic/governance rule. Neither validator proves source accuracy, path
correctness, or governance authority. The manifest schema remains a proposal.


## Deterministic rules engine

rules_engine.py evaluates declarative preconditions against a caller-supplied JSON context. It uses a fixed operator allowlist and never evaluates Python expressions or executes the requested operation.

Example rules file:

    {
      "schema_version": "1.0",
      "rules": [
        {
          "rule_id": "PRE-001",
          "field": "request.approved",
          "operator": "equals",
          "value": true,
          "message": "Approval is required"
        }
      ]
    }

Context file:

    {"request": {"approved": true}}

Run from the repository root:

    python tools/rules_engine.py rules.json context.json

Supported operators are exists, equals, not_equals, in, contains, and truthy. Rules default to blocking severity; failed warning rules are reported but do not deny the decision. Disabled rules are marked skipped. Nested dictionary paths use dot notation. Exit code 0 means allow, 2 means deny, and 1 means invalid configuration or input.

The engine returns a decision only. It does not execute operations, mutate the manifest, or grant governance authority. See 02-Research/Audit/PHASE-39-RULES-ENGINE.md.


## Gated workflow runner

`workflow_runner.py` connects the rules engine to a deliberately small set of read-only registry operations. A workflow JSON file points to a rules file, a context file, a manifest, and one allowlisted operation. All referenced files must exist under the workflow file's directory; absolute paths and directory traversal are rejected.

Example workflow definition:

    {
      "schema_version": "1.0",
      "workflow_id": "WF-REGISTRY-001",
      "manifest_path": "manifest.json",
      "rules_path": "rules.json",
      "context_path": "context.json",
      "operation": {
        "type": "registry.get",
        "artifact_id": "SIOS-001"
      }
    }

Run it from the repository root:

    python tools/workflow_runner.py path/to/workflow.json

Allowed operations are registry.list, registry.get, and registry.search. The rules gate runs before the manifest is loaded or an operation is dispatched. A denied gate returns status blocked and exit code 2; invalid configuration returns exit code 1; an unknown requested artifact returns exit code 3. A successful read-only operation returns exit code 0.

This is a minimal local workflow runner, not a general-purpose job executor. It does not execute shell commands, arbitrary Python, network calls, writes, or manifest changes. Rule approval and governance authority remain external to the engine.


## Reproducible workflow example and run reports

A complete synthetic workflow is available at `examples/workflows/registry-lookup/`. Run it from the repository root:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json

To persist a JSON report:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --report run-report.json

The report path is relative to the workflow directory. Its parent directory must exist; absolute paths, path traversal, and overwriting the workflow, manifest, rules, or context inputs are rejected. Reports include a UTC timestamp and the structured result. The example manifest contains synthetic DEMO records only, not authoritative SIOS data. CI exercises this example as part of the unit-test suite. See `02-Research/Audit/PHASE-41-REPRODUCIBLE-WORKFLOW.md`.


## Workflow execution history

The workflow runner supports optional append-only local run history in JSON Lines format. Use `--history` to record a compact execution trace:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --history history.jsonl

Each invocation appends a unique run ID, UTC timestamp, status, duration, gate decision, operation summary, and error when present. The history path must remain inside the workflow directory and cannot overwrite workflow inputs. Full context and operation results are deliberately excluded. This local file is not tamper-proof and is not a governance approval record. See `02-Research/Audit/PHASE-42-EXECUTION-HISTORY.md`.
