# Phase 38 — Registry Runtime

**Goal:** Move from checking manifest structure to using validated manifest data from executable code.

## Delivered

- Added `tools/registry_runtime.py` as a small, read-only in-memory registry runtime.
- Added exact ID lookup, list, case-insensitive substring search, and combined exact status/record-state filtering.
- Runtime refuses to load invalid manifests and returns detached copies to prevent callers from mutating its in-memory index.
- Added CLI commands and unit tests for query behavior, input validation, isolation, and exit codes.

## Examples

```sh
python tools/registry_runtime.py path/to/manifest.json list
python tools/registry_runtime.py path/to/manifest.json get SIOS-001
python tools/registry_runtime.py path/to/manifest.json search baseline
python tools/registry_runtime.py path/to/manifest.json filter --status Frozen --record-state explicit
```

## Boundaries

The runtime is read-only. It does not generate a source manifest, infer missing artifact records, update MAI-001/CIR/EIR, settle disputed statuses, or imply governance approval. A reconciled production manifest remains a separate source-data task.

## Verification

The existing CI workflow compiles the Python sources and runs the full unittest suite. CI results will be checked after opening the PR.
