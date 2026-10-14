---
id: "english:model:english-syntax-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["syntax"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:walter-2016-modal-verbs-basics"]
uses_concepts: ["english:concept:category-and-function", "english:concept:constituency", "english:concept:head-and-dependent", "english:concept:complement-and-modifier", "english:concept:finiteness", "english:concept:relative-clause", "english:concept:auxiliary-chain", "english:concept:tense-and-aspect", "english:concept:do-support-and-inversion", "english:concept:clause-architecture", "english:concept:inflection", "english:concept:paradigm-and-syncretism", "english:concept:lexical-selection", "english:concept:object-and-pp-complement", "english:concept:valency-and-argument-structure", "english:concept:semantic-role", "english:concept:phrase-and-clause", "english:concept:prosody"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-morphology-system", "english:model:english-semantics-system", "english:model:english-prosody-system"]
system_domain: "syntax"
---

# English syntax system

## Key takeaway
Syntax organizes categories, constituent structure, dependencies and grammatical functions; word order alone does not specify the whole analysis.

## Summary
This Model explains how phrases and clauses are assembled and how local grammatical relations are identified. It distinguishes categories from functions, complements from modifiers and finite from nonfinite clauses. It includes a complete bracketed example and a procedure for testing the proposed grouping. The working notation uses NP and a descriptive Subject/Predicate analysis; other frameworks are legitimate alternatives. Auxiliary selection, nested clauses and interfaces with Morphology, Lexicon, Semantics and Prosody are explained locally. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Auxiliary selection](#auxiliary-selection)
- [Nested clauses](#nested-clauses)
- [Interfaces](#interfaces)
- [Interface with Morphology](#interface-with-morphology)
- [Interface with Lexicon](#interface-with-lexicon)
- [Interface with Semantics](#interface-with-semantics)
- [Interface with Prosody](#interface-with-prosody)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

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

## Auxiliary selection

Local auxiliary selection explains the form of each following verb independently of the construction label.

### Auxiliary selection representation

| Selecting auxiliary | Selected form | Construction |
|---|---|---|
| Central modal | Plain | Modal |
| Perfect HAVE | Past participle | Perfect |
| Progressive BE | Ing form | Progressive |
| Passive BE | Past participle | Verbal passive |
| Support DO | Plain | Support for relevant finite constructions |

### Auxiliary selection worked interpretation

In may have been working, may is finite, have plain, been past participle, working ing. In has been reviewed, has is finite, been a past participle introducing passive BE, and reviewed the lexical past participle. Identical participial morphology does not identify identical constructions.

### Auxiliary selection assumptions and limits

Finite versus nonfinite and tense versus aspect are independent dimensions. BE with an adjectival participle is not automatically verbal passive. The model concerns central standard-English patterns, not all semi-auxiliaries or dialectal modal combinations.

### Auxiliary selection evaluation and counterevidence

For each chain, annotate selecting item, selected form and semantic construction separately. A mismatch such as may has exposes a selection error; an unusual but licensed chain is not rejected merely for stylistic heaviness.

### Auxiliary selection evidence status

The central-modal row has selected support from [Walter's modal-form explanation](../references/walter-2016-modal-verbs-basics.md#inspected-contribution). In *may deliver*, *may* selects the plain form *deliver*; changing the subject to *she* does not license *may delivers*. This narrow rule is used in the editing Practice. The other rows, full chains and construction distinctions remain authored analyses awaiting fuller source attachment; this citation does not validate them all.

## Nested clauses

A clause analysis records complete constituent spans and their nesting rather than counting verb-looking tokens.

The constructed passage is: “Although the roads were icy, Anna sent the reports that Maya had prepared to Leo. He thanked her because he needed them.”

### Nested clauses representation

```text
[Clause
  [Adverbial Although the roads were icy]
  [NP Anna]
  [VP sent
      [NP the reports [Relative that Maya had prepared __]]
      [PP to [NP Leo]]]]
[Clause He [VP thanked her [Adverbial because he needed them]]]
```

### Nested clauses worked interpretation

The first main clause contains both the concessive adjunct and a relative inside its Object NP. The to-PP attaches to SEND, not PREPARE in the intended reading. Across both sentences the working model counts two main clauses, two finite adverbial clauses and one finite relative clause. Had prepared is one auxiliary chain.

### Nested clauses assumptions and limits

The flat VP display is a descriptive simplification. The treatment of although/because as clause markers and the auxiliary-chain clause count are declared choices. A CP/TP analysis can differ without changing the need to record nesting.

### Nested clauses evaluation and counterevidence

Check that every token has a place and that constituent intervals are nested or disjoint, not partially crossing. The companion constructed fixture records token spans. It is a regression target for this analysis, not a corpus annotation standard.

### Nested clauses evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Interfaces
**Lexicon Syntax:** sense and construction help license complements. **Morphology Syntax:** feature realization participates in agreement and finiteness. **Syntax Semantics:** grammatical functions relate to semantic participants without being identical to them. **Syntax Prosody:** prosodic boundaries can support some groupings, but syntax does not uniquely prescribe pauses or intonation.

### Interface with Morphology

Word-form features and syntactic distributions must be represented separately even when an analysis connects them through agreement or finiteness.

Identify the controller and construction before predicting agreement; the nearest written noun is not a sufficient rule. The counterpart is explained in [Morphology](english-morphology-system.md#interface-with-syntax).

#### Interface with Morphology representation

| Endpoint | Schematic fields |
|---|---|
| grammatical word features | lexeme, number, person, tense, word_form |
| agreement and finiteness pattern | construction, controller, agreement_form, finiteness |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Morphology essential terms

**Word-form features** such as number, person and tense describe grammatical distinctions realized by forms. **Agreement** is a correspondence between a controller and a form in a construction, not agreement between adjacent written words. **Finiteness** concerns clause licensing and verb form, not whether an event occurs now. **Syncretism** means that one form realizes more than one feature combination, so a feature distinction need not produce an overt spelling contrast.

#### Interface with Morphology worked interpretation

In *This report is ready* and *These reports are ready*, singular versus plural nominal features correspond to *is* versus *are* in the illustrated construction. The head of *the report near the windows* is still singular REPORT, so *The report near the windows is ready* shows why the nearest plural noun is not a sufficient agreement rule. The examples are constructed descriptive contrasts, not a universal agreement algorithm; collective nouns and other constructions require variety-specific qualifications.

#### Interface with Morphology assumptions and limits

Agreement varies by construction and variety; syncretism can conceal feature differences. This is a proposed bridge based on existing distinctions, with external claim support pending.

#### Interface with Morphology evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Morphology evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

### Interface with Lexicon

Lexical senses and constructions constrain the category and form of licensed syntactic complements.

Explain local complement structure using the relevant lexical sense and construction rather than a generic Subject Verb Object template. The counterpart is explained in [Lexicon](english-lexicon-system.md#interface-with-syntax).

#### Interface with Lexicon representation

| Lexical sense | Working frame | Local distinctions |
|---|---|---|
| DEPEND dependence | Subject + V + on-PP | NP inside PP complements ON |
| DISCUSS transitive | Subject + V + NP | NP is Direct Object |
| PUT placement | Subject + V + NP + location complement | Location is not another Object |
| RUN management | Subject + V + NP | Different from locomotion use |

#### Interface with Lexicon worked interpretation

For "The result depends on the weather", on the weather is a PP complement of DEPEND; the weather is an NP complement of ON. The grammar is not a generic SVO template followed by an unrelated lexical pass. Selection information participates in grammatical licensing.

#### Interface with Lexicon assumptions and limits

The frames are sense-specific working descriptions. Constructional theories may locate some information outside an item-specific entry; dialectal data can change the relevant permitted forms.

#### Interface with Lexicon evaluation and counterevidence

Compare attested frames, accepted omission and meaning shifts. Count semantic arguments separately from overt NP objects. A frame must explain local hierarchy rather than infer functions from participant importance.

#### Interface with Lexicon evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

### Interface with Semantics

Construction-sensitive mappings connect grammatical functions with semantic roles without identifying the two dimensions.

Keep grammatical functions separate from participant roles when comparing constructions. The counterpart is explained in [Semantics](english-semantics-system.md#interface-with-syntax).

#### Interface with Semantics representation

| Construction | Giver | Recipient | Theme |
|---|---|---|---|
| Leo gave Maya a prize | Subject | Indirect Object | Direct Object |
| Leo gave a prize to Maya | Subject | NP inside to-PP | Direct Object |
| Maya was given a prize by Leo | NP inside by-PP | Subject | Retained Object |

#### Interface with Semantics worked interpretation

A passive can preserve the basic participant relations while changing grammatical functions. A causative alternation such as "The glass broke / Leo broke the glass" can add a Causer instead. A psych predicate can give a Stimulus Subject and Experiencer Object without passive morphology.

#### Interface with Semantics assumptions and limits

Dative alternation has lexical, semantic and discourse restrictions; the table does not establish complete synonymy. Role inventories vary. The mapping is analytical rather than evidence of a particular neural transfer operation.

#### Interface with Semantics evaluation and counterevidence

Ask which participants are added, omitted, implicit or redistributed. A changed function alone does not necessarily add a role. Keep explicit versus inferred participants separate in every example.

#### Interface with Semantics evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

### Interface with Prosody

Syntactic grouping can constrain prosodic grouping without making syntactic constituents and prosodic phrases identical.

Relate constituent spans to possible spoken grouping without treating a pause as proof of a unique parse. The counterpart is explained in [Prosody](english-prosody-system.md#interface-with-syntax).

#### Interface with Prosody representation

| Syntactic description | Prosodic description | Required distinction |
|---|---|---|
| NP or clause span | Candidate prosodic phrase span | Similar boundaries are not identity. |
| Embedded relative clause | Possible grouping around the modifier | A pause does not prove a unique parse. |
| Constituent length and embedding | Rate-sensitive phrasing options | Optional phrasing is not a new syntax by itself. |

#### Interface with Prosody worked analysis

Bracket “[The report that Maya prepared] [arrived].” The subject contains a relative clause. A proposed spoken realization may group the whole subject or use finer phrasing depending on length, focus and rate. The written brackets neither specify silence durations nor justify one exact intonation transcription. Compare this with an explicit pause after report only after recording or hearing the target.

#### Interface with Prosody evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Prosody assumptions and limits

The mapping is framework- and context-sensitive. No one-to-one match, universal pause rule or deterministic recovery of syntax from acoustics is asserted. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Prosody evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

## Evaluation and counterevidence
Preserve the original expression, record complete spans, identify local heads and test a rival structure. For a relative clause, mark its full extent and any understood dependency before attaching a following PP. Avoid partially crossing spans in this simple tree representation; more complex frameworks may be needed for discontinuity.

Diagnostic: is *the windows* a second Subject in the worked example? No. It is the NP complement of *near*, embedded inside the Subject's modifier. The presence of another noun does not create another clause.

## Assumptions and limits
NP/DP and clause-layer analyses differ. Coordination, ellipsis, discontinuous constructions and dialect-sensitive agreement need more detailed treatment. Grammaticality judgments can be influenced by processing and context; a single analyst's judgment is not a speaker study.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) identifies constituent diagnostics, adjunct discussion and function/role contrasts in a particular framework. The tree and agreement example above are constructed analyses, not measured acceptability results.

## Related knowledge
[Category and function](../concepts/category-and-function.md), [constituency](../concepts/constituency.md), [head and dependent](../concepts/head-and-dependent.md), [complement and modifier](../concepts/complement-and-modifier.md), [finiteness](../concepts/finiteness.md) and [relative clause](../concepts/relative-clause.md) expand the distinctions. [Analyze constituency](../methods/analyze-constituency.md) gives a bounded operation.
