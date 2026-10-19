# Reproducible registry lookup workflow

This is a self-contained demonstration fixture. The two registry records are synthetic examples, not authoritative SIOS artifacts.

Run from the repository root:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json

Persist a JSON execution report:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --report run-report.json

The report path is relative to this directory and must remain inside it. Keep generated run reports out of source control unless intentionally adding a reviewed fixture.

To test the gate, change approved to false or change purpose away from demonstration in context.json. The workflow should return blocked and should not load the manifest or execute the registry query.

Files:
- workflow.json: operation and local input paths
- rules.json: deterministic preconditions
- context.json: input context
- manifest.json: synthetic test data
