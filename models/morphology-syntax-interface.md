---
id: "english:model:morphology-syntax-interface"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["morphology", "syntax"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: []
interface_domains: ["morphology", "syntax"]
uses_concepts: ["english:concept:inflection", "english:concept:paradigm-and-syncretism", "english:concept:finiteness", "english:concept:auxiliary-chain"]
---

# Morphology Syntax interface

## Key takeaway
Word-form features and syntactic distributions must be represented separately even when an analysis connects them through agreement or finiteness.

## Summary
Word-form features and syntactic distributions must be represented separately even when an analysis connects them through agreement or finiteness. This KPS bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| grammatical word features | lexeme, number, person, tense, word_form |
| agreement and finiteness pattern | construction, controller, agreement_form, finiteness |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Essential terms
**Word-form features** such as number, person and tense describe grammatical distinctions realized by forms. **Agreement** is a correspondence between a controller and a form in a construction, not agreement between adjacent written words. **Finiteness** concerns clause licensing and verb form, not whether an event occurs now. **Syncretism** means that one form realizes more than one feature combination, so a feature distinction need not produce an overt spelling contrast.

## Worked interpretation
In *This report is ready* and *These reports are ready*, singular versus plural nominal features correspond to *is* versus *are* in the illustrated construction. The head of *the report near the windows* is still singular REPORT, so *The report near the windows is ready* shows why the nearest plural noun is not a sufficient agreement rule. The examples are constructed descriptive contrasts, not a universal agreement algorithm; collective nouns and other constructions require variety-specific qualifications.

## Assumptions and limits
Agreement varies by construction and variety; syncretism can conceal feature differences. This is a proposed bridge based on existing distinctions, with external claim support pending.

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
- [inflection](../concepts/inflection.md)
- [paradigm and syncretism](../concepts/paradigm-and-syncretism.md)
- [finiteness](../concepts/finiteness.md)
- [auxiliary chain](../concepts/auxiliary-chain.md)
