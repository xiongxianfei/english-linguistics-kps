---
id: "english:prosody-phonetics-interface"
aliases: []
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["phonetics","prosody"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "KPS 12 authored bridge synthesis; constructed illustration; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:prosody","layer":"document"},{"predicate":"uses","target":"english:stress","layer":"document"},{"predicate":"uses","target":"english:focus-prosody-interface","layer":"document"},{"predicate":"uses","target":"english:analyze-sound-realization","layer":"document"}]
sources: []
interface: {"source_domain":"prosody","source_representation":"prominence-pattern","predicate":"constrains","target_domain":"phonetics","target_representation":"prosodic-acoustic-description","claim":"key-takeaway","scope":"The working analysis, context and variety limits in knowledge/prosody-phonetics-interface.md; not a neural processing claim.","cardinality":"unspecified"}
---

# Prosody Phonetics interface

## Key takeaway
A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization.

## Summary
A prosodic prominence analysis must be distinguished from the phonetic measurements used to investigate its realization. This KPS 12 bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| prominence pattern | accent_location, phrasing, variety |
| prosodic acoustic description | pitch_pattern, duration, intensity, measurement_method, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Worked interpretation
The existing Nina repaired the PRINTER illustration uses capitals to mark a proposed prominence pattern. Capitals contain no measured fundamental frequency, duration or intensity values.

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
