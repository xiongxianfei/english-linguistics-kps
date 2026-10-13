---
id: "english:model:discourse-information-structure-interface"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["discourse", "information-structure"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: []
interface_domains: ["discourse", "information-structure"]
uses_concepts: ["english:concept:focus-topic-and-qud", "english:concept:common-ground", "english:concept:givenness-and-bridging", "english:concept:discourse-referent"]
---

# Discourse Information Structure interface

## Key takeaway
A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable.

## Summary
A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable. This KPS bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| discourse context | accessible_referents, prior_utterances, candidate_questions |
| focus domain | question_under_discussion, focus_span, background |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Essential terms
A **discourse context** records what has been said, which referents are accessible and what issue is being addressed. A **focus domain** is the word or larger expression that supplies relevant alternatives relative to that issue. Its **background** is what the comparison holds constant. Topic concerns what the discourse is about; none of these labels is simply another name for grammatical Subject. A question under discussion can be implicit, but an analyst must state the assumed question rather than invent an observed conversational context.

## Worked interpretation
For *Who repaired the printer?*, the answer *Nina repaired the printer* can focus *Nina*, contrasting her with other possible repairers. For *What did Nina repair?*, the same answer can focus *the printer*, contrasting it with other possible objects. For *What did Nina do?*, the focus can be the larger phrase *repaired the printer*. These constructed pairs show that the sentence string does not by itself fix one focus span or Topic. Without a stated context, preserve alternative analyses rather than selecting one as fact.

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
