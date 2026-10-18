# Change Proposal — CSL-001 §5/Appendix C and MAI-001 §4

**Origin:** Findings 5(a), 5(b), 5(c) from an independent human reviewer, per BLIND-TEST-PACKAGE.md, 2026-08-04.
**Significance:** These are the first substantive findings in this entire pilot that did **not** originate from this pilot's own reasoning chain. They are treated with correspondingly higher epistemic weight than any prior self-generated proposal in this project.

---

## Finding 1 — Adoption Status of External References Is Undocumented

**As found by the reviewer:** CSL-001's Normative Language section (§5) states "SIOS adopts the terminology defined by RFC 2119 and RFC 8174," while Appendix C states external standards are "informative unless explicitly adopted as normative by the SIOS Architecture Board." **No document confirms whether that Board adoption actually occurred**, or whether §5's use of "adopts" is describing informal terminology reuse rather than the formal act Appendix C's policy requires.

**Why this is more significant than it first appears (reviewer's own observation, correctly made):** CSL-001 uses SHALL/MUST/SHOULD/MAY as its own normative language throughout, in multiple sections — so whether RFC 2119/8174's definitions were ever formally adopted, rather than just referenced, has real bearing on how binding CSL-001's own normative statements actually are.

**Proposed fix — CSL-001, Appendix C, add a new column:**

```markdown
### Current External References

| Standard | Purpose | Board Adoption Status |
|----------|---------|------------------------|
| RFC 2119 | Requirement Keywords | [TO BE CONFIRMED — see Governance Action below] |
| RFC 8174 | Interpretation of Requirement Keywords | [TO BE CONFIRMED] |
| ISO 8601 | Date & Time Representation | [TO BE CONFIRMED] |
| Unicode | Character Encoding | [TO BE CONFIRMED] |
```

**This proposal does not itself resolve the adoption question — it cannot.** Whether the Architecture Board formally adopted these standards is a factual question about SIOS's own governance history that only SIOS's real maintainers can answer, not something resolvable by amending a document's schema. **Required governance action, separate from this documentation fix:** the Architecture Board should confirm, retroactively if necessary, whether RFC 2119/8174 (and ISO 8601, Unicode) were formally adopted — and if they were never formally voted on, decide now whether to do so, given that CSL-001's own normative force has been resting on this ambiguous status since the Foundation Baseline freeze.

**Classification:** The schema addition (the new column) is **Compatible** (Editorial Review). The underlying governance confirmation is **Structural at minimum** — it is not a new rule, but it resolves a standing ambiguity in how binding CSL-001's normative language has been all along.

---

## Finding 2 — Version Control Requirement Is Unmet

**As found by the reviewer:** Appendix C states external references "SHALL... be version controlled," but the reference table lists no version or date for any entry.

**Proposed fix — CSL-001, Appendix C, add version/date columns, populated with the actual, verifiable values:**

```markdown
### Current External References

| Standard | Purpose | Version/Date | Board Adoption Status |
|----------|---------|----------------|-------------------------|
| RFC 2119 | Requirement Keywords | 1997 (BCP 14) | [TO BE CONFIRMED] |
| RFC 8174 | Interpretation of Requirement Keywords | 2017 (BCP 14, updates RFC 2119) | [TO BE CONFIRMED] |
| ISO 8601 | Date & Time Representation | [SIOS maintainers to confirm which edition is referenced — ISO 8601 has multiple revisions] | [TO BE CONFIRMED] |
| Unicode | Character Encoding | [SIOS maintainers to confirm which Unicode version is referenced] | [TO BE CONFIRMED] |
```

**Note:** RFC 2119 and RFC 8174's version/date fields above can be populated immediately and confidently — they are stable, unrevised documents with well-established publication dates (independently confirmed during this pilot's earlier research phase, and consistent with the reviewer's own description of them). ISO 8601 and Unicode cannot be responsibly filled in without SIOS's maintainers specifying which edition/version they actually mean, since both standards have multiple, materially different versions in active use.

**Classification:** Compatible (Editorial Review) for the RFC rows; requires a short maintainer decision for the ISO 8601/Unicode rows (which edition is intended) before those two can be completed — flagged as a small open item, not blocking the rest of this proposal.

---

## Finding 3 — MAI-001's Displayed Registry Tables Do Not Match Its Own Declared Schema

**As found by the reviewer:** MAI-001 §4 defines 9 required fields per artifact (Artifact ID, Title, Status, Version, Classification, Domain, Collection, Path, Owner, Depends On, Description — 11 including the two optional/conditional ones). **Every registry table actually shown in MAI-001 §5 displays only 4: Artifact ID, Status, Version, Path.** This is not confined to the section the reviewer saw (Domain 01) — this reviewer's own independent verification confirms the same 4-field pattern holds across every domain table in the full MAI-001 document.

**This is a more consequential finding than Findings 1–2, because it is systemic (affects the entire registry), not localized to one section.**

**Two possible resolutions — a governance decision is needed to choose between them, not a unilateral documentation patch:**

**Option A — MAI-001's tables are a summary view; full records exist elsewhere.**
If this is the intended design, MAI-001 §4 should be amended to say so explicitly:
```markdown
## 4. Registry Schema

Every artifact registered in MAI-001 SHALL have a complete record containing the fields below.
The registry tables in §5 display a **Summary View** (Artifact ID, Status, Version, Path only)
for readability. The complete record for each artifact, including Title, Classification, Domain,
Collection, Owner, Depends On, and Description, SHALL be maintained in [the artifact's own
document header / a separate full-record store — SIOS maintainers to specify which].
```

**Option B — The tables are meant to be complete, and are currently non-conformant.**
If this is the intended design, every entry in every MAI-001 table needs its remaining 5–7 fields populated — a substantial, likely multi-session remediation effort, not a quick fix.

**Recommendation (non-binding):** Option A is very likely the actual intent — most of the missing fields (Title, Owner, Description) are already recoverable from each artifact's own document header (every SIOS document reviewed in this pilot has this metadata at the top), meaning the information isn't lost, just not duplicated into MAI-001's summary table. This mirrors the precedent this pilot itself used for CIR-001/EIR-001 (summary registries pointing to full detail elsewhere) — but this recommendation should not be treated as settled without the Architecture Board actually choosing between A and B, since B is also a legitimate design choice with different tradeoffs (a single-source-of-truth table vs. a distributed-but-linked model).

**Classification:** **Structural** (Architecture Review required) — this changes how MAI-001's own core schema section is interpreted project-wide, not a single localized edit.

---

## Summary Table

| Finding | Fix Type | Classification | Blocking? |
|---|---|---|---|
| 1 — Adoption status undocumented | Schema column + governance confirmation | Compatible (doc) + Structural (governance fact-finding) | Governance action needed; doc fix can proceed independently |
| 2 — Version control unmet | Schema columns, partially pre-fillable | Compatible | RFC rows: no. ISO 8601/Unicode rows: needs a maintainer decision first |
| 3 — Registry table/schema mismatch | Clarify Summary View vs. Full Record (recommended: Option A) | **Structural** | Yes — affects interpretation of the entire MAI-001 registry, should be resolved before further registry entries (including this pilot's own pending CIR-001/EIR-001/KOM-001/KSM-001 merge) are treated as fully conformant |

---

## Note on Provenance and Confidence

Unlike every prior change proposal in this pilot (all self-generated through AI self-review), **these three findings originated from a human reader outside this reasoning chain**, working from raw source material with no access to this pilot's conclusions. Per the pilot's own established convention of taking self-generated findings less at face value than externally-sourced ones, **this proposal should be given priority review over any still-pending, self-generated proposal from earlier in this pilot** (e.g., the EUM-001/ERS-001/SFA-001 amendments), precisely because its evidentiary basis is stronger.
