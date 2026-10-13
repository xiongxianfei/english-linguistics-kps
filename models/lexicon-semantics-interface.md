---
id: "english:model:lexicon-semantics-interface"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["lexicon", "semantics"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: []
interface_domains: ["lexicon", "semantics"]
uses_concepts: ["english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:semantic-predicate", "english:concept:lexical-selection"]
---

# Lexicon Semantics interface

## Key takeaway
A sense-specific lexical entry constrains an interpretation without making a spelling identify one context-independent predicate.

## Summary
A sense-specific lexical entry constrains an interpretation without making a spelling identify one context-independent predicate. This KPS bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| lexical sense entry | lexeme, sense, selection |
| predicate interpretation | predicate, arguments, contextual_restrictions |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Essential terms
A **lexical sense entry** records a word's category, a conventional meaning contribution and relevant combinatorial restrictions. A **predicate interpretation** characterizes a property, relation or situation and its participants under the selected reading. Choosing a sense is not merely choosing a spelling. Compositional structure and context constrain how the contribution combines with other expressions; this bridge does not reduce complete sentence meaning to a dictionary gloss.

## Worked interpretation
In *Maya runs every morning*, a locomotion use of RUN characterizes an activity involving Maya. In *Maya runs a company*, a management use relates Maya to the company she manages. Keeping the same spelling while selecting the locomotion contribution for the second sentence would fail to capture its ordinary intended reading. A constructional or coercion account can distribute the explanation differently; the record should state which analysis is being used instead of assuming one location for all meaning.

## Assumptions and limits
The location of lexical and constructional information differs among theories. This bridge is schematic and does not establish an exhaustive sense inventory, an automatic disambiguator or full claim-level support.

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
- [lexical entry](../concepts/lexical-entry.md)
- [sense and lexical ambiguity](../concepts/sense-and-lexical-ambiguity.md)
- [semantic predicate](../concepts/semantic-predicate.md)
- [lexical selection](../concepts/lexical-selection.md)
