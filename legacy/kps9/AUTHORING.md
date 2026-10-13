---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# KPS Authoring Contract

## Key takeaway
This is the single normative KPS 9.x authoring contract; examples and domain repositories must implement it rather than redefine it.

## Summary
This is the single normative KPS 9.x authoring contract; examples and domain repositories must implement it rather than redefine it.

## Authority and scope
This document defines the **KPS 9.x authoring convention** for the five knowledge roles, publication-based Reference records, self-contained content, metadata, naming, stage headings and local links. `TEMPLATES.md`, `NAVIGATION.md` and Methods provide examples or implementation guidance, not competing authoring requirements. This is a project convention, not a universally standardized Markdown dialect.

An *incompatible change to these requirements* needs a new KPS language major version; compatible explanations, tooling and optional guidance may change within 9.x. A domain package declares `kps_language: "9.x"` and separately records the KPS release it was checked against.

## Folder roles
- `concepts/`: one reusable definition or distinction per document.
- `principles/`: one explanatory, scoped, declarative relationship per document; a **command or chosen engineering constraint** is not itself a Principle.
- `models/`: a representation with essential terms, relationships, assumptions, implications and limits.
- `methods/`: a repeatable operation with objective, prerequisites, rationale, executable steps, observations, expected effect and validation/counterevidence.
- `practices/`: a staged operational synthesis that is usable without reading all its links. A Practice can compose other Practices when goals and decision logic genuinely warrant it, but stages do not each require a separate file.
- `references/`: structured Markdown provenance records identifying actual external publications, claim contributions, checked extent, limits and non-claims. **References are not a sixth knowledge type.**

Supporting root-level documents and verification tooling are infrastructure, not extra knowledge types.

## Filename and identity
Use lowercase, meaningful kebab-case filenames, such as `independent-representations-can-diverge.md` for a Principle, `compare-evidence.md` for a Method or `build-domain-knowledge.md` for a Practice. Reference filenames identify the **publication**, normally `creator-year-short-title.md`, `creator-undated-short-title.md`, or `organization-standard-id-year.md` when the official identifier matters. Do not infer a publication year from the date accessed.

Metadata must include a stable `id`, `type`, `version`, `language` and `status` for a knowledge object. Stable IDs are **not** Markdown link anchors. Metadata is for identities, indexing and typed dependency hints; body prose explains why the relationships matter.

```yaml
---
id: "domain:method:compare-evidence"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
uses_principles: []
uses_models: []
references: []
---
```

The included dependency-free validator accepts JSON-compatible single-line YAML field values. This is a deliberate limited profile; it is not a general YAML parser.

## Local completeness
All substantial Markdown knowledge and Reference files use one semantic `# Title`, `## Key takeaway`, and `## Summary`, then locally sufficient meaning, procedure or representation, examples as appropriate, limits and deeper links. Hide links and ask whether the intended understanding/use task still works; then restore links and check the local summary faithfully preserves its source's relevant conditions. Do **not** copy all linked sources into each file.

Knowledge by role must be self-contained: a Principle explains the actual relationship, not merely a command; a Model includes its representation rather than only a link; a Method includes actionable steps and safeguards; a Practice contains operationally sufficient information **in each stage**, not a list of Methods to visit elsewhere.

## Practice stages
A Practice heading uses **exactly** the compact pattern below, consecutively numbered in its current recommended/default order:

```markdown
## Stage1 Breathing and air access
## Stage2 Body support and recovery
## Stage3 Kick preparation and completion
```

**Stage numbers communicate recommended order**, not mandatory sequential completion and not permanent identity. Stage prerequisites and real-world safety/authority boundaries state actual dependencies. Keep the Stage name semantic and visible; avoid opaque code headings such as `TI-03` or `F4`.

At the beginning of each stage, include compact **Goal**, **Why**, **What to do**, **What to observe**, **Success signal**, and **Next** labels, followed by enough understanding, procedure, troubleshooting and stopping/fallback guidance to act without reading linked objects. Use bold repeated labels rather than identical repeated `### Summary` headings. At the start of each Practice include a global Summary and a stage map; at the end, include a current working summary based only on actual recorded experience.

## Markdown links
KPS uses UTF-8 `.md`, ordinary inline relative file links and conservative heading fragments; avoid application-specific wikilinks, embedded HTML anchors and renderer-dependent extensions. For links to a full file, use `[Text](../models/example.md)` rather than a fragile section fragment. For section links, the destination must match the complete real heading under the chosen lowercase/hyphenated profile:

```markdown
[Stage1 Breathing and air access](#stage1-breathing-and-air-access)

## Stage1 Breathing and air access
```

No YAML identity or prefix such as `TI-03` creates an anchor automatically. When renumbering or renaming a Stage, update the heading, stage map and incoming links together. Strict CommonMark itself does not define heading identifiers; test the actual reader when renderer fidelity is important. `NAVIGATION.md` contains explanatory examples, not a second contract.

## Evidence and reference records
Start with a question and candidate claim, identify required evidence, inspect what sources actually establish, check independence and disagreement when material, and separate source premises from KPS's inference. A single directly authoritative source may establish its own definition; multiple citations to one underlying study are not independent evidence.

A Reference must include its full identity, external URL/DOI, reliable publication/update-date basis or `undated`, access and inspection extent, located relevant claims, limitations and **what it does not establish**. Do not copy restricted full texts into the repository or imply full-text access from abstract-only inspection.

## Validation and review
Run `python validate.py .` and `python test_validate.py`. The checker covers structurally testable elements, including section IDs, stage order/maps, metadata relationships, missing inline Method or Practice content, and declared dependency changes. It is **not** a proof of scientific truth or user comprehension. If a canonical source changes, review affected local summaries before refreshing the dependency snapshot using `--accept-reviewed-summaries`.

Root-level GitHub community and automation files are repository infrastructure rather than KPS knowledge objects; the checker applies KPS-specific Markdown rules to the knowledge/content documents, not the GitHub form templates under `.github/`.
