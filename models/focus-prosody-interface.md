---
id: "english:focus-prosody-interface"
aliases: ["english:model:focus-prosody-interface"]
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["information-structure","information-structure:focus-and-alternatives","information-structure:focus-projection","pragmatics","prosody","prosody:pitch-accent-and-prominence"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Focus domains constrain possible prosodic realizations without being identical to the most strongly accented word.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:focus-topic-and-qud","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:prosody","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:stress","layer":"document","expected_role":"concept"}]
sources: [{"id":"source:roberts-2012-information-structure","relation":"context-only"}]
interface: {"source_domain":"information-structure","source_representation":"focus-domain","predicate":"constrains","target_domain":"prosody","target_representation":"prominence-pattern","claim":"key-takeaway","scope":"The working analysis, context and variety limits in knowledge/focus-prosody-interface.md; not a neural processing claim.","cardinality":"unspecified"}
---


# Information Structure Prosody interface

## Key takeaway
Focus domains constrain possible prosodic realizations without being identical to the most strongly accented word.

## Summary
Focus domains constrain possible prosodic realizations without being identical to the most strongly accented word. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

Focus domains constrain possible prosodic realizations without being identical to the most strongly accented word.

## Representation

| QUD | Focus domain | Background | Possible strongest word |
|---|---|---|---|
| Who repaired the printer? | Nina | __ repaired the printer | NINA |
| What did Nina repair? | the printer | Nina repaired __ | PRINTER |
| What did Nina do? | repaired the printer | Nina __ | PRINTER |

## Worked interpretation

NP focus and VP focus can share a prominent PRINTER. A broader conversation about the printer does not make Nina Topic merely because she is Subject or focused. The acoustic realization of prominence may involve pitch movement, duration and intensity.

## Assumptions and limits

The table is a constructed working illustration, not an audio measurement or a complete focus-projection grammar. Roberts' abstract supports a connection between QUD and prosodic focus; detailed derivations require full-text and competing-source review.

## Evaluation and counterevidence

Compare explicit question-answer contexts while holding the sentence string stable. Record focus span, accented word and lexically stressed syllable separately. Do not assign a unique focus domain from capitalization alone.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this object. Inspect the linked record's access extent and nonclaims.

- [Information Structure: Towards an integrated formal theory of pragmatics. Semantics and Pragmatics 5, article 6.](../sources/roberts-2012-information-structure.md#abstract) — support is limited to the named section in that record.

## Related knowledge

- [Focus topic and question under discussion](../concepts/focus-topic-and-qud.md) provides a related distinction used in the local explanation.
- [Prosody and intonation](../concepts/prosody.md) provides a related distinction used in the local explanation.
- [Stress](../concepts/stress.md) provides a related distinction used in the local explanation.
