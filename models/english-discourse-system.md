---
id: "english:model:english-discourse-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["discourse"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:mann-taboada-undated-rst-introduction", "english:reference:jurafsky-martin-2026-discourse"]
uses_concepts: ["english:concept:discourse-referent", "english:concept:anaphora-and-accessibility", "english:concept:cohesion-and-coherence", "english:concept:discourse-relation", "english:concept:temporal-causal-and-evidential-relations", "english:concept:contrast-and-concession", "english:concept:common-ground", "english:concept:speech-act", "english:concept:utterance-and-speaker-meaning", "english:concept:focus-topic-and-qud", "english:concept:givenness-and-bridging"]
uses_models: ["english:model:english-pragmatics-system", "english:model:english-information-structure-system"]
system_domain: "discourse"
---

# English discourse system

A sentence can describe an event without explaining how that event fits a conversation or a text. Discourse analysis asks how stretches of language form a connected contribution: which entities they concern, how their claims relate, and how speakers respond to one another.

This Model develops eight introductory areas inside one account. The aim is to explain a short passage or exchange by identifying its units, tracking reference, proposing relations and preserving unresolved alternatives. Reference tracking, rhetorical structure and conversation analysis contribute different perspectives; they are not successive stages of a single processing algorithm. The organization and examples here are authored teaching choices, grounded in the selected sources identified below.

## Contents

- [Discourse units](#discourse-units)
- [Discourse referents](#discourse-referents)
- [Anaphora and accessibility](#anaphora-and-accessibility)
- [Givenness and bridging](#givenness-and-bridging)
- [Cohesion and coherence](#cohesion-and-coherence)
- [Discourse relations](#discourse-relations)
- [Discourse structure](#discourse-structure)
- [Conversation and repair](#conversation-and-repair)
- [Worked analysis](#worked-analysis)
- [Discourse network](#discourse-network)
- [Interfaces](#interfaces)
  - [Interface with Pragmatics](#interface-with-pragmatics)
  - [Interface with Information Structure](#interface-with-information-structure)
- [Evidence and limits](#evidence-and-limits)
- [Related knowledge](#related-knowledge)

## Discourse units

Before relating parts of a discourse, identify the spans being related. A **sentence** is a grammatical unit; an **utterance** is a use of language in a situation; a **turn** is a participant's contribution before another takes the floor. These boundaries need not coincide. A turn can contain several sentences, while *The display*, answering *What lit up?*, can be a meaningful contribution without a full finite clause.

A **discourse unit** is a span selected for an analysis. Clauses are useful starting points for many text relations, but the segmentation must fit the account. In *The printer stopped because the cable came loose*, a cause analysis distinguishes the two clauses even though there is one written sentence. Later, an entire paragraph can supply evidence for another span. A relative clause may introduce useful background without necessarily becoming a separate unit under every annotation scheme.

Keep three kinds of representation apart:

| Representation | What it identifies | Example |
|---|---|---|
| Text spans such as U1 and U2 | The language being analyzed | U1 = *The printer stopped*; U2 = *the cable came loose* |
| Referents such as p | Entities, events or other objects of discussion | p = the printer being discussed |
| Proposed relations | Connections between situations, claims or contributions | U2 offers a cause for the stopping described in U1 |

Span labels are analytical bookkeeping. They do not identify mental processing steps or prove that all analysts would segment the text alike. State the boundaries before assigning a relation; otherwise even an apparently familiar label such as *explanation* has no definite endpoints.

## Discourse referents

A **mention** is an expression in the text. A **discourse referent** is what the analysis represents as being discussed. Several mentions can concern one referent, and one sentence can introduce several referents. In *Maya brought in a printer. The machine was old*, *a printer* and *the machine* can belong to one **coreference chain**: different expressions interpreted as referring to the same printer.

A small working record makes the distinction visible:

| Mention | Proposed referent | Basis and limits |
|---|---|---|
| *Maya* | m, a person | Introduced by name; identity outside this example is unspecified |
| *a printer* | p, a printer | Introduced as part of the asserted situation |
| *the machine* | p | Compatible description and local context favor the same printer |

Referents need not be independently existing physical objects. *Maya imagined a dragon. It had silver wings* supports discussion of a dragon within the imagined situation. Events and propositions can also be picked up: in *The printer failed. That surprised Maya*, *that* can refer to the failure or the fact that it occurred, rather than to the printer. Keep those alternatives distinct when the analysis requires them.

Introducing a referent records an interpretation of a contribution, not proof of its truth. A quoted claim, a hypothetical situation and an accepted report need different scope or commitment annotations. The [selected reference chapter](../references/jurafsky-martin-2026-discourse.md#reference-and-information-status) supports the distinction between mentions and referents; the small record above is our teaching representation, not a full dynamic semantic model.

## Anaphora and accessibility

**Anaphora** involves interpreting an expression through another accessible expression or interpretation. Coreference is one possible outcome, but the two terms are not interchangeable. In *Every technician checked their badge*, the badge owner can vary with the technician; the sentence need not select one fixed person as the antecedent of *their*. In *The printer failed. That surprised Maya*, the anaphoric target can be a larger prior contribution.

**Accessibility** concerns which interpretations remain available in the relevant linguistic and discourse context. Recency helps, but it is not a rule that a pronoun denotes the nearest noun. Compare these constructed examples:

- *Maya put the phone beside the paper notebook and charged it.* Ordinary knowledge favors the phone despite the nearer noun *notebook*.
- *Maya put the phone beside the laptop and charged it.* Both devices can be charged, so the wording leaves a more substantial ambiguity.

Grammatical compatibility, semantic plausibility, current attention and the wider context constrain candidates together. None is a universal substitute for the others. A pronoun can also depend on the situation rather than an earlier mention: pointing at a printer while saying *It is broken* is situational reference.

Linguistic scope matters too. *Maya does not own a printer. It is old* does not, on an ordinary reading without further context, establish a particular owned printer for *it*. This is not a ban on every reference following negation: a previously established printer, a quotation or a deliberately shifted hypothetical context can change the analysis. The selected source illustrates accessibility restrictions; a complete account of negation, quantification and modal discourse requires further theory.

The useful outcome is a justified candidate set. When two referents remain possible, record both and identify what additional wording or context would distinguish them.

## Givenness and bridging

A referent can be new to the current text while still being familiar or inferable. These distinctions explain why reference does not always begin with an indefinite expression and then proceed mechanically to a pronoun.

| Distinction | What is available | Constructed example |
|---|---|---|
| Discourse old | Already introduced in this discourse | *A printer arrived. The printer was damaged.* |
| Hearer old | Assumed familiar to the addressee, without requiring a prior mention here | *The sun is bright today.* |
| Inferable through bridging | An associated referent recoverable through a contextual link | *A printer arrived. The display was cracked.* |

In the last example, the display is not identical to the printer. The reader supplies a plausible part–whole link and accommodates a relevant display. That **bridging** inference differs from coreference. A printer description does not logically guarantee that the device has a display; the context can defeat or complicate the inference. If two printers and several displays are present, *the display* may need clarification.

Givenness also differs from momentary salience. An earlier mention can remain known while becoming a less natural pronoun target. Conversely, an inferable but unmentioned object can become central. These are reasons to track the discourse history and the assumed audience knowledge separately.

The categories in the [inspected textbook passages](../references/jurafsky-martin-2026-discourse.md#reference-and-information-status) support this introductory contrast. They do not establish one universal givenness scale or a deterministic rule for choosing articles and pronouns. Being given also does not prevent an expression from being focused; that depends on the current question, as the Information Structure interface explains.

## Cohesion and coherence

**Cohesion** concerns linguistic links across a text: repeated words, related vocabulary, pronouns, ellipsis and connectives. **Coherence** concerns an interpretation of how the contributions belong together. Cohesive devices help a reader construct that interpretation, but do not guarantee it.

*The printer stopped. Maya checked it* contains a possible pronominal link. *Maya checked the printer, and Leo did too* uses ellipsis: the missing predicate associated with *did too* is understood from the preceding clause. *The printer stopped. Therefore, Maya checked it* supplies an overt cue to a proposed consequence or motivated response.

Compare *The printer stopped. Printers contain parts. Parts of the city are expensive*. Repetition and lexical overlap connect the wording, but they do not by themselves establish a useful account of a printer problem. A special context might make the sequence relevant; without one, an analyst should not invent the missing purpose.

Conversely, *The room was dark. Maya found a torch* can support a coherent response-to-problem interpretation without an explicit connective. The interpretation uses assumptions about darkness and torches. Those assumptions remain defeasible: perhaps Maya was following a scavenger-hunt instruction unrelated to the darkness.

This distinction leads to a practical explanatory question: **what relation does the wording support, and what must the reader supply?** Counting pronouns or connectives does not answer it.

## Discourse relations

A **discourse relation** characterizes how specified spans contribute together. Some relations concern represented events; others concern reasons for believing a claim or the contribution an utterance makes. Distinguishing these levels avoids treating every *because* as the same kind of causal statement.

| Working distinction | What connects the spans | Constructed example and qualification |
|---|---|---|
| Temporal sequence | One situation follows another | *Maya arrived. Then the alarm sounded.* Order alone does not establish a cause. |
| Cause or result | One situation is presented as producing another | *The cable came loose, so the printer stopped.* This reports a causal account; the wording is not independent evidence that it is correct. |
| Evidence | One contribution supports belief in another | *The printer is receiving power: its indicator is lit.* The light supports the claim; it does not cause the power supply. |
| Elaboration | One span develops another with detail | *Maya inspected the printer. She examined its display and cable.* The second sentence expands the first. |
| Contrast | Relevant alternatives are compared along a dimension | *This printer is fast; that one is quiet.* The relevant comparison needs context; contrast need not be logical contradiction. |
| Concession | A contribution holds despite an expectation associated with another | *Although the printer was old, it worked well.* Oldness is presented as a possible reason to expect otherwise. |
| Condition | One situation is presented as a condition for another | *If the cable is loose, the printer may stop.* Neither clause asserts that the condition actually holds. |

This is an authored introductory selection. The [RST relation definitions](../references/mann-taboada-undated-rst-introduction.md#relations) provide selected distinctions, including evidence, cause, elaboration, contrast and concession; they are not a declaration that all discourse theories use identical labels or structures.

Direction and scope matter. In *The display is dark because the power is off*, the power state can explain the darkness. In *The power is off, because the display is dark*, the darkness may instead be offered as evidence for the speaker's conclusion. Context can support other readings, so punctuation alone does not settle the analysis. A reason for saying something is also distinct from a cause of the event described: *There is coffee in the kitchen, because you look tired* can explain the relevance of the offer rather than the existence of the coffee.

Textual order, event order and explanatory direction are separate. *Maya checked the printer. The cable had come loose* presents the cable event later in the text while locating it earlier in the described sequence. Without *then*, *before*, tense or other contextual support, adjacency alone need not establish even temporal succession.

## Discourse structure

A text has organization beyond a list of pairwise links. A later sentence can explain one clause, support a paragraph-level claim or change the issue under discussion. This requires identifying the **span** a relation applies to and how smaller contributions form larger ones.

Consider *The printer needs repair. Its display is cracked. Its feed roller jams*. One plausible analysis treats the first sentence as a claim and the next two together as supporting evidence. Rhetorical Structure Theory can represent unequal contributions through a **nucleus**, central to the relation's purpose, and a **satellite**, supporting that nucleus. In this analysis the repair claim is the nucleus and the evidence span is its satellite. This is an analysis of communicative contribution, not a distinction between grammatical main and subordinate clauses.

```text
Claim: [The printer needs repair.]
  supported by: [Its display is cracked. Its feed roller jams.]
                two items contributing to the evidence span
```

RST also permits **multinuclear** organization, in which a relation connects contributions without selecting just one as its nucleus, as in some lists or contrasts. The source describes hierarchical combinations of spans and recognizes interpretation by an analyst. A proposed tree is therefore a representational choice to justify, not something automatically read off punctuation.

The larger purpose affects the analysis. In an exchange about *Why does the printer need repair?*, the two faults can support an answer. In a parts inventory, comparable descriptions may instead develop successive items. Topic continuity concerns what an extended stretch is about; rhetorical relations concern how its contributions connect. Neither is reducible to the presence of repeated words.

Keep this span organization separate from a timeline of events and from a coreference chain. All three can describe the same passage while answering different questions. The network below deliberately combines annotated relation types for teaching; it is not a complete RST tree or a claim that one tree accounts for every text. Genre conventions, long-range coherence and competing structural theories remain beyond this introductory treatment.

## Conversation and repair

Conversation is organized through contributions and responses as well as through propositions. A question makes an answer relevant; a request makes acceptance, refusal or another responsive move relevant. Such paired actions are often called **adjacency pairs**, but their parts need not be consecutive turns: a clarification can intervene.

| Turn | Constructed exchange | Contribution |
|---|---|---|
| 1 Maya | *Can you check it?* | A possible request whose target is unclear |
| 2 Leo | *The printer or the display?* | A clarification question about the request |
| 3 Maya | *The display.* | Answers the clarification and repairs the reference |
| 4 Leo | *Yes, I will.* | Accepts the original request after the clarification |

Here turns 2–3 form an inserted exchange within the request–response sequence. Leo's turn 2 does not simply ignore the first request: it addresses a problem that obstructs a suitable response. **Repair** concerns trouble in producing, hearing or understanding a contribution; it is not limited to correcting a grammatical error. In *Check the printer—sorry, the display*, the first speaker repairs their own wording. In the table, the other participant initiates clarification and the original speaker supplies it.

**Grounding** concerns establishing enough mutual understanding for the current purpose. Understanding a statement is distinct from accepting its truth or agreeing to act. *I understand which printer you mean, but I cannot check it* can resolve reference while refusing the request. Likewise, *I know what you are claiming, but the light does not prove it works* can display understanding while challenging a conclusion.

Turns, actions and sentences do not correspond one to one. A question may function as a request; one turn can both acknowledge an explanation and challenge it. Initiative can shift when a participant asks for clarification. The [selected conversation chapter](../references/jurafsky-martin-2026-discourse.md#conversation-and-grounding) introduces these distinctions but is explicitly an initial draft stub. This written example supplies no observations about pauses, overlap, intonation, gaze or actual speaker intentions. Detailed turn allocation, preference organization and repair typologies require broader sources and recorded interaction.

## Worked analysis

Return first to the constructed passage *The printer stopped. The display was dark. Maya checked it*.

Create a printer referent, a possible associated display and Maya. The display is introduced through bridging, not by renaming the printer. For *it*, the printer is plausible, but the display remains another possible target. The second sentence could provide evidence for the stopping claim or describe an accompanying state; the wording does not establish the cause. Maya's check may be a subsequent response, but its exact timing and motive remain unspecified. Adding *because* or *although* changes the cues while still requiring an account of relation direction and scope.

A longer constructed example connects the eight areas:

> Maya brought in a printer. The display was dark. She connected the power cable. Then it lit up.
>
> Leo: What lit up—the printer or the display?
>
> Maya: The display.
>
> Leo: That does not prove the printer can print.

The four initial sentences can be labeled U1–U4 for this analysis; the three later contributions are turns T1–T3. They are not seven equally sized events. T2 is an answer fragment, and T3 comments on the evidential significance of a prior event.

| Question | Proposed analysis | What remains open |
|---|---|---|
| What is being tracked? | Maya m, printer p, display d and power cable c; *she* picks up m. | The display and cable are plausibly associated with p, but their introduction relies on bridging assumptions. |
| What does *it* mean? | Before clarification, p and d are candidates; the lighting predicate favors d in ordinary context. T2 explicitly supplies d as the intended answer. | The earlier string alone did not determine this. T2 is evidence within the constructed exchange, not an observed resolution result. |
| What makes the passage cohesive? | The printer-related vocabulary, *she*, *it* and *then* connect its wording. | Cohesive cues do not certify the causal account. |
| Which events connect? | *Then* locates lighting after connection; a power-restoration explanation is plausible. | Temporal order does not by itself prove that connecting the cable caused the lighting. |
| How does the larger exchange develop? | The narrative establishes a situation; T1–T2 resolve reference; T3 challenges a possible inference from a lit display to a working printer. | The narrative never explicitly asserted that printing succeeds. Leo is responding to a possible implication, not refuting an explicit earlier sentence. |
| What does *that* pick up? | In T3 it can pick up the fact that the display lit up. | It need not denote the physical display; event/fact reference and object reference differ. |

Change one condition and the explanation changes. If Maya answers *The printer's status light*, the analyst should revise the referent record rather than preserve d automatically. If a successful printed page is then shown, the evidence about printing changes; the earlier light alone still did not establish it. These comparisons show what the representation explains without presenting its initial interpretation as inevitable.

## Discourse network

A second constructed passage shows why a referent chain, an event ordering and a discourse relation should remain distinguishable:

> Although the roads were icy, Anna sent the reports that Maya had prepared to Leo. He thanked her because he needed them.

On a reading where *he* denotes Leo, *her* Anna and *them* the reports:

```text
roads icy --concessive obstacle--> Anna sends reports
Maya prepares reports --earlier than--> Anna sends reports
Leo needs reports --reason offered for--> Leo thanks Anna

He -> Leo; her -> Anna (preferred here); them -> reports
```

The icy-road clause invokes an expectation that is defeated, not a logical contradiction. The past perfect locates preparation before the relevant sending situation. The need for reports supplies an offered explanation for thanking, without proving every unstated motive. The assignment of *her* to Anna is a preference in this context; Maya could be intended in another context. Even a plausible named antecedent is an interpretation to justify.

The arrows deliberately represent different kinds of connection and are labeled accordingly. For each one, identify the spans, direction and textual or contextual basis. This authored network is neither a full RST nor a full SDRT implementation, and its graph shape does not establish coherence independently of those explanations.

## Interfaces

Semantics contributes the propositions and situations being connected; Syntax contributes clause structure. Neither alone determines how a passage functions as discourse. The two interfaces below focus on contextual uptake and information organization, retaining local explanations in both connected Models.

### Interface with Pragmatics

An utterance interpretation constrains possible discourse updates, while acceptance, challenge and wider context determine what becomes shared. Represent the prior context, proposed contribution, candidate referents and background, and alternative next states. These are analytical fields, not a complete dialogue-state algorithm. The counterpart is explained in [Pragmatics](english-pragmatics-system.md#interface-with-discourse).

Suppose a speaker says *A courier left a parcel*. The response *It was damaged* can maintain reference to the parcel. *No courier came today* instead challenges the preceding claim. An assertion therefore proposes information without automatically establishing its truth or shared acceptance. A parcel can become an object of discussion even while the delivery claim is disputed.

This distinction also explains why conversational grounding is not agreement. A listener can identify the intended parcel and still reject the account of how it arrived. Record proposed reference, displayed understanding and acceptance of a claim separately when the exchange distinguishes them. Quotation, hypothetical discourse and misinformation require scope and commitment annotations; the simple update vocabulary here does not resolve every case.

The reference and conversation sources support selected introductory distinctions. The combined context-update representation is authored synthesis, not a newly verified formal Pragmatics–Discourse theory. Vary the next response to see which part of the proposed update survives; keep alternatives when the available wording does not settle uptake.

### Interface with Information Structure

A stated discourse context constrains topic and focus without making grammatical Subject, Topic and Focus interchangeable. The counterpart is explained in [Information Structure](english-information-structure-system.md#interface-with-discourse).

| Endpoint | Schematic fields |
|---|---|
| discourse context | accessible_referents, prior_utterances, candidate_questions |
| focus domain | question_under_discussion, focus_span, background |

The mapping uses `kps:constrains`: the context narrows possible analyses without mechanically determining one. A **question under discussion** is the issue being addressed. A **focus domain** supplies relevant alternatives relative to that issue; its **background** is what the comparison holds constant. **Topic** concerns what the discourse is about. Field names describe an analytical record, not measured values or a complete formal theory.

For *Who repaired the printer?*, *Nina repaired the printer* can focus *Nina*, contrasting possible repairers. For *What did Nina repair?*, it can focus *the printer*, contrasting objects. For *What did Nina do?*, the larger phrase *repaired the printer* can be focused. The printer may already be given in the discourse and still be the focused answer to a question contrasting objects.

The same sentence therefore permits different focus spans as the issue changes. An implicit question must be stated as an analyst's assumption; it is not an observed conversational context. Without audio, these written contrasts do not establish a particular accent or intonation. This remains a QUD-compatible working bridge: the underlying Roberts contribution in the Information Structure Model is abstract-only, and the new Discourse sources do not independently validate its detailed focus mapping.

## Evidence and limits

The [Jurafsky and Martin record](../references/jurafsky-martin-2026-discourse.md) documents selected passages on reference, information status and conversation. The [Mann and Taboada record](../references/mann-taboada-undated-rst-introduction.md) documents the RST introduction and selected relation definitions, including span organization and nuclearity. The eight-area organization, records, comparisons and examples are authored synthesis, not copied source analyses.

This Model remains **provisional and independently unreviewed**. It supplies an introductory explanation, not a universal discourse taxonomy or complete implementation of RST, SDRT, dynamic semantics or conversation analysis. Full segmentation standards, competing accessibility accounts, long texts and genre conventions, conversation timing and richer repair organization remain gaps. No natural conversation, corpus annotation, recording, learner result or processing measurement is supplied.

A useful analysis identifies both spans of a relation, its direction, the proposed referents and the evidence that favors them. Compare at least one plausible alternative when ambiguity matters. *Maya arrived. The alarm sounded* does not entail that her arrival caused the alarm. Preserve missing context instead of treating a fluent story or a well-formed diagram as evidence.

## Related knowledge

- [Discourse referent](../concepts/discourse-referent.md), [anaphora and accessibility](../concepts/anaphora-and-accessibility.md), and [givenness and bridging](../concepts/givenness-and-bridging.md) define reference distinctions.
- [Cohesion and coherence](../concepts/cohesion-and-coherence.md), [discourse relation](../concepts/discourse-relation.md), [temporal causal and evidential relations](../concepts/temporal-causal-and-evidential-relations.md), and [contrast and concession](../concepts/contrast-and-concession.md) deepen the relation vocabulary.
- [Trace discourse interpretation](../methods/trace-discourse-interpretation.md) provides a procedure for recording and comparing analyses.
