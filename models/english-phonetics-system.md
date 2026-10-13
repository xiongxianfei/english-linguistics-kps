---
id: "english:model:english-phonetics-system"
type: "model"
version: "0.2.0"
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
This Model separates the physical production of speech, its measurable signal and the listener's interpretation. It explains the terms needed to describe a consonant or vowel, compare candidate realizations and recognize what cannot be inferred from spelling. New examples use the package's General American convention. Examples below are constructed; no recording or measurement is claimed.

## Purpose
Given a word or recording, specify what sort of evidence would justify a phonetic description. A broad dictionary form can start an investigation but cannot establish exactly what a speaker produced.

## Representation

| Component | Representation and function | Evidence needed |
|---|---|---|
| Articulation | Airflow, vocal-fold behavior and vocal-tract constrictions describe production | Observation or a justified articulatory analysis |
| Acoustics | A time-varying signal can be characterized by duration, periodicity and spectral structure | An identified recording and declared measurement procedure |
| Perception | Listeners classify sounds and perceive prominence under contextual conditions | Recorded responses or a stated perceptual judgment |
| Transcription | Selected properties are represented with symbols and diacritics | An explicit accent, level of detail and evidential basis |

These descriptions concern the same speech event but are not interchangeable. A symbol is not an acoustic measurement; an acoustic difference does not by itself prove that listeners use it contrastively.

## Essential distinctions
A consonant can be described by **place** of constriction, **manner** of airflow restriction and **laryngeal behavior**. For example, a bilabial stop involves closure at the lips. A fricative involves a constriction associated with turbulent airflow. Voicing concerns vocal-fold vibration, not the spelling of a letter.

Vowels are described using tongue height, frontness or backness, lip rounding and other relevant properties. These are a useful articulatory vocabulary, not instructions to assume that every speaker produces identical cardinal vowel positions. A diphthong changes quality within its syllabic nucleus; two vowel letters do not necessarily indicate two sounds.

Orthographic <pin>, broad phonemic /pɪn/, and an illustrative phonetic [pʰɪn] describe different things. The raised aspiration mark indicates a possible realization detail, not an extra ordinary /h/ segment. Broad versus narrow describes detail; a phonetic transcription can itself be broad. Square brackets alone do not make a transcription observed data.

Fundamental frequency describes periodicity in voiced portions of a signal; perceived pitch is related but not identical to it. Formants are resonances relevant to vowel description. Duration and intensity can contribute to prominence, but no single measure is a universal stress detector.

## Worked example
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
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) records limited transcription and aspiration passages. The [IPA Reference](../references/international-phonetic-association-undated-ipa-chart.md) supports symbol conventions, not token-specific measurements. The acoustic procedure above is an authored outline, not a newly performed experiment.

## Related knowledge
[Representation levels](../concepts/representation-levels.md) distinguishes notation in more detail. [Consonant articulation](../concepts/consonant-articulation.md) and [vowel articulation](../concepts/vowel-articulation.md) expand feature descriptions. [Analyze sound realization](../methods/analyze-sound-realization.md) supplies a bounded investigation; [Phonology Phonetics interface](phonology-phonetics-interface.md) explains the mapping.
