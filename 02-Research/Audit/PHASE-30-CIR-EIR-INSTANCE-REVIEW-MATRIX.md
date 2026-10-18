# Phase 30 — CIR/EIR Per-Instance Review Matrix

**Status:** Proposed review matrix; not applied to canonical registries  
**Source snapshot:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Parent:** Phase 29 controlled migration plan  
**C1:** Unresolved

## 1. Deliverable

The per-instance matrix is stored in `02-Research/Registry/migration/phase-30-instance-review-matrix.json`. It separates:
- CIR source IDs and their source registration paths;
- supplementary full-text, search, extraction, and resolution material;
- EIR evidence IDs and their batch, correction, review, or source-embedded locations;
- lifecycle/status claims that conflict or need contract-level verification.

This matrix is an audit artifact only. It does not promote records into a canonical registry.

## 2. CIR findings

- CIR-001 contains **14 table rows**, while its summary claims **16 sources**.
- The detail filenames `SRC-CORPUS-001-ENTRIES.md` and `SRC-CORPUS-001-ENTRIES-2.md` are not present in the pinned tree. The current source registration entries for IDs 000002–000006, 000007–000010, and 000012–000014 are inside `SRC-Batch1.md`, `SRC-Batch2.md`, and `SRC-Batch3.md`, respectively.
- SRC-000015 and SRC-000016 have dedicated resolution/extraction files, which also contain observations and evidence. The source, observation, and evidence identities must not be conflated.
- SRC-000017 has a dedicated file and is described there as Accepted, Full-Text, but is absent from the CIR table.
- SRC-000018 and SRC-000019 are described inside `SRC-000018-19.md`, a mixed-purpose completion report. Their presence there is a candidate registration signal, not proof that each record satisfies the full source contract.
- CIR says SRC-000001 is grandfathered and SRC-000011 was reserved but unused. These claims are preserved pending verification against their controlling identity/ID records.

## 3. EIR findings

- EIR-001 has **10 table rows** and describes its count as including the EV-000002 split and EV-000005 → EV-000009 supersession. Unique identifiers, active records, split children, and superseded records should be reported separately.
- EV-000001 has competing lifecycle and quality claims: the EIR cites Needs Revision; the correction batch records an Approved status scoped to a low-confidence/limited claim; REVIEW-BATCH-002 raises a competing-definition concern. Keep all provenance and do not collapse these into one unqualified status.
- EV-000002a and EV-000002b are split children recorded in a correction batch. Their origin and split relationship must remain explicit.
- EV-000003 has a retargeting recommendation and a separate version/scope correction artifact. The correction and recommendation history must be retained together.
- EV-000005 is described as superseded by EV-000009 and also has correction history. Supersession must not erase prior revisions.
- EV-000006 and EV-000007 are embedded in source resolution/extraction documents; EV-000008 and EV-000009 are represented in a full-text upgrade report. Verify each record boundary against the evidence contract before migration.
- EV-000012 appears in the SRC-000018/019 completion report but is absent from EIR-001. It remains a candidate, not a confirmed registered evidence record.

## 4. Recommended disposition

1. Review each row with the domain owner and verify the exact source/evidence record boundaries.
2. Decide whether to split individual records out of batch or mixed-purpose files in a separate, provenance-preserving PR.
3. Update CIR/EIR counts only after each ID has an agreed status and a contract-conformant record location.
4. Keep disputed evidence statuses unresolved until an authorized decision resolves them.
5. Keep GOV-DEC-C1 unresolved; this phase provides no independent-review ratification.

## 5. Automated guard

A unit test checks that the matrix is present, IDs are unique within each registry, and the matrix remains explicitly proposed/not applied. The test does not claim that every candidate is fully registered or that governance conflicts have been resolved.
