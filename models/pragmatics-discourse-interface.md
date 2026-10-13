---
id: "english:pragmatics-discourse-interface"
aliases: []
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["pragmatics","discourse","pragmatics:contextual-inference","discourse:discourse-inference"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Contextual interpretation updates an evolving discourse model, while that discourse model in turn constrains later reference and inference.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:contextual-resolution","layer":"document"},{"predicate":"uses","target":"english:discourse-referent","layer":"document"}]
sources: []
interface: {"source_domain":"pragmatics","source_representation":"utterance-interpretation","predicate":"updates-and-constrains","target_domain":"discourse","target_representation":"discourse-context","claim":"key-takeaway","scope":"Contextual interpretation across connected English utterances.","cardinality":"many-to-many"}
---

# Pragmatics Discourse interface

## Key takeaway
Contextual interpretation updates an evolving discourse model, while that discourse model in turn constrains later reference and inference.

## Summary
This interface connects utterance-level pragmatic interpretation with discourse-level representations of accessible referents, relations and shared commitments. The correspondence is iterative rather than a one-way processing staircase.

## Purpose
Make explicit how local speaker meaning and contextual inference contribute to, and are constrained by, a larger discourse context.

## Representation
| Pragmatic representation | Mapping | Discourse representation |
|---|---|---|
| resolved reference, speech act, presupposition, defeasible inference | updates-and-constrains | discourse referents, relations, questions, commitments and accessibility |

## Worked interpretation
After "A courier arrived", a later "She left the parcel" can favor the courier as the pronoun's referent. The first utterance contributes a discourse referent; the second interpretation depends on accessibility and may update the discourse with a new event and relation.

## Assumptions and limits
The model does not claim that all pragmatic inference is stored as a discourse object or that one formal discourse theory is mandatory. Common ground, private belief and public commitment should not be silently equated.

## Evaluation and counterevidence
Trace which information came from conventional meaning, contextual resolution, defeasible inference and prior discourse. Retain alternative antecedents and interpretations where the context does not decide among them.

## Evidence status
**Provisional.** Detailed formal and interactional support is pending.

## Related knowledge
- [Contextual resolution](../concepts/contextual-resolution.md)
- [Discourse referent](../concepts/discourse-referent.md)
- [Common ground](../concepts/common-ground.md)
- [Trace discourse interpretation](../methods/trace-discourse-interpretation.md)
