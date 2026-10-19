# Phase 37 — Manifest Runtime Validation

**Status:** Implementation proposal

## Implemented

- The registry manifest JSON Schema is selected as the canonical runtime validation contract.
- The validator now uses the `jsonschema` Draft 2020-12 implementation in addition to application checks for duplicate IDs and safe repository-relative paths.
- The CLI supports `--schema`; by default it loads `schemas/registry-manifest.schema.json` from the repository.
- Tests cover canonical-schema validation and explicit schema selection.

## Safety boundary

Validation is read-only. A passing manifest does not prove source accuracy, correct artifact identity, or governance approval. MAI-001 and canonical CIR/EIR are not rewritten. C1 remains unresolved.

## Verification

CI results will be checked after the pull request is created; success will not be inferred from PR creation.
