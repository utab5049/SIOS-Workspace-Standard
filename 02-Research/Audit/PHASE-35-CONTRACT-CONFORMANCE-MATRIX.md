# Phase 35 — Contract Conformance Matrix

**Status:** Proposed audit matrix; no migration applied  
**Baseline:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`

## Contract basis and limitation

The source registry document `02-Research/Corpus/CIR-001.md`, §2, explicitly defines seven registry-row fields: Source ID, Title, Corpus, Domain, Status, Full-Text Status, and Detail Location. This is a registry-row schema; it should not be conflated with a claim that every underlying source must have its own file.

The evidence batch `02-Research/Evidence/Records/EV-BATCH-001.md` explicitly names ERS-001 as the schema authority and describes a nine-section structure: Identity, Source, Research Context, Evidence Content, Classification, Quality Profile, Relationships, Lifecycle, and Governance. The canonical ERS-001 definition was not found at the assumed `01-Foundation/Registry/ERS-001.md` path. Therefore, this phase reports observable section coverage, not full authoritative schema conformance.

## Source registry field coverage

| Candidate | Observable fields | Result |
|---|---|---|
| SRC-000017 | ID, title, domain, status, full-text assertion, location | Partial; explicit Corpus field not established |
| SRC-000018 | ID, title, domain, status, full-text note, location | Partial embedded entry; separate record boundary and Corpus field not established |
| SRC-000019 | ID, title, domain, status, full-text note, location | Partial embedded entry; separate record boundary and Corpus field not established |

None is promoted. SRC-000018 and SRC-000019 must be assessed independently despite sharing a report.

## Evidence section coverage

| Evidence ID | Location | Result |
|---|---|---|
| EV-000006 | `SRC-000016-RESOLUTION.md` | Identity, Source, Research Context, Evidence Content, Quality Profile, Relationships and Governance are observable; Classification and Lifecycle not established in the inspected section |
| EV-000007 | `SRC-000015-EXTRACTION.md` | Same partial section coverage; Classification and Lifecycle not established in the inspected section |
| EV-000008 | `FULLTEXT-UPGRADE-005-012.md` | Evidence-summary fields only; not established as a full nine-section record |
| EV-000009 | `FULLTEXT-UPGRADE-005-012.md` | Evidence-summary fields only; not established as a full nine-section record |
| EV-000012 | `SRC-000018-19.md` | Embedded summary; not established as a full nine-section record |

“Observable” means found in the inspected material. It does not mean owner-approved, independently reviewed, or externally verified. Conversely, “not established” does not prove the information never existed elsewhere.

## Required next step

Locate the canonical ERS-001 definition and any controlling source-record contract/template, then repeat the field-by-field audit against their exact clauses. If a source-record contract does not exist, obtain an authorized governance decision rather than inventing requirements. Phase 33 owner decisions remain prerequisites to changing proposed CIR/EIR drafts.

## Invariants

- Canonical CIR/EIR unchanged.
- Staged GDR/OAI and migration map unchanged.
- No candidates promoted.
- No merge authorized.
- **C1 remains unresolved.**

Machine-readable matrix: `02-Research/Registry/migration/phase-35-contract-conformance-matrix.json`.
