# Conditional workflow routing

Run from the repository root:

    python tools/multi_step_workflow.py examples/workflows/conditional-routing/workflow.json

A step may include `when` with a reference to a completed direct dependency, an allowlisted operator, and an optional comparison value. When the condition is false, that step is marked `skipped`; independent eligible steps may still run. A step that depends on a skipped step is skipped because its dependency did not complete.

Supported operators: `equals`, `not_equals`, `in`, `contains`, `exists`, `truthy`. References only traverse JSON object keys and numeric array indexes. Conditions do not execute expressions or code. The top-level Rules Engine gate remains mandatory and runs before the manifest is loaded. The manifest contains synthetic DEMO records only.
