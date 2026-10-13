---
id: "english:syntax-semantics-interface"
aliases: ["english:model:syntax-semantics-interface"]
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["semantics","semantics:compositional-meaning","syntax","syntax:construction-mappings"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Construction-sensitive mappings connect grammatical functions with semantic roles without identifying the two dimensions.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:semantic-role","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:object-and-pp-complement","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:valency-and-argument-structure","layer":"document","expected_role":"concept"}]
sources: []
interface: {"source_domain":"syntax","source_representation":"clause-functions","predicate":"maps-to","target_domain":"semantics","target_representation":"participant-roles","claim":"key-takeaway","scope":"The working analysis, context and variety limits in knowledge/syntax-semantics-interface.md; not a neural processing claim.","cardinality":"unspecified"}
---


# Syntax Semantics interface

## Key takeaway
Construction-sensitive mappings connect grammatical functions with semantic roles without identifying the two dimensions.

## Summary
Construction-sensitive mappings connect grammatical functions with semantic roles without identifying the two dimensions. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

Construction-sensitive mappings connect grammatical functions with semantic roles without identifying the two dimensions.

## Representation

| Construction | Giver | Recipient | Theme |
|---|---|---|---|
| Leo gave Maya a prize | Subject | Indirect Object | Direct Object |
| Leo gave a prize to Maya | Subject | NP inside to-PP | Direct Object |
| Maya was given a prize by Leo | NP inside by-PP | Subject | Retained Object |

## Worked interpretation

A passive can preserve the basic participant relations while changing grammatical functions. A causative alternation such as "The glass broke / Leo broke the glass" can add a Causer instead. A psych predicate can give a Stimulus Subject and Experiencer Object without passive morphology.

## Assumptions and limits

Dative alternation has lexical, semantic and discourse restrictions; the table does not establish complete synonymy. Role inventories vary. The mapping is analytical rather than evidence of a particular neural transfer operation.

## Evaluation and counterevidence

Ask which participants are added, omitted, implicit or redistributed. A changed function alone does not necessarily add a role. Keep explicit versus inferred participants separate in every example.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Related knowledge

- [Semantic role](../concepts/semantic-role.md) provides a related distinction used in the local explanation.
- [Object and PP complement](../concepts/object-and-pp-complement.md) provides a related distinction used in the local explanation.
- [Valency and argument structure](../concepts/valency-and-argument-structure.md) provides a related distinction used in the local explanation.
