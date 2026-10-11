---
language: "KPS 9.x"
package_version: "0.1.0"
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
stages: [0]
evidence_status: "provisional"
reviewed: null
references: []
---
```

Use JSON-compatible single-line values. Stable IDs are not heading fragments. Replace example fields with meaningful local content.

## Required opening

```markdown
# Semantic title

## Key takeaway
The central distinction or result.

## Summary
Its meaning, use and important limitation.
```

## Role content

A Concept defines and contrasts. A Principle explains a scoped declarative relationship and counterevidence. A Model contains an actual representation with assumptions and tests. A Method includes inputs, rationale, procedure, checks and limits. A Practice contains locally executable Stage1, Stage2 and later stages with Goal, Why, What to do, What to observe, Success signal and Next. Its current-use summary stays empty until actual application.

## Evidence status

Add a visible Evidence status section and only inspected reference contributions. Empty references mean pending external support, not self-evident scientific truth. Reference records identify publication, date basis, access extent, claim locators and nonclaims. Every new scientific object remains provisional until documented review supports a stronger status.
