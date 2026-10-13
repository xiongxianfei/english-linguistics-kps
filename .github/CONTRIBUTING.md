---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# Contributing

## Key takeaway
Contributions should improve a bounded claim, representation or evidence record without hiding uncertainty.

## Summary
Contributions should improve a bounded claim, representation or evidence record without hiding uncertainty. The initial broad release remains provisional; supporting links and checks do not constitute independent scientific review.

## Before editing

Read [Authoring](../docs/AUTHORING.md) and [Scope](../docs/SCOPE.md). Inspect the target, direct dependencies, local evidence and review priorities. Preserve IDs for revisions; create a new object only when it has a distinct reusable role. Stages and perspectives are metadata, not additional types.

## Pull request content

Explain what changed, why it matters, the source passages actually inspected, which examples are constructed, and which theoretical or dialect limits apply. Report actual checks, not intended ones. Include counterevidence when relevant; do not add a prestigious citation unrelated to the claim.

## Scientific review

An independent reviewer can narrow, challenge or reject an analysis. A review record must identify reviewer, date, exact object version, supported claims, inspection extent and remaining limits. The initial release has no such independent records and stays provisional. Review status is not promoted by automation alone.

## Checks and snapshots

Run the commands in [Checks](../docs/CHECKS.md). Regenerate indexes with tools/build_navigation.py. Review dependent summaries before refreshing their hashes. A broken link, removed qualifier or missing source record must not be silenced through a status change or CI disablement.

## Licensing and privacy

Contribute only material you have the right to publish under the repository license. Do not upload restricted textbooks, screenshots, charts, recordings or private learner data. Reference external publications and summarize narrowly in your own words. AI assistance must not fabricate sources, source access or human approval.
