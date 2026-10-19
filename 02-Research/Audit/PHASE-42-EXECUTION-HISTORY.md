# Phase 42 — Workflow Execution History

## Outcome

Adds optional append-only local execution history for the gated workflow runner. Each invocation creates a unique run ID and records a UTC timestamp, workflow ID when available, terminal status, elapsed milliseconds, gate decision, operation type/status, and a concise error field.

## Usage

From the repository root:

    python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --history history.jsonl

Repeat the command to append another record. Each line in the JSONL file is one independent JSON object. The parent directory must already exist. Absolute paths, traversal outside the workflow directory, and overwriting the workflow's input files are rejected.

## Design boundaries

- History is opt-in; no history file is created unless `--history` is supplied.
- The JSONL file is append-only from the runner's perspective; no list/edit/delete API is introduced.
- Records intentionally exclude full context, manifest records, and operation result payloads to reduce accidental data retention.
- A history record is an execution trace, not evidence of factual correctness, policy approval, or governance authority.
- Local JSONL storage is suitable for development and reproducible tests, not concurrent multi-process production workloads or tamper-proof audit requirements.

## Tests

Unit tests cover append behavior, unique run IDs through the CLI, line-delimited JSON parsing, and rejection of traversal and protected input paths.
