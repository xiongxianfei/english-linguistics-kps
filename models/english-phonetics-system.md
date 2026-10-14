---
id: "english:model:english-phonetics-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["phonetics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:international-phonetic-association-undated-ipa-chart", "english:reference:mit-2006-tobi-tutorial", "english:reference:coleman-undated-speech-acoustics", "english:reference:praat-undated-spectrogram-manual", "english:reference:flemming-2015-speech-perception"]
uses_concepts: ["english:concept:representation-levels", "english:concept:consonant-articulation", "english:concept:vowel-articulation", "english:concept:connected-speech", "english:concept:phone-phoneme-and-allophone", "english:concept:prosody", "english:concept:stress"]
uses_models: ["english:model:english-phonology-system", "english:model:english-prosody-system", "english:model:english-information-structure-system"]
system_domain: "phonetics"
uses_principles: ["english:principle:realization-varies-with-environment"]
uses_methods: ["english:method:analyze-sound-realization"]
---

# English phonetics system

## Key takeaway
Phonetics describes speech production, the acoustic signal and perception; a written transcription is an analysis, not a recording.

## Summary
This Model connects eight Phonetics topics: its boundary with Phonology, speech production, consonant and vowel articulation, transcription, acoustics, perception and connected speech. It explains the source and filter distinction, how to read signal representations, and why an acoustic difference does not establish a listener's response. Existing sound-attribute tables and interfaces remain locally available. A constructed pin/spin/bin comparison connects category, articulation, timing, transcription and perceptual questions. General American is the declared convention for new word examples; no audio measurement or listener experiment is reported.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Phonetics vs Phonology](#phonetics-vs-phonology)
- [Speech production](#speech-production)
- [Consonant articulation](#consonant-articulation)
- [Vowel articulation](#vowel-articulation)
- [IPA and transcription](#ipa-and-transcription)
- [Speech acoustics](#speech-acoustics)
- [Speech perception](#speech-perception)
- [Connected speech processes](#connected-speech-processes)
- [Worked example](#worked-example)
- [Interfaces](#interfaces)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

## Purpose
Given a sound category, describe its relevant articulatory attributes and explain how changing them changes the description. Explain how production can shape a signal and how a perceptual question differs from measuring that signal. Given a word or recording, distinguish a predicted realization from an observed token. A broad dictionary form can start an investigation but cannot establish exactly what a speaker produced.

## Representation

| Component | Representation and function | Evidence needed |
|---|---|---|
| Articulation | Airflow, vocal-fold behavior and vocal-tract constrictions describe production | Observation or a justified articulatory analysis |
| Acoustics | A time-varying signal can be characterized by duration, periodicity and spectral structure | An identified recording and declared measurement procedure |
| Perception | Listeners classify sounds and perceive prominence under contextual conditions | Recorded responses or a stated perceptual judgment |
| Transcription | Selected properties are represented with symbols and diacritics | An explicit accent, level of detail and evidential basis |

These descriptions concern the same speech event but are not interchangeable. A symbol is not an acoustic measurement; an acoustic difference does not by itself prove that listeners use it contrastively.

## Essential distinctions

A **phone** is a phonetic sound category; a **token** is a particular production. A **phoneme** is a language-specific contrastive category; an **allophone** is a contextual realization under a phonological analysis. Articulation describes production, acoustics describes the signal, and perception concerns listeners' responses. None is established simply by writing an IPA symbol.

## Phonetics vs Phonology

Phonetics asks how speech is produced, transmitted and perceived. Phonology asks how a language organizes sound contrasts and patterns. The distinction is useful even where the explanations overlap.

For example, aspiration after a stop release is a phonetic property. Whether aspirated and less aspirated realizations belong to one phoneme in a particular environment is a phonological analysis. English *pin* and *spin* motivate a contextual comparison; *pin* and *bin* motivate a lexical contrast. A physical difference alone does not settle phoneme identity. The [Phonology interface](#interface-with-phonology) explains how the two descriptions constrain each other.

## Speech production

Ordinary English speech principally uses outgoing lung air. **Respiration** supplies airflow; **phonation** concerns activity at the larynx, or voice box; **articulation** shapes the tract and its constrictions. The **glottis** is the opening between the vocal folds. Vibration of the paired vocal folds can supply periodic, or repeating, excitation, while airflow through a narrow constriction can generate turbulent noise. These sources can occur together, as in a voiced fricative.

The tongue, lips and jaw alter constrictions. The **velum**, or soft palate, controls access to the nasal cavity. Compare category descriptions [b] and [m]: both have lip closure, but [m] permits nasal airflow. Lip position alone therefore cannot identify the sound.

These mechanisms are coordinated rather than three instructions to perform successively. Voiceless speech still has an acoustic source; it does not mean “no sound.” The inspected [Anderson production script](../references/anderson-2018-essentials-of-linguistics.md#speech-production-passage) supplies the introductory mechanism, and [Coleman's source account](../references/coleman-undated-speech-acoustics.md) distinguishes vibration from noise.

## Consonant articulation

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

## Vowel articulation

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

## IPA and transcription

Orthographic ⟨pin⟩, broad phonemic /pɪn/, and an illustrative phonetic [pʰɪn] describe different things. The raised aspiration mark indicates a possible realization detail, not an extra ordinary /h/ segment. Broad versus narrow describes detail; a phonetic transcription can itself be broad. Square brackets alone do not make a transcription observed data.

The **International Phonetic Alphabet (IPA)** supplies symbols for sounds rather than ordinary spelling. A recording could justify a narrower account, but adding symbols without evidence does not make it more accurate. Write the variety, purpose and observation basis alongside a transcription. The [notation policy](../docs/PRONUNCIATION.md) states this package's conventions; the IPA chart supplies general symbol categories rather than one English inventory.

## Speech acoustics

Acoustics describes the physical sound signal. **Fundamental frequency (F0)** is the repetition rate in a periodic interval, measured in hertz; it is related to perceived pitch. **Duration** is an interval's length. **Intensity** concerns acoustic power per unit area and is related to loudness; a recording's amplitude also depends on gain and microphone placement. These measures answer different questions.

### Source and filter

The **source** supplies excitation, such as vocal-fold vibration or turbulence. The vocal tract **filter** shapes its frequency content through resonances. **Formants** are resonant frequency regions used to characterize vowel quality; F1 and F2 name the first two. **Harmonics** of a periodic source occur at integer multiples of F0. A formant is not simply another name for a harmonic or for F0.

This distinction explains why raising pitch need not change [i] into another vowel: a source change and a tract-shape change are different interventions. Conversely, changing the tract configuration can alter vowel quality while F0 remains similar. This is a useful simplified account, not a claim that the source and tract are physically independent in every condition. [Coleman's inspected teaching text](../references/coleman-undated-speech-acoustics.md) supports the distinction.

### Signal representations

| View | What it represents | Useful question and limit |
|---|---|---|
| Waveform | Signal amplitude over time | Where might an event begin or end? A large peak is not a phoneme label |
| Spectrum | Frequency content in a selected interval | Which frequency regions carry energy? The selected interval matters |
| Spectrogram | Frequency content over time, with shading or color for its strength | How do periodicity, noise and resonant bands change? Display settings affect what is visible |

In a usual speech spectrogram, time runs horizontally and frequency vertically. Darker regions represent stronger spectral energy under the selected scale. They do not automatically mean a louder speaker or a different vowel. The [Praat manual](../references/praat-undated-spectrogram-manual.md) explains axes, shading and display changes. A spectrogram is a representation derived from a recording, not an anatomical photograph or an automatic transcription.

### Timing and comparison

**Voice onset time (VOT)** compares a stop release with the onset of voicing. When both landmarks are identifiable, use `VOT = voicing onset time - release time`. Positive values indicate voicing begins after release; negative values indicate it began before release. The choice of landmarks and uncertainty must be stated.

In a purely constructed timing example, release at 1.000 seconds and voicing onset at 1.050 seconds yield +50 milliseconds. That arithmetic does not establish which sound a real speaker produced or what a listener heard. Do not apply one universal VOT threshold across places, contexts and varieties. The [MIT perception lecture](../references/flemming-2015-speech-perception.md) treats VOT as one cue among several.

## Speech perception

Perception asks what listeners hear or categorize from the signal. An **acoustic cue** is a signal property investigated for its contribution to that response. Finding a production difference does not by itself establish its perceptual use.

**Identification** asks which label a listener assigns. **Discrimination** asks whether stimuli can be distinguished. Hearing a difference need not require assigning different phoneme labels. A sharp change in labeling alone does not establish strict categorical perception. The [MIT lecture](../references/flemming-2015-speech-perception.md) motivates these distinctions and the use of multiple cues.

For the constructed timing case, retain two separate questions: “How far apart are release and voicing onset?” and “Which category does the listener report?” A listener study would need actual stimuli, instructions and responses. Its outcome cannot be filled in from +50 milliseconds alone. Context, the other cues and the task must be considered. This introductory account supplies questions for investigation, not a complete hearing model or a listening lesson.

## Connected speech processes

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

### Connecting the whole analysis

Use the constructed General American comparison *pin* /pɪn/, *spin* /spɪn/ and *bin* /bɪn/. This is a proposed analysis, not a set of recorded productions.

| Part of the Model | Reasoning in the comparison |
|---|---|
| Phonetics and Phonology | The /p/ environments differ in pin/spin; /p/ versus /b/ distinguishes pin/bin |
| Production and consonants | The initial stops involve lip closure; their release and laryngeal timing need separate descriptions |
| Vowels | /ɪ/ identifies the declared vowel category, not identical formant values in all three tokens |
| Transcription | [pʰ] can state the predicted aspiration in pin; the spelling alone cannot verify it |
| Acoustics | Compare release, aspiration and periodic onset in recordings; report uncertain boundaries |
| Perception | Ask separately whether listeners distinguish candidate productions and how they label them |
| Connected speech | Phrase context, overlapping gestures and prominence can alter the realizations |

A shorter aspiration interval in *spin* does not automatically turn its /p/ into /b/. Conversely, recording two different intervals would not by itself establish how listeners classify the sounds. The useful result is a connected explanation with explicit evidence requirements, not a table of invented measurements.

## Interfaces

An **interface** connects two descriptions of the same speech event. It states which information relates across them, under what conditions, and what evidence can test the proposed relationship. These correspondences do not specify a fixed sequence of mental processing.

| Connection | Other representation | Phonetic representation and relationship |
|---|---|---|
| Phonology–Phonetics | Sound categories, neighboring sounds, syllable positions and stress | Candidate articulations and timing; the category together with its environment constrains likely realizations |
| Prosody–Phonetics | Which syllables are prominent and how words group into phrases | Pitch-related patterns, duration, intensity and boundary cues; several physical cues can contribute to the same prominence or grouping analysis |

### Contributions from word structure and writing

Morphology contributes word structure and grammatical forms, which can affect the sound environments under analysis; this does not directly determine one waveform. Orthography supplies a written representation. Neither written letters nor word boundaries alone establish a particular articulation, pause or acoustic value. Preserve them as context while distinguishing sound categories, prosodic organization and observed realization.

### Interface with Phonology

Phonological representations constrain possible phonetic analyses without uniquely specifying an observed speech token.

Use category and environment as constraints on a production hypothesis; identify recordings before claiming an observed realization. The counterpart is explained in [Phonology](english-phonology-system.md#interface-with-phonetics).

#### Interface with Phonology representation

| Endpoint | Schematic fields |
|---|---|
| phonological form | segments, syllables, stress |
| phonetic realization | transcription_level, context, observed_or_predicted, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Phonology essential terms

A **phonological form** describes language-specific categories and structural positions. A **phonetic realization** describes speech production or the resulting sound in a particular context. Slashes conventionally mark a phonemic analysis; square brackets mark a phonetic description. Neither notation by itself identifies a recording. Stress, neighboring sounds, rate and speaker variety can condition realization, so a phonological string need not determine one narrow transcription.

#### Interface with Phonology worked interpretation

Broad /pɪn/ and /spɪn/ both contain /p/. A stressed onset in *pin* can be aspirated, represented schematically as [pʰ], while the post-/s/ realization in *spin* is commonly less aspirated. The phonological environment helps explain a predicted difference without changing /p/ into a different phoneme merely because the phones differ. No token has been recorded here. To claim an observed difference, identify recordings and the criteria used to inspect the realization.

#### Interface with Phonology assumptions and limits

A variety, stress and segmental context must be stated. This bridge does not assert a universal phonetics–phonology boundary or an executable production model. No audio is supplied for this worked comparison.

#### Interface with Phonology evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Phonology evidence status

**Provisional.** This bridge is an authored synthesis; selected source contributions are identified in the Model evidence section. They do not establish the complete mapping, measurements of this example, independent review or learner outcomes.

Aspiration is voiceless airflow after release. Compare stop release with voicing onset in identified recordings; a mismatch requires checking stress, environment and variety. No exact duration follows from /p/, and a measured difference alone does not establish a different phoneme.

### Interface with Prosody

A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization.

Compare pitch-related frequency, timing and intensity with a proposed prominence analysis; do not identify an acoustic peak with focus. The counterpart is explained in [Prosody](english-prosody-system.md#interface-with-phonetics).

#### Interface with Prosody representation

| Endpoint | Schematic fields |
|---|---|
| prominence pattern | accent_location, phrasing, variety |
| prosodic acoustic description | pitch_pattern, duration, intensity, measurement_method, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Prosody essential terms

A **prominence pattern** represents relative highlighting, stress and phrasing within an utterance. A **prosodic acoustic description** records properties of an identified signal, such as fundamental frequency in voiced intervals, duration and intensity. Perceived pitch is related to fundamental frequency but is not identical to it; prominence is not simply loudness or the highest pitch value. A proposed pitch accent and a measured frequency peak are different analytical claims.

#### Interface with Prosody worked interpretation

For a reply to *Who repaired the printer?*, an analyst might predict prominence on *Nina* in *Nina repaired the printer*. A recording could realize that prominence through a combination of pitch-related movement, timing, intensity and other cues. No specific contour or measurement follows from capitalizing NINA in a transcript. To test the proposed correspondence, preserve the question context, identify the token and compare annotated prominence with the actual signal, retaining uncertainty where the cues disagree.

#### Interface with Prosody assumptions and limits

The relation is schematic and potentially many-to-many, but its cardinality remains unspecified here. Acoustic cues, speakers and contexts need empirical investigation; an abstract prominence label does not predict numerical measurements.

#### Interface with Prosody evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Prosody evidence status

**Provisional.** This bridge is an authored synthesis; selected source contributions are identified in the Model evidence section. They do not establish the complete mapping, measurements of this example, independent review or learner outcomes.

Phrasing is grouping within an utterance. A phrase boundary need not contain silence; a disagreement between annotation and signal remains evidence to investigate. The [MIT tutorial record](../references/mit-2006-tobi-tutorial.md) supplies selected support for these distinctions without supplying measurements for this example.

## Evaluation and counterevidence
For a proposed phonetic claim, identify the token, speaker/variety, context, notation and observation. Compare repeated tokens rather than treating one production as a universal norm. If no recording exists, the correct output is a qualified prediction, not an acoustic finding.

A useful check: does /r/ necessarily mean a trill? No. In this package it is a broad rhotic convention; a more detailed phone description may use [ɹ]. The phonemic symbol does not specify every physical feature.

## Assumptions and limits
This is a foundational explanatory Model, not a complete General American inventory, a clinical assessment or a validated pronunciation course. Individual variation, mergers, connected-speech reduction and transcription choices require local qualification. Instrumental analysis and controlled perception experiments remain further work.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records selected articulation, transcription, connected-speech and aspiration passages, including their Canadian scope. The [IPA Reference](../references/international-phonetic-association-undated-ipa-chart.md) supports the chart categories. The [MIT tutorial record](../references/mit-2006-tobi-tutorial.md) supplies selected support for prominence, phrasing and physical cues. These sources do not supply measurements of the constructed examples. The new [Coleman record](../references/coleman-undated-speech-acoustics.md) supports source/filter distinctions, the [Praat record](../references/praat-undated-spectrogram-manual.md) supports spectrogram interpretation, and the [Flemming record](../references/flemming-2015-speech-perception.md) supports selected perceptual-cue distinctions. The comparisons and interface summaries are authored applications. Timing arithmetic is synthetic; no audio, source graphs or listener responses were measured.

## Related knowledge
[Representation levels](../concepts/representation-levels.md) distinguishes notation in more detail. [Consonant articulation](../concepts/consonant-articulation.md) and [vowel articulation](../concepts/vowel-articulation.md) expand feature descriptions. [Analyze sound realization](../methods/analyze-sound-realization.md) supplies a bounded investigation; [Phonology Phonetics interface](#interface-with-phonology) explains the mapping.
