---
id: "english:discourse-information-structure-interface"
aliases: []
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["discourse","information-structure"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "KPS 12 authored bridge synthesis; constructed illustration; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:focus-topic-and-qud","layer":"document"},{"predicate":"uses","target":"english:common-ground","layer":"document"},{"predicate":"uses","target":"english:givenness-and-bridging","layer":"document"},{"predicate":"uses","target":"english:discourse-referent","layer":"document"}]
sources: []
interface: {"source_domain":"discourse","source_representation":"discourse-context","predicate":"constrains","target_domain":"information-structure","target_representation":"focus-domain","claim":"key-takeaway","scope":"The working analysis, context and variety limits in knowledge/discourse-information-structure-interface.md; not a neural processing claim.","cardinality":"unspecified"}
---

# Discourse Information Structure interface

## Key takeaway
A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable.

## Summary
A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable. This KPS 12 bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| discourse context | accessible_referents, prior_utterances, candidate_questions |
| focus domain | question_under_discussion, focus_span, background |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Worked interpretation
The questions Who repaired the printer? and What did Nina repair? provide different constructed contexts for Nina repaired the printer. They do not make a permanently fixed topic or focus an intrinsic property of the sentence string.

## Assumptions and limits
This is a QUD-compatible working bridge, not a consensus theory of discourse. Context may be insufficient to identify one topic or focus; alternative analyses must remain explicit.

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
- [focus topic and qud](../concepts/focus-topic-and-qud.md)
- [common ground](../concepts/common-ground.md)
- [givenness and bridging](../concepts/givenness-and-bridging.md)
- [discourse referent](../concepts/discourse-referent.md)
