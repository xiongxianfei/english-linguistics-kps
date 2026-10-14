---
id: "english:practice:edit-english-and-learn"
type: "practice"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
perspectives: ["syntax", "semantics", "pragmatics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:skillsmith-editor-skill", "english:reference:walter-2016-modal-verbs-basics", "english:reference:british-council-undated-grammar-reference", "english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:ambiguity-and-vagueness", "english:concept:modality", "english:concept:speech-act"]
uses_models: ["english:model:english-syntax-system"]
stage_titles: ["Stage1 Establish the communication target", "Stage2 Diagnose the concrete difficulty", "Stage3 Make the smallest justified revision", "Stage4 Check fidelity and explain the pattern"]
practice_format: "staged-inline-stageN-v1"
stage_order: "recommended; unresolved meaning returns to clarification before revision"
---

# Edit English and learn from revisions

## Key takeaway
Improve a piece of English for its intended reader, preserve what its author means, and explain the useful linguistic reason behind each substantive change.

## Summary
This written-English Practice connects a communication target to diagnosis, a minimal revision and a transferable explanation. Three constructed cases distinguish a grammatical correction, unresolved structural ambiguity and an optional register change. Retaining the original is a valid result. Selected sources support the local linguistic explanations; the workflow is an authored synthesis, with no recorded learner outcomes.

## Target and boundaries

Use this Practice when you want a clearer piece of writing and an understanding of why a revision helps. Bring the original text, the intended message and whatever audience, genre, variety and tone requirements are known. You need no linguistic terminology in advance: the distinctions needed for these cases are explained inline.

The worked cases target ordinary standard written English. They are invented teaching examples, not quotations from a learner or evidence of recurring errors. A requested variety or deliberate conversational voice can change an editing decision. Translation and speech performance require additional work beyond this Practice; spelling or a transcript cannot establish a person's pronunciation or intonation.

The [Skillsmith editor reference](../references/skillsmith-editor-skill.md) records the workflow's starting point. The executable skill owns assistant triggers, language defaults and output formatting. This Practice explains decisions that a human reader can make without running that skill; it does not turn those software preferences into linguistic rules.

## Stage map

The stages give a recommended order, not compulsory prerequisites for every sentence. An understood communication target and sufficiently resolved meaning are prerequisites for a final revision; return to earlier stages when either changes.

- [Stage1 Establish the communication target](#stage1-establish-the-communication-target)
- [Stage2 Diagnose the concrete difficulty](#stage2-diagnose-the-concrete-difficulty)
- [Stage3 Make the smallest justified revision](#stage3-make-the-smallest-justified-revision)
- [Stage4 Check fidelity and explain the pattern](#stage4-check-fidelity-and-explain-the-pattern)

## Stage1 Establish the communication target

1. Separate the editing instruction from the text to be edited.
2. Write down what the reader should understand or do, who the reader is, and the requested degree of formality or directness.
3. Preserve names, quantities, technical terms, negation, time references and uncertainty.

These details constrain a revision: a polished promise is a poor substitute for an author's uncertain forecast.

For example, the target in Case A is a tentative project update, not a delivery guarantee. In Case C it is a colleague's request for a report, with an explicitly requested softer tone. If the writer only asks for proofreading, do not silently impose that tone change.

When context would change the message, ask a narrow question and keep the alternatives visible. If context would only affect a minor stylistic preference, leave the original or label the proposed alternative. Continue once the communication target is clear enough for the particular decision; do not require a questionnaire for every sentence.

## Stage2 Diagnose the concrete difficulty

Identify the exact span and the relationship that makes it difficult. Use the following distinctions to choose the next action.

| Finding | Meaning here | Action |
|---|---|---|
| Grammatical mismatch | A form conflicts with the construction in the stated target variety | Correct the form while preserving the intended message; Case A |
| Unresolved meaning | More than one materially different reading fits the available text | Ask for clarification or offer explicitly conditional alternatives; Case B |
| Optional register adjustment | The original is grammatical, but another form may better serve the requested social setting or tone | Explain the trade-off and let the author retain the original; Case C |
| No substantive difficulty | The original already fits the target | Keep it; do not manufacture a correction or a learning claim |

Register means language choices associated with a situation, audience and purpose. A grammatical sentence can still be unsuitable for a particular situation; an unfamiliar or informal expression is not thereby ungrammatical. Several issues can coexist, so diagnose each proposed change rather than assigning one label to the entire text.

Select only the relevant linguistic perspective. Syntax helps explain how words combine; semantics helps compare interpretations; pragmatics connects a form to its use in context. Other tasks may require morphology, vocabulary, discourse connections or information structure. These cases do not require ten separate analyses. If you cannot state the mechanism behind a proposed correction, inspect a suitable source or leave the judgment explicitly unresolved.

## Stage3 Make the smallest justified revision

Explain the mechanism before deciding what to replace. Change only what addresses the identified difficulty. A short edit can still alter meaning, so word count alone does not establish fidelity. The following cases model the decision, including its limits.

### Case A Correct a verb form without strengthening a claim

**Context:** A team member is proofreading a project update. Delivery tomorrow is possible, not confirmed.

**Original:** “We may delivers the update tomorrow.”

**Analysis:** In this construction, the central modal auxiliary *may* selects the plain, or base, form of the following verb. That form is *deliver*; *delivers* carries an inflectional ending. The dependency on *may* determines the choice, not simply the subject *we*. The same selection holds in *She may deliver*. Here, *may* expresses possibility.

**Revision:** “We may deliver the update tomorrow.”

**Explanation:** Syntax explains the selected verb form; semantics explains why *may* must be retained. A useful note is: “After *may*, use the base verb: *may deliver*, not *may delivers*. Keep *may* when the event is only possible.” Replacing it with *will* would strengthen this particular update beyond the supplied intention.

**Limits:** This is a scoped standard-English construction, not a rule that every verb after every modal-like expression lacks *to*. For example, *ought to* has a different pattern. The same word *may* can concern permission elsewhere; the context here establishes possibility. If the original were already “We may deliver the update tomorrow,” proofreading would require no change.

Support: [Walter on modal forms](../references/walter-2016-modal-verbs-basics.md#inspected-contribution) and [British Council on possibility](../references/british-council-undated-grammar-reference.md#possibility). The [auxiliary selection](../models/english-syntax-system.md#auxiliary-selection) generalizes the local form relationship; [modality](../concepts/modality.md) distinguishes contextual readings.

### Case B Clarify attachment before choosing a meaning

**Context:** An author is describing a sighting. No surrounding sentence tells us who had the equipment.

**Original:** “I saw the manager with binoculars.”

**Analysis:** The prepositional phrase *with binoculars* can modify the seeing event, naming the instrument used, or the noun phrase *the manager*, describing that person. These are different structural attachments and different readings; the sentence is not simply grammatically wrong.

**Revision:** Ask: “Were you using binoculars, or did the manager have them?” Pending an answer, retain the original and flag the unresolved reading. Offer these conditional candidates:

- If the observer used them: “Using binoculars, I saw the manager.”
- If the manager had them: “I saw the manager who had binoculars.”

**Explanation:** Syntax supplies the alternative attachments; semantics supplies their different interpretations. The transferable lesson is to make the intended connection explicit when a modifier supports competing readings. A more fluent sentence is not a justified edit if it silently chooses the wrong event or participant.

**Limits:** Surrounding context may already settle the reading; deliberate ambiguity may be appropriate. The second candidate specifies possession and should be checked with the author if a more precise relation matters. Neither candidate is the final answer until the intended reading is known. Written punctuation alone does not guarantee disambiguation.

Support: [Anderson on structural ambiguity](../references/anderson-2018-essentials-of-linguistics.md#editing-ambiguity-passage). This is a constructed application of the attachment distinction, not the source's sentence. [Ambiguity and vagueness](../concepts/ambiguity-and-vagueness.md) distinguishes multiple readings from borderline categories and missing contextual values.

### Case C Offer a register choice without inventing an error

**Context:** A writer wants a less direct request to a colleague. The report is still needed today.

**Original:** “Send me the report today.”

**Analysis:** The original is a grammatical imperative, a clause form commonly used to direct action. In this setting, an interrogative beginning *Could you* can function as a request rather than merely asking about ability. A speech act is the communicative action performed through an utterance; it need not match the sentence form one-to-one.

**Revision, optional:** “Could you send me the report today?”

**Explanation:** The requested action, recipient and timing remain. The interpersonal presentation changes to serve the requested softer tone. A useful note is: “The original is grammatical. *Could you …?* offers an indirect request form for this context; use it when that degree of directness suits your relationship and purpose.” This is a pragmatics choice, not a compulsory grammar correction.

**Limits:** The form does not guarantee politeness, compliance or a particular emotional response. Relationships, genre and local conventions matter. Direct wording may fit a task instruction or an urgent exchange. If proofreading is the only target and directness is intentional, retain the original. Do not replace *today* with *when convenient*: that changes the timing requirement.

Support: [British Council on requests](../references/british-council-undated-grammar-reference.md#requests). The particular colleague scenario and recommendation are authored applications. [Speech act](../concepts/speech-act.md) explains why interrogative form and request function can coexist.

## Stage4 Check fidelity and explain the pattern

1. Read the original and candidate against the target from Stage1. Compare who does what, to whom, when, under what conditions, with what certainty and what requested tone.
2. Reject an edit that adds an unsupported fact or commitment. Return to clarification if choosing between interpretations would decide the author's meaning for them.
3. Deliver the justified revision, conditional alternatives or unchanged original, with the explanation described below.

For these cases, a usable result preserves *may* in A, leaves B pending until the author resolves the attachment, and labels C as optional while preserving *today*. A result that merely sounds smoother fails if it loses one of those distinctions.

Deliver the usable text first, then a short explanation of the important choice when learning notes are wanted. Anchor the note to the actual original and revision, name the mechanism in plain language, and state when it applies. Explain only as many patterns as the text and learning target justify; do not infer a native language, proficiency level or repeated habit from one example. If nothing needs changing, say so without inventing a lesson. Respect a request for text without notes.

If the learner asks for an exercise, use one related example and discuss their actual reasoning. Keep personal samples and results outside this public repository unless appropriate publication permission exists. An explanation supplied by an editor is not evidence that the learner can use the pattern independently.

## Current practice summary

**Actual task:** No learner application recorded. The three cases above are constructed authoring examples.

**What worked:** No observed learning or communication outcome established.

**Unresolved:** Independent linguistic review, use with authentic texts, contextual judgments and transfer to new writing remain pending.

**Next check:** With a willing learner, use one real editing decision and record whether they can explain the choice and its limits on a different example; do not treat a corrected sentence alone as demonstrated learning.

## Evidence status

**Provisional.** Selected source passages support modal forms, possibility, request constructions and structural ambiguity. Their Reference records identify the inspected extent. The workflow, editing recommendations and cases are an AI-assisted authored synthesis; they are not a validated teaching intervention, a corpus study or independent expert approval. Broader linked Concepts and Models retain their own support limits.
