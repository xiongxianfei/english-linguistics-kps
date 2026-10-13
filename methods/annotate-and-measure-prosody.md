---
id: "english:annotate-and-measure-prosody"
aliases: []
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["prosody","prosody:prosodic-annotation-and-measurement","phonetics","phonetics:acoustic-phonetics"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"A prosodic investigation should keep interpretive labels, annotation decisions and acoustic measurements separate while linking each result to an identifiable recording and context.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:prosody","layer":"document"},{"predicate":"uses","target":"english:analyze-sound-realization","layer":"document"},{"predicate":"tests","target":"english:prosody-phonetics-interface","layer":"operational","claim":"key-takeaway"}]
sources: []
---

# Annotate and measure prosody

## Key takeaway
A prosodic investigation should keep interpretive labels, annotation decisions and acoustic measurements separate while linking each result to an identifiable recording and context.

## Summary
This Method provides a bounded workflow for examining phrasing, prominence and intonation in recorded speech. It does not make capitalization, punctuation or predicted IPA count as acoustic evidence.

## Objective
Produce a revisable record connecting an utterance, context, prosodic annotation and selected measurements without treating any one cue as a complete analysis.

## Inputs and prerequisites
An identifiable recording with permission to analyze it; its transcript, speaker/variety information when available, discourse context, and a stated annotation question. Basic familiarity with stress, prosodic phrasing and the distinction between pitch, duration and intensity is required.

## Rationale
Prosodic categories are analytical, while measurements describe aspects of a signal. Separating those layers prevents an assumed prominence label from being reported as an observation.

## Procedure
1. Preserve the recording identifier, time span, transcript and relevant context.
2. Mark uncertain word and phrase boundaries before assigning prosodic labels.
3. State the annotation system or plain-language convention being used.
4. Propose prominent syllables, phrasing and pitch events, retaining alternatives where needed.
5. Inspect the signal and record only measurements relevant to the question, including method and units.
6. Compare the measurements with competing annotations rather than selecting only confirming cues.
7. Record speaker, variety, recording quality and segmentation limitations.
8. Separate observations, derived measurements and interpretive conclusions in the report.

## Expected effect
The output is an auditable annotation-and-measurement record that can be rechecked against the recording. It is not a validated automatic intonation analysis or evidence that one cue uniquely realizes one category.

## Validation and counterevidence
Another analyst should be able to locate the same interval and reproduce the stated measurement procedure. Disagreement over boundaries or labels must remain visible. Stop short of token-specific claims when the recording or measurement basis is unavailable.

## Limits
Prosodic annotation systems make theoretical and practical choices. Small or noisy recordings cannot establish population-level distributions, and speaker normalization may be necessary for comparison.

## Evidence status
**Provisional.** The procedure is proposed for transparent analysis; its reliability and teaching effectiveness have not been independently validated.

## Related knowledge
- [Prosody and intonation](../concepts/prosody.md)
- [Stress](../concepts/stress.md)
- [Analyze sound realization](analyze-sound-realization.md)
- [Prosody Phonetics interface](../models/prosody-phonetics-interface.md)
