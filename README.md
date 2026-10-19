# SIOS Website: sios.ir

**Identity:** SIOS is the canonical project identity.

This is the SIOS Enterprise Workspace, as originally frozen 2026-07-14, **plus the complete record of the first research pilot ever executed against it**: real sources, real evidence, the first content in 03-Framework, four independent blind human reviews, a 22-phase adversarial architecture validation, an independent cross-repository audit, two ratified governance decisions, and four amended Frozen documents (all additive — nothing original was rewritten).

**Start here:**
- `WORKSPACE_MANIFEST.md` — workspace identity and principles (original)
- `13-Workspace/ARS-001.md` — a 15-minute narrative walkthrough of what actually happened, told through one real finding
- `13-Workspace/Reports/FINAL-REPORT.md` — compact pilot results summary
- `13-Workspace/Reports/COMPREHENSIVE-STATUS-REPORT.md` — the historical comprehensive status report
- `13-Workspace/Reports/CURRENT-STATE-RECONCILIATION-2026-10.md` — current conflicts and decisions required before implementation
- `02-Research/Audit/ICRAA-Part1.md` — the most rigorous available check on everything else in this archive
- `02-Research/Audit/REVIEW-LEDGER.md` — review claims and evidence ledger
- `02-Research/Audit/INDEPENDENT-REVIEW-PROTOCOL.md` — proposed method for independent review
- `CHANGELOG.md` — every change made to the original Frozen baseline, in one place


## Controlled workflow retries

Multi-step workflow steps may opt into a bounded retry policy with `"retry": {"max_attempts": 2}`. The value includes the initial attempt and must be an integer from 1 to 3. Omitting the policy means one attempt, with no retry. Only `OSError` raised during the read-only operation dispatch is retried; validation errors, invalid bindings, and exact-ID misses are not. Results expose the total `attempts` and, when retries occur, a concise `retry_history`. Retries are immediate and bounded; this does not add retries for side effects or make local history tamper-proof.


## Workflow failure recovery

The multi-step runner continues evaluating independent branches after a step fails. Steps whose declared dependencies did not complete are marked `skipped`; independent steps may still complete. The overall workflow status remains `operation_failed` if any step fails or an exact registry lookup is not found, even when other steps succeed. This is best-effort branch recovery, not rollback or compensation. Workflow operations remain read-only, and no governance state is changed.

## Workflow summary reports

Multi-step workflow results include a `summary` alongside the existing detailed `steps` array. The summary reports total, successful, empty, not-found, failed, skipped, and not-run counts, plus a compact per-step view with dependencies, skip reasons, errors, and dependencies that prevented a step from running. The detailed step results remain available for compatibility. A rules-gate denial reports all steps as `not_run`; summaries are diagnostic only and do not change execution or governance decisions.

