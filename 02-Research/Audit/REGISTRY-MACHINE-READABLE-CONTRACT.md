# SIOS Registry Machine-Readable Contract

**State:** Canonical machine-readable schema for software validation. This schema governs validation shape; it does not override MAI-001 source claims or independently ratify artifact statuses.

## Why this contract exists

The current MAI-001 summary uses grouped cells and mixed status/version formatting. Examples include ID ranges, lists of IDs sharing one status, and entries with no visible version. A parser must not guess how those entries expand or invent paths and versions.

This contract defines the JSON manifest shape used by runtime tooling. It does not rewrite MAI-001 or silently resolve disputed source data.

## Contract rules

1. **Schema authority is explicit.** The JSON Schema is the canonical shape used by runtime validation. Manifest data retains `authority_state: proposed`; this is a data-level state and does not change the schema’s role as the implementation reference.
2. **One artifact per record.** Each `artifacts[]` item describes one artifact ID. Grouped source text must not be silently expanded into multiple records.
3. **Preserve source wording.** Keep status text as written. Do not normalize `Approved (Candidate)` into `Approved` or infer missing versions.
4. **Unknown is explicit.** Use `null` for an unverified path, unspecified version, or unresolved status. Do not invent values.
5. **Provenance matters.** Include `source_location` when known and notes for ambiguities.
6. **Paths must be verified separately.** A non-null path is a claim to check against the repository; it is not proof that the file exists or is the correct artifact.
7. **Duplicate IDs are an application-level validation rule.** JSON Schema alone does not guarantee uniqueness of `artifact_id` across objects.
8. **Read-only first.** Validation reports findings; it must not edit MAI-001, secondary indexes, or artifact files.

## Fields

- `schema_version`: fixed to `1.0.0` for this contract.
- `authority_state`: fixed to `proposed` so the manifest data does not claim governance ratification.
- `source_document`: source selected for preparation, or null until governance decides.
- `artifact_id`: a single explicit artifact identifier.
- `status`, `version`, `path`: source-backed values or null where unknown.
- `record_state`: `explicit`, `grouped`, `ambiguous`, or `unverified`.
- `source_location`: optional section/row locator.
- `notes`: optional explanation of ambiguity or follow-up required.

## Validation layers and known differences

- The standard-library CLI checker provides narrow application-level checks, including duplicate IDs and repository path safety.
- CI uses the `jsonschema` package's Draft 2020-12 implementation to validate the schema and representative manifest fixtures against it.
- Shared synthetic fixtures are checked by both validators. These fixtures are test-only and are not claimed to have been extracted from project registry sources.
- Expected difference: the current JSON Schema does not enforce cross-record uniqueness of `artifact_id`; the application validator does.
- Expected difference: the current JSON Schema does not encode repository path traversal safety; the application validator does.
- Passing either layer does not establish source accuracy, path correctness, or governance authority. These are separate review questions.

## Runtime boundary

- `schemas/registry-manifest.schema.json` is the canonical machine-readable shape used by the validator.
- `tools/manifest_validator.py` applies Draft 2020-12 schema validation plus application checks for duplicate IDs and safe repository-relative paths.
- `authority_state: proposed` prevents the manifest data from claiming governance ratification; selecting the schema as the implementation reference does not certify source accuracy or settle disputed artifact status.
- The validator is read-only and never edits MAI-001, secondary indexes, or artifact files. Source-data reconciliation remains separate from running the code.
