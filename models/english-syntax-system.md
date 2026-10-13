---
id: "english:model:english-syntax-system"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["syntax"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:category-and-function", "english:concept:constituency", "english:concept:head-and-dependent", "english:concept:complement-and-modifier", "english:concept:finiteness", "english:concept:relative-clause"]
uses_models: ["english:model:lexicon-syntax-interface", "english:model:morphology-syntax-interface", "english:model:syntax-semantics-interface", "english:model:syntax-prosody-interface"]
system_domain: "syntax"
---

# English syntax system

## Key takeaway
Syntax organizes categories, constituent structure, dependencies and grammatical functions; word order alone does not specify the whole analysis.

## Summary
This Model explains how phrases and clauses are assembled and how local grammatical relations are identified. It distinguishes categories from functions, complements from modifiers and finite from nonfinite clauses. It includes a complete bracketed example and a procedure for testing the proposed grouping. The working notation uses NP and a descriptive Subject/Predicate analysis; other frameworks are legitimate alternatives.

## Purpose
Given an expression and intended reading, identify the full spans that behave as units, their heads and their local relations. The goal is a revisable structural analysis, not assigning labels to isolated words without context.

## Representation

| Dimension | Question | Example distinction |
|---|---|---|
| Category | What sort of expression is this? | Noun, verb, NP, PP, clause |
| Constituency | Which words form a structural unit? | The complete object NP versus only its head noun |
| Dependency | Which element locally licenses or modifies which? | A verb and its PP complement; the preposition and its NP |
| Function | What job does the unit perform here? | Subject, Object, complement, modifier |
| Clause architecture | How are predicates, auxiliaries and clauses related? | Finite auxiliary plus a selected nonfinite verb form |

A category does not uniquely determine a function. An NP can be a Subject or Object, and a Subject need not be an Agent. A PP can occur in several grammatical functions.

## Essential distinctions
A **constituent** is a unit in a proposed structure. A **head** helps determine the category and combinatorial properties of its phrase. **Complements** are licensed within the relevant lexical/constructional pattern; **modifiers** add information without belonging to that same selection relation. Neither optionality nor semantic importance alone reliably decides complementhood.

A **clause** contains a predicational organization. Finiteness concerns grammatical form and clause licensing, not simply whether a clause describes present time. In *Maya has repaired the printer*, *has* is finite and *repaired* is a participial form selected in the perfect construction. The surface form of a regular past and participle can coincide.

Coordination relates coordinate units; subordination places a clause within a larger structure. Relative clauses modify nominal expressions in the working analysis. Long-distance dependencies require identifying both the overt expression and the position or relation it is associated with; spelling order is not enough.

## Worked analysis
Consider *The student near the windows repairs the printer*.

```text
Clause
  Subject NP
    Determiner: the
    Head noun: student
    Modifier PP
      Head preposition: near
      Complement NP: the windows
  Predicate VP
    Head verb: repairs
    Object NP: the printer
```

The Subject is the whole NP *the student near the windows*. In the ordinary agreement pattern illustrated here, singular *student* controls the form *repairs*; nearby plural *windows* is inside the modifier PP. The object is *the printer*, not merely *printer*. Replacing the Subject NP with *she* preserves the relevant grouping: *She repairs the printer*.

The replacement is one piece of evidence, not a universal algorithm. Compare another appropriate diagnostic and consider the intended interpretation. A failed substitution may reflect a bad replacement choice or discourse mismatch rather than nonconstituency.

## Interfaces
**Lexicon Syntax:** sense and construction help license complements. **Morphology Syntax:** feature realization participates in agreement and finiteness. **Syntax Semantics:** grammatical functions relate to semantic participants without being identical to them. **Syntax Prosody:** prosodic boundaries can support some groupings, but syntax does not uniquely prescribe pauses or intonation.

## Evaluation and counterevidence
Preserve the original expression, record complete spans, identify local heads and test a rival structure. For a relative clause, mark its full extent and any understood dependency before attaching a following PP. Avoid partially crossing spans in this simple tree representation; more complex frameworks may be needed for discontinuity.

Diagnostic: is *the windows* a second Subject in the worked example? No. It is the NP complement of *near*, embedded inside the Subject's modifier. The presence of another noun does not create another clause.

## Assumptions and limits
NP/DP and clause-layer analyses differ. Coordination, ellipsis, discontinuous constructions and dialect-sensitive agreement need more detailed treatment. Grammaticality judgments can be influenced by processing and context; a single analyst's judgment is not a speaker study.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) identifies constituent diagnostics, adjunct discussion and function/role contrasts in a particular framework. The tree and agreement example above are constructed analyses, not measured acceptability results.

## Related knowledge
[Category and function](../concepts/category-and-function.md), [constituency](../concepts/constituency.md), [head and dependent](../concepts/head-and-dependent.md), [complement and modifier](../concepts/complement-and-modifier.md), [finiteness](../concepts/finiteness.md) and [relative clause](../concepts/relative-clause.md) expand the distinctions. [Analyze constituency](../methods/analyze-constituency.md) gives a bounded operation.
