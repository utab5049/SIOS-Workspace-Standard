# Phase 34 — CIR/EIR Contract and Record-Boundary Audit

**Status:** Proposed audit only; no registry migration applied  
**Baseline:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Reviewed branch:** `work/phase-33-cir-eir-owner-decision-gate`

## Objective

Inspect the source/evidence candidates carried forward from Phases 28–33, focusing on whether each candidate is a distinct record and whether the available repository evidence is enough to verify its controlling record contract.

This phase deliberately does **not** invent a new schema. The evidence batch identifies **ERS-001** as the evidence schema authority and describes a full nine-section structure. Field-level conformance remains unverified unless checked against that controlling definition.

## Findings

### Source candidates

- **SRC-000017** — `02-Research/Corpus/Sources/SRC-000017-Studer.md` contains identifiable bibliographic fields and labels the source Accepted, Full-Text. However, the same document embeds OBSU-000026 and prescriptive registry-update instructions. Those instructions are not, by themselves, an authorized CIR/EIR decision.
- **SRC-000018** and **SRC-000019** — both appear as subsections in `SRC-000018-19.md`, a mixed-purpose completion report. The report contains source metadata, observations, EV-000012 and roadmap closure claims. Their presence does not establish full source-contract conformance as individual registered instances.

### Evidence candidates

| ID | Current location | Boundary finding | Contract status |
|---|---|---|---|
| EV-000006 | `SRC-000016-RESOLUTION.md` | Embedded in source-resolution document | Not verified |
| EV-000007 | `SRC-000015-EXTRACTION.md` | Embedded in source-extraction document | Not verified |
| EV-000008 | `FULLTEXT-UPGRADE-005-012.md` | Embedded in multi-ID upgrade report | Not verified |
| EV-000009 | `FULLTEXT-UPGRADE-005-012.md` | Embedded in multi-ID report; supersedes EV-000005 per current claims | Not verified |
| EV-000012 | `SRC-000018-19.md` | Evidence summary embedded in completion report | Not verified as an individual evidence record |

A status reported by EIR or a completion document is not the same as contract conformance, owner adjudication, or proof of independent review. EV-000001's conflicting claims and EV-000003's correction history remain preserved from earlier phases.

## What is needed before conformance can be claimed

1. Inspect the controlling source-record contract and ERS-001 definition directly; do not infer required fields from examples alone.
2. Confirm exact boundaries and required fields for each embedded evidence entry.
3. Obtain the pending owner decisions in the Phase 33 gate, with identity, date, rationale and evidence references.
4. Update proposed CIR/EIR drafts only to reflect explicit decisions, then run validation in a separate migration PR.

## Safety invariants

- Canonical CIR/EIR unchanged.
- Staged GDR/OAI and migration map unchanged.
- No candidate source or evidence record promoted.
- No merge authorized.
- **C1 remains unresolved.**

Machine-readable detail: `02-Research/Registry/migration/phase-34-cir-eir-contract-audit.json`.
