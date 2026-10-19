# Phase 41 — Reproducible Workflow and Run Reports

## Outcome

Provides a self-contained synthetic registry lookup example that exercises workflow definition, context, rules, manifest validation, registry search, and a persisted JSON execution report.

## Example

Run from the repository root:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json

Write a report:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --report run-report.json

The report is written relative to the workflow directory. The target directory must already exist; absolute paths, directory traversal, and overwriting the workflow's input files are rejected. The report contains a report schema version, UTC generation timestamp, workflow filename, and structured workflow result.

## Repeatable test coverage

- CI runs the example workflow against its synthetic fixture data.
- Tests verify the successful gate and registry search, report generation, and refusal to overwrite inputs or write outside the workflow directory.
- The example uses invented DEMO records only. They are not extracted from or asserted as authoritative SIOS registry records.

## Boundaries

The runner remains read-only with respect to the registry manifest. The optional report is the only intentional file output. This phase does not ratify rules, resolve governance conflicts, or imply that the proposed manifest is an approved production source.
