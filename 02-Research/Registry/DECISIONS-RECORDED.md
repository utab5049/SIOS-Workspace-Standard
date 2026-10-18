# Governance Decisions — Recorded and Decision 2 Executed

**Decision 1 (C1):** **1B — Do not ratify yet.** Status: **Blocked on independent sample review** (see BLIND-TEST-PACKAGE-3.md). No pilot artifact is to be treated as canonically registered until that review occurs.

**Decision 2 (C3):** **3A — Tables are a summary view.** Status: **Executed now**, per your own note that it has no dependency on Decision 1.

---

## Applied Amendment — MAI-001 §4

```markdown
## 4. Registry Schema

Every artifact registered in MAI-001 SHALL have a complete record containing the fields below.

The registry tables in §5 display a **Summary View** — Artifact ID, Status, Version, Path —
for readability. The complete record for each artifact (Title, Classification, Domain,
Collection, Owner, Depends On, Description) is maintained in that artifact's own document
header, which every SIOS document already carries. §5's tables are an index into that
distributed record set, not a duplicate of it.

| Field | Description | Required | Where Maintained |
|-------|-------------|----------|-------------------|
| Artifact ID | Canonical identifier | Yes | §5 table + document header |
| Status | Draft, Review, Approved, Frozen, Deprecated, Archived | Yes | §5 table + document header |
| Version | Semantic version | Yes | §5 table + document header |
| Path | Workspace path | Yes | §5 table |
| Title | Official title | Yes | Document header only |
| Classification | Artifact type | Yes | Document header only |
| Domain | Workspace domain | Yes | Document header only |
| Collection | Collection within domain | Yes | Document header only |
| Owner | Responsible entity | Yes | Document header only |
| Depends On | Artifact dependencies | No | Document header only |
| Description | Brief description | Yes | Document header only |
```

**Classification:** Compatible (per AERA-001F §5.1 — clarifies existing convention, no data loss, no structural change to what's tracked, only to how it's displayed).

**This resolves C3.** No further action needed on this item.

---

## Decision 1 — path forward

Per your own reasoning: **1B → Independent Review → Ratification.** The sample package for that review is BLIND-TEST-PACKAGE-3.md.
