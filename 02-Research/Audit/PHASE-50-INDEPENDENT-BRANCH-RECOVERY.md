# Phase 50 — Independent Branch Recovery

## Scope
Allow independent workflow branches to continue after an individual step fails, while preventing downstream steps from running when their dependencies did not complete.

## Behavior
- A failed step is recorded with its existing structured outcome/error details.
- Any step whose dependencies are not completed is marked `skipped` with reason `dependency_not_completed`.
- Independent steps remain eligible for execution after failures.
- A not-found exact registry lookup marks the overall workflow as failed but does not stop unrelated branches.
- The overall status remains `operation_failed` if any operation fails, even when independent steps succeed.

## Safety boundaries
This is branch-level recovery, not rollback, compensation, or an assertion that the workflow fully succeeded. Existing operations remain read-only. No new side effects, arbitrary execution, network access, or governance decisions are introduced. `authority_state: proposed` remains unchanged.

## Validation
Tests cover an execution error with both dependent and independent steps, and a not-found result followed by an independent successful step.
