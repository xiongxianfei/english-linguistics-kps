---
id: "english:model:phonology-prosody-interface"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["phonology", "prosody"]
evidence_status: "provisional"
source_status: "external-support-pending"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: []
interface_domains: ["phonology", "prosody"]
uses_concepts: ["english:concept:syllable-structure", "english:concept:stress", "english:concept:phonotactics", "english:concept:prosody"]
---

# Phonology Prosody interface

## Key takeaway
Syllable organization and lexical stress constrain prosodic realization, but do not uniquely determine phrasal prominence or grouping.

## Summary
Syllable organization and lexical stress constrain prosodic realization, but do not uniquely determine phrasal prominence or grouping. This note supplies a working analysis, a diagnostic and explicit limits.

## Purpose

Explain a bounded correspondence between syllable and lexical-stress organization and phrasal prominence and prosodic grouping. This is a descriptive working Model, not a claim about a universal processing pipeline.

## Representation

Keep a segment string and syllable parse, lexical stress positions, proposed phrasal accents, and phrase-edge annotations in different fields. A word can contain a lexically stressed syllable even when that word does not receive the strongest prominence in an utterance. Prosody is independently browsable here but overlaps phonological analysis; the domain boundary is an organizing convention.

## Worked analysis

In a constructed “The students repaired the printers,” lexical word forms remain the same across a who-question and a what-question context. A proposed accent can shift from students to printers, while each word retains its lexical stress organization. Do not rewrite the lexical entry to encode every sentence-specific accent.

## Evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

## Assumptions and limits

This does not assign a complete metrical or tonal analysis. Stress, reduction, syllabification and phrasing vary with variety, rate and theoretical assumptions. No recorded production, corpus sample or independent expert review is supplied for this bridge Model.

## Evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

## Related knowledge

- [Syllable structure](../concepts/syllable-structure.md)
- [Stress](../concepts/stress.md)
- [Phonotactics](../concepts/phonotactics.md)
- [Prosody and intonation](../concepts/prosody.md)
- [Focus domain and alternatives](../concepts/focus-topic-and-qud.md)
