---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# English package authoring guide

## Key takeaway
Author one locally sufficient Markdown object in its primary role folder and keep provenance and limits beside the claim.

## Summary
This guide applies the upstream [KPS authoring contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/ce17edc3ce9fa42e47b1d05740489291a3087fb6/docs/authoring.md) to English linguistics. It does not define another entity language. Five knowledge roles and publication-based Reference records are sufficient for this package; subsystem and interface syntheses are Models.

## Roles and identity
A Concept defines a distinction; a Principle explains a scoped declarative relationship; a Model supplies a representation, its assumptions and implications; a Method supplies a bounded operation; a Practice combines actions and decision points for a recurring purpose. Give every knowledge object one primary type and a stable ID. Its canonical folder must match the type. A role or a domain label is not scientific evidence.

Use meaningful lowercase kebab-case filenames. Metadata includes id, type, version, language and status. For the dependency-free checker, each YAML value must fit on one line and be JSON-compatible. For example:

```yaml
---
id: "english:concept:example-distinction"
type: "concept"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
evidence_status: "provisional"
reviewed: null
references: []
---
```

Domain labels are optional local metadata, not an ontology registry. Explain substantive relationships in the body. Existing uses_concepts, uses_models and similar fields declare document dependencies, not causal relations or compulsory prerequisites.

## Reconstruct knowledge for learning

Start from the target Practice: what the reader should understand, analyze or investigate, and how the response will be checked. Reuse established linguistic distinctions and models, with the adopted framework and source subset identified. Reconstruct their relevant explanations around that target and develop the Practice and supporting objects together. The [subject map](subject-map.md) owns the shared outline of the knowledge; the [learning Practice](../practices/learn-english-linguistics.md) selects from it and adds a learning route and activities. Update the subject map when topic coverage or relationships change, preserving source boundaries. Keep it authored and separate from the generated role index.

One primary type describes each document's contribution; it does not exclude supporting content from other roles. A Model may explain Concepts, and a Practice may include definitions, relationships and representations at the point of use. Useful overlap is allowed when meanings and conditions remain consistent. Split only for independent use or readability, preserving coherent explanations rather than forcing one file per topic or term. Teaching order and file boundaries are local choices, not a new linguistic taxonomy.

This is compatible local authoring guidance. The pinned upstream release and checker remain as declared; no adoption of an unpublished Core release or new metadata requirement is implied.

## Local completeness
Every substantial file has one title, Key takeaway and Summary. Its intended task must remain possible when links are hidden. Define necessary terms locally, include the actual relationship or representation, work through an example when interpretation is otherwise ambiguous, and preserve scope and counterevidence. Repeat the necessary explanation in a receiving Model without copying entire publications or creating an alternative definition.

Subsystem Models explain internal structure and interfaces, not just lists of links. Interface Models identify both representations, the proposed mapping, conditions, example and failure/uncertainty cases. Indexes are catalogs; their summaries help orientation but do not replace these explanations.

## Methods and Practices
Methods state inputs, rationale, executable steps, expected outputs and validation or stop conditions. Practices use consecutively numbered Stage1, Stage2 and later headings with a working stage map. Stage order is recommended; actual prerequisites and safety boundaries must be explicit. These are local procedural stages, not a repository-wide learning sequence.

Keep the action, necessary explanation, example, interpretation and next/fallback decision together. The upstream 9.1.0 checker supports steps-first content and does not require six repeated labels. Existing complete legacy stages remain valid. A current Practice summary contains actual recorded experience or an explicitly blank record, never fabricated results.

## References and evidence
Store publication records in references/. Identify the creator, publication, reliable date basis or undated, URL/DOI, inspected extent, specific contributions, limitations and nonclaims. A reference link alone does not support every claim in the receiving file. Preserve abstract-only access and distinguish source statements from authored synthesis and constructed examples.

New scientific claims remain provisional until actual review supports a stronger state. Framework choices, variable English usage and missing audio must be visible. Do not relabel a Canadian transcription as General American by blind symbol replacement.

## Editing and publication
Read the affected content and its dependencies. Revise locally sufficient explanations and review receiving summaries before accepting dependency fingerprints. Regenerate only the optional catalogs with tools/build_navigation.py. Run the checks in [Checks](CHECKS.md) and state failures or evidence limits honestly. One branch and one PR are enough; do not merge or create releases without authorization.

Ordinary relative Markdown links are used for navigation. Metadata IDs are not heading anchors. Prefer text representations and tables when sufficient; no visual toolchain is required for this package.
