# Phase 36 — Authoritative Contract Location and Completeness Audit

**Status:** Proposed audit only; no migration or governance decision applied  
**Baseline:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Parent:** Phase 35 contract conformance matrix

## Purpose

Phase 35 reported that the canonical ERS-001 definition could not be located at an assumed path. This phase checks the repository tree for the actual contract path and distinguishes path discovery from proof that a complete normative schema exists.

## Findings

### 1. ERS-001 is present, but the located file is not a complete field-level schema

The actual path is `02-Research/Evidence/ERS-001.md`. The earlier assumed path, `01-Foundation/Registry/ERS-001.md`, was incorrect.

The located file identifies itself as “Frozen v1.1.0” and lists the nine sections: Identity, Source, Research Context, Evidence Content, Classification, Quality Profile, Relationships, Lifecycle, and Governance. It then provides §6.1, Claim Granularity Principle, and rules ERS-R-001 and ERS-R-002.

However, the file as retrieved does not define required fields, data types, cardinality, validation constraints, or full normative requirements for those nine sections. Therefore, Phase 35's path-level uncertainty is resolved, but full ERS-001 conformance still cannot be certified. This is a content-completeness finding, not a claim that the file is absent.

### 2. EV-BATCH-001 demonstrates a pattern, not a substitute contract

`02-Research/Evidence/Records/EV-BATCH-001.md` explicitly names ERS-001 as schema authority and states “full 9-section structure.” Its example records visibly use the nine headings. That is useful implementation evidence, but examples cannot safely fill gaps in the normative definition.

### 3. CIR-001 and EIR-001 are located

- `02-Research/Corpus/CIR-001.md` §2 explicitly specifies seven registry-row fields: Source ID, Title, Corpus, Domain, Status, Full-Text Status, and Detail Location.
- The displayed CIR-001 §3 table has 14 rows and no explicit Corpus column, while its summary claims 16 sources and a different full-text/abstract-only split. The Phase 31–35 reconciliation and Phase 33 owner gate already track this; Phase 36 does not resolve it.
- `02-Research/Evidence/EIR-001.md` §2 defines an index table, not the full structure of an evidence record. ERS-001 remains the stated contract authority for the latter.

## Decision and next actions

1. Obtain an authorized owner decision on whether the located ERS-001 file is intentionally fragmentary, incomplete, or superseded.
2. Have the schema owner publish or restore the complete normative definition, including field-level requirements and validation constraints.
3. Rerun evidence-instance conformance only after the contract is authoritative and complete.
4. Resolve the existing Phase 33 owner decisions before modifying canonical CIR-001 or EIR-001.

## Invariants

- No canonical CIR-001 or EIR-001 edits.
- No staged GDR/OAI or migration-map changes.
- No source/evidence candidates promoted.
- No merge authorized by this phase.
- C1 remains unresolved.
