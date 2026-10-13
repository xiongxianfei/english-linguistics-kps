---
id: "english:nested-clause-model"
aliases: ["english:model:nested-clause-model"]
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["syntax","syntax:clause-architecture"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"A clause analysis records complete constituent spans and their nesting rather than counting verb-looking tokens.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:clause-architecture","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:relative-clause","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:auxiliary-chain","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:head-and-dependent","layer":"document","expected_role":"concept"}]
sources: []
---


# Nested clause model

## Key takeaway
A clause analysis records complete constituent spans and their nesting rather than counting verb-looking tokens.

## Summary
A clause analysis records complete constituent spans and their nesting rather than counting verb-looking tokens. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

A clause analysis records complete constituent spans and their nesting rather than counting verb-looking tokens.

## Representation

```text
[Clause
  [Adverbial Although the roads were icy]
  [NP Anna]
  [VP sent
      [NP the reports [Relative that Maya had prepared __]]
      [PP to [NP Leo]]]]
[Clause He [VP thanked her [Adverbial because he needed them]]]
```

## Worked interpretation

The first main clause contains both the concessive adjunct and a relative inside its Object NP. The to-PP attaches to SEND, not PREPARE in the intended reading. Across both sentences the working model counts two main clauses, two finite adverbial clauses and one finite relative clause. Had prepared is one auxiliary chain.

## Assumptions and limits

The flat VP display is a descriptive simplification. The treatment of although/because as clause markers and the auxiliary-chain clause count are declared choices. A CP/TP analysis can differ without changing the need to record nesting.

## Evaluation and counterevidence

Check that every token has a place and that constituent intervals are nested or disjoint, not partially crossing. The companion constructed fixture records token spans. It is a regression target for this analysis, not a corpus annotation standard.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Related knowledge

- [Clause architecture](../concepts/clause-architecture.md) provides a related distinction used in the local explanation.
- [Relative clause](../concepts/relative-clause.md) provides a related distinction used in the local explanation.
- [Auxiliary chain](../concepts/auxiliary-chain.md) provides a related distinction used in the local explanation.
- [Head and dependent](../concepts/head-and-dependent.md) provides a related distinction used in the local explanation.
