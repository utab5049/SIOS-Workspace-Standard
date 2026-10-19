# Phase 48 — Standardized Step Outcomes and Errors

## Implementation

The multi-step runner now adds a normalized `outcome` field while retaining the existing `status` and `error` fields for compatibility. Outcomes distinguish `success`, `empty`, `not_found`, `failed`, `skipped`, and `not_run`.

Failure details use `error_detail` with a stable code, a human-readable message, and a `retryable` boolean. Current registry operations are read-only, so known missing-record and invalid-input errors are classified as non-retryable. No automatic retries are introduced.

## Execution behavior

- Empty search/list-like results are successful executions with an `empty` outcome.
- Exact ID lookup misses use `not_found` and `ARTIFACT_NOT_FOUND`.
- Invalid resolved step inputs fail the workflow with `INVALID_STEP_INPUT` rather than escaping as an unstructured exception.
- Other expected operation errors use `OPERATION_ERROR`.
- Steps not run because of gate denial are `not_run`; conditional/dependency/failure skips are `skipped`.
- Existing status strings and human-readable error strings remain available.

## Verification

`tests/test_workflow_outcomes.py` covers empty results, missing records, structured binding failures, downstream skipping, and gate denial. The full CI suite is the acceptance check for this phase.

## Governance boundary

This phase only standardizes runtime reporting. It does not authorize records, alter manifest authority, add side effects, or implement automatic retry behavior. Local execution state remains non-tamper-proof.
