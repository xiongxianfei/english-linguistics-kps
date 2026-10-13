---
id: "english:morphology-phonology-interface"
aliases: ["english:model:morphology-phonology-interface"]
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["morphology","morphology:allomorphy","phonetics","phonology","phonology:phonological-processes"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Regular English inflection links morphological features to sound-conditioned exponents.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:allomorphy","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:inflection","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:consonant-articulation","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:representation-levels","layer":"document","expected_role":"concept"}]
sources: []
interface: {"source_domain":"morphology","source_representation":"inflection-features","predicate":"maps-to","target_domain":"phonology","target_representation":"phonological-exponent","claim":"key-takeaway","scope":"The working analysis, context and variety limits in knowledge/morphology-phonology-interface.md; not a neural processing claim.","cardinality":"unspecified"}
---


# Morphology Phonology interface

## Key takeaway
Regular English inflection links morphological features to sound-conditioned exponents.

## Summary
Regular English inflection links morphological features to sound-conditioned exponents. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

Regular English inflection links morphological features to sound-conditioned exponents.

## Representation

| Morpheme | Special environment first | Voiceless remainder | Voiced remainder |
|---|---|---|---|
| Regular plural | Sibilants -> /ɪz/ | /s/ | /z/ |
| Regular past | /t,d/ -> /ɪd/ | /t/ | /d/ |

The weak vowel can differ across accents; /əz/ and /əd/ are relevant alternatives. Vowels are included in the voiced environments of this simplified model.

## Worked interpretation

Watch ends in /tʃ/, not /h/, so watches selects the syllabic plural. Laugh ends in /f/, so laughs has /s/ and laughed /t/. DELIVER ends in a voiced vowel or rhotic realization in the accents at issue, so delivered has /d/.

## Assumptions and limits

These are regular-pattern models, not full lexical pronunciation tools. Irregular stems, lexicalized adjectives, suffix-conditioned stress and accent variation are outside the algorithm. A single-underlying-exponent analysis is a compatible alternative explanation of the surface variants.

## Evaluation and counterevidence

The supplied pure functions accept final phonemes, not English spellings; tests include sibilants, vowels and /t,d/. Passing proves implementation agreement with these declared cases, not scientific completeness.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Related knowledge

- [Allomorphy](../concepts/allomorphy.md) provides a related distinction used in the local explanation.
- [Inflection](../concepts/inflection.md) provides a related distinction used in the local explanation.
- [Consonant articulation](../concepts/consonant-articulation.md) provides a related distinction used in the local explanation.
- [Orthography phonology and phonetics](../concepts/representation-levels.md) provides a related distinction used in the local explanation.
