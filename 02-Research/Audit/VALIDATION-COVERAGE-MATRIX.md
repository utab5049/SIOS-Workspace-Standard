# Registry Validation Coverage Matrix

**Status:** Engineering audit of the proposed manifest checks. This document is not a governance decision and does not ratify the manifest schema.

## Scope and interpretation

This matrix describes the implementation and tests through Phase 11. “Covered” means an explicit check exists in the named layer; it does not mean every possible malformed input is handled perfectly.

Legend:
- **Yes** — explicit check exists.
- **Partial** — some related cases are covered, but the layer does not fully enforce the rule.
- **No** — no such check exists in that layer.
- **Governance** — cannot be decided by a structural validator.

## Rule-by-rule coverage

| Rule / concern | JSON Schema (Draft 2020-12) | SIOS application validator | Automated test coverage | Notes / gap |
|---|---|---|---|---|
| Root must be an object | Yes | Yes | Yes | Direct application-validator test; schema meta-validation and representative conformance tests are separate. |
| Required top-level fields | Yes | Yes | Yes | Required keys are also compared in schema compatibility tests. |
| Unknown top-level fields rejected | Yes | Yes | Yes | Both layers use a closed field set. |
| Schema version fixed to 1.0.0 | Yes | Yes | Yes | Version is a proposal constant, not a release approval. |
| Authority state remains proposed | Yes | Yes | Yes | Validators intentionally cannot ratify authority. |
| source_document is string or null | Yes | Yes | Yes | Wrong nullable-field types are directly tested for the application validator. |
| artifacts must be an array | Yes | Yes | Yes | Dedicated application-validator test. |
| Artifact record must be an object | Yes | Yes | Yes | Dedicated application-validator test. |
| Required artifact fields | Yes | Yes | Yes | Missing artifact field is tested. |
| Unknown artifact fields rejected | Yes | Yes | Yes | Covered by the conformance suite. |
| Artifact ID syntax | Yes | Yes | Yes | Pattern parity is checked; invalid ID is tested. |
| Duplicate artifact IDs across records | No | Yes | Yes | Intentional difference. Duplicate detection is an application-level rule. |
| status string/null and non-empty when string | Yes | Yes | Partial | Empty status is tested; broader boundary cases are not exhaustive. |
| version, path, source_location string/null | Yes | Yes | Yes | Wrong nullable-field types are directly tested for the application validator. |
| record_state allowed values | Yes | Yes | Yes | Invalid enum value is tested in both layers. |
| notes is an array of strings | Yes | Yes | Yes | Non-string note item is covered in the JSON Schema conformance suite. |
| Repository path traversal / unsafe path | No | Yes | Yes | Intentional difference. Schema validates a string/null shape, not filesystem safety. |
| Path exists in current checkout | No | Partial | Yes | Temporary-directory tests cover both missing-path warning and existing-path success when --repo-root is supplied. |
| JSON file can be read and parsed | No | Yes, CLI layer | Yes | Malformed JSON and missing/unreadable file findings are tested. |
| CLI exit code on malformed JSON | No | Yes | Yes | Test confirms malformed input returns exit code 1. |
| Validator leaves manifest file unchanged | Not applicable | Read-only behavior | Yes | Test compares file bytes before and after validation. |
| Schema document itself is valid Draft 2020-12 | Yes, through meta-schema check | No | Yes | Checked with Draft202012Validator.check_schema. |
| Status/version/path agree with source documents | No | No | No | Requires source review and provenance; never infer missing values. |
| Referenced path is the correct artifact | No | No | No | Existence is not identity or provenance. |
| Grouped/ranged source IDs are expanded correctly | No | No | No | Must be explicitly resolved; never silently expand grouped source rows. |
| Duplicate IDs are truly duplicates under project conventions | No | Syntactic duplicate check only | Partial | ID normalization/case policy has not been decided by governance. |
| Manifest authority / relation to MAI-001 | No | No | No | Explicit governance decision required. |
| Repository-wide registry contradictions resolved | No | No | No | The known contradiction remains unresolved; current CI does not treat it as automatically resolved. |

## Remaining engineering work

1. Consider shared schema/application fixtures for every nullable field and additional boundary values for non-empty strings.
2. Keep application-only rules (duplicate IDs and path safety) explicitly listed rather than claiming full equivalence with JSON Schema.
3. Add source-derived fixtures only after provenance and source conventions are explicitly reviewed.
4. Treat these tests as regression protection, not proof of factual accuracy or governance approval.

## Governance boundary

This matrix reports implementation coverage; it does not approve any contract rule. The JSON Schema remains proposed, no authoritative manifest is generated, and MAI-001 or the secondary registry documents must not be edited as a side effect of validation.
