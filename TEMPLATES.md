# KPS 12 authoring templates

## Key takeaway
Canonical JSON owns metadata and a role-neutral Markdown file owns the explanation.

## Summary
The example below illustrates serialization only. Placeholder IDs must be replaced with registered entities before validation; examples do not create evidence.

## Knowledge record
```json
{
  "schema": "kps:12:entity",
  "id": "example:distinction",
  "kind": "knowledge",
  "label": "Example distinction",
  "version": "0.1.0",
  "status": "draft",
  "roles": ["kps:role:concept"],
  "domains": ["example:domain"],
  "aliases": [],
  "relations": [],
  "content": "knowledge/example-distinction.md",
  "claims": ["example:distinction:claim:key-takeaway"],
  "claim_extraction": "summary-only; other body assertions require review",
  "evidence_status": "provisional",
  "reviewed": null
}
```

The referenced Claim must declare its owner and owner_version, statement, scope and extraction provenance. The domain must be a registered Domain entity. Use [AUTHORING](AUTHORING.md) and [the core schema](schema/entity.schema.json) for remaining conditional requirements.

## Markdown explanation
Use a semantic title followed by Key takeaway, Summary and all role-specific sections. Include examples, limitations, alternatives and visible evidence state. Practice stages must remain usable without following external links. A Model must show a representation rather than only name one.

## Evidence record
Context-only records preserve a document's source linkage. Support, qualification or contradiction requires a Claim target and an inspected passage locator with an explicit assessment. Never replace a missing locator with an invented page number or a publication title.
