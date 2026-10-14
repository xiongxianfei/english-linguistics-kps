---
id: "english:model:english-information-structure-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["information-structure"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:roberts-2012-information-structure"]
uses_concepts: ["english:concept:focus-topic-and-qud", "english:concept:givenness-and-bridging", "english:concept:common-ground", "english:concept:discourse-referent", "english:concept:prosody", "english:concept:stress"]
uses_models: ["english:model:english-discourse-system", "english:model:english-prosody-system", "english:model:english-syntax-system"]
system_domain: "information-structure"
---

# English information structure system

## Key takeaway
Information structure distinguishes topic, focus, givenness and the question under discussion rather than equating them with grammatical positions or accented words.

## Summary
This Model explains how an utterance organizes information relative to a discourse. It defines topic, focus, background, givenness and the question under discussion, then compares different contexts for the same sentence. It includes the prosodic connection without asserting that capitalization or an accent uniquely determines a focus domain. Interfaces with Discourse and Prosody explain why context, focus spans and accented words must be recorded separately. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Interfaces](#interfaces)
  - [Interface with Discourse](#interface-with-discourse)
  - [Interface with Prosody](#interface-with-prosody)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

## Purpose
For an utterance in context, identify what issue is being addressed, which alternatives are relevant and what information is treated as accessible. Keep that analysis separate from grammatical function and actual acoustic observation.

## Representation

| Dimension | Working interpretation | Not equivalent to |
|---|---|---|
| Topic | What the relevant discourse stretch is about | Every grammatical Subject |
| Question under discussion | The issue the participants are addressing | Necessarily a question spoken aloud |
| Focus | The expression or domain related to relevant alternatives | Every new word or only the loudest word |
| Background | Material held constant in the focus comparison | Everything previously mentioned |
| Givenness | Accessibility or prior activation under a chosen account | Lack of focus |

These labels characterize an expression in a use, not permanent properties stored on the word. Different frameworks formalize focus and givenness differently.

## Essential distinctions
A **question under discussion**, or QUD, supplies an issue against which an answer can be evaluated. A **focus domain** can be a word, phrase or larger constituent. Relevant alternatives might differ in a participant, an action or a whole proposition. **Contrast** can select among previously mentioned alternatives; focused material therefore need not be new.

A grammatical Subject is a syntactic function. Topic is a discourse-related interpretation. They may align, but an answer focused on the Subject does not thereby establish that the Subject is the Topic. Likewise, the background of a focus analysis is not a complete presupposition theory.

Information packaging can use word order, clefts, passive constructions and prosodic prominence. The same propositional core can be packaged differently, but alternative constructions may carry additional presuppositions or restrictions; they are not automatically interchangeable paraphrases.

## Worked analysis
Hold the wording *Maya repaired the printer* constant.

| Contextual question | Working focus domain | Background for this comparison | Possible accented word |
|---|---|---|---|
| Who repaired the printer? | Maya | __ repaired the printer | MAYA |
| What did Maya repair? | the printer | Maya repaired __ | PRINTER |
| What did Maya do? | repaired the printer | Maya __ | PRINTER |

The last two cases show why a prominent *printer* need not uniquely identify the focus domain. In the third context, the action phrase is the answer even if one word carries the strongest accent. Capitalization here is a schematic prominence cue, not an observed pitch contour.

If Maya and Nina have both already been mentioned, *MAYA repaired it, not Nina* can still focus Maya contrastively. Prior mention alone cannot decide that something is background. A topic assignment requires the wider discourse rather than a universal Subject-equals-Topic rule.

## Interfaces
**Discourse Information Structure:** accessible referents and the current issue constrain plausible topic/focus analyses. **Information Structure Prosody:** focus and prominence interact under language- and context-specific constraints; the mapping can be underdetermined. **Syntax Prosody:** available structures and phrase boundaries interact with realization. **Pragmatics** concerns relevance and conversational commitments, which are not encoded by word order alone.

### Interface with Discourse

A stated discourse context constrains an information-structure analysis without making grammatical Subject, Topic and Focus interchangeable.

State the assumed discourse context and question before assigning a focus span or Topic. The counterpart is explained in [Discourse](english-discourse-system.md#interface-with-information-structure).

#### Interface with Discourse representation

| Endpoint | Schematic fields |
|---|---|
| discourse context | accessible_referents, prior_utterances, candidate_questions |
| focus domain | question_under_discussion, focus_span, background |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Discourse essential terms

A **discourse context** records what has been said, which referents are accessible and what issue is being addressed. A **focus domain** is the word or larger expression that supplies relevant alternatives relative to that issue. Its **background** is what the comparison holds constant. Topic concerns what the discourse is about; none of these labels is simply another name for grammatical Subject. A question under discussion can be implicit, but an analyst must state the assumed question rather than invent an observed conversational context.

#### Interface with Discourse worked interpretation

For *Who repaired the printer?*, the answer *Nina repaired the printer* can focus *Nina*, contrasting her with other possible repairers. For *What did Nina repair?*, the same answer can focus *the printer*, contrasting it with other possible objects. For *What did Nina do?*, the focus can be the larger phrase *repaired the printer*. These constructed pairs show that the sentence string does not by itself fix one focus span or Topic. Without a stated context, preserve alternative analyses rather than selecting one as fact.

#### Interface with Discourse assumptions and limits

This is a QUD-compatible working bridge, not a consensus theory of discourse. Context may be insufficient to identify one topic or focus; alternative analyses must remain explicit.

#### Interface with Discourse evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Discourse evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

### Interface with Prosody

Focus domains constrain possible prosodic realizations without being identical to the most strongly accented word.

Distinguish the span in focus from the word or syllable carrying a possible accent. The counterpart is explained in [Prosody](english-prosody-system.md#interface-with-information-structure).

#### Interface with Prosody representation

| QUD | Focus domain | Background | Possible strongest word |
|---|---|---|---|
| Who repaired the printer? | Nina | __ repaired the printer | NINA |
| What did Nina repair? | the printer | Nina repaired __ | PRINTER |
| What did Nina do? | repaired the printer | Nina __ | PRINTER |

#### Interface with Prosody worked interpretation

NP focus and VP focus can share a prominent PRINTER. A broader conversation about the printer does not make Nina Topic merely because she is Subject or focused. The acoustic realization of prominence may involve pitch movement, duration and intensity.

#### Interface with Prosody assumptions and limits

The table is a constructed working illustration, not an audio measurement or a complete focus-projection grammar. Roberts' abstract supports a connection between QUD and prosodic focus; detailed derivations require full-text and competing-source review.

#### Interface with Prosody evaluation and counterevidence

Compare explicit question-answer contexts while holding the sentence string stable. Record focus span, accented word and lexically stressed syllable separately. Do not assign a unique focus domain from capitalization alone.

#### Interface with Prosody evidence status

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this section. Inspect the linked record's access extent and nonclaims.

- [Information Structure: Towards an integrated formal theory of pragmatics. Semantics and Pragmatics 5, article 6.](../references/roberts-2012-information-structure.md#abstract) — support is limited to the named section in that record.

## Evaluation and counterevidence
Keep sentence, QUD, focus span, accented syllable/word and proposed Topic in separate fields. Compare question-answer pairs while holding wording stable. Test whether changing the context changes the analysis without changing the grammatical Subject. Do not assign a unique focus domain from a transcript without contextual evidence.

## Assumptions and limits
The QUD-based perspective is a working framework, not a universal consensus. Detailed focus projection, contrastive topics, givenness accounts and language-variety differences remain further work. The table is constructed and does not report recording or listener judgments.

## Evidence status
**Provisional; independent review pending.** The [Roberts Reference](../references/roberts-2012-information-structure.md) records the journal abstract's proposal connecting QUDs, discourse relevance and prosodic focus. It does not verify this table's detailed projection conditions. Those remain explicitly authored working analyses.

## Related knowledge
[Focus topic and QUD](../concepts/focus-topic-and-qud.md), [givenness and bridging](../concepts/givenness-and-bridging.md) and [common ground](../concepts/common-ground.md) provide focused explanations. [Information Structure Prosody interface](#interface-with-prosody) and [an accented word need not exhaust the focus domain](../principles/accent-does-not-exhaust-focus.md) develop the key contrast.
