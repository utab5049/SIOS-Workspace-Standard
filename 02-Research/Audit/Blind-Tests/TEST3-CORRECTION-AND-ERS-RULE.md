# Correction Report — Test #3's Findings Re-Checked Against Verbatim Originals

## What the direct check found

**EV-000003's actual claim** (verbatim, from EV-BATCH-001.md): *"...has cited RFC 2119 and RFC 8174 as adopted external normative references **since the Foundation Baseline v1.0 freeze (2026-07-14)**..."*

This has a precise, verifiable date — tied directly to CSL-001's own Frozen metadata. **My Blind Test Package #3, B.2, paraphrased this as "since its founding version"** — vaguer, undated, weaker. The reviewer's "temporal overclaim" finding is **correct about what I showed them, but the original Evidence Record was actually more rigorously evidenced than my test excerpt represented.**

**KSM-001's actual structure**: §4 ("Conceptual Model") contains only evidence-traced claims. §9 ("Recommended Next Actions") is a **separate, explicitly labeled non-normative section** stating the ENR-registration follow-up and next steps — clearly walled off from the evidentiary content. **My test package's B.4 excerpt blended a finding with process/status commentary into one paragraph** — a contamination *I introduced while writing the test*, not present in the real document's actual section structure.

## What this means, precisely

Test #3's general finding — that Framework-level synthesis is a real risk point for smuggling in unsupported claims — **remains a valid, valuable, generalizable principle.** But its **specific application to KSM-001** does not hold up against the verbatim original: the real document was more disciplined than the simplified excerpt I built for testing purposes.

**This is a new finding in its own right, and it belongs in the same family as the other two:** just as the pilot's own analysis overclaimed certainty beyond its evidence (Tests #1–2), **the act of constructing a "representative excerpt" for a blind test is itself a synthesis step that can introduce the very flaw being tested for.** Testing methodology is not exempt from the finding it's trying to surface.

**Decision 1 (C1) remains correctly blocked** — this correction does not mean "ratify now." It means Test #3, as run, did not actually test the real artifacts faithfully, so its "needs another look" verdict is not yet real evidence about KOM-001/KSM-001/EV-000003/EV-000004 themselves. A properly-constructed test still needs to run.

---

## Formalized Rule — New ERS-001 §6.1 (per the epistemic principle both of you converged on)

```markdown
### 6.1 Claim Granularity Principle (New)

Confidence, Support Level, and Traceability fields SHALL attach to the smallest
independently-assessable sub-claim within an Evidence Record, not automatically
inherit from a parent claim or surrounding paragraph.

**Rule ERS-R-001:** Where an Evidence Record's Claim field contains a compound
statement (e.g., a finding plus a temporal qualifier, or a finding plus a
causal/historical attribution), each qualifier that is independently checkable
SHALL carry its own verification basis, stated explicitly, rather than
inheriting the Claim's overall Support Level by default.

**Rule ERS-R-002:** When an Evidence Record or Framework document is excerpted
or summarized for any purpose (including external review), the excerpt SHALL
preserve each sub-claim's actual evidentiary basis. A summary that compresses
away a cited date, source, or qualifier while retaining the claim's original
confidence label is itself a Claim Granularity violation, regardless of who
produces the summary.
```

**Classification:** Compatible (Editorial Review) — adds a discipline requirement, changes no existing claims' status.

**Rule ERS-R-002 exists specifically because of what just happened in this engagement** — it is directly traceable to a real, observed failure mode (this reviewer's own test-excerpt construction), not a hypothetical.

---

## Test #4 — Corrected, Using Verbatim Text

*A fourth package is warranted, this time quoting EV-000003, EV-000004, and KSM-001 §4/§9 verbatim rather than paraphrasing, to test the real artifacts rather than a summary of them. Ready to build on request — flagging first rather than producing it unprompted, since Decision 1 doesn't need a fourth test immediately; it needs *a correct* one whenever the next one runs.**
