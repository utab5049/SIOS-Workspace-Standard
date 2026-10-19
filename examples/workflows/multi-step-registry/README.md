# Multi-step registry workflow example

This self-contained example uses synthetic DEMO records only. It is not authoritative SIOS registry data.

Run from the repository root:

```sh
python tools/multi_step_workflow.py examples/workflows/multi-step-registry/workflow.json
python tools/multi_step_workflow.py examples/workflows/multi-step-registry/workflow.json --state examples/workflows/multi-step-registry/state.json
python tools/multi_step_workflow.py examples/workflows/multi-step-registry/workflow.json --state examples/workflows/multi-step-registry/state.json --resume
```

Three allowlisted read-only registry operations run in dependency order. The rules gate must allow execution before the manifest is loaded. A failed step stops downstream execution. Matching fingerprints permit completed steps to be reused; changed workflow, manifest, rules, or context files invalidate the checkpoint.

Delete the generated `state.json` when no longer needed. State is local mutable data, not tamper-proof evidence. The runner does not execute shell commands, arbitrary code, network calls, or side-effecting operations.
