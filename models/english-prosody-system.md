---
id: "english:model:english-prosody-system"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["prosody"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:roberts-2012-information-structure"]
uses_concepts: ["english:concept:stress", "english:concept:prosody", "english:concept:connected-speech"]
uses_models: ["english:model:phonology-prosody-interface", "english:model:syntax-prosody-interface", "english:model:focus-prosody-interface", "english:model:prosody-phonetics-interface"]
system_domain: "prosody"
---

# English prosody system

## Key takeaway
Prosody organizes prominence, phrasing, timing and intonation across segments; no single pitch movement uniquely determines meaning.

## Summary
This Model distinguishes lexical stress, phrasal prominence, pitch accent, boundary behavior and acoustic realization. It explains why a word can retain lexical stress without carrying the strongest accent in an utterance, and why a rise is not a universal question marker. Text examples are schematic; no acoustic trace or learner performance has been observed.

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

## Essential distinctions
**Stress** concerns relative prominence in a structured pattern; it is not simply loudness. **Intonation** concerns pitch organization over an utterance or phrase. In an accent-and-boundary account, pitch events associated with prominent positions are distinguished from tonal events associated with phrase edges. The chosen annotation system must be declared before assigning categorical labels.

**Rhythm** concerns patterns of timing and prominence. Calling English stress-timed does not establish exactly equal intervals between stresses. Speech rate, phrase length, segment properties and context affect observed timing.

Fundamental frequency is an acoustic correlate relevant to perceived pitch during voicing. Duration and intensity are separate measurements. A highest-frequency point is not automatically the focus, and automated measurements can require correction. This Model does not prescribe undocumented thresholds.

## Worked analysis
For *Maya repaired the printer*, imagine a context asking *What did Maya repair?* A schematic response can place prominence on *printer*. In a context asking *What did Maya do?*, prominence on the same word can participate in a broader focus on *repaired the printer*.

Write the lexical stress positions, proposed accented word and focus span separately. Do not read the capital letters PRINTER as a complete intonational transcription. A recording would be needed to describe the realized pitch movement, timing and phrasing.

A declarative used for confirmation can rise, while an ordinary information-seeking wh-question can fall. The distinction between clause type and use therefore cannot be replaced by a rule that rising pitch always means a question or that falling pitch always means an assertion.

## Interfaces
**Phonology Prosody:** syllables, stress domains and segment patterns interact. **Syntax Prosody:** structural grouping constrains some possibilities without imposing a unique phrase boundary after each constituent. **Information Structure Prosody:** context-sensitive focus and contrast influence prominence without identifying focus with the accented word. **Prosody Phonetics:** proposed prosodic structure is realized through variable physical cues.

## Evaluation and counterevidence
For actual data, preserve the audio, context, speaker/variety and annotation convention. Inspect alignment and ambiguous boundaries. Compare the same wording across contexts and different wordings in a similar context. A proposed interpretation should survive consideration of at least one alternative explanation.

Diagnostic: does the highest measured pitch prove which word is in focus? No. Lexical/prosodic structure, boundaries, speaker range, tracking error and context may matter. The acoustic peak and the focus analysis are separate claims.

## Assumptions and limits
The prominence and edge vocabulary is a working account, not a complete ToBI system or universal prosodic grammar. Intonational meaning, focus projection, rhythm and variety-specific patterns require additional studies. No audio measurement or experimental comprehension result is claimed.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records a limited suprasegmental discussion. The [Roberts Reference](../references/roberts-2012-information-structure.md) supports a broad QUD/prosodic-focus connection at abstract level. Neither certifies the full representation or examples in this Model.

## Related knowledge
[Stress](../concepts/stress.md), [prosody and intonation](../concepts/prosody.md) and [connected speech](../concepts/connected-speech.md) expand the distinctions. [Syntax Prosody interface](syntax-prosody-interface.md), [Information Structure Prosody interface](focus-prosody-interface.md) and [Prosody Phonetics interface](prosody-phonetics-interface.md) explain the principal connections.
