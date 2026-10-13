---
id: "english:lexicon-syntax-interface"
aliases: ["english:model:lexicon-syntax-interface"]
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["lexicon","lexicon:argument-frames","syntax","syntax:construction-mappings"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Lexical senses and constructions constrain the category and form of licensed syntactic complements.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:lexical-selection","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:head-and-dependent","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:object-and-pp-complement","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:valency-and-argument-structure","layer":"document","expected_role":"concept"}]
sources: []
interface: {"source_domain":"lexicon","source_representation":"lexical-selection-frame","predicate":"constrains","target_domain":"syntax","target_representation":"syntactic-complement-structure","claim":"key-takeaway","scope":"The working analysis, context and variety limits in knowledge/lexicon-syntax-interface.md; not a neural processing claim.","cardinality":"unspecified"}
---


# Lexicon Syntax interface

## Key takeaway
Lexical senses and constructions constrain the category and form of licensed syntactic complements.

## Summary
Lexical senses and constructions constrain the category and form of licensed syntactic complements. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

Lexical senses and constructions constrain the category and form of licensed syntactic complements.

## Representation

| Lexical sense | Working frame | Local distinctions |
|---|---|---|
| DEPEND dependence | Subject + V + on-PP | NP inside PP complements ON |
| DISCUSS transitive | Subject + V + NP | NP is Direct Object |
| PUT placement | Subject + V + NP + location complement | Location is not another Object |
| RUN management | Subject + V + NP | Different from locomotion use |

## Worked interpretation

For "The result depends on the weather", on the weather is a PP complement of DEPEND; the weather is an NP complement of ON. The grammar is not a generic SVO template followed by an unrelated lexical pass. Selection information participates in grammatical licensing.

## Assumptions and limits

The frames are sense-specific working descriptions. Constructional theories may locate some information outside an item-specific entry; dialectal data can change the relevant permitted forms.

## Evaluation and counterevidence

Compare attested frames, accepted omission and meaning shifts. Count semantic arguments separately from overt NP objects. A frame must explain local hierarchy rather than infer functions from participant importance.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Related knowledge

- [Lexical selection](../concepts/lexical-selection.md) provides a related distinction used in the local explanation.
- [Head and dependent](../concepts/head-and-dependent.md) provides a related distinction used in the local explanation.
- [Object and PP complement](../concepts/object-and-pp-complement.md) provides a related distinction used in the local explanation.
- [Valency and argument structure](../concepts/valency-and-argument-structure.md) provides a related distinction used in the local explanation.
