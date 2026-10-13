# Phonology Phonetics interface

## Key takeaway
Phonological representations constrain possible phonetic analyses without uniquely specifying an observed speech token.

## Summary
Phonological representations constrain possible phonetic analyses without uniquely specifying an observed speech token. This KPS 12 bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| phonological form | segments, syllables, stress |
| phonetic realization | transcription_level, context, observed_or_predicted, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Worked interpretation
For the existing illustrative pin /pɪn/ example, [pʰɪn] is a possible context-sensitive phonetic description. It is not a measured token. The spelling, broad form and phonetic description must remain separate.

## Assumptions and limits
A variety, stress and segmental context must be stated. This bridge does not assert a universal phonetics–phonology boundary or an executable production model. No audio has been recorded or inspected during migration.

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
- [representation levels](representation-levels.md)
- [phone phoneme and allophone](phone-phoneme-and-allophone.md)
- [phonological word model](phonological-word-model.md)
- [realization varies with environment](realization-varies-with-environment.md)
