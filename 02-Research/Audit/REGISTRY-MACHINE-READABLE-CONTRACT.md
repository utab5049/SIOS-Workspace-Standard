# Proposed Registry Machine-Readable Contract

**State:** Proposal only — not ratified, not an authoritative registry, and not a replacement for MAI-001.

## Why this contract exists

The current MAI-001 summary uses grouped cells and mixed status/version formatting. Examples include ID ranges, lists of IDs sharing one status, and entries with no visible version. A parser must not guess how those entries expand or invent paths and versions.

This proposal defines a separate JSON manifest shape that future tooling can validate without rewriting the current governance records.

## Contract rules

1. **No automatic authority change.** The manifest stays marked `authority_state: proposed` until an explicit governance decision ratifies its role.
2. **One artifact per record.** Each `artifacts[]` item describes one artifact ID. Grouped source text must not be silently expanded into multiple records.
3. **Preserve source wording.** Keep status text as written. Do not normalize `Approved (Candidate)` into `Approved` or infer missing versions.
4. **Unknown is explicit.** Use `null` for an unverified path, unspecified version, or unresolved status. Do not invent values.
5. **Provenance matters.** Include `source_location` when known and notes for ambiguities.
6. **Paths must be verified separately.** A non-null path is a claim to check against the repository; it is not proof that the file exists or is the correct artifact.
7. **Duplicate IDs are an application-level validation rule.** JSON Schema alone does not guarantee uniqueness of `artifact_id` across objects.
8. **Read-only first.** Validation reports findings; it must not edit MAI-001, secondary indexes, or artifact files.

## Fields

- `schema_version`: fixed to `1.0.0` for this proposal.
- `authority_state`: fixed to `proposed` so the file cannot be mistaken for ratified state.
- `source_document`: source selected for preparation, or null until governance decides.
- `artifact_id`: a single explicit artifact identifier.
- `status`, `version`, `path`: source-backed values or null where unknown.
- `record_state`: `explicit`, `grouped`, `ambiguous`, or `unverified`.
- `source_location`: optional section/row locator.
- `notes`: optional explanation of ambiguity or follow-up required.

## Activation gates

Before implementing a manifest importer or making these checks merge-blocking:

- Ratify the manifest's authority and its relationship to MAI-001.
- Define accepted artifact-ID syntax from actual repository conventions.
- Agree on status vocabulary and whether versions may be absent.
- Decide how grouped/ranged IDs are resolved and recorded.
- Verify path semantics and duplicate-ID policy.
- Add fixtures derived from reviewed source records and tests for invalid paths, duplicate IDs, missing fields, and unresolved entries.

Until those gates are closed, the existing validator remains narrow and the current MAI-001 remains unchanged. This proposal does not resolve the known disagreement between registry documents.
