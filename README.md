---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# English Linguistics KPS

## Key takeaway
A broad provisional model of English across Stages 0 through 7, organized as reusable KPS knowledge objects rather than a course transcript.

## Summary
A broad provisional model of English across Stages 0 through 7, organized as reusable KPS knowledge objects rather than a course transcript. The initial broad release remains provisional; supporting links and checks do not constitute independent scientific review.

## Start here

Read the [whole system model](models/english-system-architecture.md), [stage coverage](COVERAGE.md), [knowledge index](INDEX.md), and [scientific review queue](REVIEW-QUEUE.md). For a complete worked case, see the [integrated utterance analysis](models/integrated-utterance-analysis.md).

This is the user-authorized broad first draft. It is not independently reviewed linguistic reference material, an exhaustive grammar, a proficiency assessment, or a claim that all English theories agree.

## What is included

The initial package contains 108 knowledge objects: 72 Concepts, 13 Principles, 15 Models, 6 Methods and 2 research-maintenance Practices. Five publication-based Reference records document exactly what was inspected. Stage 0 covers foundations; Stage 1 morphology and lexicon; Stage 2 syntax; Stage 3 semantics; Stage 4 pragmatics; Stage 5 discourse and information structure; Stage 6 phonetics and phonology; Stage 7 interfaces and integration.

## Evidence status

Every linguistic object has status draft, evidence_status provisional and reviewed null. Some objects have selected-passage source support; many still need claim-level external support. Even source-linked objects may contain constructed examples or author synthesis that the linked passage does not establish. The [source register](references/README.md) distinguishes inspected text, abstract-only inspection, limitations and nonclaims. No independent expert review or learner outcome is claimed.

## Architecture

KPS role is independent of linguistic subsystem and stage. A Concept defines a distinction; a Principle explains a scoped relationship; a Model represents a proposed structure; a Method gives an operation; a Practice combines operations for a recurring analytical or maintenance goal. References support provenance and are not a sixth core type. Interfaces are Models with explicit assumptions, not a new role folder. [Typed graph data](knowledge-graph.json) connects stable identities and supports navigation; its arrows are not a causal brain model.

## Use locally

Clone or download this repository and open README.md in a Markdown reader or open the directory as an Obsidian vault. Ordinary relative Markdown links are canonical; no Obsidian plugin, wikilink extension or sibling KPS installation is required. Unicode IPA is text, not a pronunciation recording. No third-party textbook, chart image, font or old AI-generated summary poster is bundled.

## Checks

Use Python 3.10 or newer; the included upstream checker uses modern type annotations. No third-party Python packages are required.

```bash
python3 validate.py .
python3 test_validate.py
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

These commands check publication structure, declared review status and the internal consistency of constructed fixtures. They do not certify linguistic truth. See [check scope](CHECKS.md).

## Contribute

Read [AUTHORING](AUTHORING.md), [domain scope](SCOPE.md), and [CONTRIBUTING](CONTRIBUTING.md). Prefer a small, evidence-aware correction over mass generation. Preserve counterexamples, source limits and theoretical alternatives. Never refresh summary-dependencies.json merely to silence a warning.

## Version and license

Domain version: 0.1.0, provisional. KPS language: 9.x. Upstream tooling is pinned to release 9.0.1 and the commit recorded in [compatibility](COMPATIBILITY.md) and [upstream lock](upstream-lock.json). New original content and tooling use the MIT license in LICENSE; upstream attribution and exclusions are in [NOTICE](NOTICE.md). Third-party publications retain their own licenses.
