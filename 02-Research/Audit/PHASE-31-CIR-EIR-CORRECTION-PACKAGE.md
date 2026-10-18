# Phase 31 — CIR/EIR Correction Package

**Status:** Proposed correction package; canonical changes not applied  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Parent:** Phase 30 per-instance review matrix

## Deliverables

- `02-Research/Registry/migration/proposals/phase-31-correction-package/CIR-001.proposed.md`
- `02-Research/Registry/migration/proposals/phase-31-correction-package/EIR-001.proposed.md`
- `02-Research/Registry/migration/phase-31-correction-package.json`

## CIR-001 proposed corrections

The current CIR table has 14 rows. Its summary says 16 sources and 4 full-text / 12 abstract-only, which does not match those rows. The current rows classify 5 as full-text and 9 as abstract-only. The proposed draft corrects the paths to repository-relative locations and fixes the arithmetic for the rows currently listed; it does not silently add SRC-000017/018/019.

SRC-000017 has a dedicated Accepted/Full-Text file but needs an explicit registry-owner decision. SRC-000018/019 appear in a mixed-purpose completion report and need source-contract review. SRC-000001's grandfathering and SRC-000011's reserved status remain claims to verify against controlling ID records.

## EIR-001 proposed corrections

The proposed draft replaces ambiguous bare filenames with repository-relative paths and separates batch/correction/review material. It keeps the 10 current table rows and does not promote EV-000012.

- **EV-000001:** conflicting review and correction claims remain visible; no unqualified status is selected.
- **EV-000003:** preserve the version 1.1 temporal-scope split, the Needs Revision note pending independent review, and the retarget recommendation.
- **EV-000005:** preserve both correction history and supersession by EV-000009.
- **EV-000006–EV-000009:** confirm embedded record boundaries and contract compliance before migration.

## Required approvals before canonical application

1. Registry owner confirms candidate source inclusion and ID-ledger claims.
2. Evidence owner reviews disputed statuses and confirms record boundaries.
3. Validation confirms all referenced paths and required contract fields.
4. A separate PR applies only approved changes to canonical CIR/EIR files and records rollback/provenance.

## Safety boundary

This phase adds proposals only. Canonical CIR/EIR files, staged GDR/OAI records, the migration map, and C1 are unchanged. C1 remains unresolved.