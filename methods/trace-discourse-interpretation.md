---
id: "english:method:trace-discourse-interpretation"
type: "method"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
stages: [7]
perspectives: ["interfaces-and-integration"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:mann-taboada-undated-rst-introduction"]
uses_concepts: ["english:concept:discourse-referent", "english:concept:anaphora-and-accessibility", "english:concept:temporal-causal-and-evidential-relations", "english:concept:focus-topic-and-qud"]
---

# Trace discourse interpretation

## Key takeaway
Track reference and discourse relations while distinguishing asserted information from defeasible inference.

## Summary
Track reference and discourse relations while distinguishing asserted information from defeasible inference. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Objective

Track reference and discourse relations while distinguishing asserted information from defeasible inference.

## Inputs and prerequisites

A short passage, a stated context if known, and an account of which sentences or spans are being related. An unknown context should be recorded as unknown, not supplied as a hidden fact.

## Rationale

Pronoun chains and connectives support cohesion, but coherence requires interpreted relations. Recency, compatibility, salience and QUD relevance can point toward different readings.

## Procedure

1. Introduce labels for discourse referents and identify their introducing expressions.
2. List candidate antecedents for each pronoun and the evidence favoring each.
3. Separate textual order from event-time ordering.
4. Label relations between explicit spans, such as reason, result, elaboration, contrast or concession.
5. Record the active QUD, likely topic and focus only where context supports them.
6. Mark conclusions as explicit, presupposed, entailed or defeasibly inferred.

## Worked example

"Maya left. She had missed an earlier train." The second clause describes an earlier event. A causal link from missing the train to leaving may be unclear without context: the temporal marking alone does not prove a reason. In "The lights are off; Maya must have left", lights-off is evidence for a conclusion, not necessarily its cause.

## Expected effect

The output is an explicit, revisable analysis with its assumptions and uncertainties exposed. This is a design expectation, not a measured learning outcome.

## Validation and counterevidence

Every relation needs two spans, a direction when relevant, and a stated basis. Pronoun preferences must not be silently promoted to logical entailments. Check whether changing context preserves a plausible alternative.

## Limits

An analyst may disagree with another about relation labels. This method is not a fully implemented RST parser, and no natural-discourse annotation accuracy is claimed.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this object. Inspect the linked record's access extent and nonclaims.

- [Rhetorical Structure Theory website introduction and relation definitions](../references/mann-taboada-undated-rst-introduction.md#relations) — support is limited to the named section in that record.

## Related knowledge

- [Discourse referent](../concepts/discourse-referent.md) provides a related distinction used in the local explanation.
- [Anaphora and accessibility](../concepts/anaphora-and-accessibility.md) provides a related distinction used in the local explanation.
- [Temporal causal and evidential relations](../concepts/temporal-causal-and-evidential-relations.md) provides a related distinction used in the local explanation.
- [Focus topic and question under discussion](../concepts/focus-topic-and-qud.md) provides a related distinction used in the local explanation.
