# Independent Review Protocol

**Version:** 0.1.0  
**Status:** Proposed protocol — requires maintainer approval before being treated as normative.  
**Scope:** Independent review of the SIOS research pilot and its governance evidence.

## 1. Objective

Determine whether a reviewer who did not produce the target conclusions can reproduce selected research and evidence transformations, identify unsupported claims, and provide a traceable assessment of the governance records.

This protocol does not assume that previous reviews were invalid. It requires the repository to expose enough evidence to establish what was reviewed, by whom (using a privacy-preserving alias where needed), under what conditions, and with what result.

## 2. Independence declaration

Before receiving the review package, each reviewer records:

- Reviewer alias and relevant competence.
- Whether they authored, selected, summarized, or previously evaluated any target source, observation, evidence record, framework output, or governance decision.
- Any financial, organizational, or personal relationship that could reasonably affect impartiality.
- Whether any AI tools were used and what role they played.
- Whether they can assess the material without relying on the original author's conclusions.

A reviewer with a material conflict may still provide useful technical feedback, but the review must not be labelled independent without a documented rationale accepted by the governance owner.

## 3. Review package

Provide a version-pinned package containing:

1. The exact commit SHA and list of in-scope artifacts.
2. Source references and available full text, not abstracts alone where the claim requires full-text support.
3. The source → observation → evidence → framework traceability chain for sampled claims.
4. The applicable rules, rubric, and expected output format.
5. Relevant historical decisions and the specific question the reviewer must answer.
6. Known limitations, including unavailable sources or incomplete extraction.
7. A clean report template that does not disclose the original author's preferred conclusion before the reviewer records an initial judgment.

Do not change the package after review starts. Any correction requires a new version and an explicit scope note.

## 4. Minimum review tasks

- **Traceability:** Select claims and trace them backward to evidence and source passages.
- **Support:** Determine whether each cited passage actually supports the observation and the resulting claim.
- **Counterevidence:** Identify relevant contradictory evidence, alternative explanations, and uncertainty.
- **Reproducibility:** Recreate a small, predeclared sample using the documented method and record any divergence.
- **Governance:** Check whether the recorded decision, approval authority, artifact version, and registration state can be traced to evidence.
- **Limits:** State what the sample cannot establish; do not generalize beyond the reviewed scope.

The sample should be selected or approved by someone other than the original producer where practical. The selection method must be recorded before results are known.

## 5. Required output

Each reviewer submits:

- Review ID and review date.
- Reviewed commit SHA and artifact versions.
- Independence declaration and AI-use statement.
- Sample selection and method.
- Findings, each linked to a precise source location or artifact.
- Severity and rationale.
- Corrections proposed and whether each is a factual, methodological, or governance issue.
- Overall conclusion limited to the stated scope.
- Unresolved questions and confidence/limitations.
- Permission to publish the report or a redacted version.

The repository maintainer must not rewrite a reviewer conclusion. Responses and corrections should be recorded separately.

## 6. Decision and closure

A governance owner, not the review author alone, decides whether the review satisfies the applicable requirement. Record the decision, rationale, authority basis, date, and any remaining conditions in the review ledger and the appropriate decision record.

A review does not by itself ratify C1/C3, amend MAI-001, or make the Runner executable.

## 7. Acceptance criteria

The independent-review stage is complete only when:

- At least one genuinely independent review has a version-pinned package and a traceable output.
- The sample and its limitations are documented.
- Findings are dispositioned without erasing the original reviewer record.
- The governance owner records whether the review meets the relevant requirement.
- Public status summaries match the ledger and decision record.

## 8. Current status

**Not complete.** This document defines a proposed procedure; it is not itself a review, does not prove reviewer independence, and does not resolve the repository's governance-state conflicts.
