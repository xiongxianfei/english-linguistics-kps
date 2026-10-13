---
id: "english:method:analyze-sound-realization"
type: "method"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
stages: [7]
perspectives: ["interfaces-and-integration"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics","english:reference:sounds-american-undated-chart-and-terms","english:reference:tophonetics-undated-english-transcription","english:reference:international-phonetic-association-undated-interactive-chart"]
uses_concepts: ["english:concept:representation-levels", "english:concept:allomorphy", "english:concept:phone-phoneme-and-allophone", "english:concept:consonant-articulation", "english:concept:connected-speech"]
---

# Analyze sound realization

## Key takeaway
Distinguish morphological exponents, phonological categories and observed phonetic realizations.

## Summary
Distinguish morphological exponents, phonological categories and observed phonetic realizations. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Objective

Distinguish morphological exponents, phonological categories and observed phonetic realizations.

## Inputs and prerequisites

The word or utterance and its intended sense, a declared accent and transcription convention (default: General American), and explicit source/provenance information. A recording is required for token-specific acoustic claims. A spelling alone supports only a predicted pronunciation analysis.

## Rationale

Spelling can hide the conditioning sound, and an allomorph can contain several phonemes. Keeping levels separate avoids treating the plural morpheme as a phoneme or aspiration as a new word.

## Procedure

1. State spelling, intended lexeme and grammatical feature.
2. Default to **General American** unless an alternate accent is explicitly requested. Find a candidate broad word form, for example using the **American** option at toPhonetics. Check lexical sense, homographs, alternate readings and the weak-form setting; retain uncertainty and cross-check disputed forms with an independent dictionary.
3. For regular inflection, identify the final sound and select the relevant exponent.
4. Annotate syllables, lexical stress and relevant sound environment. Use the official IPA chart for symbol meaning, and Sounds American as a teaching reference for articulatory gestures; neither alone establishes the lexical pronunciation.
5. Predict connected-speech processes only with explicit conditions.
6. If audio exists, distinguish measured or heard features from predicted ones; record uncertainty. Cite each source's actual inspected extent, and do not copy third-party charts, videos, recordings or transcription databases into the repository.

## General American lookup procedure

The default convention is specified in [PRONUNCIATION](../docs/PRONUNCIATION.md). A broad /r/ is a language-analysis shorthand for an American rhotic, not an observed IPA trill. toPhonetics describes its American text outputs as phonemic, not narrow phone-by-phone acoustics; Sounds American is pedagogical articulation guidance; the interactive IPA chart is an inventory of phone symbols. If sources disagree, document the accent, conventions, morphological form, lexical sense and unresolved evidence, rather than choosing whichever symbol looks most precise.

## Worked example

WATCH ends in /tʃ/, so its regular plural has a syllabic ending conventionally /ɪz/. LAUGH ends in /f/, so laughs has /s/ and laughed has /t/. In the supplied English aspiration pattern /p/ has [pʰ] in a stressed onset such as pin, but [p] after /s/ in spin.

## Expected effect

The output is an explicit, revisable analysis with its assumptions and uncertainties exposed. This is a design expectation, not a measured learning outcome.

## Validation and counterevidence

Check the special /t,d/ or sibilant cases before the general voicing cases. Do not apply regular suffix functions to irregular stems. Without a recording, mark narrow phonetic transcriptions as illustrative rather than observed.

## Limits

Accent, stress, rate and morphology can affect realization. The accompanying functions implement selected regular patterns only, not pronunciation from arbitrary spelling.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this object. Inspect the linked record's access extent and nonclaims.

- [Essentials of Linguistics, first edition, McMaster University](../references/anderson-2018-essentials-of-linguistics.md#allomorphs) — support is limited to the named section in that record.

- [Essentials of Linguistics, first edition, McMaster University](../references/anderson-2018-essentials-of-linguistics.md#aspiration) — support is limited to the named section in that record.

## Additional source records

- [Sounds American chart and terms](../references/sounds-american-undated-chart-and-terms.md#located-contributions) identifies an American instructional articulation resource, not a verified measurement.
- [toPhonetics transcription tool and FAQ](../references/tophonetics-undated-english-transcription.md#located-contributions) establishes tool options and its stated broad convention, not output accuracy for any particular word.
- [Interactive IPA chart](../references/international-phonetic-association-undated-interactive-chart.md#located-contributions) identifies a general IPA symbol resource, not a fixed English inventory.

## Related knowledge

- [Orthography phonology and phonetics](../concepts/representation-levels.md) provides a related distinction used in the local explanation.
- [Allomorphy](../concepts/allomorphy.md) provides a related distinction used in the local explanation.
- [Phone phoneme and allophone](../concepts/phone-phoneme-and-allophone.md) provides a related distinction used in the local explanation.
- [Consonant articulation](../concepts/consonant-articulation.md) provides a related distinction used in the local explanation.
- [Connected speech](../concepts/connected-speech.md) provides a related distinction used in the local explanation.
