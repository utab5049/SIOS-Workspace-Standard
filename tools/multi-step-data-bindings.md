# Multi-step workflow data bindings

An operation argument may reference an earlier step result using an explicit object:

    {"$ref": {"step_id": "search_records", "path": "result.0.artifact_id"}}

The source step must be a declared direct dependency and must have completed with a result. The path traverses dictionary keys and numeric list indexes only. The resolved value must be a non-empty string, suitable for the current registry operation arguments. There is no expression language, template evaluation, or arbitrary code execution.

Example: `examples/workflows/data-binding/workflow.json`. The example uses synthetic records only.
