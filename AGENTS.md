---
package_version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
---

# Agent guidance

## Key takeaway

Apply the shared Core Engineering Principles together with this repository's authoring, evidence and contribution boundaries.

## Summary

These repository-wide instructions apply to knowledge, code, tools and workflows. The nine Core Engineering Principles are maintained verbatim across the six knowledge repositories; propose shared revisions together and keep domain-specific instructions below. Each repository carries its own copy for independent use. These are working agreements, not scientific KPS Principle objects or a replacement for the authoring contract.

## Project purpose

Help readers understand and analyze English linguistic systems and their interfaces through source-grounded explanations and learning Practices. Use the [Body of Knowledge Outline](docs/body-of-knowledge-outline.md) for required coverage, capabilities and gaps, [Scope](docs/SCOPE.md) for framework and variety limits, and the [knowledge index](docs/INDEX.md) to locate existing explanations.

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Preserve unique evidence, provenance, and historically useful knowledge; remove obsolete representations, not valuable facts.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.

## Project guidance

- Follow [Authoring](docs/AUTHORING.md), which applies the pinned KPS contract. Preserve the five primary roles, stable identities and locally sufficient explanations; supporting definitions and representations may overlap where useful.
- Start from the learning target and established linguistic distinctions and models. Preserve the adopted framework and source subset; teaching order is not a new linguistic taxonomy.
- Keep the authored body of knowledge outline focused on scope, topics, capabilities, relationships, sources and coverage gaps. Maintain its text and overview together; Practice catalogues and development roadmaps belong elsewhere. Retain useful topic-level links to existing explanations across the five roles.
- Inspect affected sources and dependencies. Distinguish source statements, authored inference, pedagogical simplification and observations. Label constructed examples; a citation title is not evidence of source inspection.
- Keep dialect, transcription and theoretical limits visible. Do not relabel a Canadian transcription as General American by blind symbol replacement. Missing context, audio and recordings remain missing.
- Keep provisional analyses provisional until actual review supports a change. Do not invent evidence or review records, or treat a diagram, IPA string or unit test as proof of linguistic truth.
- Keep private conversations and learner records outside the public repository. Do not bundle restricted third-party publications, charts or recordings under the repository license.

## Verification

Run the existing publication checks from [Checks](docs/CHECKS.md):

```bash
python3 validate.py .
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

When canonical catalog inputs change, rebuild navigation with the existing tool. Review changed source meaning and receiving summaries before using `--accept-reviewed-summaries`; the flag records review and does not perform it. Report actual failures and distinguish structural checks from linguistic and reader review.

## Contribution workflow

Follow [Contributing](.github/CONTRIBUTING.md): use one branch and one PR to `main` for a coherent change. Merge or create releases only with owner authorization. Preserve branch protections, unrelated work and LF text under `.gitattributes`; do not force-push shared branches. Keep the validator pinned and adopt upstream changes only through a separate compatibility review.
