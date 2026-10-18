# Full-Text Upgrade — SRC-000005 and SRC-000012

**Purpose:** Resolves the "13 of 16 sources abstract-only" limitation for these two sources specifically, and corrects the earlier over-generalized framing — full-text access is achievable for open-access sources via this environment's tools; it was not previously attempted for most sources, not structurally blocked.

---

## SRC-000005 Full-Text Upgrade (LLMs for Ontology Engineering)

**Bibliographic correction:** Full text reveals this paper has gone through multiple versions. The Semantic Web Journal preprint (PDF retrieved) analyzes 30 papers/41 experiments; a later SAGE-published version (2026, DOI 10.1177/22104968261465514) expands this to 36 papers/49 studies. **SRC-000005's registration should be updated to cite the SAGE version as authoritative** (it is the peer-reviewed published version), with the SWJ preprint noted as an earlier draft. Authors confirmed: Jiayi Li, Daniel Garijo, María Poveda-Villalón (Universidad Politécnica de Madrid).

### OBSU-000015 (supersedes OBSU-000003's abstract-level claim)

| Field | Value |
|---|---|
| Observation ID | OBSU-000015 |
| Source ID | SRC-000005 |
| Location | §4.1, §4.1.5 (full text) |
| Extracted Statement | The review's own quantitative breakdown (Figure 2) shows LLM research attention is heavily skewed toward the ontology implementation phase (63.4% of identified tasks — conceptualization, encoding, matching, evaluation), while ontology publication (9.8%) and especially maintenance (2.4%, a single study) are almost unaddressed in the literature reviewed. |
| Observation Type | Finding |
| Confidence | High (full-text, includes the source's own reported figures) |

### OBSU-000016

| Field | Value |
|---|---|
| Observation ID | OBSU-000016 |
| Source ID | SRC-000005 |
| Location | §4.3.5, §5.3 (full text) |
| Extracted Statement | The review reports that of 41 studies with evaluation, most define their own tasks, datasets, and metrics independently, and states plainly that this makes meaningful cross-study performance comparison rare — a methodological fragmentation problem the authors identify as a priority for future standardization work (proposing unified benchmarks as a specific recommendation). |
| Observation Type | Finding |
| Confidence | High |

### EV-000008 (new, replaces low-confidence EV portion derived from OBSU-000003)

**Primary Type:** GAP
**Linked RQ:** RQ-350 (evaluation/validation standardization), RQ-440 (ontology engineering)
**Claim:** "As of this review (2025–2026), no standardized evaluation protocol or shared benchmark set exists across LLM-assisted ontology engineering studies, resulting in results that are individually valid but not meaningfully comparable across the field."
**Support Level:** E3 (empirical — based on the review's own systematic tabulation of 41 studies' evaluation methods, not mere assertion)
**Confidence:** High
**Consistency check against EV-000006 (versioning gap) and EV-000005 (evidence-rating interpretability critique):** These three findings share a common shape — each identifies a standardization/comparability gap in a technical or methodological field, at different points along the knowledge lifecycle (ontology methodology comparability, ontology versioning, evidence-rating interpretability). This is a **cross-source pattern worth flagging explicitly in a future KOM-001/KSM-001 revision**, rather than treating these three as unrelated single-domain findings.
**Traceability:** Complete (full text, section-cited)

---

## SRC-000012 Full-Text Upgrade (Guidance to Best Tools and Practices for Systematic Reviews)

**Bibliographic correction:** Lead author confirmed as **John P. A. Ioannidis** — a highly influential meta-science/meta-research methodologist (relevant context: his prior work is foundational to the "most published research findings are false" literature). This raises this source's authority significantly above what abstract-level registration reflected.

### OBSU-000017

| Field | Value |
|---|---|
| Observation ID | OBSU-000017 |
| Source ID | SRC-000012 |
| Location | Introduction (full text) |
| Extracted Statement | The source states that a substantial proportion of published systematic reviews are methodologically flawed, biased, redundant, or uninformative despite methodological improvements and standardized appraisal tools becoming available in recent years, because authors, guideline developers, peer reviewers, and journal editors frequently do not consistently apply or enforce these updated standards. |
| Observation Type | Finding |
| Confidence | High |

### OBSU-000018

| Field | Value |
|---|---|
| Observation ID | OBSU-000018 |
| Source ID | SRC-000012 |
| Location | Abstract / Conclusion (full text) |
| Extracted Statement | The source explicitly cautions against superficial application of its own recommended tools and terminology, stating that adopting a checklist or tool by name is not a substitute for genuine methodological training or understanding of what that tool can and cannot do. |
| Observation Type | Limitation |
| Confidence | High |

### EV-000009 (new, sharpens EV-000005's original critique)

**Primary Type:** CRT
**Linked RQ:** RQ-350
**Claim:** "A leading meta-research methodologist's own guidance explicitly warns that adopting standardized review tools/checklists by name (e.g., PRISMA compliance) does not, by itself, guarantee methodological rigor — superficial or checkbox-style application of even well-designed tools is documented as a live, named risk in the field, not a hypothetical one."
**Context Summary:** This meaningfully sharpens EV-000005's earlier, softer framing ("interpretability problems... spin in conclusions") into something more pointed and directly attributable to a specific, authoritative source. It also has a **direct, uncomfortable implication for this pilot itself**: OPS-001's own checklists (§6 Session Opening Checklist, §13 Session Closing Checklist, §11.1 Pre-Registration Checks) are exactly the kind of "checklist as proxy for rigor" structure this source warns about. Completing OPS-001's checklists in this pilot (which was done, honestly, throughout) does not by itself establish that the underlying methodological rigor was achieved — only that the checklist was followed. This is worth stating plainly rather than letting checklist-completion imply more confidence than it should.
**Support Level:** E3
**Confidence:** High
**Traceability:** Complete

---

## Net Effect on Corpus Confidence

| Record | Before | After |
|---|---|---|
| EV-000005 | Medium confidence, abstract-level, generic critique | Superseded in relevance by EV-000009: High confidence, full-text, specifically attributable, self-referentially applicable to this pilot's own use of OPS-001 checklists |
| SRC-000005-derived evidence | Low-Medium (OBSU-000003, abstract) | High (OBSU-000015/016, EV-000008, full-text with the source's own reported statistics) |

**Remaining sources still abstract-only:** SRC-000002 (Gruber — likely paywalled, 1993 Elsevier journal, not attempted), SRC-000003, SRC-000004, SRC-000006, SRC-000007 (PRISMA — likely retrievable, not yet attempted), SRC-000008, SRC-000009, SRC-000010, SRC-000013/014 (already full-text — RFC standards), SRC-000015, SRC-000016 (already full-text, resolved earlier).

**Honest scope boundary:** This pass upgraded 2 of the remaining abstract-only sources as a demonstration and because they backed the two CRT-type records most central to this pilot's integrity claims. A full sweep of all remaining sources was not attempted in this turn — flagged as remaining work, not silently completed.
