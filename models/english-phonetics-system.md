---
id: "english:model:english-phonetics-system"
type: "model"
version: "0.2.3"
language: "KPS 9.x"
status: "draft"
domains: ["phonetics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:international-phonetic-association-undated-ipa-chart", "english:reference:mit-2006-tobi-tutorial"]
uses_concepts: ["english:concept:representation-levels", "english:concept:consonant-articulation", "english:concept:vowel-articulation", "english:concept:connected-speech"]
uses_models: ["english:model:phonology-phonetics-interface", "english:model:prosody-phonetics-interface"]
system_domain: "phonetics"
---

# English phonetics system

## Key takeaway
Phonetics describes speech production, the acoustic signal and perception; a written transcription is an analysis, not a recording.

## Summary
This Model connects vocal-fold activity and vocal-tract configuration with sound descriptions while separating production, acoustic evidence and perception. It explains consonant and vowel attributes, contextual realizations and connected-speech processes including elision. Inline interfaces show how phonological categories and prosodic structure relate to phonetic descriptions and evidence. New word examples use the package's General American convention. Examples are constructed; no recording or measurement is claimed.

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

## Connected speech and elision

Speech gestures overlap as the articulators move between sounds; this is **coarticulation**. Consequently, a word's realization in a phrase can differ from its fuller citation form, the pronunciation used as a reference when discussing the word in isolation. Rate, prominence, neighboring sounds, style and variety must be considered. These differences can occur within a word as well as across word boundaries.

| Process | What changes | Illustrative comparison |
|---|---|---|
| Elision or segment deletion | A segment present in the fuller comparison has no separate realization in the reduced analysis | *Asked*: [æskt] compared with possible [æst], omitting [k] |
| Assimilation | A sound takes on a property of a neighbor | The vowel in *can* may be nasalized before /n/: [æ̃], where the tilde marks nasalization |
| Reduction | A sound becomes less fully articulated, for example with a more central vowel; a segment may remain | Unstressed *you* may have [jə] rather than [ju] |
| Linking | Articulation continues across a word boundary | *An apple* can be spoken continuously; joining the words does not itself delete a sound |

These are schematic comparisons for the declared General American reference, not recordings or obligatory pronunciations. The [inspected connected-speech passages](../references/anderson-2018-essentials-of-linguistics.md#connected-speech-passages) support bounded process distinctions; the table does not exhaust possible changes or make them mutually exclusive.

**How to interpret elision.** In the *asked* comparison, [s] and [t] remain while the intervening [k] is absent from the reduced transcription. The word and its past-tense interpretation need not change. For an actual token, identify the expected segment, inspect its interval and neighboring transitions, and compare alternatives. A stop can lack an audible release while retaining a closure; weak or overlapping cues can also be difficult to hear. Failure to hear a burst alone therefore does not establish deletion. Report an uncertain or reduced realization when the evidence cannot distinguish these possibilities.

Elision is thus an analysis of a spoken realization, not an instruction to remove a written letter or to omit sounds whenever speaking faster. The [Connected Speech Concept](../concepts/connected-speech.md) provides the reusable distinctions; their necessary meaning is included here.

## Worked example
**Classifying a sound.** Compare [b] with [m]. Both are voiced and bilabial in these categories. With the nasal passage closed, lip closure blocks outgoing airflow in [b]; opening the nasal passage permits airflow in [m]. The manner difference therefore explains why the same lip closure does not identify the same sound. This is an articulatory illustration, not a report about a measured token.

**Comparing contextual realizations.**
Compare candidate productions of *pin* and *spin*. Both broad forms contain /p/. A stressed onset in *pin* can have aspiration; the post-/s/ stop in *spin* is commonly less aspirated. The useful question is not whether the letter changed, but whether the realizations differ in a specified environment.

Without audio, record this as a predicted contrast. With suitable recordings, identify each token, mark the stop release and voicing onset when discernible, record the interval and document ambiguous boundaries. Do not invent a millisecond value or infer that every General American speaker has the same interval.

## Interfaces

An **interface** connects two descriptions of the same speech event. It states which information relates across them, under what conditions, and what evidence can test the proposed relationship. These correspondences do not specify a fixed sequence of mental processing.

| Connection | Other representation | Phonetic representation and relationship |
|---|---|---|
| Phonology–Phonetics | Sound categories, neighboring sounds, syllable positions and stress | Candidate articulations and timing; the category together with its environment constrains likely realizations |
| Prosody–Phonetics | Which syllables are prominent and how words group into phrases | Pitch-related patterns, duration, intensity and boundary cues; several physical cues can contribute to the same prominence or grouping analysis |

### Phonology and phonetic realization

The category /p/ occurs in both *pin* /pɪn/ and *spin* /spɪn/. In the constructed General American comparison, beginning a stressed syllable without preceding /s/ supports a prediction of aspirated [pʰ]; following /s/ in the same onset supports less aspirated [p]. Aspiration is voiceless airflow after the release. Thus the shared category does not require identical timing in both environments.

To test that correspondence, identify the recordings and compare stop release with the onset of vocal-fold vibration. A mismatch calls for checking the transcription, stress, context and speaker variety before revising the generalization. The category alone supplies no exact duration, and a measured difference alone does not establish a different phoneme. The [Phonology–Phonetics Model](phonology-phonetics-interface.md) expands this correspondence; the essential example is given here.

### Prosody and physical cues

**Prominence** is relative highlighting; **phrasing** is grouping within an utterance. In a constructed answer to *Who repaired the printer?*, *Maya* may carry the main prominence in *Maya repaired the printer*. That proposal identifies a location to investigate. It does not assign a pitch value, loudness or duration to the word.

An actual analysis compares the proposed prominent syllable and phrase boundaries with the recording. Pitch movement and timing may support the proposal; a prominent syllable need not have the highest pitch, and a phrase boundary need not contain silence. A disagreement between annotation and signal should remain visible rather than be resolved by inventing measurements. These distinctions have selected support in the [MIT tutorial record](../references/mit-2006-tobi-tutorial.md); the [Prosody–Phonetics Model](prosody-phonetics-interface.md) develops the investigation further.

### Contributions from word structure and writing

Morphology contributes word structure and grammatical forms, which can affect the sound environments under analysis; this does not directly determine one waveform. Orthography supplies a written representation. Neither written letters nor word boundaries alone establish a particular articulation, pause or acoustic value. Preserve them as context while distinguishing sound categories, prosodic organization and observed realization.

## Evaluation and counterevidence
For a proposed phonetic claim, identify the token, speaker/variety, context, notation and observation. Compare repeated tokens rather than treating one production as a universal norm. If no recording exists, the correct output is a qualified prediction, not an acoustic finding.

A useful check: does /r/ necessarily mean a trill? No. In this package it is a broad rhotic convention; a more detailed phone description may use [ɹ]. The phonemic symbol does not specify every physical feature.

## Assumptions and limits
This is a foundational explanatory Model, not a complete General American inventory, a clinical assessment or a validated pronunciation course. Individual variation, mergers, connected-speech reduction and transcription choices require local qualification. Instrumental analysis and controlled perception experiments remain further work.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records selected articulation, transcription, connected-speech and aspiration passages, including their Canadian scope. The [IPA Reference](../references/international-phonetic-association-undated-ipa-chart.md) supports the chart categories. The [MIT tutorial record](../references/mit-2006-tobi-tutorial.md) supplies selected support for prominence, phrasing and physical cues. These sources do not supply measurements of the constructed examples. The comparisons and interface summaries are authored applications, and the acoustic procedure is an investigation outline, not a newly performed experiment.

## Related knowledge
[Representation levels](../concepts/representation-levels.md) distinguishes notation in more detail. [Consonant articulation](../concepts/consonant-articulation.md) and [vowel articulation](../concepts/vowel-articulation.md) expand feature descriptions. [Analyze sound realization](../methods/analyze-sound-realization.md) supplies a bounded investigation; [Phonology Phonetics interface](phonology-phonetics-interface.md) explains the mapping.
