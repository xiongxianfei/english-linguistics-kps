---
id: "english:model:english-discourse-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["discourse"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:mann-taboada-undated-rst-introduction"]
uses_concepts: ["english:concept:discourse-referent", "english:concept:anaphora-and-accessibility", "english:concept:cohesion-and-coherence", "english:concept:discourse-relation", "english:concept:temporal-causal-and-evidential-relations", "english:concept:contrast-and-concession", "english:concept:common-ground", "english:concept:speech-act", "english:concept:utterance-and-speaker-meaning", "english:concept:focus-topic-and-qud", "english:concept:givenness-and-bridging"]
uses_models: ["english:model:english-pragmatics-system", "english:model:english-information-structure-system"]
system_domain: "discourse"
---

# English discourse system

## Key takeaway
Discourse analysis connects utterances through referents, coherence relations and interaction while distinguishing text evidence from inferred interpretation.

## Summary
This Model explains how more than one clause or turn forms an interpretable discourse. It separates segmentation, referent tracking, cohesion, coherence and relations between situations or communicative acts. The worked example identifies alternative causal and evidential readings rather than treating a connective as a complete analysis. A worked relation network and interfaces with Pragmatics and Information Structure connect text, context and proposed discourse updates. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Discourse network](#discourse-network)
- [Interfaces](#interfaces)
- [Interface with Pragmatics](#interface-with-pragmatics)
- [Interface with Information Structure](#interface-with-information-structure)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

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

## Discourse network

A discourse model tracks referents and relations while keeping textual order distinct from event order and causal direction.

The constructed passage is: “Although the roads were icy, Anna sent the reports that Maya had prepared to Leo. He thanked her because he needed them.”

### Discourse network representation

```text
roads icy --concessive obstacle--> Anna sends reports
Maya prepares reports --earlier than--> Anna sends reports
Leo needs reports --reason offered for--> Leo thanks Anna

He -> Leo; her -> Anna (preferred); them -> reports
```

### Discourse network worked interpretation

The reference of her is preferential, not logically forced by the string; a context could make Maya relevant. The icy-road relation defeats an expectation rather than asserting a contradiction. The thanks clause relates to the need for reports without proving every unstated motive.

### Discourse network assumptions and limits

This is a small authored relation network, not a full RST or SDRT implementation. No single relation inventory is declared universal. The supplied examples are constructed, not annotated natural discourse.

### Discourse network evaluation and counterevidence

For each edge, identify textual units, relation direction, connective if present, and contextual evidence. A graph of arrows without these annotations does not establish coherence.

### Discourse network evidence status

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this section. Inspect the linked record's access extent and nonclaims.

- [Rhetorical Structure Theory website introduction and relation definitions](../references/mann-taboada-undated-rst-introduction.md#relations) — support is limited to the named section in that record.

## Interfaces
**Pragmatics Discourse:** referents, assumptions and commitments change through interaction; rejection prevents automatic acceptance. **Discourse Information Structure:** accessibility and the current issue shape topic, focus and background. **Semantics** contributes the propositions and situations linked by a discourse relation. **Syntax** supplies clause structure but does not alone determine the discourse network.

### Interface with Pragmatics

An utterance interpretation constrains possible discourse updates, while acceptance, challenge and wider context determine what actually becomes shared.

Track proposed context updates and uptake rather than recording every assertion as an established fact. The counterpart is explained in [Pragmatics](english-pragmatics-system.md#interface-with-discourse).

#### Interface with Pragmatics representation

Represent a context before the utterance, the proposed contribution, candidate referents and background, and alternative next states. An assertion proposes information; it does not automatically make that information true or accepted. A discourse referent can be introduced for discussion without identifying a real object independently of the conversation.

#### Interface with Pragmatics worked analysis

A speaker says “A courier left a parcel.” One possible next utterance, “It was damaged,” maintains reference to the parcel. Another, “No courier came today,” challenges the preceding claim. The first statement therefore does not justify unconditionally storing courier-arrival as an established fact. Record the discourse proposal and its uptake separately.

#### Interface with Pragmatics evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Pragmatics assumptions and limits

The update vocabulary is a working analytical device. No full dynamic semantics or algorithm for all dialogue responses is implemented; misinformation, quotation and hypothetical discourse require explicit scope. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Pragmatics evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Information Structure

A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable.

Relate accessible referents and the current issue to possible topic and focus analyses. The counterpart is explained in [Information Structure](english-information-structure-system.md#interface-with-discourse).

#### Interface with Information Structure representation

| Endpoint | Schematic fields |
|---|---|
| discourse context | accessible_referents, prior_utterances, candidate_questions |
| focus domain | question_under_discussion, focus_span, background |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Information Structure essential terms

A **discourse context** records what has been said, which referents are accessible and what issue is being addressed. A **focus domain** is the word or larger expression that supplies relevant alternatives relative to that issue. Its **background** is what the comparison holds constant. Topic concerns what the discourse is about; none of these labels is simply another name for grammatical Subject. A question under discussion can be implicit, but an analyst must state the assumed question rather than invent an observed conversational context.

#### Interface with Information Structure worked interpretation

For *Who repaired the printer?*, the answer *Nina repaired the printer* can focus *Nina*, contrasting her with other possible repairers. For *What did Nina repair?*, the same answer can focus *the printer*, contrasting it with other possible objects. For *What did Nina do?*, the focus can be the larger phrase *repaired the printer*. These constructed pairs show that the sentence string does not by itself fix one focus span or Topic. Without a stated context, preserve alternative analyses rather than selecting one as fact.

#### Interface with Information Structure assumptions and limits

This is a QUD-compatible working bridge, not a consensus theory of discourse. Context may be insufficient to identify one topic or focus; alternative analyses must remain explicit.

#### Interface with Information Structure evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Information Structure evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Evaluation and counterevidence
Underline both spans in each proposed relation, name its direction and explain what in the text supports it. Test a rival relation or antecedent. Distinguish explicit connective evidence from a contextual preference. If both readings remain possible, retain both rather than forcing a unique graph.

Diagnostic: does *Maya arrived. The alarm sounded* entail that Maya caused the alarm? No. Even an inferred temporal order would not establish causation.

## Assumptions and limits
This is a small descriptive model. Full dialogue management, discourse segmentation standards, genre differences and competing coherence theories require more detailed work. Constructed text and one analyst's interpretation are not an annotated corpus or inter-annotator agreement study.

## Evidence status
**Provisional; independent review pending.** The [RST Reference](../references/mann-taboada-undated-rst-introduction.md) identifies selected relation definitions and their interpretation limits. The printer passage and its alternative readings are authored examples, not copied source analyses.

## Related knowledge
[Discourse referent](../concepts/discourse-referent.md), [anaphora and accessibility](../concepts/anaphora-and-accessibility.md), [cohesion and coherence](../concepts/cohesion-and-coherence.md), [discourse relation](../concepts/discourse-relation.md) and [temporal causal and evidential relations](../concepts/temporal-causal-and-evidential-relations.md) expand the distinctions. [Trace discourse interpretation](../methods/trace-discourse-interpretation.md) supports a repeatable analysis.
