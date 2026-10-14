---
id: "english:model:english-information-structure-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["information-structure"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:roberts-2012-information-structure", "english:reference:krifka-2008-information-structure"]
uses_concepts: ["english:concept:focus-topic-and-qud", "english:concept:givenness-and-bridging", "english:concept:common-ground", "english:concept:discourse-referent", "english:concept:prosody", "english:concept:stress"]
uses_models: ["english:model:english-discourse-system", "english:model:english-prosody-system", "english:model:english-syntax-system", "english:model:english-semantics-system"]
system_domain: "information-structure"
---

# English information structure system

Information Structure explains how an utterance fits what participants are discussing. The same sentence can answer different questions, contrast different alternatives, or present a familiar referent in a newly relevant role. To analyze that organization, keep topic, focus, givenness, grammatical function and spoken prominence distinct.

This Model develops seven connected areas. The reader should be able to explain why changing a question changes an answer's focus, why old information can be focused, and why neither word order nor a prominent word determines the entire analysis. The account is an introductory synthesis using an alternatives-based perspective and a questions-under-discussion perspective; it is not a claim that all theories use identical terms. Examples are constructed, and no recording or learner response is supplied.

## Contents

- [Topic and comment](#topic-and-comment)
- [Focus and background](#focus-and-background)
- [Questions under discussion](#questions-under-discussion)
- [Givenness and accessibility](#givenness-and-accessibility)
- [Contrast and alternatives](#contrast-and-alternatives)
- [Information packaging](#information-packaging)
- [Focus and prosodic realization](#focus-and-prosodic-realization)
- [Worked analysis](#worked-analysis)
- [Interfaces](#interfaces)
  - [Interface with Discourse](#interface-with-discourse)
  - [Interface with Prosody](#interface-with-prosody)
  - [Interface with Syntax](#interface-with-syntax)
  - [Interface with Semantics](#interface-with-semantics)
- [Evidence and limits](#evidence-and-limits)

## Topic and comment

A **topic** is what a relevant utterance or discourse stretch is about. A **comment** is what is said about that topic. A topic expression is a piece of language; its referent is the person, object or situation being discussed. Keep the two apart when representing an analysis.

In *As for the printer, Maya repaired it yesterday*, *the printer* explicitly identifies an aboutness topic. *Maya* is the grammatical Subject of the following clause, while *it* refers back to the printer. This is why Subject and Topic cannot be treated as interchangeable labels. In a different context, *Maya repaired the printer* could contribute information about Maya.

Topic–comment organization also differs from focus–background organization. Suppose the printer is already the topic and someone asks *When did Maya repair it?* In *Maya repaired it YESTERDAY*, the comment concerns the repair, while the time expression supplies the focused alternative. The entire comment need not be the focus.

A topic can be introduced rather than previously mentioned: *A colleague of mine has bought a printer* can establish the colleague as the person the speaker will discuss. Conversely, *What happened? — A printer caught fire* can present a whole situation without requiring a separately expressed aboutness topic. The scope of a topic assignment therefore matters: distinguish an utterance topic from the broader subject of a conversation, and leave an assignment unresolved when context is insufficient.

[Krifka's selected topic discussion](../references/krifka-2008-information-structure.md#topics-and-contrast) motivates these distinctions. Its account of aboutness is a theoretical proposal, not direct evidence that human memory consists of topic-indexed files.

## Focus and background

In the working account, **focus** identifies an expression or domain whose alternatives matter to the interpretation. **Background** describes what is held constant in a particular comparison. These are properties of an expression in use, not permanent attributes of a word.

For *Who repaired the printer? — MAYA repaired the printer*, possible answers differ in the repairer:

```text
Maya repaired the printer.
Nina repaired the printer.
Leo repaired the printer.
```

The focus domain is *Maya*; the working background is `__ repaired the printer`. If the question instead asks *What did Maya repair?*, possible answers differ in the object and the background becomes `Maya repaired __`. A **narrow focus** may cover one constituent; a **broad focus** may cover a larger phrase or the whole clause. The size is established by the intended alternatives, not by counting capitalized words.

Calling focus “new information” loses an important distinction. If Maya and Nina were both just mentioned, *MAYA repaired it, not Nina* can focus an already familiar name. Nor does focus mean “the most important word”: importance does not specify which alternatives are being compared.

The blank-slot notation is a local explanatory device. It does not adopt a complete structured-meaning formalism or imply that the background is an independently established presupposition in every construction. [Krifka's selected focus passages](../references/krifka-2008-information-structure.md#focus-and-questions) distinguish alternative-based interpretation from several competing definitions and representations.

## Questions under discussion

A **question under discussion**, or QUD, is the issue a contribution addresses. It may be spoken explicitly or inferred from the exchange. It helps explain why a true sentence can nevertheless be an unsuitable answer to a particular question.

| Issue | Relevant answer variation | Candidate focus in the same sentence |
|---|---|---|
| Who repaired the printer? | Different repairers | *Maya* |
| What did Maya repair? | Different objects | *the printer* |
| What did Maya do? | Different activities | *repaired the printer* |
| What happened? | Different situations | Potentially the whole clause |

A question is not identical to its answer or to the grammatical wh-word. For *Who repaired the printer?*, the answer's focus is the repairer expression, not an absent *who*. A yes/no question raises alternatives about whether a proposition holds; it does not necessarily ask the listener to replace a noun.

Questions can form a local strategy. *Who repaired which machine?* can be addressed through *What did Maya repair?* and *What did Nina repair?* An answer to one subquestion need not settle the whole issue. This is useful for interpreting contrastive topics below, without imposing a fixed question tree on every conversation.

An implicit QUD is an analytical hypothesis. For *Maya repaired the printer*, the wording alone does not tell us which row applies. State the assumed issue and compare alternatives. Roberts's [abstract](../references/roberts-2012-information-structure.md#abstract) motivates a QUD-based account; the newly inspected Krifka passages discuss question–answer congruence and implicit questions. Neither establishes that one contextual interpretation is uniquely recoverable here.

## Givenness and accessibility

**Givenness** concerns what is already available under the adopted account of context. **Accessibility** concerns how readily a referent or interpretation can be picked up in the relevant discourse environment. Prior mention, shared familiarity, inferability and current salience should not be collapsed into one old/new flag.

In *A printer arrived. The display was cracked*, the display has not been mentioned, but a printer can make a related display inferable. This **bridging** relation is not identity: display and printer are different referents, and the association remains defeasible. In *Maya and Nina arrived. MAYA repaired the printer*, both names are discourse old while one can still be focused. Shared background knowledge also need not have been mentioned in the immediately preceding sentence.

These distinctions affect expression choice. A pronoun often draws on an accessible referent; an explicit noun phrase may clarify an ambiguous one. Givenness can favor reduced prominence, but it does not prohibit accent: *I meant HIM, not her* can contrast accessible referents. Reduced prominence also does not imply that a referent has disappeared from the meaning.

Krifka's selected givenness discussion supports separating focus from givenness and considering their interaction. The local [Discourse account](english-discourse-system.md#givenness-and-bridging) supplies reference tracking and bridging explanations. No single hierarchy of accessibility or automatic rule for pronouns, articles and accent is adopted here.

## Contrast and alternatives

An answer can select an alternative without explicitly correcting anyone. **Corrective focus** instead opposes an earlier proposed alternative: *Nina repaired it* followed by *MAYA repaired it, not Nina*. Both uses involve alternatives, but the corrective context makes the rejected candidate explicit.

A **contrastive topic** can organize a broader issue into partial answers. Under *Who repaired which machine?*, consider *As for MAYA, she repaired the PRINTER; as for NINA, she repaired the SCANNER*. Maya and Nina organize the answer by person, while printer and scanner answer the corresponding subquestions. Topic and focus can therefore interact within one contribution. Capitalization marks intended contrast in this constructed example; it does not document a particular rising contour.

Alternatives can also affect semantic interpretation. Compare two intended readings of *Maya only lent Leo the printer*:

| Intended focus | Relevant alternatives | Bounded interpretation |
|---|---|---|
| *the printer* | Other relevant items she might lend Leo | She lent Leo the printer and no other relevant item |
| *Leo* | Other relevant people she might lend the printer to | She lent Leo the printer and no other relevant person |

Under the first reading, lending a scanner to Leo would violate the exclusion. Under the second, lending the same printer to Nina would violate it. Each reading leaves other matters open: excluding other items lent to Leo does not by itself exclude lending the printer to Nina. This simplified comparison holds the domain and intended reading fixed. It does not settle the presuppositional status of the positive contribution of *only*, every possible association, or how listeners resolve the sentence without context.

The semantic contribution of *only* and the focus alternatives must be represented together. Scope, focus and accent are distinct; moving an accent does not automatically license every imaginable scope. [Krifka's selected semantic-focus discussion](../references/krifka-2008-information-structure.md#focus-and-questions) supplies this connection; the Semantics interface explains it from the other side.

## Information packaging

English can organize a contribution through prosody, expression choice and syntactic construction. **Information packaging** concerns how those resources fit the discourse. It does not imply that every alternative construction has exactly the same meaning or appropriateness.

| Constructed form | Possible contribution | Boundary |
|---|---|---|
| *Maya repaired the printer* | A clause compatible with different focus domains | Context is still needed |
| *The printer was repaired by Maya* | Makes the printer Subject and can support continuity about it | Passive Subject is not automatically Topic |
| *As for the printer, Maya repaired it* | Explicitly introduces an aboutness topic | It is not simply an ordinary Object moved with no other change |
| *It was Maya who repaired the printer* | A cleft can highlight identification of the repairer | Cleft background and possible exhaustive interpretation need separate analysis |

A **cleft** divides the contribution into an identifying portion and another clause. Its ordinary use can treat the repair event as background while identifying Maya. That does not make clefts universally interchangeable with an accented simple clause. The construction, context and interpretation all require attention.

The [Syntax interface](#interface-with-syntax) distinguishes grammatical changes from discourse effects. The construction examples are authored comparisons; Krifka discusses packaging and notes that cleft focus can differ interpretively from in-situ focus. A full grammar of clefts, topicalization, passive choice and information ordering remains outside this introductory account.

## Focus and prosodic realization

A focus span need not be identical to the word carrying a pitch accent, an intonational event associated with a prominent syllable. Compare *What did Maya repair?* with *What did Maya do?* A response with main prominence on *printer* can support either NP focus (*the printer*) or VP focus (*repaired the printer*). **Focus projection** names the issue of how a local accent can support a broader focus interpretation under an adopted account.

Givenness can affect where prominence falls within a larger domain. Suppose the printer has already been discussed and the question is *What did Maya do with it?* The answer *She REPAIRED the printer* can contrast repairing with replacing or discarding it while the object remains familiar. This is a possible contextual pattern, not an exceptionless instruction that given objects must be deaccented.

Keep four records separate: the QUD, the intended focus span, a proposed accented syllable, and any observed signal. Lexical stress within *printer*, conventionally /ˈprɪntər/ here, is another level. Neither the spelling nor capitalization supplies a measured pitch track. Krifka's section 4.3 discusses givenness and accent placement; detailed focus projection and variety-specific realization require broader evidence. The [Prosody interface](#interface-with-prosody) preserves this distinction locally in both Models.

## Worked analysis

The constructed exchange is:

> Leo: Maya and Nina both checked the machines. Who repaired which one?
>
> Maya: As for Nina, she repaired the scanner. I repaired the printer.
>
> Leo: So Nina repaired the printer?
>
> Maya: No, I repaired the printer.

Initially Maya, Nina and the machines are established as referents. The question organizes the missing information by repairer and machine. The first answer divides that issue into partial answers: Nina/scanner and Maya/printer. A plausible information-structure analysis treats the people as contrastive topics in this context, with machine alternatives supplying the corresponding answers. This does not establish observed accents.

Leo's follow-up introduces an incorrect pairing relative to the preceding answer. Maya's final *I* can carry corrective focus against Nina even though Maya is already familiar. If the wider conversation is about the printer, the repairer expression can be focused without becoming the conversation's aboutness topic. The grammatical Subject remains *I* in that clause regardless of whether it is being contrasted.

Now change the follow-up to *So you replaced the printer?* The same reply, *I repaired the printer*, can instead focus the action *repaired*. The people and object stay familiar, while the relevant alternatives change. Finally compare *What happened next?*: a broader event description may become relevant. The proposed analysis must change with the issue rather than permanently tagging words as topic or focus.

The earlier three-way comparison with *Maya repaired the printer* and the corresponding *Nina repaired the printer* examples below make the same point with a fixed sentence. These are explanatory contrasts, not a completed learning activity or a record of participants' actual intentions.

## Interfaces

The same contribution has discourse history, grammatical structure, compositional meaning and possible spoken realization. The interfaces connect those descriptions without imposing a processing sequence.

### Interface with Discourse

Discourse records prior contributions, accessible referents and candidate issues. Information Structure relates that context to topic, focus and background. Represent the correspondence as `discourse context {accessible_referents, prior_utterances, candidate_questions}` constraining `focus domain {question_under_discussion, focus_span, background}`. The relation uses `kps:constrains`; these are analytical fields, not an algorithm or measured mental state. The counterpart is explained in [Discourse](english-discourse-system.md#interface-with-information-structure).

For *Who repaired the printer?*, *Nina repaired the printer* can focus Nina; for *What did Nina repair?*, it can focus the printer; for *What did Nina do?*, it can focus the larger VP. A prior mention does not by itself choose between those analyses. Track both the history and the current issue, and preserve alternatives if either is missing. An assertion's uptake and truth are still Pragmatics and Discourse questions, not consequences of assigning focus.

### Interface with Prosody

Information Structure supplies a context-dependent focus domain; Prosody supplies possible accent and phrasing patterns. Neither uniquely determines the other. The counterpart is explained in [Prosody](english-prosody-system.md#interface-with-information-structure).

| QUD | Focus domain | Background | Possible strongest word |
|---|---|---|---|
| Who repaired the printer? | Nina | __ repaired the printer | NINA |
| What did Nina repair? | the printer | Nina repaired __ | PRINTER |
| What did Nina do? | repaired the printer | Nina __ | PRINTER |

The final two rows share a possible accented word but differ in focus span. Given material can also be accented contrastively. Test any realization claim against an identified recording and context; acoustic cues can disagree and automatic pitch tracking can be wrong. Krifka supplies selected support for focus/givenness interactions, while the Roberts contribution remains abstract-only. No detailed phonological derivation or observed realization is supplied here.

### Interface with Syntax

Syntax describes constituents and functions; Information Structure describes their role in a particular exchange. In *Maya repaired the printer*, Maya is Subject; in *The printer was repaired by Maya*, the printer is Subject while Maya is inside a by-PP. Under an intended repair-event reading, these forms can organize the same participants differently. Neither Subject assignment establishes Topic or Focus without context.

The explicit topic construction *As for the printer, Maya repaired it* makes the distinction particularly visible. Clefts add their own constructional and interpretive conditions, so they cannot be treated as moving emphasis with no grammatical consequences. Record construction, Subject/Object spans, context and proposed focus separately. The counterpart in [Syntax](english-syntax-system.md#interface-with-information-structure) provides the local grammatical explanation; the comparison is not a universal construction-selection algorithm.

### Interface with Semantics

Semantics provides ordinary interpretation and the contribution of focus-sensitive expressions; Information Structure supplies relevant alternatives. For *Maya only lent Leo the printer*, contrasting items and contrasting recipients give different exclusions, as explained above. The object-focused reading rules out relevant other items lent to Leo; the recipient-focused reading rules out relevant other people lent this printer. Neither implies the other's exclusion.

This is why packaging cannot always be assumed to leave truth conditions unchanged. Keep ordinary proposition, alternative set, operator scope and discourse context distinct. The counterpart in [Semantics](english-semantics-system.md#interface-with-information-structure) gives the same bounded interpretation. The comparison adopts selected Krifka distinctions without a complete semantics for *only*, *also* or *even*.

## Evidence and limits

[Krifka 2008](../references/krifka-2008-information-structure.md) supplies inspected passages on focus, questions, givenness, topics, contrast and packaging. [Roberts 2012](../references/roberts-2012-information-structure.md) remains abstract-only. These sources support the specified distinctions, not the correctness of every authored example or one universally accepted theory. New Model support does not silently upgrade evidence attached to separate Concepts or Principles.

The account remains **provisional and independently unreviewed**. Full formal focus projection, inventories of constructions, fine-grained accessibility, cross-variety realization and processing evidence remain gaps. No audio, corpus analysis, listener judgment or learner result is reported. A useful analysis states the question, focus alternatives, given referents and grammatical spans, then explains which observations would distinguish competing accounts.

[Focus topic and QUD](../concepts/focus-topic-and-qud.md), [givenness and bridging](../concepts/givenness-and-bridging.md), [common ground](../concepts/common-ground.md) and [an accented word need not exhaust the focus domain](../principles/accent-does-not-exhaust-focus.md) provide optional depth.
