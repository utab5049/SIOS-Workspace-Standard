# Phase 25 — Tree-Level Inventory and MAI-001 Path Crosswalk

**Status:** Tree enumeration completed; content/status reconciliation remains pending  
**Pinned source commit:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Source tree SHA:** `5bc0ff427e7937139e85d3222e65cb0f4b1ab11b`  
**Migration state:** Staged only; no canonical registry updates

## 1. Executive result

The complete recursive Git tree for the pinned source commit was retrieved. GitHub reported `truncated=false`, so the returned tree is complete for that commit.

- **217** tree entries: **168 files** and **49 directories**
- **149** Markdown files and **6** JSON files
- **122** files across the six artifact-bearing domains `01-Foundation`, `02-Research`, `03-Framework`, `04-Runner`, `07-Tools`, and `13-Workspace`
- **40** files in the bounded registry/audit/report areas used for governance reconciliation
- **48** candidate identifiers expanded from MAI-001's grouped labels
- **47** candidates have exactly one exact-basename path match in the pinned tree
- **1** candidate, `SRE-000001-A`, has no exact-basename path match in the pinned tree

An exact filename match is only path-level evidence. It does not validate file contents, lifecycle status, authority, registration state, or the truth of claims in MAI-001.

## 2. Reproducible artifacts

1. `02-Research/Registry/migration/phase-25-source-tree-manifest.json` — full recursive tree snapshot with each entry's path, type, mode, Git object SHA, and file size where available.
2. `02-Research/Registry/migration/phase-25-mai001-path-crosswalk.json` — expanded 48-ID candidate crosswalk with matched paths and explicit content/status verification flags.
3. This report — findings, limitations, and next gates.

The manifest preserves the source commit and tree identifiers. The inventory is pinned to that commit rather than the changing PR branch.

## 3. MAI-001 candidate crosswalk

The crosswalk uses exact basename matching only: an artifact identifier must equal a file basename ending in `.md` or `.json`. It deliberately avoids fuzzy substring matching, which would incorrectly treat versioned MAI-001 delta/merge documents as the canonical `MAI-001` record.

| Outcome | Count | Interpretation |
|---|---:|---|
| Exactly one exact-basename path | 47 | A path exists in the pinned tree; inspect content next |
| No exact-basename path | 1 | `SRE-000001-A`; no matching filename in this snapshot |
| Multiple exact-basename paths | 0 | No exact duplicate basename found for these candidate IDs |
| Total candidates | 48 | Expanded from the grouped labels in MAI-001 |

The missing exact path for `SRE-000001-A` is not proof that the artifact never existed or that a past review did not occur. It means only that this pinned tree contains no file with that exact basename.

## 4. Additional candidates outside the MAI-001 list

The tree also contains files that warrant classification before the OAI can be considered complete, including:

- Versioned registry and reconciliation documents: `MAI-001-FINAL-MERGE-V3.md`, `MAI-001-FINAL-MERGE-V4.md`, `MAI-001-FINAL-MERGE-V5.md`, `MAI-001-REGISTRY-DELTA.md`, and `MAI-001-REGISTRY-DELTA-V2.md`.
- Research corpus/source material: `SRC-000015-EXTRACTION.md`, `SRC-000016-RESOLUTION.md`, `SRC-000017-Studer.md`, `SRC-000018-19.md`, and the three `SRC-Batch` documents.
- Evidence and observation records under `02-Research/Evidence/Records/` and `02-Research/Observation/Records/`, including `EV-BATCH-001.md`, `EV-CORRECTIONS-BATCH-001.md`, `OBSU-BATCH-001.md`, and the `FULLTEXT-UPGRADE` records.
- Audit/review packages: AAVP parts 1–3, ICRAA parts 1–2, review batches, blind-test packages, and review protocols.
- Governance records in `02-Research/Registry/` that express conflicting claims, including `C1-RATIFIED-FINAL.md`, `DECISIONS-RECORDED.md`, `DECISION-MAI001-OPTION-B.md`, and `GOVERNANCE-DECISION-PACKAGE.md`.

These are **classification candidates**, not automatically separate OAI artifacts. Some may be source records, evidence packages, audit reports, superseded drafts, or alternate representations of the same underlying item. The next pass must classify them based on headers and contents, not filename shape alone.

## 5. Confirmed registry conflict remains

The pinned tree contains:

- `01-Foundation/Registry/MAI-001.md`, which declares itself authoritative and lists many artifact claims.
- `12-Registry/README.md` and `12-Registry/INDEX.md`, which both state that no artifacts are currently registered.
- Multiple historical or alternate MAI-001 merge/delta documents in `02-Research/Registry/`.

The tree enumeration confirms that all these files coexist in the same snapshot. It does not resolve which claim should prevail. GDR owns governance decisions; OAI should preserve provenance and the conflict until an authorized decision resolves it.

## 6. What this phase establishes — and does not establish

**Established**
- A complete, pinned path/object inventory of the repository tree at the source commit.
- An explicit, repeatable filename crosswalk for the 48 candidate identifiers transcribed and expanded from MAI-001.
- One missing exact path match and a concrete set of additional files requiring classification.
- Evidence that the current three-record OAI package is only a small initial slice, not a complete inventory.

**Not established**
- Whether every path's contents match its claimed identifier or version.
- Whether every file is an artifact requiring its own OAI record.
- Whether MAI-001's lifecycle statuses are correct or still effective.
- Whether C1's independent-review claim is substantiated.
- A meaningful overall OAI coverage percentage; the denominator requires classification of the 122 domain files and other repository content.

## 7. Next phase gates

1. Read artifact headers and relevant contents for the 47 path-matched candidates and classify each as artifact, source/evidence record, report, template, duplicate/alternate, or unresolved.
2. Investigate the `SRE-000001-A` gap using history and references; do not infer nonexistence from the current tree.
3. Classify the additional candidates listed in §4 and check for artifacts outside the six primary domains.
4. Generate proposed OAI records with exact path, source commit, source claims, lifecycle uncertainty, and reconciliation status.
5. Validate every proposed record against the OAI schema and cross-check source decision IDs against GDR.
6. Keep all records staged. Do not edit legacy registries or promote the records until a separate migration PR has reviewed the resulting reconciliation.

## 8. Decision

**Phase 25 tree enumeration: COMPLETE. Content reconciliation: NOT COMPLETE. Canonical migration: NOT APPLIED.**

`GOV-DEC-C1` remains unresolved. This phase makes no new ratification or authority decision.
