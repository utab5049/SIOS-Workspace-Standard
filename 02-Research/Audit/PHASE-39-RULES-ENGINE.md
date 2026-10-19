# Phase 39 — Deterministic Rules Engine

## Outcome

Adds a small, executable rules engine for evaluating operation preconditions against a caller-supplied JSON context. This phase moves the repository from query-only runtime code toward deterministic decision logic.

## Implementation

- tools/rules_engine.py validates a versioned declarative rules document and evaluates it without eval, dynamic code, network access, or side effects.
- tests/test_rules_engine.py covers allow/deny outcomes, nested fields, missing data, supported operators, warnings, disabled rules, malformed configuration, and CLI exit codes.
- Each rule has a unique rule_id, field, operator, and any operator-required value. Optional fields are description, enabled, severity, and message.
- Supported operators: exists, equals, not_equals, in, contains, and truthy.
- severity: block is the default and denies the decision when a rule fails. severity: warning reports a failed check without denying. Disabled rules are reported as skipped.
- Nested dictionary fields use dot paths such as request.approved. A missing field fails all checks except exists with value false.
- CLI exit codes: 0 for allow, 2 for deny, 1 for invalid input or configuration.

## Example

Rules file:

    {
      "schema_version": "1.0",
      "rules": [
        {
          "rule_id": "PRE-001",
          "field": "request.approved",
          "operator": "equals",
          "value": true,
          "message": "Approval is required"
        }
      ]
    }

Context file:

    {"request": {"approved": true}}

Run from repository root:

    python tools/rules_engine.py rules.json context.json

## Boundaries

This engine evaluates conditions and returns a decision only. It does not execute the requested operation, mutate a registry or manifest, grant authority, or resolve governance/source conflicts. A passing rule set is not proof that the rules themselves are approved or factually correct. No existing governance record or authority state is changed by this phase.
