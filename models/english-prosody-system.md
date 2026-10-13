---
id: "english:model:english-prosody-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["prosody"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:roberts-2012-information-structure", "english:reference:mit-2006-tobi-tutorial"]
uses_concepts: ["english:concept:stress", "english:concept:prosody", "english:concept:connected-speech"]
uses_models: ["english:model:phonology-prosody-interface", "english:model:syntax-prosody-interface", "english:model:focus-prosody-interface", "english:model:prosody-phonetics-interface"]
system_domain: "prosody"
---

# English prosody system

## Key takeaway
Prosody organizes prominence, phrasing, timing and intonation across segments; no single pitch movement uniquely determines meaning.

## Summary
This Model relates syllables and lexical stress to utterance prominence, rhythm and phrase boundaries. Separate annotation layers show how an accented syllable, the span in focus and a phrase-ending pitch movement can differ. Constructed comparisons explain why a rise is not a universal question marker and why stress does not imply equal timing or maximum pitch. No acoustic trace or learner performance has been observed.

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

## Interfaces
**Phonology Prosody:** syllables, stress domains and segment patterns interact. **Syntax Prosody:** structural grouping constrains some possibilities without imposing a unique phrase boundary after each constituent. **Information Structure Prosody:** context-sensitive focus and contrast influence prominence without identifying focus with the accented word. **Prosody Phonetics:** proposed prosodic structure is realized through variable physical cues.

## Evaluation and counterevidence
For actual data, preserve the audio, context, speaker/variety and annotation convention. Inspect alignment and ambiguous boundaries. Compare the same wording across contexts and different wordings in a similar context. A proposed interpretation should survive consideration of at least one alternative explanation.

Diagnostic: does the highest measured pitch prove which word is in focus? No. Lexical/prosodic structure, boundaries, speaker range, tracking error and context may matter. The acoustic peak and the focus analysis are separate claims.

## Assumptions and limits
The prominence and edge vocabulary is a working account, not a complete ToBI system or universal prosodic grammar. Intonational meaning, focus projection, rhythm and variety-specific patterns require additional studies. No audio measurement or experimental comprehension result is claimed.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records a limited suprasegmental discussion. The [MIT ToBI tutorial](../references/mit-2006-tobi-tutorial.md) supports distinguishing prominence from phrasing and high/low accents from phrase endings. The [Roberts Reference](../references/roberts-2012-information-structure.md) supports a broad QUD/prosodic-focus connection at abstract level; it does not independently verify the particular focus-projection examples here. The question table and layered analysis are authored illustrations, not observed productions or a completed ToBI annotation. Rhythm and context-dependent interpretations retain the limits above.

## Related knowledge
[Stress](../concepts/stress.md), [prosody and intonation](../concepts/prosody.md) and [connected speech](../concepts/connected-speech.md) expand the distinctions. [Syntax Prosody interface](syntax-prosody-interface.md), [Information Structure Prosody interface](focus-prosody-interface.md) and [Prosody Phonetics interface](prosody-phonetics-interface.md) explain the principal connections.
