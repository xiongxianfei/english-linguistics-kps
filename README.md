# English Linguistics KPS 12

## Key takeaway
A foundational model of English linguistics is authored once in five role-based Markdown collections and projected into domain, relation, interface, evidence and learning views.

## Summary
Package **0.2.0** implements repository profile **KPS 12.0.0-draft.2**. It covers Phonetics, Phonology, Morphology, Lexicon, Syntax, Semantics, Pragmatics, Discourse, Information Structure and Prosody, together with major representation interfaces. All linguistic content remains provisional and no structural check certifies scientific truth.

## Canonical knowledge

- `concepts/` defines reusable things and distinctions.
- `principles/` states scoped relationships and constraints.
- `models/` represents structures and interfaces.
- `methods/` gives bounded analytical operations.
- `practices/` coordinates recurring work.
- `sources/` records external provenance and inspection limits.
- `sequences/` contains optional authored routes through the same knowledge.

Every knowledge item has exactly one primary role determined by its folder. Domains and relation predicates are open, kebab-case metadata introduced where needed. There is no separate ontology or entity store.

## Start here

Read [KPS](KPS.md), [authoring](AUTHORING.md), [domain coverage](views/coverage.md), [interfaces](views/interfaces.md), and the [foundations sequence](sequences/english-linguistics-foundations.md). The [English system architecture](models/english-system-architecture.md) and [integrated utterance analysis](models/integrated-utterance-analysis.md) show how levels interact.

## Build and validate

```bash
python3 tools/build.py --check
python3 validate.py .
python3 -m unittest discover -s tests -v
python3 tools/query.py --domain information-structure
python3 tools/query.py --interfaces
```

`views/` and `generated/` are derived and may be rebuilt. Canonical knowledge lives only in the role folders, `sources/`, and `sequences/`.

## Evidence boundary

Key takeaways are exported as summary claims, not a complete atomic decomposition of every sentence. A citation is context unless a knowledge file records a located support assessment. Constructed examples, theory choices, accent limits and missing observations remain explicit. No expert review, corpus validation, speaker study or learner outcome is implied by file count or green tests.
