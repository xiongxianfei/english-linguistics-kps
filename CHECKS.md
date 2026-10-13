---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# Checks and review boundaries

## Key takeaway
Structural checks detect publication errors; content review decides whether an explanation is usable and justified.

## Summary
Use Python 3.10 or newer and the standard library. The checker is the pinned upstream KPS 9.1.0 file. Domain tests retain the original constructed linguistic fixtures and add coverage, layout and self-contained-section checks. They do not certify scientific truth or reader comprehension.

## Commands
```bash
python3 validate.py .
python3 test_validate.py
python3 -m unittest discover -s tests -v
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
```
The first checks KPS structure, local links, typed document dependencies and dependency fingerprints. Regression suites test failure cases and constructed examples. Domain checks confirm the ten subsystem Models, fourteen interfaces, provenance declarations and absence of abandoned storage layers. Catalog freshness ensures summaries match canonical Markdown.

## Content review
For every new Model, hide links and inspect whether its purpose, necessary terms, representation, example, assumptions and counterevidence are locally available. A section's presence is only a mechanical check; the explanation may still be wrong or incomplete. Check referent/function/role distinctions, accent labels, inference scope and source-claim fit. Do not manufacture observations to fill empty acoustic or learner-result fields.

## Dependency snapshots
summary-dependencies.json records which local summaries depend on which files. Ordinary validation and catalog generation never accept changed fingerprints. Review the changed source and receiving summaries first; only then run the explicit --accept-reviewed-summaries option. The edition's review note records the limited editorial review, not independent linguistic approval.

## GitHub
One branch and one PR are the delivery workflow. The existing read-only PR check runs the ordinary commands; no workflow writes content or creates releases. Main remains unchanged until an authorized merge. A local test result and a remote CI result must be reported separately when either is unavailable.
