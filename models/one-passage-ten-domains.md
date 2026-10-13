---
id: "english:model:one-passage-ten-domains"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["phonetics", "phonology", "morphology", "lexicon", "syntax", "semantics", "pragmatics", "discourse", "information-structure", "prosody"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:roberts-2012-information-structure"]
uses_models: ["english:model:english-system-architecture", "english:model:integrated-utterance-analysis"]
uses_methods: ["english:method:analyze-complete-utterance"]
---

# One passage across ten linguistic domains

## Key takeaway
The same utterance supports distinct linked analyses; a grammatical function, a semantic role, a focus and a phonetic realization are not interchangeable labels.

## Summary
This self-contained case analyzes *Those students repaired the printers. They tested them again.* Each domain contributes a different representation. The interpretation is constructed and revisable, and the sound tier is a prediction only because no recording is available. The ten rows are analytical perspectives, not ten temporal processing stages or a compulsory learning sequence.

## Purpose
Make the whole-system mechanism concrete: preserve one expression, describe each relevant level and connect the representations without silently importing unsupported assumptions.

## Representation

| Domain | Proposed representation of the example |
|---|---|
| Phonetics | Actual pronunciation and measurements are unknown; a broad form is not an observed token |
| Phonology | Ordinary regular plural in *students* ends /s/; plural in *printers* ordinarily ends /z/ in the declared General American convention |
| Morphology | STUDENT and PRINTER have plural forms; REPAIR and TEST appear in past forms |
| Lexicon | REPAIR and TEST are used with an affected object in these constructions |
| Syntax | *Those students* is the first Subject; *the printers* its Object; *they* and *them* occupy corresponding functions in the next clause |
| Semantics | Students are the repairing/testing participants; printers are the affected participants; events are located before the utterance in the intended reading |
| Pragmatics | *Those* requires a contextual identification; pronoun interpretation remains context-dependent |
| Discourse | The second sentence plausibly continues the same participants and describes a subsequent activity |
| Information structure | The focus depends on the issue being answered; a Subject is not automatically a Topic |
| Prosody | Prominence and phrasing can differ with the context; no unique contour follows from the written passage |

## Word forms and lexical structure
A lexeme is a vocabulary identity such as STUDENT; *students* is a grammatical word form. In *printers*, a working analysis distinguishes the derivational -er associated with PRINT from the plural exponent. A spelling-based split alone would not justify that derivation in an unrelated word.

For ordinary regular patterns, stem-final /t/ in *student* licenses plural /s/ here. In the package's rhotic convention, the final voiced rhotic realization in *printer* is compatible with plural /z/. The regular past of *test* has a syllabic ending, conventionally /ɪd/ in this package, with other weak-vowel realizations possible. These are morphological/phonological analyses, not measurements of speakers.

## Clause structure and semantic participants

```text
Clause 1
  Subject NP: Those students
  Predicate VP
    Verb: repaired
    Object NP: the printers
Clause 2
  Subject NP: They
  Predicate VP
    Verb: tested
    Object NP: them
    Modifier: again
```

The complete Object in the first clause is *the printers*. In the intended interpretation, the Subject participants are Agents and the printers are affected Themes or Patients under the chosen terminology. The passive *The printers were repaired by those students* changes grammatical functions without thereby turning the printers into repairing Agents. Role inventories differ; name the convention rather than treating a label as an observed property.

## Reference and discourse
*They* plausibly refers to the students and *them* to the printers. Those readings are not logically forced by the string; a wider context could make another plural group accessible. *Again* ordinarily introduces a repetition-related background in this use, but what repeated and its scope require interpretation.

Narrative order encourages a repair-then-test reading. Do not infer that repair caused testing, that all printers passed, or that the repairs were successful. Those are additional claims. A repair to a participant interpretation should propagate to the semantic and discourse analyses that depend on it.

## Information structure and prosody
With the question *Who repaired the printers?*, a possible answer focuses *those students*. With *What did those students repair?*, the focus can be *the printers*. With *What did those students do?*, the focus can include *repaired the printers*. The same prominent word *printers* could occur in the latter two contexts; that does not make the focus spans identical.

No context and no recording have been supplied. Therefore record the focus analyses as alternatives and the prosodic realizations as possibilities. Do not populate a narrow IPA transcription or an acoustic table merely to make all ten rows look equally complete.

## Evaluation and counterevidence
1. Identify each complete NP and its local grammatical function.
2. State the lexical sense and participant interpretation without equating Subject with Agent by definition.
3. Test another plausible pronoun context and note which interpretations change.
4. Compare two explicit questions and retain separate focus spans and accent predictions.
5. Mark the sound analysis as predicted until recordings are actually inspected.

A correct structural label on an incomplete span is still a faulty analysis. Missing evidence is a valid result, not an empty cell to invent.

## Assumptions and limits
The passage, questions and alternate passive are authored illustrations. The working syntax uses NP and descriptive clause functions. This case is not a parser benchmark, an acoustic experiment or a validated lesson. It does not exhaust negation, quantification, ellipsis, dialect variation or competing theoretical analyses.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) gives bounded background for inflection and function/role distinctions. The [Roberts Reference](../references/roberts-2012-information-structure.md) identifies the QUD framework's general proposal, not independent validation of this case.

## Related knowledge
[English system architecture](english-system-architecture.md) summarizes the ten perspectives. [Integrated utterance analysis](integrated-utterance-analysis.md) supplies a different, nested-clause case. [Analyze complete utterance](../methods/analyze-complete-utterance.md) gives an operational procedure; neither replaces the worked explanation above.
