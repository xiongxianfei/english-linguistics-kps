# Migration from KPS 9

## Key takeaway
The KPS 9 knowledge bodies are preserved in role folders while role, domain, relation, source and view semantics are simplified for KPS 12.

## Summary
This branch starts from commit `034f21daa6946b744b367515cb4dbfc6a6720c4f`. Existing knowledge files retain their primary role and explanatory body. Frontmatter changes to role-independent IDs, embedded claims, open domain/relation metadata and `sources/` provenance. Git history is the immutable KPS 9 record; no duplicate active store is introduced.

## Mapping

| KPS 9 | KPS 12 foundation |
|---|---|
| `type` plus role folder | role inferred only from the role folder |
| role-bearing IDs | role-independent IDs with old IDs as aliases |
| `perspectives` and stages | open domain metadata and optional authored Sequences |
| `uses_concepts` etc. | typed `relations`, usually `uses` in the document layer |
| `references/` | `sources/`; knowledge files reference source records |
| manually prominent indexes | generated domain, relation, interface, review and search views |
| root graph source | canonical Markdown compiled to `generated/knowledge-graph.json` |

## New foundation content

Five bridge interfaces from the earlier KPS 12 draft are retained. This foundation adds lexical–morphological, pragmatic–discourse and syntax–prosody interfaces, plus explicit introductory coverage for lexical relations, lexical variation, interaction, social pragmatics, information packaging, plural interpretation, ellipsis, phonological theory alternatives and prosodic measurement.

## Compatibility

Old IDs remain aliases. Ordinary links are rewritten to canonical role folders and `sources/`. KPS 9 tooling is not expected to parse the new frontmatter. Declining the pull request leaves `main` unchanged; after an authorized merge, rollback should use an ordinary reviewed revert.
