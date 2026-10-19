# Phase 43 — Workflow History Inspector

## Outcome

Added a read-only command-line inspector for the local JSON Lines execution history introduced in Phase 42.

## Implementation

- `tools/workflow_inspector.py` loads and validates each non-empty JSONL line.
- Filters by exact run ID and status, inclusive ISO-8601 time bounds, and maximum number of newest matching runs.
- Displays a concise text summary by default or full structured JSON with `--json`.
- Reports status counts, average duration where available, workflow and operation identifiers, and recorded errors.
- Rejects malformed JSON, missing required fields, timestamps without a timezone, and inverted time ranges with a non-zero exit.
- `tests/test_workflow_inspector.py` covers JSONL parsing, malformed input, filters, sorting, limits, and JSON CLI output.

## Example

```sh
python tools/workflow_inspector.py path/to/history.jsonl
python tools/workflow_inspector.py path/to/history.jsonl --status blocked
python tools/workflow_inspector.py path/to/history.jsonl --since 2026-10-01T00:00:00Z --limit 20 --json
```

## Boundaries

The inspector only reads local history. It does not mutate records, re-run workflows, call external services, validate the truth of recorded events, or establish tamper-proof audit evidence. Empty history is a valid zero-result report. The existing proposed manifest authority state and unresolved governance decisions remain unchanged.

## Verification

Automated unit tests are included and run by the repository's existing CI workflow. The phase is complete when the pull request CI run succeeds.
