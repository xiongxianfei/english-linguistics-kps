---
id: "english:syntax-prosody-interface"
aliases: []
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["syntax","prosody","syntax:constituency-and-dependency","prosody:prosodic-phrasing"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Syntactic structure constrains prosodic phrasing, but prosodic boundaries need not reproduce every syntactic constituent boundary one for one.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:constituency","layer":"document"},{"predicate":"uses","target":"english:prosody","layer":"document"}]
sources: []
interface: {"source_domain":"syntax","source_representation":"syntactic-structure","predicate":"constrains","target_domain":"prosody","target_representation":"prosodic-phrasing","claim":"key-takeaway","scope":"Spoken English phrasing under the assumptions stated in this Model.","cardinality":"many-to-many"}
---

# Syntax Prosody interface

## Key takeaway
Syntactic structure constrains prosodic phrasing, but prosodic boundaries need not reproduce every syntactic constituent boundary one for one.

## Summary
This interface relates clause and phrase structure to phrasing and prominence in spoken English. It treats syntax and prosody as distinct representations linked by defeasible, construction- and context-sensitive correspondences.

## Purpose
Support analyses in which constituent structure informs possible phrasing without inferring a syntactic tree directly from pauses or punctuation.

## Representation
| Syntactic representation | Mapping | Prosodic representation |
|---|---|---|
| constituents, heads, dependencies, clause boundaries | constrains | prosodic phrases, boundary strength, prominence distribution |

## Worked interpretation
A relative clause may form a prosodic unit in one speaking style, while a short integrated relative may be phrased with surrounding material in another. A pause can reflect planning or emphasis rather than a unique syntactic boundary.

## Assumptions and limits
Prosodic phrasing depends on speech rate, information structure, construction and variety. The model is not an automatic parser and does not claim direct isomorphism.

## Evaluation and counterevidence
Annotate syntax and prosody independently, then compare proposed correspondences. Use recordings for token-specific claims and retain mismatches rather than forcing identical trees.

## Evidence status
**Provisional.** Claim-level source review and measured examples are pending.

## Related knowledge
- [Constituency](../concepts/constituency.md)
- [Clause architecture](../concepts/clause-architecture.md)
- [Prosody and intonation](../concepts/prosody.md)
- [Annotate and measure prosody](../methods/annotate-and-measure-prosody.md)
