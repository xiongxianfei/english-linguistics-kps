---
id: "english:lexicon-morphology-interface"
aliases: []
version: "1.0.0-draft.1"
language: "KPS 12.x"
status: "draft"
domains: ["lexicon","morphology","lexicon:lexical-identity","morphology:word-formation"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
claims: [{"id":"key-takeaway","statement":"Lexical entries and morphological structure constrain one another without reducing every word form or derived word to an independently listed spelling.","scope":"As stated and limited in this file.","evidence_status":"provisional"}]
relations: [{"predicate":"uses","target":"english:lexical-entry","layer":"document"},{"predicate":"uses","target":"english:derivation","layer":"document"}]
sources: []
interface: {"source_domain":"lexicon","source_representation":"lexical-entry","predicate":"constrains","target_domain":"morphology","target_representation":"morphological-structure","claim":"key-takeaway","scope":"English lexical and morphological analyses under the assumptions stated in this Model.","cardinality":"many-to-many"}
---

# Lexicon Morphology interface

## Key takeaway
Lexical entries and morphological structure constrain one another without reducing every word form or derived word to an independently listed spelling.

## Summary
This interface connects lexical identity and stored information with inflectional and word-formation analyses. It preserves a distinction between a lexeme, its grammatical word forms, productive patterns and lexicalized outcomes.

## Purpose
Represent how lexical entries supply bases and idiosyncratic information while morphology builds or relates forms under language-specific patterns.

## Representation
| Lexical representation | Mapping | Morphological representation |
|---|---|---|
| lexeme, sense, stored stem/allomorph, listed restrictions | constrains | roots, bases, affixes, features and word-formation structure |

## Worked interpretation
*Writer* can be related to *write* through a productive derivational pattern, while its conventional senses and usage still belong to a lexical entry. The past form *wrote* requires stored or otherwise lexically specific information that a regular suffix rule alone does not predict.

## Assumptions and limits
Theories disagree about how much structure is stored, constructed or distributed across a lexicon and grammar. The bridge is descriptive and does not choose a universal architecture.

## Evaluation and counterevidence
For a proposed analysis, identify what is predictable, what is item-specific and what evidence distinguishes a productive pattern from lexical storage. Avoid inferring mental storage directly from orthographic listing.

## Evidence status
**Provisional.** Claim-level external support and competing-framework review are pending.

## Related knowledge
- [Lexical entry](../concepts/lexical-entry.md)
- [Lexeme and word form](../concepts/lexeme-and-word-form.md)
- [Derivation](../concepts/derivation.md)
- [Productivity and lexicalization](../concepts/productivity-and-lexicalization.md)
