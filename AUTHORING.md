# KPS 12 authoring contract

## Key takeaway
Choose one primary role, author one complete Markdown file, and let metadata plus build tools create every other organization.

## Summary
Canonical knowledge is stored in `concepts/`, `principles/`, `models/`, `methods/` and `practices/`; external provenance is stored in `sources/`. Do not add `entities/`, `ontology/`, `references/` or a generic `knowledge/` store.

## Required metadata

Every knowledge file declares `id`, `aliases`, `version`, `language`, `status`, `domains`, evidence fields, `claims`, `relations` and `sources`. Values use JSON-compatible single-line YAML. The folder supplies the primary role, so a `role` or `type` field is invalid.

Domain and predicate names may be introduced locally. Use stable lower-case kebab-case and prefer an existing term when it means the same thing. A new relation must identify a resolvable target and a layer such as `document`, `semantic` or `operational`.

## Role obligations

- Concept: Definition, Distinctions, Scope and limits.
- Principle: Statement, Explanation, Scope and counterevidence.
- Model: Purpose, Representation, Assumptions and limits, Evaluation and counterevidence.
- Method: Objective, Inputs and prerequisites, Rationale, Procedure, Expected effect, Validation and counterevidence, Limits.
- Practice: ordered Stage headings with Goal, Why, What to do, What to observe, Success signal and Next.

Every file also has one title, Key takeaway, Summary and Evidence status. Local explanation must remain useful when links are hidden.

## Claims and evidence

The `key-takeaway` claim must exactly match the visible section. Add smaller claims only when their scope and evidence can be maintained. Never infer support from a prestigious citation, invent passage locators, or promote provisional work through automation. Sources retain access extent and nonclaims.

## Interfaces

Only Models may declare `interface`. State source/target domains and representations, predicate, owning claim, scope and cardinality. Explain the mapping with an example and keep prediction separate from observation.

## Workflow

Edit canonical Markdown, run `python3 tools/build.py`, then `python3 validate.py .` and the unit tests. Review generated vocabulary changes and affected summaries before opening a bounded pull request. Generated files are never hand-authored truth.
