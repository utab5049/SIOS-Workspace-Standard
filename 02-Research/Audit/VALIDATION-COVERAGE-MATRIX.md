# Registry Validation Coverage Matrix

**Status:** Engineering audit of the proposed manifest checks. This document is not a governance decision and does not ratify the manifest schema.

## Scope and interpretation

This matrix describes the current implementation on the Phase 9 branch. “Covered” means an explicit check exists in the named layer; it does not mean every possible malformed input is handled perfectly. Test references identify the closest existing tests, not exhaustive proof.

Legend:
- **Yes** — explicit check exists.
- **Partial** — some related cases are covered, but the layer does not fully enforce the rule.
- **No** — no such check exists in that layer.
- **Governance** — cannot be decided by a structural validator.

## Rule-by-rule coverage

| Rule / concern | JSON Schema (Draft 2020-12) | SIOS application validator | Automated test coverage | Notes / gap |
|---|---|---|---|---|
| Root must be an object | Yes | Yes | Partial | Schema and application behavior are tested indirectly; add a dedicated root-type fixture if this becomes a release gate. |
| Required top-level fields | Yes | Yes | Yes | Required keys are also compared in schema compatibility tests. |
| Unknown top-level fields rejected | Yes | Yes | Yes | Both layers use a closed field set. |
| Schema version fixed to 1.0.0 | Yes | Yes | Yes | Version is a proposal constant, not a release approval. |
| Authority state remains proposed | Yes | Yes | Yes | Validators intentionally cannot ratify authority. |
| source_document is string or null | Yes | Yes | Partial | Schema types are compared; the conformance suite does not yet enumerate all wrong-type cases. |
| artifacts must be an array | Yes | Yes | Partial | Application code checks this; dedicated shared fixture not yet present. |
| Artifact record must be an object | Yes | Yes | Partial | Schema enforces item type; application validator has RECORD_TYPE. |
| Required artifact fields | Yes | Yes | Yes | A missing path is included in the conformance test. |
| Unknown artifact fields rejected | Yes | Yes | Yes | Covered by the conformance suite. |
| Artifact ID syntax | Yes | Yes | Yes | Pattern parity is checked; invalid ID is tested against JSON Schema. |
| Duplicate artifact IDs across records | No | Yes | Yes | Intentional difference. Duplicate detection is an application-level rule. |
| status string/null and non-empty when string | Yes | Yes | Partial | Empty status is tested against JSON Schema; application has a corresponding check. |
| version, path, source_location string/null | Yes | Yes | Partial | Schema types are compared; exhaustive wrong-type fixture coverage is not present. |
| record_state allowed values | Yes | Yes | Yes | Invalid enum value is tested in both layers. |
| notes is an array of strings | Yes | Yes | Yes | Non-string note item is covered in the JSON Schema conformance suite. |
| Repository path traversal / unsafe path | No | Yes | Yes | Intentional difference. Schema validates a string/null shape, not filesystem safety. |
| Path exists in current checkout | No | Partial | No dedicated test | Application emits a warning only when --repo-root is supplied; path existence does not prove semantic correctness. |
| JSON file can be read and parsed | No | Yes, CLI layer | No dedicated test | CLI reports read and JSON parse errors; this is outside the in-memory validation function. |
| Schema document itself is valid Draft 2020-12 | Yes, through meta-schema check | No | Yes | Checked with Draft202012Validator.check_schema. |
| Status/version/path agree with source documents | No | No | No | Requires source review and provenance; never infer missing values. |
| Referenced path is the correct artifact | No | No | No | Existence is not identity or provenance. |
| Grouped/ranged source IDs are expanded correctly | No | No | No | Must be explicitly resolved; never silently expand grouped source rows. |
| Duplicate IDs are truly duplicates under project conventions | No | Syntactic duplicate check only | Partial | ID normalization/case policy has not been decided by governance. |
| Manifest authority / relation to MAI-001 | No | No | No | Explicit governance decision required. |
| Repository-wide registry contradictions resolved | No | No | No | The known contradiction remains unresolved; current CI does not treat it as automatically resolved. |

## Recommended next engineering tests

1. Add shared fixtures for root type, non-array artifacts, non-object artifact items, and wrong types for nullable fields.
2. Test CLI file-read and malformed-JSON findings.
3. Test --repo-root path-exists warning behavior using a temporary directory.
4. Keep application-only rules (duplicate IDs and path safety) explicitly listed rather than claiming full equivalence with JSON Schema.
5. Once governance agrees on source conventions, add reviewed source-derived fixtures with explicit provenance. Until then, retain synthetic fixtures only.

## Governance boundary

This matrix reports implementation coverage; it does not approve any contract rule. The JSON Schema remains proposed, no authoritative manifest is generated, and MAI-001 or the secondary registry documents must not be edited as a side effect of validation.
