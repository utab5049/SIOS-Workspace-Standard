# Multi-step workflow example

Run `python tools/multi_step_workflow.py examples/workflows/registry-lookup/multi-step-workflow.json` from the repository root. Add `--state examples/workflows/registry-lookup/multi-step-state.json --resume` to reuse completed steps when all input fingerprints match.

The example uses synthetic DEMO records and allowlisted read-only registry operations. It does not approve governance records.
