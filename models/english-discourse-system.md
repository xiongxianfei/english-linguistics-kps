---
id: "english:model:english-discourse-system"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["discourse"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:mann-taboada-undated-rst-introduction"]
uses_concepts: ["english:concept:discourse-referent", "english:concept:anaphora-and-accessibility", "english:concept:cohesion-and-coherence", "english:concept:discourse-relation", "english:concept:temporal-causal-and-evidential-relations"]
uses_models: ["english:model:pragmatics-discourse-interface", "english:model:discourse-information-structure-interface"]
system_domain: "discourse"
---

# English discourse system

## Key takeaway
Discourse analysis connects utterances through referents, coherence relations and interaction while distinguishing text evidence from inferred interpretation.

## Summary
This Model explains how more than one clause or turn forms an interpretable discourse. It separates segmentation, referent tracking, cohesion, coherence and relations between situations or communicative acts. The worked example identifies alternative causal and evidential readings rather than treating a connective as a complete analysis.

## Purpose
Given a passage, account for which spans connect, what entities remain accessible and how the parts contribute to the exchange. The output is a proposed relation network, not a claim that proximity alone establishes meaning.

## Representation

| Component | Representation | Question |
|---|---|---|
| Segmentation | Clauses, turns or other justified discourse units | What spans are being related? |
| Reference tracking | Introduced and accessible discourse referents | What can a pronoun reasonably refer to? |
| Cohesion | Overt links such as pronouns, repetition and connectives | Which textual cues connect the units? |
| Coherence | An interpretation of why the units belong together | What explanatory or communicative relation is proposed? |
| Interaction | Proposals, questions, responses and repairs | How do later turns accept or challenge earlier material? |

Segmentation depends on the analysis; a sentence is not always one discourse unit. A discourse referent is an analytical representation, not proof of a real-world object's existence.

## Essential distinctions
**Anaphora** involves dependence on an earlier or otherwise accessible interpretation. Accessibility is constrained by linguistic structure and context, not merely by choosing the nearest noun. **Bridging** connects an expression to an associated but not explicitly identical referent, as when a described building makes a relevant entrance inferable.

**Cohesion** is the presence of surface links. **Coherence** concerns the interpreted connections. Repeating words can create cohesion without yielding a sensible explanation. Conversely, two utterances can be coherent without an explicit connective.

A **cause** relation concerns situations; **evidence** concerns grounds for accepting a proposition; **elaboration** supplies detail; **concession** presents an outcome against an expectation. A sequence in the text does not establish temporal succession, and temporal succession does not prove causation.

Rhetorical Structure Theory distinguishes relations using the participating spans and their interpreted contribution. This package uses selected working distinctions rather than implementing all of RST or claiming that its inventory is universal.

## Worked analysis
Consider *The printer stopped. The display was dark. Maya checked it*.

Create referents for the printer, its display and Maya. For *it*, the printer is a plausible interpretation, but the display is another possible target in a suitable context. Preserve that uncertainty rather than labeling the pronoun mechanically.

The second sentence could provide evidence for the claim that the printer stopped, or describe an accompanying result. The wording alone does not settle that causal structure. The third sentence may narrate a subsequent response, but the analyst should not invent a motive or exact time interval.

Now add *because* or *although* and compare the reading. These cues narrow the proposed relation, but relation scope still needs attention: a because-clause can explain an event, a belief or the reason for saying something. Identify which interpretation is being asserted.

## Interfaces
**Pragmatics Discourse:** referents, assumptions and commitments change through interaction; rejection prevents automatic acceptance. **Discourse Information Structure:** accessibility and the current issue shape topic, focus and background. **Semantics** contributes the propositions and situations linked by a discourse relation. **Syntax** supplies clause structure but does not alone determine the discourse network.

## Evaluation and counterevidence
Underline both spans in each proposed relation, name its direction and explain what in the text supports it. Test a rival relation or antecedent. Distinguish explicit connective evidence from a contextual preference. If both readings remain possible, retain both rather than forcing a unique graph.

Diagnostic: does *Maya arrived. The alarm sounded* entail that Maya caused the alarm? No. Even an inferred temporal order would not establish causation.

## Assumptions and limits
This is a small descriptive model. Full dialogue management, discourse segmentation standards, genre differences and competing coherence theories require more detailed work. Constructed text and one analyst's interpretation are not an annotated corpus or inter-annotator agreement study.

## Evidence status
**Provisional; independent review pending.** The [RST Reference](../references/mann-taboada-undated-rst-introduction.md) identifies selected relation definitions and their interpretation limits. The printer passage and its alternative readings are authored examples, not copied source analyses.

## Related knowledge
[Discourse referent](../concepts/discourse-referent.md), [anaphora and accessibility](../concepts/anaphora-and-accessibility.md), [cohesion and coherence](../concepts/cohesion-and-coherence.md), [discourse relation](../concepts/discourse-relation.md) and [temporal causal and evidential relations](../concepts/temporal-causal-and-evidential-relations.md) expand the distinctions. [Trace discourse interpretation](../methods/trace-discourse-interpretation.md) supports a repeatable analysis.
