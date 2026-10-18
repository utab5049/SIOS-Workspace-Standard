# P2.1 Complete — SRC-000017 (Studer, Benjamins, Fensel 1998) Registered, Full Text

---

## SRC-000017

**Title:** Knowledge Engineering: Principles and Methods
**Authors:** Studer, R.; Benjamins, V.R.; Fensel, D.
**Year:** 1998
**Journal:** Data & Knowledge Engineering, 25(1-2), 161-197
**DOI:** 10.1016/S0169-023X(97)00056-6
**Open Access Copy:** KIT institutional repository (publikationen.bibliothek.kit.edu/189497/3003)
**Domain:** Ontology Engineering (Domain C) / Knowledge Organization (Domain B)
**Corpus:** CORPUS-001
**Status:** Accepted, Full-Text
**Citation Count:** 489+ (per ACM record)

---

## OBSU-000026

| Field | Value |
|---|---|
| Observation ID | OBSU-000026 |
| Source ID | SRC-000017 |
| Location | §6.1 (full text) |
| Extracted Statement | The source states its working definition — an ontology is a formal, explicit specification of a shared conceptualization — and explicitly attributes this definition to two prior works, cited as references [74] and [22] in its own bibliography: **Gruber's 1995 paper** ("Towards Principles for the Design of Ontologies used for Knowledge Sharing") and **Borst's 1997 PhD thesis** ("Construction of Engineering Ontologies"). |
| Observation Type | Definition |
| Confidence | High |

---

## The Correction This Resolves

**Earlier framing (REVIEW-BATCH-002, Finding 1; later softened in FULLTEXT-UPGRADE-009) treated this as "Gruber (1993) vs. Studer et al. (1998)" — two competing definitions.** That framing was itself imprecise. The full text shows:

```
Gruber (1993) — original definition, in the pilot corpus as SRC-000002
      │
      ▼
Gruber (1995) — refined definition — NOT currently in this corpus
      │         (co-cited with Borst 1997 by Studer et al.)
      ▼
Borst (1997) — adds emphasis on "shared" and formality — NOT currently in this corpus
      │
      ▼
Studer, Benjamins, Fensel (1998) — synthesizes both — SRC-000017 in this corpus
```

This is a **single evolving lineage**, not two rival schools. SRC-000005 (which uses the Studer wording) is not disagreeing with Gruber's original 1993 work — it's citing a later, refined descendant of it.

## Final, Precise Correction to EV-000001

**`Consistency` field, final wording:** *"Consistent — corpus sources trace a single evolutionary definitional lineage (Gruber 1993 → Gruber 1995 → Borst 1997 → Studer et al. 1998), not two competing definitions. SRC-000002 anchors the lineage's origin; SRC-000005 and SRC-000017 reflect its 1998 refinement; SRC-000009 and SRC-000016 independently cite the 1993 original directly. No genuine conflict exists in this corpus — only citation-generation depth."*

**This is the true final state of a claim that went through four correction cycles** (original overclaim → adversarial overcorrection → majority-position softening → this lineage clarification, which is the first version actually grounded in reading the connecting text rather than inferring from which name appears in each abstract). **This is also a small, honest lesson about this pilot's own method:** the two intermediate "corrections" were each reasonable given what was known at the time, and each was still wrong in a specific, nameable way — which is exactly why OPS-001's rule against deleting prior versions matters. The path to the right answer ran directly through two wrong ones.

---

## Registry Updates

- **CIR-001:** Add SRC-000017 (17th source; full-text).
- **EIR-001:** EV-000001 finalized as above — this closes out the item permanently, with no further open question.
- **KOM-001:** §3.1's "one alternative on record, not yet independently sourced" note is now obsolete — replace with the lineage diagram above. This is a real, final content update to KOM-001, not just a registry bookkeeping change.

## P2.1 Status: Complete

The task specified in ROADMAP.md P2.1 ("register Studer et al. 1998 independently") is done, and it produced a better answer than the task's own framing anticipated — it didn't just add a second source to compare against the first, it revealed the two weren't in tension to begin with.
