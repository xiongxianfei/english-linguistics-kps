---
id: "english:model:english-semantics-system"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["semantics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:compositionality", "english:concept:reference-and-denotation", "english:concept:semantic-role", "english:concept:quantification-and-scope", "english:concept:negation-and-entailment", "english:concept:tense-and-aspect", "english:concept:modality"]
uses_models: ["english:model:lexicon-semantics-interface", "english:model:syntax-semantics-interface", "english:model:semantics-pragmatics-interface", "english:model:quantifier-scope-model"]
system_domain: "semantics"
---

# English semantics system

## Key takeaway
Semantic analysis distinguishes conventional meaning, compositional structure, reference and inference under an explicitly fixed interpretation.

## Summary
This Model organizes lexical meaning, predication, participants, quantification, scope, negation, tense, aspect and modality. It shows how a small change in operator scope can change truth conditions and why an apparent inference must be tested against countermodels. Formal examples use a deliberately finite domain; they do not settle every reading of English.

## Purpose
For an expression in a stated context, make explicit what interpretation is being evaluated and what follows from it. Keep the contribution of an expression separate from additional assumptions about the speaker's intention.

## Representation

| Component | Analytical contribution |
|---|---|
| Lexical contribution | Conventional senses and properties of words |
| Composition | How interpreted parts combine with structure |
| Reference and denotation | Individuals, sets or other values under an interpretation |
| Predication and roles | Situations and the ways participants are involved |
| Operators and scope | Quantification, negation and modality interacting over representations |
| Time and aspect | Temporal location, viewpoint and situation type |

A semantic predicate is not the same thing as a syntactic Predicate phrase. Semantic roles such as Agent, Theme, Recipient or Experiencer are analytical labels, not replacements for Subject and Object.

## Essential distinctions
**Entailment** holds when a conclusion must be true whenever the premise is true under the specified interpretation. A single coherent countermodel with a true premise and false conclusion defeats that proposed entailment. This differs from a likely inference or conversational suggestion.

**Ambiguity** permits distinct interpretations; **vagueness** leaves borderline cases within an interpretation. A sense, its denotation in a context and its emotional associations should not be collapsed into one field.

Quantifiers concern amounts or distributions over domains. Scope determines how operators interact. Negation can take scope over a quantifier or fall inside its scope; *not every* and *no* therefore need not have the same truth conditions.

Tense locates a situation relative to reference points; aspect concerns how the situation is presented or internally organized. A progressive does not entail completion. A perfect construction does not simply mean completed. Modality evaluates possibilities or necessities relative to a relevant set of alternatives, such as circumstances, evidence or rules.

## Worked analysis
Consider *Every student read a report*. Two schematic interpretations are:

```text
For every student x, there is a report y that x read.
There is a report y such that every student x read y.
```

In a constructed domain, Anna reads report A and Ben reads report B, with neither reading the other report. The first representation is true; the second is false. This shows that the two formulas are not equivalent. It does not prove that every speaker and context freely admits both readings of the sentence.

Under the first interpretation, there need not be one report shared by all students. Conversely, a report read by every student satisfies both formulas in this simple nonempty example. Empty domains and presuppositional assumptions must be specified rather than hidden.

For *Not every student passed*, the finite classical interpretation excludes universal success. It does not by itself require that at least one student passed: a situation where all failed is a counterexample to that stronger inference.

## Interfaces
**Lexicon Semantics:** a selected sense contributes to composition. **Syntax Semantics:** hierarchy and construction influence composition and participant mapping. **Semantics Pragmatics:** contextual values and discourse assumptions help determine an utterance interpretation; formal semantics can itself be context-sensitive. Information structure and prosody may affect which alternatives are salient without erasing lexical constraints.

## Evaluation and counterevidence
State the reading, domain and background assumptions before testing an inference. Write a small countermodel, preserve scope distinctions and separate explicit participants from inferred ones. If a reading is unnatural, distinguish a formal possibility from an empirically supported English interpretation.

## Assumptions and limits
Role inventories, plural meanings, intensional semantics and the syntax of scope vary across theories. The finite formulas here are teaching models, not complete semantic derivations or experimental findings. Detailed lexical aspect, presupposition projection and modal bases require further evidence.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records limited word-meaning and participant-role passages. The quantifier and negation cases are constructed logical analyses; existing tests check consistency with declared formulas, not natural-language scope accessibility.

## Related knowledge
[Compositionality](../concepts/compositionality.md), [reference and denotation](../concepts/reference-and-denotation.md), [semantic role](../concepts/semantic-role.md), [quantification and scope](../concepts/quantification-and-scope.md), [negation and entailment](../concepts/negation-and-entailment.md), [tense and aspect](../concepts/tense-and-aspect.md) and [modality](../concepts/modality.md) expand the foundations. [Quantifier scope model](quantifier-scope-model.md) supplies the explicit finite-domain representation.
