---
id: "english:model:phonology-phonetics-interface"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["phonetics", "phonology"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: []
interface_domains: ["phonetics", "phonology"]
uses_concepts: ["english:concept:representation-levels", "english:concept:phone-phoneme-and-allophone"]
uses_models: ["english:model:phonological-word-model"]
uses_principles: ["english:principle:realization-varies-with-environment"]
---

# Phonology Phonetics interface

## Key takeaway
Phonological representations constrain possible phonetic analyses without uniquely specifying an observed speech token.

## Summary
Phonological representations constrain possible phonetic analyses without uniquely specifying an observed speech token. This KPS bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| phonological form | segments, syllables, stress |
| phonetic realization | transcription_level, context, observed_or_predicted, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Essential terms
A **phonological form** describes language-specific categories and structural positions. A **phonetic realization** describes speech production or the resulting sound in a particular context. Slashes conventionally mark a phonemic analysis; square brackets mark a phonetic description. Neither notation by itself identifies a recording. Stress, neighboring sounds, rate and speaker variety can condition realization, so a phonological string need not determine one narrow transcription.

## Worked interpretation
Broad /pɪn/ and /spɪn/ both contain /p/. A stressed onset in *pin* can be aspirated, represented schematically as [pʰ], while the post-/s/ realization in *spin* is commonly less aspirated. The phonological environment helps explain a predicted difference without changing /p/ into a different phoneme merely because the phones differ. No token has been recorded here. To claim an observed difference, identify recordings and the criteria used to inspect the realization.

## Assumptions and limits
A variety, stress and segmental context must be stated. This bridge does not assert a universal phonetics–phonology boundary or an executable production model. No audio has been recorded or inspected during migration.

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
- [representation levels](../concepts/representation-levels.md)
- [phone phoneme and allophone](../concepts/phone-phoneme-and-allophone.md)
- [phonological word model](phonological-word-model.md)
- [realization varies with environment](../principles/realization-varies-with-environment.md)
