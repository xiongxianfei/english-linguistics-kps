---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# KPS compatibility

## Key takeaway
English content version, upstream Core version and KPS document language are separate declarations.

## Summary
English package 0.2.0 follows the KPS 9.x Markdown contract inspected in upstream Core 11.0.0. The copied checker is the proposed upstream 9.2.0 revision, pinned by commit and blob rather than presented as an official release. Closed experimental KPS 12 proposals are not the contract for this PR.

## Upstream basis
The inspected [upstream revision](https://github.com/xiongxianfei/knowledge-practice-system/tree/4b6d3ed7a660416e698ac7fbd99c8360a00198e6) is 4b6d3ed7a660416e698ac7fbd99c8360a00198e6. The local validate.py exactly matches its Git blob b391e28d6c64b3848ea426268c8cce65997c3074. upstream-lock.json records this pin and the earlier baseline. The copied regression suite is removed. The matching full suite remains in Core at `internal/tests/test_validate.py` at the pinned commit. Local checks verify the checker against the lock, validate this package and exercise domain examples and review declarations.

## Content preservation
All 110 knowledge items from main commit 034f21daa6946b744b367515cb4dbfc6a6720c4f are retained. Of those, 104 files are byte-identical. The four Practices retain their explanations and stage titles while existing action lines become numbered for checker 9.1.0; two Practices also receive a current Reference link label. Two other items receive the same label correction without changing their claims. The six revised object versions advance accordingly. Twenty additional Models supply ten subsystem explanations, nine interfaces and a shared worked case. Original IDs and paths remain usable. No source store is renamed because main already uses references/.

## Deliberate simplification
The optional knowledge-graph.json export is removed; Markdown and ordinary links suffice. No entities/, ontology/, sources/, views/, generated/, sequences/ or duplicated legacy/ repository is added. Git history retains earlier content. Legacy global stage metadata in preserved notes is ignored by navigation; local Practice stages remain meaningful operations.

## Limits
Compatibility does not mean scientific review or complete adoption of the upstream Core's separate curation policy. No automatic merge, tag, release, visualization dependency or remote build service is introduced.

## Flexible Model adoption

This task explicitly adopts the Core commit pinned above. The checker is byte-identical to Core 9.2.0, and publication.json declares that tool floor. Morphology uses introductory prose and linked Contents. The domain checker and catalog accept that opening, and the former fixed-heading assertion is replaced by a check that the actual domain tools support flexible Model prose. Evidence declarations, review provenance, ten subsystem identities, link integrity and constructed linguistic checks remain. Other Models keep their useful existing sections; no sibling domain is upgraded.
