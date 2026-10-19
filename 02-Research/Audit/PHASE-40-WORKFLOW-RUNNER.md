# Phase 40 — Gated Workflow Runner

## Outcome

Connects the read-only Registry Runtime and deterministic Rules Engine through one minimal end-to-end workflow. The runner validates a workflow definition, loads a JSON context, evaluates preconditions, and dispatches a limited read-only registry operation only when the gate allows it.

## Implementation

- tools/workflow_runner.py provides the CLI and orchestration.
- tests/test_workflow_runner.py covers allow/deny flow, registry get/list/search, invalid operation types, path traversal, and missing artifact behavior.
- A workflow document declares schema_version 1.0, workflow_id, manifest_path, rules_path, context_path, and an operation.
- Supported operation types are registry.list, registry.get, and registry.search.
- Referenced files must be relative to the workflow file's directory and remain inside that directory.
- Gate denial returns status blocked and CLI exit code 2. Invalid input returns 1. A requested but missing artifact returns operation_failed and exit code 3. Successful read-only operations return 0.

## Execution order

1. Validate the workflow shape and operation allowlist.
2. Resolve and load rules and context files.
3. Evaluate all enabled preconditions.
4. If denied, return the gate report without loading the manifest or dispatching an operation.
5. If allowed, validate/load the manifest using Registry Runtime and perform the selected read-only query.
6. Return a structured JSON envelope containing workflow ID, status, gate report, and operation result.

## Boundaries

The runner is not a general-purpose executor. It does not run shell commands or arbitrary code, access the network, mutate files, change manifests, or approve governance records. The allow decision means only that the supplied rules passed for the supplied context; it does not certify the correctness or authority of those rules. The manifest and rule sources remain caller-supplied inputs.

This phase intentionally implements a thin orchestration layer rather than a new service or agent architecture.
