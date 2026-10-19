# Phase 47 — Conditional Workflow Routing

## Implementation

Added optional per-step `when` conditions to the multi-step workflow runner. A condition references a completed direct dependency's output and evaluates it using a fixed operator allowlist: `equals`, `not_equals`, `in`, `contains`, `exists`, and `truthy`.

## Execution behavior

- A false condition marks the step `skipped` with reason `condition_not_met`.
- Independent eligible steps may continue.
- A step whose dependency did not complete remains skipped.
- Invalid condition shapes, operators, and non-direct dependency references are rejected.
- References traverse JSON object keys and numeric array indexes only; no expression or code evaluation is performed.
- The top-level rules gate remains before manifest loading, and registry operations remain read-only and allowlisted.

## Verification

`tests/test_workflow_conditions.py` covers true and false routing, independent branch continuation, direct-dependency enforcement, and rejection of unknown operators. The example under `examples/workflows/conditional-routing/` contains synthetic records only.

## Governance boundary

This phase adds execution control flow only. It does not approve records, change the proposed manifest authority state, or resolve governance questions. Local state is not tamper-proof evidence.
