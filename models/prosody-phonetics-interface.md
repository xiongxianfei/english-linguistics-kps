---
id: "english:model:prosody-phonetics-interface"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["phonetics", "prosody"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: []
interface_domains: ["phonetics", "prosody"]
uses_concepts: ["english:concept:prosody", "english:concept:stress"]
uses_models: ["english:model:focus-prosody-interface"]
uses_methods: ["english:method:analyze-sound-realization"]
---

# Prosody Phonetics interface

## Key takeaway
A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization.

## Summary
A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization. This KPS bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| prominence pattern | accent_location, phrasing, variety |
| prosodic acoustic description | pitch_pattern, duration, intensity, measurement_method, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Essential terms
A **prominence pattern** represents relative highlighting, stress and phrasing within an utterance. A **prosodic acoustic description** records properties of an identified signal, such as fundamental frequency in voiced intervals, duration and intensity. Perceived pitch is related to fundamental frequency but is not identical to it; prominence is not simply loudness or the highest pitch value. A proposed pitch accent and a measured frequency peak are different analytical claims.

## Worked interpretation
For a reply to *Who repaired the printer?*, an analyst might predict prominence on *Nina* in *Nina repaired the printer*. A recording could realize that prominence through a combination of pitch-related movement, timing, intensity and other cues. No specific contour or measurement follows from capitalizing NINA in a transcript. To test the proposed correspondence, preserve the question context, identify the token and compare annotated prominence with the actual signal, retaining uncertainty where the cues disagree.

## Assumptions and limits
The relation is schematic and potentially many-to-many, but its cardinality remains unspecified here. Acoustic cues, speakers and contexts need empirical investigation; an abstract prominence label does not predict numerical measurements.

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
- [prosody](../concepts/prosody.md)
- [stress](../concepts/stress.md)
- [focus prosody interface](focus-prosody-interface.md)
- [analyze sound realization](../methods/analyze-sound-realization.md)
