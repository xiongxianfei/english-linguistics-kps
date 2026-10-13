# AI contribution guidance

## Key takeaway
Automated contributors may help author and validate structure but must not fabricate linguistic evidence, source inspection, speaker data, learner outcomes or human review.

## Work method

Read KPS.md, AUTHORING.md, SCOPE.md and the target dependencies. Change canonical Markdown only; regenerate views. Prefer a bounded, evidence-aware correction over mass text generation. Preserve uncertainty, competing analyses and constructed-example labels.

## Repository rules

Every knowledge file has exactly one primary role determined by its folder. Authors may introduce domains and predicates, but must use stable kebab-case and inspect possible duplicates. Use `sources/`, not `references/`; do not create `entities/`, `ontology/` or a generic `knowledge/` store.

## Execution

Run actual checks and report failures honestly. Structural validation does not establish scientific truth. Do not disable checks, refresh evidence status or invent review records to make CI green.
