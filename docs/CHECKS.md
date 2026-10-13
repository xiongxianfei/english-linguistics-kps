---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# Checks and review boundaries

## Key takeaway
Structural checks detect publication errors; content review decides whether an explanation is usable and justified.

## Summary
Use Python 3.10 or newer and the standard library. The checker is the pinned upstream KPS 9.1.0 file. Domain tests retain constructed linguistic fixtures, source and review declarations, and the pinned checker integrity check. They do not certify scientific truth or reader comprehension.

## Commands
```bash
python3 validate.py .
python3 -m unittest discover -s tests -v
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
```
The first checks KPS structure, local links, typed document dependencies and dependency fingerprints. Regression suites test failure cases and constructed examples. Domain checks inspect subsystem coverage and provenance declarations. Catalog freshness ensures summaries match canonical Markdown.

## Content review
For every new Model, hide links and inspect whether its purpose, necessary terms, representation, example, assumptions and counterevidence are locally available. A section's presence is only a mechanical check; the explanation may still be wrong or incomplete. Check referent/function/role distinctions, accent labels, inference scope and source-claim fit. Do not manufacture observations to fill empty acoustic or learner-result fields.

## Learning Practice review

For a learning Practice, inspect the target questions against the adopted disciplinary structure before trying its examples. Check a new or ambiguous case, the feedback, and whether essential explanations remain usable with links hidden. Compare overlapping Concepts, Models and Practice passages for meaning and scope. Record coverage, usability and source-fidelity gaps separately; no keyword test establishes them.

## Dependency snapshots
summary-dependencies.json records which local summaries depend on which files. Ordinary validation and catalog generation never accept changed fingerprints. Review the changed source and receiving summaries first; only then run the explicit --accept-reviewed-summaries option. The edition's review note records the limited editorial review, not independent linguistic approval.

## GitHub
One branch and one PR are the delivery workflow. The existing read-only PR check runs the ordinary commands; no workflow writes content or creates releases. Main remains unchanged until an authorized merge. A local test result and a remote CI result must be reported separately when either is unavailable.

## Tool audit

| Existing tool | Purpose retained |
|---|---|
| `validate.py` | KPS structure, links and dependencies in this package |
| `tools/check_domain.py` | Missing evidence declarations, unsupported review claims and domain coverage |
| `tools/build_navigation.py` | Keep one knowledge index aligned with the canonical Markdown |
| `tools/linguistic_examples.py` and `tests/` | Constructed examples, checker integrity, provenance and review declarations |

These tools serve existing checks; none is required for reading. Catalog generation does not rewrite knowledge or accept dependency fingerprints. Keep the pinned validator local for standalone use, with Core as the upstream owner. Adopt a newer copy only through a separate compatibility review. No new sync, build or publishing script is needed.

## Text bytes

`.gitattributes` keeps text in LF format because fingerprints use exact file bytes. Restore intended line endings before interpreting a checksum difference as a content change.

## Supporting document locations

The root retains the README, agent guidance, licensing, validator and required metadata. Authoring, pronunciation guidance and the single knowledge index live in `docs/`. Supporting maintenance documents moved as follows; external bookmarks need updating because old paths do not redirect.

| Former root path | Current path |
|---|---|
| `AUTHORING.md` | [docs/AUTHORING.md](AUTHORING.md) |
| `PRONUNCIATION.md` | [docs/PRONUNCIATION.md](PRONUNCIATION.md) |
| `INDEX.md` | [docs/INDEX.md](INDEX.md) |
| `COVERAGE.md`, `REVIEW-QUEUE.md` | Consolidated into the index and [review priorities](REVIEW.md#priority-evidence-gaps) |
| `CHECKS.md` | [docs/CHECKS.md](CHECKS.md) |
| `COMPATIBILITY.md` | [docs/COMPATIBILITY.md](COMPATIBILITY.md) |
| `NAVIGATION.md` | [docs/NAVIGATION.md](NAVIGATION.md) |
| `REVIEW.md` | [docs/REVIEW.md](REVIEW.md) |
| `SCOPE.md` | [docs/SCOPE.md](SCOPE.md) |
| `TEMPLATES.md` | [docs/TEMPLATES.md](TEMPLATES.md) |
| `CONTRIBUTING.md` | [.github/CONTRIBUTING.md](../.github/CONTRIBUTING.md) |

## Layout dependency review

The 2026-10-13 cleanup preserved the knowledge explanations, metadata, identities and stage headings. Two Practice maintenance notes now name `docs/CHECKS.md` instead of its former root path. Their statements and receiving summaries retain the same meaning and limits; fingerprints, where affected, were refreshed only after this path-only review. This does not constitute independent linguistic review.

## Test allowlist

Retain checks of the pinned validator against its lock, the actual package, source-access and review declarations, constructed linguistic examples, catalog freshness and the generator's read-only dependency behavior. Shared validator failure-case regressions remain in Core at the pinned revision. Versioned inventories and exact wording are reviewed as content rather than frozen in assertions. Pronunciation and reader review responsibilities are in [Review](REVIEW.md#pronunciation-and-reader-review).

## Navigation cleanup dependency review

The supporting-document cleanup moved pronunciation guidance into `docs/PRONUNCIATION.md` without changing its claims or conventions. Seven knowledge files and the source-register link changed only that destination. Their metadata, explanatory text and Practice stages are unchanged. The 18 affected receiving summaries were compared with the prior tree before refreshing their fingerprints; their claims and evidence limits remain unchanged. This is a path-only editorial review, not new linguistic source inspection or independent scientific review.
