# Phase 51 — Workflow Summary Reports

## Purpose

Make multi-step execution results easier to assess without removing the detailed step records or changing workflow execution semantics.

## Changes

- Added a top-level `summary` to successful, failed, and rules-gate-blocked multi-step workflow results.
- Added counts for total steps and each normalized outcome, plus aggregate `successful` (success + empty) and `unsuccessful` (failed + not_found) counts.
- Added compact per-step details: outcome, declared dependencies, skip reason, error details, and dependencies that did not complete when a step was skipped for dependency failure.
- Preserved the existing `steps` records and gate-before-manifest behavior.
- Added tests for independent-branch failure recovery summaries and gate-blocked `not_run` counts.

## Boundaries

This is a reporting change only. It does not retry additional operations, alter branch recovery, add side effects, or resolve governance questions. Test fixtures are synthetic. The manifest `authority_state` remains unchanged.
