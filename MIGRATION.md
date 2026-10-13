# KPS 9 to KPS 12 migration

## Key takeaway
The entire existing package is migrated with preserved bodies, identities and evidence limits, not regenerated as new scientific knowledge.

## Summary
This package jumps directly from KPS 9.x to the owner-requested KPS 12.x label. The English package version is 0.2.0 and the local implementation profile is 12.0.0-draft.1. Nothing here asserts that KPS 10, KPS 11 or an upstream KPS 12 release was published.

## Mapping
| KPS 9 | KPS 12 |
|---|---|
| Role-based `type` and directories | Independent `roles` on generic entity records; neutral content paths |
| `english:concept:...` and similar IDs | `english:...` canonical IDs; original IDs retained as aliases |
| `uses_concepts` and similar | `kps:uses`, retaining an expected target-role constraint |
| `references` | `kps:cites` plus context-only evidence; no automatic support assertion |
| Root `stages` | Membership in the named legacy navigation Sequence |
| Interface Model prose | Interface entity, explicit representation endpoints, scoped mapping claim |
| Whole-document evidence state | Preserved state plus versioned summary claims and separately addressable evidence records |
| Graph format 1 | Entity/edge graph format 12 with separate relationship layers |

## Preservation and transformations
`legacy/kps9/` is a byte-for-byte snapshot of base commit `034f21daa6946b744b367515cb4dbfc6a6720c4f`. `migration/manifest.json` records each original file hash and each canonical body destination. Canonical content drops legacy frontmatter because metadata moves into JSON. Relative links are rewritten to the neutral content/source paths without rewriting the linguistic explanations. Old paths become redirects with their original heading anchors.

The maintenance Practice receives a separately recorded migration note identifying the active KPS 12 validator and the explicit editorial-review-record requirement. This is an operational clarification, not a change in linguistic claims. The exact transform is recorded for preservation checking.

## What is new
Ten domain entities and their internal classification scopes are explicit. Five original interfaces become structured interface records. Five additional provisional bridge Models cover Phonology–Phonetics, Prosody–Phonetics, Discourse–Information Structure, Morphology–Syntax and Lexicon–Semantics. They are authored syntheses with constructed illustrations and no new external verification. Their addition does not make interface coverage exhaustive.

## Claim extraction boundary
Only each object's Key takeaway is exposed as a versioned summary claim. This is a full schema/storage migration, not a completed atomic-claim or scientific-evidence audit. Source records preserve their historical inspection extent. Context-only evidence is not support. Review queues identify body-claim decomposition and external passage review as outstanding tasks.

## Reproduce the migration
From the migrated repository, with an empty output directory outside this package:

```bash
python3 tools/migrate_kps12.py --source legacy/kps9 --target /tmp/english-kps12-rebuilt
python3 /tmp/english-kps12-rebuilt/validate.py /tmp/english-kps12-rebuilt
```

The migrator reads frozen classification and interface plans and the `migration/template-manifest.json` list of runtime/specification assets. It refuses to overwrite a nonempty destination and does not access the network. Reproduction uses the preserved baseline; it is not an instruction to rerun migration over edited current content.

## Editorial dependency review
Changes to content or document dependencies invalidate the recorded baseline. Inspect changed sources and affected summaries, record the exact before/after snapshot hashes and affected IDs, then use `tools/accept_dependency_review.py --record ...`. Keep this editorial decision separate from scientific evidence review. Automatic graph regeneration cannot remove the warning.

## Rollback
The migration is proposed on a separate branch. Before merge, leave `main` unchanged by declining the PR. After an authorized merge, use an ordinary reviewed revert, not a force-push. The preserved KPS 9 snapshot and original commit remain historical references.
