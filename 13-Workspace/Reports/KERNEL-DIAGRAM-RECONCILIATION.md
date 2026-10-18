# Kernel Diagram — Reconciliation Against Existing SIOS Structure

**Resolves:** ROADMAP.md P1.3
**Method:** Every box in the proposed diagram checked against existing Workspace Domains (00–15), Canonical Object Families (ADR-0004), the Research pipeline vocabulary (RQD-001/OUM-001/EUM-001), and Constitutional Principles (SIOS-BASELINE-001).

---

## The Proposed Diagram (as given)

```
                SIOS
                 │
      ┌──────────┴──────────┐
      │                     │
   Knowledge            Runtime
      │                     │
 Authoring           Execution
      │                     │
 Validation          APIs
      │                     │
 Compiler           MCP
      │                     │
 Knowledge Graph     LLMs
      └──────────┬──────────┘
                 │
               Users
```

---

## Box-by-Box Reconciliation

| Box | Existing SIOS Match | Verdict |
|---|---|---|
| Knowledge Authoring | 02-Research domain; OPS-001's Search→Screening→Extraction workflow | ✅ Reuse existing — rename to "Research" or "Authoring (02-Research)" |
| Validation | OPS-001 §10 (Review Operations); EUM-001B (Evidence Quality Attributes) | ✅ Reuse existing — this term is already correct as-is |
| Compiler | No direct match. Closest function: Evidence → Knowledge Model → Standard synthesis, per EUM-001's pipeline diagram and RQD-001's RQ-600 (Standardization) | ⚠️ Needs a decision — see §2 below |
| Knowledge Graph | **Not yet a canonical SIOS object.** ADR-0004 §6.2's Knowledge Object Family lists Knowledge Space, Knowledge Model, Knowledge Asset, Knowledge Component — no "Knowledge Graph." RQD-001 explicitly lists "What is a knowledge graph and how is it structured?" (RQ-450) as an **open, currently-unanswered question**, and KOM-001 itself marks RQ-450 "Insufficient Evidence — Pending." | ❌ **Problem** — see §3 below |
| Runtime Execution | No match. 04-Runner exists but is scoped to *research automation* (ARR-001: executing search queries), not to serving/deploying a live knowledge system to end users. | ⚠️ Genuinely new territory — see §4 below |
| APIs | No match, same reasoning as Runtime Execution | ⚠️ Genuinely new territory |
| MCP | No match in any Frozen document. | ❌ **Constitutional conflict** — see §5 below |
| LLMs | No match in any Frozen document. | ❌ **Constitutional conflict** — see §5 below |

---

## §2 — "Compiler": Reuse or Define Once

SIOS already has a real pipeline stage this box is pointing at — Evidence synthesized into a Knowledge Model, then into a Standard (visible in EUM-001's own position-in-pipeline diagram, and in this pilot's actual KSM-001/KOM-001 output). Two acceptable paths, either is fine, but pick one deliberately rather than leaving it implicit:

- **(a)** Rename the box to match existing vocabulary — "Synthesis" or "Standardization," directly traceable to RQ-600.
- **(b)** Keep "Compiler" as an intentional, evocative product-metaphor, but add exactly one sentence, once, in whatever document introduces this diagram: *"Compiler is this diagram's term for what RQD-001/EUM-001 specify as the Evidence → Knowledge Model → Standard synthesis stage."* Then the metaphor is allowed to exist without becoming a second, competing name for the same thing (which is what CSL-001 P6 and MFP-003 both actually prohibit — not metaphor itself, but *silent* duplication).

---

## §3 — "Knowledge Graph": This Box Is Claiming More Certainty Than SIOS Currently Has

This is the more substantive problem. The diagram places "Knowledge Graph" as a load-bearing, already-settled component of the kernel. But within SIOS's own research pipeline, *whether SIOS's knowledge should even take graph form* is an open research question with zero supporting evidence in the corpus so far (RQ-450, flagged Pending in this pilot's own KOM-001). Putting it in the poster as if it were settled output does exactly what the Architect's Trap discussion warned about: it lets an appealing idea slip into "final" status without going through the evidence gate.

**Recommendation:** Replace "Knowledge Graph" with the actually-defined, actually-canonical term from ADR-0004 — **"Knowledge Model"** — until RQ-450 is answered. If graph representation is later confirmed as the right structure, the poster can be updated then, backed by evidence, not before.

---

## §4 — "Runtime Execution" / "APIs": Legitimately New, Should Be Labeled As Such

Nothing wrong with these existing conceptually — every real system needs a serving/deployment layer eventually. But they don't correspond to anything in the current 00–15 domain structure, and 04-Runner's existing definition ("automation, execution pipelines, and research infrastructure" — AERA-001C §5) is specifically about *research* execution, not *serving knowledge to end users*. Silently treating "Runtime Execution" as if it's the same thing as 04-Runner would itself create a duplicate-definition problem.

**Recommendation:** If this becomes real, it likely needs its own future domain or a clearly-scoped extension to 04-Runner's definition — a Structural or Architectural governance decision, not something to resolve by drawing it on a poster. For now, label it explicitly as **"Runtime (proposed, not yet a Workspace Domain)"** rather than presenting it as equally settled alongside "Knowledge Authoring."

---

## §5 — "MCP" and "LLMs": Direct Conflict With CP-007 (Vendor Neutrality)

This is the sharpest finding. SIOS-BASELINE-001 §6, Constitutional Principle **CP-007 — Vendor Neutrality**, states plainly: *"No constitutional or normative standard shall depend upon proprietary technologies."*

- **MCP** (Model Context Protocol) is a specific, single-vendor-originated integration protocol. Naming it directly in SIOS's flagship diagram — the one document explicitly intended to be "the most important shape in the whole project," per the original proposal — ties that flagship image to one company's current technology choice.
- **LLMs**, as a box label, is less severe (it's a technology *category*, not a vendor), but it still anchors the diagram to the current AI paradigm specifically, when SIOS-MAN-001's own language ("future intelligent systems," "artificial intelligence systems increasingly participate...") is deliberately written to outlast any one technology generation.

**This is not a minor wording note — it is a direct, checkable conflict between a proposed artifact and a Frozen constitutional principle**, exactly the category of issue this entire pilot has been built to surface.

**Recommendation:**
- Replace "MCP" with a vendor-neutral functional label: **"Agent Interfaces"** or **"Tool Protocols"** — MCP can still be *mentioned* in explanatory prose elsewhere as *one current example* of such a protocol, which is fine (CP-007 restricts constitutional *dependency*, not *illustration*).
- Replace "LLMs" with **"Intelligent Systems"** or **"AI Consumers"** — matching SIOS-MAN-001's own chosen vocabulary, and remaining accurate even if the dominant AI architecture changes.

---

## Revised Diagram

```
                SIOS
                 │
      ┌──────────┴──────────┐
      │                     │
   Knowledge         Runtime (proposed —
   Authoring          not yet a Domain)
      │                     │
  Validation            Agent Interfaces
      │                     │
  Compiler*          (protocol-neutral)
      │                     │
 Knowledge Model     Intelligent Systems
 (RQ-450 pending)      (AI Consumers)
      └──────────┬──────────┘
                 │
               Users

*"Compiler" = Evidence → Knowledge Model → Standard synthesis (RQD-001/EUM-001)
```

---

## Summary

| Issue Type | Count | Examples |
|---|---|---|
| Clean reuse of existing vocabulary | 2 | Knowledge Authoring, Validation |
| Needs one-time explicit definition, no conflict | 1 | Compiler |
| Overclaims settled status on an open question | 1 | Knowledge Graph → Knowledge Model |
| Genuinely new, should be labeled provisional | 2 | Runtime Execution, APIs |
| **Direct conflict with a Frozen constitutional principle** | 2 | **MCP, LLMs (CP-007 violation)** |

**Recommendation to whoever owns this diagram:** don't discard it — the instinct behind it (SIOS needs one image people can understand in 30 seconds) is exactly right, and was correctly identified as more important than another specification. But ship the revised version, not the original — the current version would put a real constitutional conflict on the single most visible artifact in the entire project.
