# English Linguistics KPS 12

## Key takeaway
English linguistics is represented as a network of generic knowledge entities, with independent roles, domains, claims, evidence and scoped interfaces.

## Summary
Domain package **0.2.0** implements **KPS 12.x**, local profile **12.0.0-draft.1**. All 110 legacy knowledge objects and 10 source records are preserved and migrated; five explicitly provisional bridge Models extend interface coverage. Scientific status remains provisional. This is a working repository implementation, not an announcement of an upstream KPS 12 release or an independently reviewed grammar.

## Start here
Read the [KPS 12 core specification](spec/KPS12.md), [ten domain views](DOMAINS.md), [representation interfaces](INTERFACES.md), [role index](INDEX.md), [coverage gaps and legacy route](COVERAGE.md), and [claim review queue](REVIEW-QUEUE.md). The [whole-system Model](knowledge/english-system-architecture.md) and [integrated utterance analysis](knowledge/integrated-utterance-analysis.md) remain available.

## Ten independently navigable domains
Phonetics, Phonology, Morphology, Lexicon, Syntax, Semantics, Pragmatics, Discourse, Information Structure and Prosody are explicit domain entities. Their internal subdomains, memberships, interfaces and unrepresented areas are visible in [DOMAINS](DOMAINS.md). Domain overlap is allowed; folder location does not determine subject membership.

## Canonical layout
`entities/` contains the canonical generic JSON entity records. `knowledge/` contains role-neutral Markdown explanations; `sources/` retains bibliographic explanations and nonclaims. Roles, domains, representations, interfaces, claims, evidence and the legacy route are themselves addressable entities. `knowledge-graph.json` and `views/` are generated views, not independent sources of truth.

Old paths remain as redirects. The byte-preserved [KPS 9 baseline](legacy/kps9/README.md), [migration guide](MIGRATION.md) and migration manifests make preservation and identity changes inspectable.

## Evidence boundary
Key takeaways are exposed as versioned summary claims. This does not decompose every sentence into an atomic proposition. Legacy citations are migrated as **context-only**, retaining their original access limits; they are not automatically converted into claim support. No claim is promoted to reviewed by migration or green tests. Five added bridge Models use constructed examples and explicitly pending external support.

## Pronunciation policy
[PRONUNCIATION.md](PRONUNCIATION.md) retains **General American English as the primary reference variety** for new pronunciation analyses, separates broad phonemic forms from phonetic realizations, and preserves source-rights limits. The [word-pronunciation Practice](knowledge/learn-word-pronunciation.md) and [phone-classification Practice](knowledge/classify-and-produce-phone.md) retain their full stages and pending learner outcomes.

## Use and validate
Python 3.10 or newer; no third-party Python packages are required.

```bash
python3 validate.py .
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
python3 tools/check_preservation.py
python3 tools/kps12.py query --domain linguistics:prosody
python3 tools/kps12.py query --interfaces
python3 tools/kps12.py query --id english:concept:phone-phoneme-and-allophone
```

The last command resolves a preserved KPS 9 identity to its canonical KPS 12 entity.

See [CHECKS](CHECKS.md) for exact test boundaries and [AUTHORING](AUTHORING.md) before changing content. Generated views never silently accept dependency changes.

## License and release status
Original package content and tooling are MIT-licensed; external sources retain their rights. See [NOTICE](NOTICE.md). This branch is a reviewable KPS 12 migration; merging, tagging and publishing a release are separate actions.
