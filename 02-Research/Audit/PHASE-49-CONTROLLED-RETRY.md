# Phase 49 — Controlled Workflow Retry

## Scope
Add an opt-in, bounded retry policy to multi-step workflow operations. The policy defaults to a single attempt and permits at most three total attempts.

## Behavior
- Per-step configuration: `"retry": {"max_attempts": 2}`.
- Only `OSError` raised while dispatching an allowlisted read-only registry operation is retried.
- Invalid workflow configuration, invalid data bindings, and missing exact registry IDs are not retried.
- Step results include `attempts`; retries add `retry_history` entries with a stable error code and retryability flag.
- Retries are immediate, deterministic, and capped. No backoff, network access, shell execution, new write operation, or side-effecting action is introduced.

## Safety boundaries
This policy does not retry arbitrary exceptions or make non-idempotent operations safe. All currently allowlisted operations remain read-only. The manifest's `authority_state` is not changed, and no governance decision is implied.

## Validation
Automated tests cover default single-attempt behavior, transient failure followed by success, exhausted bounded attempts, invalid retry settings, and a non-retryable not-found outcome.
