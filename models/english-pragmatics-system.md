---
id: "english:model:english-pragmatics-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["pragmatics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:roberts-2012-information-structure"]
uses_concepts: ["english:concept:common-ground", "english:concept:deixis", "english:concept:contextual-resolution", "english:concept:presupposition", "english:concept:implicature", "english:concept:speech-act", "english:concept:utterance-and-speaker-meaning", "english:concept:discourse-referent", "english:concept:anaphora-and-accessibility"]
uses_models: ["english:model:english-semantics-system", "english:model:english-discourse-system"]
system_domain: "pragmatics"
---

# English pragmatics system

## Key takeaway
Pragmatic analysis separates contextual resolution, discourse background and defeasible reasoning about what a speaker is doing.

## Summary
Pragmatics investigates interpretation in use. This Model distinguishes utterance context, deixis, common ground, presupposition, implicature and speech acts. A worked conversation shows why a likely interpretation is not automatically an entailment or proof of intention. Context contributes to meaning without permitting arbitrary replacement of conventional expression meaning. An utterance-interpretation worksheet and interfaces with Semantics and Discourse separate interpretation from uptake. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Utterance interpretation](#utterance-interpretation)
- [Interfaces](#interfaces)
- [Interface with Semantics](#interface-with-semantics)
- [Interface with Discourse](#interface-with-discourse)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

## Purpose
Given an utterance and available context, state what is encoded, what must be resolved, what is treated as background and what is inferred. Missing context should remain an explicit uncertainty.

## Representation

| Analytical layer | What it asks | Example |
|---|---|---|
| Conventional contribution | What does the expression contribute in this use? | A selected lexical sense and grammatical construction |
| Contextual resolution | Which values are supplied by the occasion? | The referent of *I*, a relevant location for *here* |
| Background commitments | What is taken for granted or accommodated? | Prior activity associated with a use of *stop* |
| Conversational reasoning | What additional interpretation is suggested? | A possible not-all inference from *some* |
| Interactional action | What is being attempted in the exchange? | A request, assertion, question or offer |

These are analytical distinctions, not necessarily successive psychological stages. Different theories place their boundaries differently.

## Essential distinctions
An **utterance** is an expression used on an occasion. **Deixis** relates an expression to contextual coordinates such as speaker, time or place. **Common ground** is what participants treat as shared for the exchange; it need not be true, and participants can disagree about it.

A **presupposition** is a background condition or commitment associated with an expression or construction under an analysis. Its behavior under negation, questions and larger embeddings is informative, but projection can be context-sensitive. Accommodation means accepting an otherwise unstated background to make an utterance interpretable; rejection or clarification may instead occur.

A **conversational implicature** is an additional interpretation supported by assumptions about the exchange rather than simply identical to literal truth conditions. Cancellation and contextual change help diagnose it, but no single test works for every phenomenon. A **speech act** concerns the action performed or attempted through speaking; grammatical clause type does not uniquely fix that action.

## Worked analysis
A manager asks, *Did you inspect all the printers?* A technician replies, *I inspected some of them*.

Resolve *I* to the replying speaker and *them* to the contextually relevant printers, unless another antecedent is established. On a basic existential reading, the reply reports inspection of at least some printers. In this context it may suggest that not all were inspected. The continuation *in fact, I inspected all of them* can cancel that stronger suggestion, although its conversational naturalness depends on the context.

Do not record the not-all interpretation as logically forced. The speaker might be uncertain, answering a different concern or using a different contextual contrast. Likewise, *Can you check the printer?* can function as a request rather than merely an inquiry into ability, but its actual uptake requires interactional evidence.

## Utterance interpretation

An utterance interpretation records conventional constraints, contextual values and defeasible communicated inferences separately.

### Utterance interpretation representation

| Field | Constructed example |
|---|---|
| Expression | Could you pass that folder? |
| Clause type | Interrogative |
| Conventional contribution | Modal question about passing |
| Contextual values | Addressee and demonstrated folder |
| Likely force | Request |
| Possible effect | Hearer passes the folder |
| Uncertainty | Ability inquiry remains possible in another context |

### Utterance interpretation worked interpretation

The request is not a permanent lexical definition of could. The contextual folder must be identified before the request can be acted on. Recognition of the request does not guarantee compliance, and the effect must not be invented as an observed outcome.

### Utterance interpretation assumptions and limits

Conventionalized indirect constructions complicate a rigid literal-then-inferred sequence. This representation is an analyst worksheet, not a measured comprehension process.

### Utterance interpretation evaluation and counterevidence

For every added inference, record why the speaker might intend it and whether a coherent cancellation is possible. Preserve alternative readings when the contextual evidence does not decide.

### Utterance interpretation evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Interfaces
**Semantics Pragmatics:** conventional contributions, contextual values and defeasible inferences jointly constrain interpretation. **Pragmatics Discourse:** an interpretation can be accepted, challenged or used in later turns; an assertion does not automatically become shared knowledge. **Discourse Information Structure:** the issue being addressed helps organize focus and relevance. **Prosody** can contribute cues, but a tone is not a universal code for one intention.

### Interface with Semantics

Conventional meaning, contextual resolution and defeasible inference jointly constrain utterance interpretation.

Explain contextual resolution and speaker-related inference without discarding conventional meaning constraints. The counterpart is explained in [Semantics](english-semantics-system.md#interface-with-pragmatics).

#### Interface with Semantics representation

```text
I -> speaker-related interpretation rule -> Maya in this utterance
here -> contextually anchored location -> the desk in this situation
some -> existential contribution -> possible not-all implicature
stop -> background prior activity -> accommodation or challenge
```

#### Interface with Semantics worked interpretation

Resolving I to Maya supplies a contextual value; inferring not all from some adds a cancellable interpretation under suitable assumptions. Neither mechanism licenses replacing arbitrary lexical meaning with whatever a hearer finds convenient.

#### Interface with Semantics assumptions and limits

The semantic/pragmatic boundary is theory-dependent. Formal semantics may itself take contexts as arguments; this model is not based on context-free semantics. Presupposition involves both conventional triggers and discourse behavior.

#### Interface with Semantics evaluation and counterevidence

Annotate what a source explicitly supports, what the analyst resolves, and which inference remains defeasible. Retain a distinction between a possible speaker intention and an observed conversational response.

#### Interface with Semantics evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

### Interface with Discourse

An utterance interpretation constrains possible discourse updates, while acceptance, challenge and wider context determine what actually becomes shared.

Distinguish the contribution proposed by an utterance from what later interaction accepts or challenges. The counterpart is explained in [Discourse](english-discourse-system.md#interface-with-pragmatics).

#### Interface with Discourse representation

Represent a context before the utterance, the proposed contribution, candidate referents and background, and alternative next states. An assertion proposes information; it does not automatically make that information true or accepted. A discourse referent can be introduced for discussion without identifying a real object independently of the conversation.

#### Interface with Discourse worked analysis

A speaker says “A courier left a parcel.” One possible next utterance, “It was damaged,” maintains reference to the parcel. Another, “No courier came today,” challenges the preceding claim. The first statement therefore does not justify unconditionally storing courier-arrival as an established fact. Record the discourse proposal and its uptake separately.

#### Interface with Discourse evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Discourse assumptions and limits

The update vocabulary is a working analytical device. No full dynamic semantics or algorithm for all dialogue responses is implemented; misinformation, quotation and hypothetical discourse require explicit scope. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Discourse evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

## Evaluation and counterevidence
Hold the wording fixed and vary the context. Separate referent resolution from an added inference. Compare cancellation, denial and responses under clearly stated readings. Record alternative explanations, especially when the analyst has not observed the conversation or speaker.

Diagnostic: does a declarative sentence always make an assertion? No. Form constrains possible uses, but a declarative may also participate in confirmation-seeking, quoting or other acts under appropriate conditions.

## Assumptions and limits
The semantic/pragmatic boundary, presupposition treatment and theories of speech acts are contested. This foundation does not claim access to a speaker's private mental state, cultural universality of politeness strategies or a validated interaction classifier.

## Evidence status
**Provisional; independent review pending.** The [Roberts Reference](../references/roberts-2012-information-structure.md) records an abstract-level QUD framework, not verification of every inference in this Model. The distinctions are developed in the linked canonical notes; the conversation above is constructed and needs no claim of actual speaker behavior.

## Related knowledge
[Common ground](../concepts/common-ground.md), [deixis](../concepts/deixis.md), [contextual resolution](../concepts/contextual-resolution.md), [presupposition](../concepts/presupposition.md), [implicature](../concepts/implicature.md), [speech act](../concepts/speech-act.md) and [utterance and speaker meaning](../concepts/utterance-and-speaker-meaning.md) provide focused explanations.
