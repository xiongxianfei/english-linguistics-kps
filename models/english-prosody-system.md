---
id: "english:model:english-prosody-system"
type: "model"
version: "0.2.3"
language: "KPS 9.x"
status: "draft"
domains: ["prosody"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:roberts-2012-information-structure", "english:reference:mit-2006-tobi-tutorial"]
uses_concepts: ["english:concept:stress", "english:concept:prosody", "english:concept:connected-speech", "english:concept:syllable-structure", "english:concept:phonotactics", "english:concept:constituency", "english:concept:relative-clause", "english:concept:phrase-and-clause", "english:concept:focus-topic-and-qud"]
uses_models: ["english:model:english-phonology-system", "english:model:english-syntax-system", "english:model:english-information-structure-system", "english:model:english-phonetics-system"]
system_domain: "prosody"
uses_methods: ["english:method:analyze-sound-realization"]
---

# English prosody system

## Key takeaway
Prosody organizes prominence, phrasing, timing and intonation across segments; no single pitch movement uniquely determines meaning.

## Summary
This Model relates syllables and lexical stress to utterance prominence, rhythm and phrase boundaries. Separate annotation layers show how an accented syllable, the span in focus and a phrase-ending pitch movement can differ. Constructed comparisons explain why a rise is not a universal question marker and why stress does not imply equal timing or maximum pitch. No acoustic trace or learner performance has been observed. Interfaces with Phonology, Syntax, Information Structure and Phonetics connect lexical stress, grouping, focus and physical cues. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Units and attributes at each level](#units-and-attributes-at-each-level)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Interfaces](#interfaces)
- [Interface with Phonology](#interface-with-phonology)
- [Interface with Phonetics](#interface-with-phonetics)
- [Interface with Syntax](#interface-with-syntax)
- [Interface with Information Structure](#interface-with-information-structure)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

## Purpose
Describe how an utterance groups and highlights material while keeping phonological organization, discourse interpretation and physical realization distinct.

## Representation

| Component | What it describes | Important boundary |
|---|---|---|
| Lexical stress | Relative organization of syllables within a lexical form | Not identical to the strongest word in a sentence |
| Phrasal prominence | Relative highlighting within an utterance | Can respond to focus, contrast and context |
| Pitch accent | A pitch event associated with a prominent position in an intonational analysis | Not every pitch fluctuation is an accent |
| Phrasing and boundaries | Grouping into prosodic units and edge-related patterns | A comma need not correspond to a pause |
| Acoustic realization | Pitch-related frequency, duration, intensity and other cues | A transcript is not a measurement |

These dimensions interact. A useful representation keeps the segment string, stress pattern, proposed accent/boundaries and context in separate annotation layers.

## Units and attributes at each level

A **syllable** groups segments around a nucleus, usually a vowel. A word can contain several syllables; an utterance groups words into prosodic phrases. These are different units, so each attribute needs an explicit location or span.

| Unit | Relevant attribute | Values or distinctions and their interpretation |
|---|---|---|
| Syllable within a word | Lexical stress | Primary, secondary where applicable, or unstressed; IPA ˈ and ˌ precede the relevant syllable |
| Syllable in an utterance | Pitch accent | A tonal event associated with prominence; a relatively high or low target can both mark an accent |
| Prosodic phrase | Grouping and boundary | Which words group together and where the group ends; boundary cues may include pitch movement and lengthening, without a required silent pause |
| Phrase ending | Intonational pattern | A fall, rise or more complex contour; its location and context matter for interpretation |
| Stretch of speech | Rhythm | Relative timing of prominent and less prominent material; compare durations instead of assuming equal intervals |
| Voiced interval or segment | Physical realization | Fundamental frequency in hertz, duration in milliseconds, and intensity under a stated measurement convention; these are observations only when measured |

An **intonational phrase** is a prosodic grouping with its own intonational organization. In the selected ToBI account, an accent belongs to a prominent syllable while phrase tones and boundary tones describe the ending. A high accent followed by a low ending and a low accent followed by a high ending are both possible. The final pitch therefore does not identify the location or height of an earlier accent. The [MIT tutorial record](../references/mit-2006-tobi-tutorial.md) locates the supporting descriptions; this Model uses plain-language annotations rather than attempting a full ToBI transcription.

## Essential distinctions
**Stress** concerns relative prominence in a structured pattern; it is not simply loudness. **Intonation** concerns pitch organization over an utterance or phrase. In an accent-and-boundary account, pitch events associated with prominent positions are distinguished from tonal events associated with phrase edges. The chosen annotation system must be declared before assigning categorical labels.

**Rhythm** concerns patterns of timing and prominence. Calling English stress-timed does not establish exactly equal intervals between stresses. Speech rate, phrase length, segment properties and context affect observed timing.

Fundamental frequency is an acoustic correlate relevant to perceived pitch during voicing. Duration and intensity are separate measurements. A highest-frequency point is not automatically the focus, and automated measurements can require correction. This Model does not prescribe undocumented thresholds.

## Worked analysis
Use *Maya repaired the printer* in three constructed contexts. **Focus** is the expression or span that selects among relevant alternatives in the exchange; it need not be only the accented word. Bold marks the proposed main accented word, not a measured loudness or a complete intonational transcription.

| Contextual question | Possible response | Intended focus span |
|---|---|---|
| Who repaired the printer? | **Maya** repaired the printer. | Maya, compared with other possible repairers |
| What did Maya repair? | Maya repaired the **printer**. | The printer, compared with other possible objects |
| What did Maya do? | Maya repaired the **printer**. | Repaired the printer, compared with other possible activities |

For the second response, a locally complete schematic analysis is:

| Layer | Constructed analysis |
|---|---|
| Word stress | *Printer* has primary stress on its first syllable: broad General American /ˈprɪntər/ |
| Utterance prominence | Main accent on that first syllable of *printer* |
| Focus | The object phrase *the printer* answers the stated question |
| Grouping | One proposed phrase containing the whole response |
| Intonation | A falling ending is one candidate realization; the written answer does not prescribe it |
| Timing and signal | No recorded durations, intensity values or pitch track are available |

Moving main prominence to *Maya* does not move *printer*'s lexical stress to its second syllable. Conversely, the second and third responses show why the accented word alone does not determine the focus span. These comparisons motivate separate word-stress, accent and context fields; they do not predict every speaker's realization.

Rhythm adds a timing question: how are the syllables between prominent positions realized at the chosen speaking rate? Extra syllables do not justify inventing an equal inter-stress interval or deleting sounds from a transcription. Record timing from actual speech before claiming compression, lengthening or reduction in a token.

A declarative used for confirmation can rise, while an ordinary information-seeking wh-question can fall. The distinction between clause type and use therefore cannot be replaced by a rule that rising pitch always means a question or that falling pitch always means an assertion.

### Connected speech and prominence

Prosodic context matters when investigating **reduction** (a less fully articulated sound) or **elision** (a segment absent from a reduced realization). For example, unstressed *you* may have [jə] instead of [ju]: the vowel remains, so this comparison illustrates reduction, not deletion. The [selected connected-speech passages](../references/anderson-2018-essentials-of-linguistics.md#connected-speech-passages) discuss reduced vowels and optional omissions. Stress and prominence help describe the conditions, but do not determine which sounds a particular speaker omitted. Keep the prosodic analysis and the proposed segment change separate; no elision is required merely to produce an assumed English rhythm.

## Interfaces
**Phonology Prosody:** syllables, stress domains and segment patterns interact. **Syntax Prosody:** structural grouping constrains some possibilities without imposing a unique phrase boundary after each constituent. **Information Structure Prosody:** context-sensitive focus and contrast influence prominence without identifying focus with the accented word. **Prosody Phonetics:** proposed prosodic structure is realized through variable physical cues.

### Interface with Phonology

Syllable organization and lexical stress constrain prosodic realization, but do not uniquely determine phrasal prominence or grouping.

Keep lexical stress organization separate from utterance accent and phrasing when comparing the same words across contexts. The counterpart is explained in [Phonology](english-phonology-system.md#interface-with-prosody).

#### Interface with Phonology representation

Keep a segment string and syllable parse, lexical stress positions, proposed phrasal accents, and phrase-edge annotations in different fields. A word can contain a lexically stressed syllable even when that word does not receive the strongest prominence in an utterance. Prosody is independently browsable here but overlaps phonological analysis; the domain boundary is an organizing convention.

#### Interface with Phonology worked analysis

In a constructed “The students repaired the printers,” lexical word forms remain the same across a who-question and a what-question context. A proposed accent can shift from students to printers, while each word retains its lexical stress organization. Do not rewrite the lexical entry to encode every sentence-specific accent.

#### Interface with Phonology evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Phonology assumptions and limits

This does not assign a complete metrical or tonal analysis. Stress, reduction, syllabification and phrasing vary with variety, rate and theoretical assumptions. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Phonology evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Phonetics

A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization.

State a prominence or phrasing analysis before asking which signal properties could support its realization. The counterpart is explained in [Phonetics](english-phonetics-system.md#interface-with-prosody).

#### Interface with Phonetics representation

| Endpoint | Schematic fields |
|---|---|
| prominence pattern | accent_location, phrasing, variety |
| prosodic acoustic description | pitch_pattern, duration, intensity, measurement_method, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Phonetics essential terms

A **prominence pattern** represents relative highlighting, stress and phrasing within an utterance. A **prosodic acoustic description** records properties of an identified signal, such as fundamental frequency in voiced intervals, duration and intensity. Perceived pitch is related to fundamental frequency but is not identical to it; prominence is not simply loudness or the highest pitch value. A proposed pitch accent and a measured frequency peak are different analytical claims.

#### Interface with Phonetics worked interpretation

For a reply to *Who repaired the printer?*, an analyst might predict prominence on *Nina* in *Nina repaired the printer*. A recording could realize that prominence through a combination of pitch-related movement, timing, intensity and other cues. No specific contour or measurement follows from capitalizing NINA in a transcript. To test the proposed correspondence, preserve the question context, identify the token and compare annotated prominence with the actual signal, retaining uncertainty where the cues disagree.

#### Interface with Phonetics assumptions and limits

The relation is schematic and potentially many-to-many, but its cardinality remains unspecified here. Acoustic cues, speakers and contexts need empirical investigation; an abstract prominence label does not predict numerical measurements.

#### Interface with Phonetics evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Phonetics evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

### Interface with Syntax

Syntactic grouping can constrain prosodic grouping without making syntactic constituents and prosodic phrases identical.

Compare proposed phrase boundaries with syntactic grouping while allowing length, focus and rate to affect realization. The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-prosody).

#### Interface with Syntax representation

| Syntactic description | Prosodic description | Required distinction |
|---|---|---|
| NP or clause span | Candidate prosodic phrase span | Similar boundaries are not identity. |
| Embedded relative clause | Possible grouping around the modifier | A pause does not prove a unique parse. |
| Constituent length and embedding | Rate-sensitive phrasing options | Optional phrasing is not a new syntax by itself. |

#### Interface with Syntax worked analysis

Bracket “[The report that Maya prepared] [arrived].” The subject contains a relative clause. A proposed spoken realization may group the whole subject or use finer phrasing depending on length, focus and rate. The written brackets neither specify silence durations nor justify one exact intonation transcription. Compare this with an explicit pause after report only after recording or hearing the target.

#### Interface with Syntax evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Syntax assumptions and limits

The mapping is framework- and context-sensitive. No one-to-one match, universal pause rule or deterministic recovery of syntax from acoustics is asserted. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Syntax evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Information Structure

Focus domains constrain possible prosodic realizations without being identical to the most strongly accented word.

Use explicit question contexts to interpret prominence while retaining alternative focus spans. The counterpart is explained in [Information Structure](english-information-structure-system.md#interface-with-prosody).

#### Interface with Information Structure representation

| QUD | Focus domain | Background | Possible strongest word |
|---|---|---|---|
| Who repaired the printer? | Nina | __ repaired the printer | NINA |
| What did Nina repair? | the printer | Nina repaired __ | PRINTER |
| What did Nina do? | repaired the printer | Nina __ | PRINTER |

#### Interface with Information Structure worked interpretation

NP focus and VP focus can share a prominent PRINTER. A broader conversation about the printer does not make Nina Topic merely because she is Subject or focused. The acoustic realization of prominence may involve pitch movement, duration and intensity.

#### Interface with Information Structure assumptions and limits

The table is a constructed working illustration, not an audio measurement or a complete focus-projection grammar. Roberts' abstract supports a connection between QUD and prosodic focus; detailed derivations require full-text and competing-source review.

#### Interface with Information Structure evaluation and counterevidence

Compare explicit question-answer contexts while holding the sentence string stable. Record focus span, accented word and lexically stressed syllable separately. Do not assign a unique focus domain from capitalization alone.

#### Interface with Information Structure evidence status

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this section. Inspect the linked record's access extent and nonclaims.

- [Information Structure: Towards an integrated formal theory of pragmatics. Semantics and Pragmatics 5, article 6.](../references/roberts-2012-information-structure.md#abstract) — support is limited to the named section in that record.

## Evaluation and counterevidence
For actual data, preserve the audio, context, speaker/variety and annotation convention. Inspect alignment and ambiguous boundaries. Compare the same wording across contexts and different wordings in a similar context. A proposed interpretation should survive consideration of at least one alternative explanation.

Diagnostic: does the highest measured pitch prove which word is in focus? No. Lexical/prosodic structure, boundaries, speaker range, tracking error and context may matter. The acoustic peak and the focus analysis are separate claims.

## Assumptions and limits
The prominence and edge vocabulary is a working account, not a complete ToBI system or universal prosodic grammar. Intonational meaning, focus projection, rhythm and variety-specific patterns require additional studies. No audio measurement or experimental comprehension result is claimed.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records selected suprasegmental and connected-speech discussions. The [MIT ToBI tutorial](../references/mit-2006-tobi-tutorial.md) supports distinguishing prominence from phrasing and high/low accents from phrase endings. The [Roberts Reference](../references/roberts-2012-information-structure.md) supports a broad QUD/prosodic-focus connection at abstract level; it does not independently verify the particular focus-projection examples here. The question table and layered analysis are authored illustrations, not observed productions or a completed ToBI annotation. Rhythm and context-dependent interpretations retain the limits above.

## Related knowledge
[Stress](../concepts/stress.md), [prosody and intonation](../concepts/prosody.md) and [connected speech](../concepts/connected-speech.md) expand the distinctions. [Syntax Prosody interface](#interface-with-syntax), [Information Structure Prosody interface](#interface-with-information-structure) and [Prosody Phonetics interface](#interface-with-phonetics) explain the principal connections.
