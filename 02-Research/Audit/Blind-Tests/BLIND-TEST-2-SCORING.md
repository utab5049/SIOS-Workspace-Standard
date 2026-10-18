# Blind Test #2 — Scoring and Correction

## Scoring

**Not "strong confirmation," not the "naive two-definitions" error.** The reviewer found something more precise than either predicted outcome: they agreed Source 1 and 2 are conceptually aligned, but **explicitly refused to confirm the specific dependency chain** the pilot had asserted (Gruber 1993 → Gruber 1995 → Borst 1997 → Studer 1998), on the correct technical ground that **Source 2 cites the 1995/1997 works, not 1993 — and those two intermediate works were never actually registered or read by the pilot; the chain was inferred from a citation list, not verified against the texts themselves.**

This is a real, correct catch. **P2.1-COMPLETE.md stated the lineage as established fact.** It was an inference from Studer et al.'s bibliography, dressed as a confirmed historical chain.

## The pattern that now appears twice, independently

Test #1 (RFC finding): the AI stated an active "violation" where the more careful reading is "an undefined boundary."
Test #2 (this one): the AI stated a "confirmed evolutionary lineage" where the more careful reading is "textually aligned, dependency chain unverified."

**Same shape both times: correct core observation, overstated as more certain/specific than the evidence chain actually supports.** Two different reviewers, two unrelated domains (governance compliance vs. citation-lineage), same failure mode. This is now a generalizable finding about this reasoning system's output, not a one-off.

## Correction applied — EV-000001 / KOM-001 §3.1

**Old claim:** "Corpus sources trace a single evolutionary definitional lineage (Gruber 1993 → Gruber 1995 → Borst 1997 → Studer et al. 1998)."

**Corrected claim:** "Sources 1993, 2024, and 2001 (SRC-000002, SRC-000009, SRC-000016) directly cite or restate Gruber's 1993 definition. Source 1998 (SRC-000017) offers a closely-aligned definition but attributes it to Gruber (1995) and Borst (1997) — neither of which is registered or verified in this corpus. **The specific claim of a single, verified evolutionary chain from 1993 to 1998 is not established; what is established is that four sources converge on the same conceptual core, with one source's exact lineage unverified.**"

**`Support Level`:** unchanged at E1 for the core definition; **the lineage-chain sub-claim specifically should carry its own, lower rating (E1, unverified inference) rather than inheriting the core definition's confidence.**
