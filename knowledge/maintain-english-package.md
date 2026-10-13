# Maintain English package

## Key takeaway
Review changes and publish a coherent provisional package without confusing file integrity with linguistic truth.

## Summary
Review changes and publish a coherent provisional package without confusing file integrity with linguistic truth. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose and prerequisites

This is a proposed research-maintenance Practice for readers using the package, not an English-learning course. The numbered stages give a recommended order; actual prerequisites, evidence availability and review needs determine entry. Earlier stages can be revisited. No use outcomes or learning gains have been recorded.

## Stage map

- [Stage1 Scope the change](#stage1-scope-the-change)
- [Stage2 Review content and dependencies](#stage2-review-content-and-dependencies)
- [Stage3 Check and publish](#stage3-check-and-publish)

## Stage1 Scope the change

**Goal:** Define the smallest coherent update.

**Why:** Large unbounded generations make inconsistent terminology and unsourced claims harder to notice.

**What to do:** Read the affected object, declared dependencies and source status before editing.

**What to observe:** Scope creep, duplicated definitions and stage labels mistaken for knowledge types.

**Success signal:** The change has a clear reason and affected-object list.

**Next:** Revise content while preserving identities and provenance.

**Procedure**

Choose one topic or interface and identify the canonical object. Preserve its stable ID when revising its path or wording. Stages 0 through 7 are navigation metadata, not required Practice steps. Check whether the change is a factual correction, scope change, terminology choice or authoring convention; each has different evidence requirements.

**Decision points and fallback**

If the required evidence is not available, publish the uncertainty and review task rather than imply completion. Avoid unrelated edits merely to increase coverage.

## Stage2 Review content and dependencies

**Goal:** Keep local summaries faithful to the revised knowledge.

**Why:** A changed source or definition can leave dependent models inconsistent even when all links resolve.

**What to do:** Inspect modified claims, examples, reference records and affected local summaries.

**What to observe:** Removed qualifiers, altered theoretical commitments and falsely upgraded review status.

**Success signal:** The changed summaries are reviewed for their declared scope.

**Next:** Refresh the dependency baseline only after this inspection.

**Procedure**

Compare the actual source passage or earlier object with the revised claim. Retain distinctions such as complementary distribution versus proof of allophony, and Recipient versus Patient. Read each dependent summary locally. Update the review queue with the remaining gaps. Refresh summary-dependencies.json only after the review, using the documented flag; never put unconditional refresh into CI.

**Decision points and fallback**

If a linked source changed but has not been reinspected, retain the warning and provisional status. Do not mark an item reviewed merely because an AI or validator found no formatting errors.

## Stage3 Check and publish

**Goal:** Merge a reproducible, honestly labelled change.

**Why:** Automated structure checks and independent content review answer different questions.

**What to do:** Run the upstream validator and regression suite plus domain checks; inspect the PR diff and merge status.

**What to observe:** Missing links, wrong typed IDs, stale snapshots and unexpected automation permissions.

**Success signal:** Actual check results are recorded and the final tree matches the intended draft.

**Next:** Merge through a PR when authorized, then verify the main-branch result.

**Procedure**

Run python3 validate.py ., python3 test_validate.py, python3 tools/check_domain.py and python3 -m unittest discover -s tests -v. Review generated indexes with --check mode and ensure the permanent workflow has read-only contents access. The authoring assistant can record its own structural/content review but cannot claim independent human approval. Record release scope and limitations before publishing.

**Decision points and fallback**

On failed checks, fix the cause rather than disable tests or protection. A requested broad provisional merge can proceed after structural checks with outstanding scientific-review tasks clearly documented; never represent that merge as expert certification.

## Current practice summary

**Actual task:** No external application recorded.

**What worked:** Not established.

**Unresolved:** Independent scientific review and real use remain pending.

**Next check:** Apply to a bounded linguistic question and record the actual evidence separately.

The repository build checks in CHECKS.md concern publication structure and constructed model fixtures, not effectiveness of this Practice.

## Limits

The Practice is an authored operational synthesis. It is not an experimentally validated learning intervention or a guarantee of correct linguistic judgments.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this object. Inspect the linked record's access extent and nonclaims.

- [Knowledge Practice System 9.0.1](../sources/xiongxianfei-2026-knowledge-practice-system.md#checks) — support is limited to the named section in that record.

## Related knowledge

- [Evidence and analysis](evidence-and-analysis.md) provides a related distinction used in the local explanation.
- [Linguistic interface](interface.md) provides a related distinction used in the local explanation.
- [Constraint and preference](constraint-and-preference.md) provides a related distinction used in the local explanation.

## KPS 12 migration note

The active root validator now checks the KPS 12 entity profile. The historical upstream KPS 9 validator remains under legacy/kps9 and is not the active language contract. Existing command entrypoints are retained. Dependency acceptance now requires an explicit editorial review record through tools/accept_dependency_review.py; a bare refresh flag is not supported. These operational clarifications do not establish scientific review.
