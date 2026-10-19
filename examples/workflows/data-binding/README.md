# Workflow data binding example

Run from the repository root:

    python tools/multi_step_workflow.py examples/workflows/data-binding/workflow.json

A step may read a value from a completed direct dependency using an explicit reference object. Only dictionary keys and numeric list indexes are supported. Expressions and arbitrary code are not supported. The sample data is synthetic and is not authoritative SIOS registry data.
