---
id: "english:model:english-semantics-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["semantics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:compositionality", "english:concept:reference-and-denotation", "english:concept:semantic-role", "english:concept:quantification-and-scope", "english:concept:negation-and-entailment", "english:concept:tense-and-aspect", "english:concept:modality", "english:concept:semantic-predicate", "english:concept:situation-type", "english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:lexical-selection", "english:concept:object-and-pp-complement", "english:concept:valency-and-argument-structure", "english:concept:contextual-resolution", "english:concept:implicature", "english:concept:presupposition", "english:concept:common-ground"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-syntax-system", "english:model:english-pragmatics-system"]
system_domain: "semantics"
---

# English semantics system

## Key takeaway
Semantic analysis distinguishes conventional meaning, compositional structure, reference and inference under an explicitly fixed interpretation.

## Summary
This Model organizes lexical meaning, predication, participants, quantification, scope, negation, tense, aspect and modality. It shows how a small change in operator scope can change truth conditions and why an apparent inference must be tested against countermodels. Formal examples use a deliberately finite domain; they do not settle every reading of English. Finite-domain scope and temporal-reference representations are included alongside interfaces with Lexicon, Syntax and Pragmatics. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Quantifier scope](#quantifier-scope)
- [Temporal reference](#temporal-reference)
- [Interfaces](#interfaces)
  - [Interface with Lexicon](#interface-with-lexicon)
  - [Interface with Syntax](#interface-with-syntax)
  - [Interface with Pragmatics](#interface-with-pragmatics)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

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

## Quantifier scope

A finite-domain toy model makes scope differences explicit without claiming that logic alone predicts English reading availability.

### Quantifier scope representation

```text
EVERY > A:
  for every x in teachers, some y in books satisfies recommend(x,y)
A > EVERY:
  some y in books satisfies recommend(x,y) for every x in teachers

NOT > EVERY:
  not all relevant individuals satisfy P
EVERY > NOT:
  all relevant individuals fail to satisfy P
```

### Quantifier scope worked interpretation

Three teachers with nonoverlapping recommendations satisfy EVERY > A but not A > EVERY. A common recommended book satisfies both. A > EVERY does not mean that exactly one book exists or that nobody recommends additional books.

### Quantifier scope assumptions and limits

Classical quantification treats an empty universal restrictor vacuously. With no relevant teachers, shared-book claims also depend on whether the book domain is empty. These edge cases are retained in regression tests, not hidden behind informal some/not-all glosses.

### Quantifier scope evaluation and counterevidence

Enumerate small domains and relations to verify formal implications. Such tests validate only the explicit logical implementation. Actual acceptability and accessibility of inverse scope require linguistic evidence.

### Quantifier scope evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Temporal reference

Temporal interpretation separates tense, reference time, event structure and aspectual viewpoint.

### Temporal reference representation

```text
Bounded past-perfect example:
E: finish report < R: Ravi arrives < S: speech time

Progressive example:
work interval: [--------- R ---------]

Continuing present-perfect example:
residence: [prior interval ----- now ---- possible continuation]
```

### Temporal reference worked interpretation

"Maya had finished when Ravi arrived" supports an earlier completion. "Maya was finishing" presents an internal phase and does not entail completion. "Maya has lived here for years" can continue at speech time, showing why a strict E-before-R picture is not adequate for every perfect.

### Temporal reference assumptions and limits

The E/R/S diagram is a useful simplification, not an exhaustive tense theory. Present forms can occur in schedules and historical presents; aspect interacts with lexical sense and complements.

### Temporal reference evaluation and counterevidence

Check which orderings are required, merely favored or unspecified. Do not infer actual-world completion from a participial form or introduce an independently dated event absent from context.

### Temporal reference evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Interfaces
**Lexicon Semantics:** a selected sense contributes to composition. **Syntax Semantics:** hierarchy and construction influence composition and participant mapping. **Semantics Pragmatics:** contextual values and discourse assumptions help determine an utterance interpretation; formal semantics can itself be context-sensitive. Information structure and prosody may affect which alternatives are salient without erasing lexical constraints.

### Interface with Lexicon

A sense-specific lexical entry constrains an interpretation without making a spelling identify one context-independent predicate.

Compose the relevant sense with other expressions and context rather than treating spelling as a unique predicate. The counterpart is explained in [Lexicon](english-lexicon-system.md#interface-with-semantics).

#### Interface with Lexicon representation

| Endpoint | Schematic fields |
|---|---|
| lexical sense entry | lexeme, sense, selection |
| predicate interpretation | predicate, arguments, contextual_restrictions |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Lexicon essential terms

A **lexical sense entry** records a word's category, a conventional meaning contribution and relevant combinatorial restrictions. A **predicate interpretation** characterizes a property, relation or situation and its participants under the selected reading. Choosing a sense is not merely choosing a spelling. Compositional structure and context constrain how the contribution combines with other expressions; this bridge does not reduce complete sentence meaning to a dictionary gloss.

#### Interface with Lexicon worked interpretation

In *Maya runs every morning*, a locomotion use of RUN characterizes an activity involving Maya. In *Maya runs a company*, a management use relates Maya to the company she manages. Keeping the same spelling while selecting the locomotion contribution for the second sentence would fail to capture its ordinary intended reading. A constructional or coercion account can distribute the explanation differently; the record should state which analysis is being used instead of assuming one location for all meaning.

#### Interface with Lexicon assumptions and limits

The location of lexical and constructional information differs among theories. This bridge is schematic and does not establish an exhaustive sense inventory, an automatic disambiguator or full claim-level support.

#### Interface with Lexicon evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Lexicon evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

### Interface with Syntax

Construction-sensitive mappings connect grammatical functions with semantic roles without identifying the two dimensions.

Track which participants are preserved, added or implicit when grammatical functions change. The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-semantics).

#### Interface with Syntax representation

| Construction | Giver | Recipient | Theme |
|---|---|---|---|
| Leo gave Maya a prize | Subject | Indirect Object | Direct Object |
| Leo gave a prize to Maya | Subject | NP inside to-PP | Direct Object |
| Maya was given a prize by Leo | NP inside by-PP | Subject | Retained Object |

#### Interface with Syntax worked interpretation

A passive can preserve the basic participant relations while changing grammatical functions. A causative alternation such as "The glass broke / Leo broke the glass" can add a Causer instead. A psych predicate can give a Stimulus Subject and Experiencer Object without passive morphology.

#### Interface with Syntax assumptions and limits

Dative alternation has lexical, semantic and discourse restrictions; the table does not establish complete synonymy. Role inventories vary. The mapping is analytical rather than evidence of a particular neural transfer operation.

#### Interface with Syntax evaluation and counterevidence

Ask which participants are added, omitted, implicit or redistributed. A changed function alone does not necessarily add a role. Keep explicit versus inferred participants separate in every example.

#### Interface with Syntax evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

### Interface with Pragmatics

Conventional meaning, contextual resolution and defeasible inference jointly constrain utterance interpretation.

Separate conventional contributions and contextual values from additional defeasible inferences. The counterpart is explained in [Pragmatics](english-pragmatics-system.md#semantics-pragmatics-interface).

#### Interface with Pragmatics representation

```text
I -> speaker-related interpretation rule -> Maya in this utterance
here -> contextually anchored location -> the desk in this situation
some -> existential contribution -> possible not-all implicature
stop -> background prior activity -> accommodation or challenge
```

#### Interface with Pragmatics worked interpretation

Resolving I to Maya supplies a contextual value; inferring not all from some adds a cancellable interpretation under suitable assumptions. Neither mechanism licenses replacing arbitrary lexical meaning with whatever a hearer finds convenient.

#### Interface with Pragmatics assumptions and limits

The semantic/pragmatic boundary is theory-dependent. Formal semantics may itself take contexts as arguments; this model is not based on context-free semantics. Presupposition involves both conventional triggers and discourse behavior.

#### Interface with Pragmatics evaluation and counterevidence

Annotate what a source explicitly supports, what the analyst resolves, and which inference remains defeasible. Retain a distinction between a possible speaker intention and an observed conversational response.

#### Interface with Pragmatics evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Evaluation and counterevidence
State the reading, domain and background assumptions before testing an inference. Write a small countermodel, preserve scope distinctions and separate explicit participants from inferred ones. If a reading is unnatural, distinguish a formal possibility from an empirically supported English interpretation.

## Assumptions and limits
Role inventories, plural meanings, intensional semantics and the syntax of scope vary across theories. The finite formulas here are teaching models, not complete semantic derivations or experimental findings. Detailed lexical aspect, presupposition projection and modal bases require further evidence.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records limited word-meaning and participant-role passages. The quantifier and negation cases are constructed logical analyses; existing tests check consistency with declared formulas, not natural-language scope accessibility.

## Related knowledge
[Compositionality](../concepts/compositionality.md), [reference and denotation](../concepts/reference-and-denotation.md), [semantic role](../concepts/semantic-role.md), [quantification and scope](../concepts/quantification-and-scope.md), [negation and entailment](../concepts/negation-and-entailment.md), [tense and aspect](../concepts/tense-and-aspect.md) and [modality](../concepts/modality.md) expand the foundations. [Quantifier scope](#quantifier-scope) supplies the explicit finite-domain representation.
