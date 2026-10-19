# Phase 44 — Workflow State and Safe Resume

## Outcome

Added a local checkpoint file for the current single-operation workflow runner. The runner can persist lifecycle status and reuse a completed result with `--resume` when the workflow definition and referenced input files have the same fingerprint.

## Usage

```sh
python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --state state.json
python tools/workflow_runner.py examples/workflows/registry-lookup/workflow.json --state state.json --resume
```

The state file must be a relative path inside the workflow directory, its parent directory must already exist, and it cannot overwrite workflow inputs. Writes use a temporary file and atomic replacement. `--resume` requires `--state`. The rules gate is evaluated before the manifest is fingerprinted or a cached result is reused; a denied gate does not read the manifest.

## Behavior

- Persists `running` before execution and the final status/result after the run.
- Reuses a completed result only when the stored fingerprint matches the current workflow, manifest, rules, and context files.
- A changed input invalidates the checkpoint and triggers a fresh run.
- A checkpoint left in `running` is rerun from the beginning. Current operations are read-only registry queries, so this is safe for the supported operation set.
- State files contain the returned result and must be treated as local data.

## Scope and limitations

This phase does not implement a general multi-step DAG, distributed locking, crash-safe transactions for side effects, or automatic continuation from an arbitrary intermediate step. The runner currently supports only allowlisted read-only registry operations. State is not tamper-proof evidence and does not represent governance approval. The gate and proposed manifest authority remain unchanged.

## Verification

Added `tests/test_workflow_state.py` for matching resume, invalidation after input changes, path protections, and fingerprint changes. The repository CI test suite is the verification gate for this phase.
