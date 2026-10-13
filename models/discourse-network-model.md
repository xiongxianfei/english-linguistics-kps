---
id: "english:discourse-network-model"
aliases: ["english:model:discourse-network-model"]
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["discourse","discourse:discourse-relations"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "AI-assisted authored synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"A discourse model tracks referents and relations while keeping textual order distinct from event order and causal direction.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:discourse-referent","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:discourse-relation","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:contrast-and-concession","layer":"document","expected_role":"concept"},{"predicate":"uses","target":"english:temporal-causal-and-evidential-relations","layer":"document","expected_role":"concept"}]
sources: [{"id":"source:mann-taboada-undated-rst-introduction","relation":"context-only"}]
---


# Discourse network model

## Key takeaway
A discourse model tracks referents and relations while keeping textual order distinct from event order and causal direction.

## Summary
A discourse model tracks referents and relations while keeping textual order distinct from event order and causal direction. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

A discourse model tracks referents and relations while keeping textual order distinct from event order and causal direction.

## Representation

```text
roads icy --concessive obstacle--> Anna sends reports
Maya prepares reports --earlier than--> Anna sends reports
Leo needs reports --reason offered for--> Leo thanks Anna

He -> Leo; her -> Anna (preferred); them -> reports
```

## Worked interpretation

The reference of her is preferential, not logically forced by the string; a context could make Maya relevant. The icy-road relation defeats an expectation rather than asserting a contradiction. The thanks clause relates to the need for reports without proving every unstated motive.

## Assumptions and limits

This is a small authored relation network, not a full RST or SDRT implementation. No single relation inventory is declared universal. The supplied examples are constructed, not annotated natural discourse.

## Evaluation and counterevidence

For each edge, identify textual units, relation direction, connective if present, and contextual evidence. A graph of arrows without these annotations does not establish coherence.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Selected source contributions are recorded below. They do not verify every example, theoretical choice or generalization in this object. Inspect the linked record's access extent and nonclaims.

- [Rhetorical Structure Theory website introduction and relation definitions](../sources/mann-taboada-undated-rst-introduction.md#relations) — support is limited to the named section in that record.

## Related knowledge

- [Discourse referent](../concepts/discourse-referent.md) provides a related distinction used in the local explanation.
- [Discourse relation](../concepts/discourse-relation.md) provides a related distinction used in the local explanation.
- [Contrast and concession](../concepts/contrast-and-concession.md) provides a related distinction used in the local explanation.
- [Temporal causal and evidential relations](../concepts/temporal-causal-and-evidential-relations.md) provides a related distinction used in the local explanation.
