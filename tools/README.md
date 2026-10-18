# SIOS Repository Tools

## Registry consistency validator

`registry_validator.py` is a read-only, deliberately narrow first check for a
known contradiction between the Master Artifact Index (MAI-001) and the
secondary `12-Registry` status documents.

Run from the repository root:

```sh
python tools/registry_validator.py
python -m unittest discover -s tests -v
```

The validator exits with code `1` when it finds a covered contradiction and
code `0` when no covered contradiction is found. A passing result is **not**
proof that the complete registry is correct: this first version does not yet
validate every artifact ID, version, metadata field, dependency, or link.

It never edits files and does not automatically choose which conflicting
document is authoritative. Governance owners must resolve findings explicitly.
The validator is not the SIOS Runner and does not claim to execute the research
pipeline.
