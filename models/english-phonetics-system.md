---
id: "english:model:english-phonetics-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["phonetics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:international-phonetic-association-undated-ipa-chart"]
uses_concepts: ["english:concept:representation-levels", "english:concept:consonant-articulation", "english:concept:vowel-articulation"]
uses_models: ["english:model:phonology-phonetics-interface", "english:model:prosody-phonetics-interface"]
system_domain: "phonetics"
---

# English phonetics system

## Key takeaway
Phonetics describes speech production, the acoustic signal and perception; a written transcription is an analysis, not a recording.

## Summary
This Model connects vocal-fold activity and vocal-tract configuration with sound descriptions while separating production, acoustic evidence and perception. It explains consonant and vowel attributes with selected category tables, then compares feature bundles and contextual realizations. New word examples use the package's General American convention. Examples are constructed; no recording or measurement is claimed.

## Purpose
Given a sound category, describe its relevant articulatory attributes and explain how changing them changes the description. Given a word or recording, distinguish a predicted realization from an observed token. A broad dictionary form can start an investigation but cannot establish exactly what a speaker produced.

## Representation

| Component | Representation and function | Evidence needed |
|---|---|---|
| Articulation | Airflow, vocal-fold behavior and vocal-tract constrictions describe production | Observation or a justified articulatory analysis |
| Acoustics | A time-varying signal can be characterized by duration, periodicity and spectral structure | An identified recording and declared measurement procedure |
| Perception | Listeners classify sounds and perceive prominence under contextual conditions | Recorded responses or a stated perceptual judgment |
| Transcription | Selected properties are represented with symbols and diacritics | An explicit accent, level of detail and evidential basis |

These descriptions concern the same speech event but are not interchangeable. A symbol is not an acoustic measurement; an acoustic difference does not by itself prove that listeners use it contrastively.

## Essential distinctions

### Consonant attributes and their physical meaning

For ordinary English speech, outgoing air passes through the larynx and vocal tract. The **vocal folds** can vibrate; the tongue and lips create constrictions; the **velum**, or soft palate, regulates the opening into the nasal cavity. Coordinating these actions changes the resulting sound. A **phone** is a phonetic sound category; a **token** is a particular production, whose details require evidence.

| Attribute | Meaning | Categories needed here |
|---|---|---|
| Voicing | Vocal-fold vibration during the relevant interval | Voiced, as [z]; voiceless, as [s] |
| Place | Location of the constriction | Bilabial: both lips; labiodental: lower lip and upper teeth; dental: tongue at the teeth; alveolar: ridge behind upper teeth; postalveolar: behind that ridge; palatal: hard palate; velar: soft palate; glottal: vocal-fold region |
| Manner | How airflow is obstructed or directed | Oral stop: complete oral closure with nasal passage closed; nasal: oral closure with nasal airflow; fricative: narrow constriction with friction; affricate: closure followed by a fricated release; approximant: closer approach without fricative-like friction; lateral approximant: airflow around the tongue's sides |

The following selected phone categories make those dimensions concrete. Paired symbols are voiceless then voiced; unpaired symbols have their voicing stated. This is a reference selection, not every English realization.

| Phone categories | Place | Manner |
|---|---|---|
| [p b] | Bilabial | Oral stop |
| [t d] | Alveolar | Oral stop |
| [k ɡ] | Velar | Oral stop |
| [f v] | Labiodental | Fricative |
| [θ ð] | Dental | Fricative |
| [s z] | Alveolar | Fricative |
| [ʃ ʒ] | Postalveolar | Fricative |
| [tʃ dʒ] | Postalveolar | Affricate |
| [m], [n], [ŋ] (voiced) | Bilabial, alveolar, velar respectively | Nasal |
| [j] (voiced) | Palatal | Approximant |
| [l] (voiced) | Alveolar | Lateral approximant |
| [h] (voiceless) | Glottal in the IPA classification | Fricative in the IPA classification |

The [IPA Reference](../references/international-phonetic-association-undated-ipa-chart.md) supplies symbol categories; the [Anderson articulation passages](../references/anderson-2018-essentials-of-linguistics.md#sound-model-passages) explain their production. Broad English /b d ɡ/ do not guarantee uninterrupted voicing in every token. Additional descriptions may be needed for timing, secondary articulations or the particular realization of /r/.

### Vowel attributes and changing quality

A vowel has a relatively open oral tract. **Height** describes the tongue body's relative high/close to low/open position; **backness** describes front, central or back position; **rounding** describes the lips. Height is not pitch: raising perceived pitch does not turn a low vowel into a high vowel.

| Selected phone | Height | Backness | Rounding |
|---|---|---|---|
| [i] | Close | Front | Unrounded |
| [ɪ] | Near-close | Near-front | Unrounded |
| [e] | Close-mid | Front | Unrounded |
| [ɛ] | Open-mid | Front | Unrounded |
| [æ] | Near-open | Front | Unrounded |
| [ɑ] | Open | Back | Unrounded |
| [ɔ] | Open-mid | Back | Rounded |
| [o] | Close-mid | Back | Rounded |
| [ʊ] | Near-close | Near-back | Rounded |
| [u] | Close | Back | Rounded |
| [ə] | Mid | Central | Neutral or unrounded in the working English description |

These are IPA quality labels, not exact targets for every American speaker. In the declared broad General American convention, *see* /si/, *sit* /sɪt/ and *sat* /sæt/ illustrate vowel distinctions. Compare [i] with [æ]: both are front and unrounded, but their heights differ. Compare [i] with [u]: both are close, but backness and rounding differ. Thus changing one dimension does not require changing all the others.

A **monophthong** is represented as one vowel quality; a **diphthong** has a change of quality within the nucleus, the syllable's central part. *My* /maɪ/ illustrates the latter. The trajectory, duration and precise endpoints vary with accent and context. Nasalization adds nasal resonance; rhoticity adds an r-like quality. They need further description when relevant and cannot be read from a vowel letter alone. The selected table does not settle English tense/lax classes, mergers or the full vowel inventory.

### From production to transcription and evidence

Orthographic <pin>, broad phonemic /pɪn/, and an illustrative phonetic [pʰɪn] describe different things. The raised aspiration mark indicates a possible realization detail, not an extra ordinary /h/ segment. Broad versus narrow describes detail; a phonetic transcription can itself be broad. Square brackets alone do not make a transcription observed data.

**Fundamental frequency (F0)** counts repeating cycles per second, in hertz, in periodic voiced portions of a signal; perceived pitch is related but not identical to it. **Formants** are vocal-tract resonances whose frequencies help describe vowel quality. F0 and formants describe different properties, so a higher-pitched [i] can still belong to the same vowel category. **Duration** is an interval's length in time; **intensity** describes acoustic energy and is related to perceived loudness. Duration and intensity can contribute to prominence, but no single measure is a universal stress detector.

## Worked example
**Classifying a sound.** Compare [b] with [m]. Both are voiced and bilabial in these categories. With the nasal passage closed, lip closure blocks outgoing airflow in [b]; opening the nasal passage permits airflow in [m]. The manner difference therefore explains why the same lip closure does not identify the same sound. This is an articulatory illustration, not a report about a measured token.

**Comparing contextual realizations.**
Compare candidate productions of *pin* and *spin*. Both broad forms contain /p/. A stressed onset in *pin* can have aspiration; the post-/s/ stop in *spin* is commonly less aspirated. The useful question is not whether the letter changed, but whether the realizations differ in a specified environment.

Without audio, record this as a predicted contrast. With suitable recordings, identify each token, mark the stop release and voicing onset when discernible, record the interval and document ambiguous boundaries. Do not invent a millisecond value or infer that every General American speaker has the same interval.

## Interfaces
**Phonology** supplies language-specific categories and environments; phonetics concerns their actual realization. **Prosody** supplies prominence and phrasing conditions that can affect timing and pitch. **Morphology** can place segments at different word boundaries. Orthography is a separate writing representation, not a mandatory stage of spoken language.

## Evaluation and counterevidence
For a proposed phonetic claim, identify the token, speaker/variety, context, notation and observation. Compare repeated tokens rather than treating one production as a universal norm. If no recording exists, the correct output is a qualified prediction, not an acoustic finding.

A useful check: does /r/ necessarily mean a trill? No. In this package it is a broad rhotic convention; a more detailed phone description may use [ɹ]. The phonemic symbol does not specify every physical feature.

## Assumptions and limits
This is a foundational explanatory Model, not a complete General American inventory, a clinical assessment or a validated pronunciation course. Individual variation, mergers, connected-speech reduction and transcription choices require local qualification. Instrumental analysis and controlled perception experiments remain further work.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records selected articulation, transcription and aspiration passages, including their Canadian scope. The [IPA Reference](../references/international-phonetic-association-undated-ipa-chart.md) supports the chart categories; neither source supplies measurements of these constructed examples. The comparisons are authored applications, and the acoustic procedure is an investigation outline, not a newly performed experiment.

## Related knowledge
[Representation levels](../concepts/representation-levels.md) distinguishes notation in more detail. [Consonant articulation](../concepts/consonant-articulation.md) and [vowel articulation](../concepts/vowel-articulation.md) expand feature descriptions. [Analyze sound realization](../methods/analyze-sound-realization.md) supplies a bounded investigation; [Phonology Phonetics interface](phonology-phonetics-interface.md) explains the mapping.
