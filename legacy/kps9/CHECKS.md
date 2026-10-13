---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# Validation and review limits

## Key takeaway
Structural correctness, declared-model consistency and scientific review are separate claims.

## Summary
Structural correctness, declared-model consistency and scientific review are separate claims. The initial broad release remains provisional; supporting links and checks do not constitute independent scientific review.

## Commands

```bash
python3 validate.py .
python3 test_validate.py
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

The original upstream suite contains 31 regression tests. The domain suite covers publication invariants, constructed fixtures, the General American policy and the two integrated pronunciation Practices. Inspect the current test count rather than assuming the initial suite is unchanged. Inspect actual run results in the PR and validation-evidence.json rather than assuming the commands passed.

## What is checked

The upstream validator covers metadata, local links/fragments, typed IDs, headings, Practice stage structure and dependent-summary hashes. The domain checker adds stage coverage, visible provisional status, Reference access/date metadata and restrictions on unsupported review promotion. Generated indexes must match current canonical objects.

## Constructed model tests

Suffix functions are tested on explicitly declared regular English final-sound patterns. Scope tests include shared witnesses and empty restrictors. A token-span fixture checks five finite clauses and places the Recipient to-PP outside the relative. These tests establish implementation consistency with the declared model, not empirical support for the model.

## Pronunciation Practice checks

The new Practice tests check stage maps, local content, General American scope, source links, acyclic composition and explicit pending states for missing listening or production. They also protect the distinction between symbol classification, auditory inference and learner performance. These are document-contract checks, not a test of anyone's hearing, articulation, pronunciation, retention or the procedures' effectiveness. The [recorded local check results](data/pronunciation-practice-validation.json) identify the actual commands, scope and source-file hashes; PR CI provides a separate execution on the committed changes.

## Dependency review

After inspecting affected local summaries and source scope, run:

```bash
python3 tools/build_navigation.py
python3 validate.py . --accept-reviewed-summaries
python3 validate.py .
```

Never put the refresh command into ordinary CI. For the initial draft, the authoring assistant reviewed generated links and summaries before recording the first baseline. That was an authoring review, not independent scientific review. Future baseline updates need their own inspection.

## What is not checked

No tool here certifies linguistic truth, source completeness, naturalness in all dialects, measured pronunciation, prosodic interpretation, or learner competence. All linguistic objects remain provisional regardless of green checks. No independent reviewer approval is fabricated.

## Publication security

The permanent CI workflow uses read-only contents permission and no deployment credentials. A one-time implementation-branch materializer was used to create the initial files and is removed before merge. The main package does not retain a branch-writing workflow or automatically accept future generated content.
