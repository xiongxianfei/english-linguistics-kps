---
language: "KPS 9.x"
package_version: "0.2.0"
status: "draft"
---

# English knowledge templates

## Key takeaway
Templates implement the KPS contract but do not establish that a claim has evidence.

## Summary
Templates implement the KPS contract but do not establish that a claim has evidence. The initial broad release remains provisional; supporting links and checks do not constitute independent scientific review.

## Metadata

```yaml
---
id: "english:concept:example"
type: "concept"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
domains: ["foundations"]
evidence_status: "provisional"
reviewed: null
references: []
---
```

Use JSON-compatible single-line values. Stable IDs are not heading fragments. Replace example fields with meaningful local content.

## Opening for other roles

```markdown
# Semantic title

## Key takeaway
The central distinction or result.

## Summary
Its meaning, use and important limitation.
```

## Model opening

```markdown
# Subsystem name

A short introduction explaining what the Model helps readers understand
and the scope it covers.

## Contents

- [Subject topic](#subject-topic)

## Subject topic

Explain the subject using headings that make its important topics visible.
```

Determine coverage from credible disciplinary sources and the intended scope, then reconcile it with the body-of-knowledge outline. Explain essential parts, relationships and relevant interfaces locally. Identify assumptions, evidence limits and significant omissions wherever they help the reader. These are responsibilities, not prescribed headings. There is no fixed topic count, illustration quota or repeated topic template. Existing useful sections may remain; Key takeaway and Summary are optional for Models.

## Role content

A Concept defines and contrasts. A Principle explains a scoped declarative relationship and counterevidence. A subsystem Model contains its central question, essential terms, representation, parts and relationships, examples where useful, interface explanations, assumptions and limits. Component and interface explanations stay inside the ten subsystem Models. A Method includes inputs, rationale, procedure, checks and limits. A Practice contains locally executable Stage1, Stage2 and later stages with prerequisites, numbered actions or a decision table, necessary explanation, expected output and fallback decisions. Use a stage map and keep each stage usable without leaving the file. Fixed repeated labels are optional, not required. New steps-first Practices declare practice_format: "steps-first-v1". The current-use summary contains only recorded experience or an explicitly blank record.

## Evidence status

Keep evidence status visible in the body and attach only inspected reference contributions. Models may integrate this into subject-appropriate prose; other roles retain their Evidence status section. Empty references mean pending external support, not self-evident scientific truth. Reference records identify publication, date basis, access extent, claim locators and nonclaims. Every new scientific object remains provisional until documented review supports a stronger status.
