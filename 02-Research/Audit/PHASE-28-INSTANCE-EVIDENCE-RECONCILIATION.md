# Phase 28 — Source and Evidence Instance Reconciliation

**Status:** Reconciliation dataset and seven additional proposed OAI records created  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Canonical migration:** Not applied  
**C1:** Unresolved

## 1. Summary

Phase 28 checks the actual repository tree and the content of CIR-001, EIR-001, source batches, evidence batches, observation records, and correction/review artifacts. It finds that registry tables, detail-location labels, and later-added records are not fully aligned.

The machine-readable findings are in `02-Research/Registry/migration/phase-28-instance-evidence-reconciliation.json`.

## 2. CIR-001 findings

- CIR-001 claims 16 sources total but its table contains 14 source rows.
- The referenced detail-location names `SRC-CORPUS-001-ENTRIES.md` and `SRC-CORPUS-001-ENTRIES-2.md` do not exist in the pinned repository tree. Actual source registrations are grouped in `02-Research/Corpus/Sources/SRC-Batch1.md`, `SRC-Batch2.md`, and `SRC-Batch3.md`.
- Bare detail filenames such as `FULLTEXT-UPGRADE-005-012.md` and `SRE-000001-D.md` resolve to supplementary files under other directories, not necessarily to the original source-registration record. Registry paths should be explicit repository-relative paths and distinguish registration from supporting evidence.
- `SRC-000017-Studer.md` contains a later source registration marked Accepted, Full-Text, but SRC-000017 is not listed in CIR-001.
- `SRC-000018-19.md` includes SRC-000018 and SRC-000019 headings as part of a completion report. Their existence in that report does not by itself establish that both satisfy the full source-registration contract.

## 3. EIR-001 findings

- EIR-001 lists ten evidence IDs/entries, but the later `SRC-000018-19.md` report also contains `EV-000012`; its classification and conformance to the evidence-record contract need verification before adding it to EIR-001.
- Several detail locations are bare filenames. The exact repository paths include `02-Research/Corpus/Sources/SRC-000015-EXTRACTION.md`, `02-Research/Corpus/Sources/SRC-000016-RESOLUTION.md`, and `02-Research/Observation/Records/FULLTEXT-UPGRADE-005-012.md`.
- EV-000001 has conflicting status claims: EIR-001 says Needs Revision, the correction batch says Approved as a low-confidence assertion, and REVIEW-BATCH-002 records a competing-definition concern.
- EV-000003 has a later applied-corrections record (`APPLIED-CORRECTIONS-EV003-KSM001.md)) documenting version 1.1 and a split by temporal scope.
- EV-000005 is marked superseded by EV-000009, while a correction entry for EV-000005 also exists. Version and supersession chronology should be represented explicitly rather than flattened to one status.

## 4. Instance versus container

The following remain batch/report containers, not substitutes for individual records:
- `SRC-Batch1.md`, `SRC-Batch2.md`, `SRC-Batch3.md` contain source registrations.
- `EV-BATCH-001.md` and `EV-CORRECTIONS-BATCH-001.md` contain evidence versions/corrections.
- `OBSU-BATCH-001.md` contains individual observation IDs.
- `SRC-000018-19.md` is a mixed-purpose completion report with source, observation, and evidence IDs.

Phase 28 adds seven proposed OAI records for these source batches, SRC-000017, the SRC-000018/19 completion report, the EV-000003 correction artifact, and the full-text upgrade report. These proposals are stored outside the staged OAI package and do not increase canonical inventory counts.

## 5. Validation and limits

- Proposal records preserve source paths and the pinned source commit.
- CIR/EIR changes are recommendations only; no canonical registry text was changed.
- No absence conclusion is drawn from a missing detail-location file alone.
- REVIEW-BATCH-001 and REVIEW-BATCH-002 document review activity and limitations but do not establish qualifying reviewer independence.
- GOV-DEC-C1 remains unresolved.

## 6. Recommended next step

A separate migration PR should normalize repository-relative detail paths, reconcile source/evidence counts and record IDs, and preserve correction/supersession history. Before any status is changed, the relevant content must be reviewed against its schema and authorized governance requirements. The migration map and canonical staged package should be updated only after that review.
