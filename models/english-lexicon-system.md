---
id: "english:model:english-lexicon-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["lexicon"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:lexeme-and-word-form", "english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:lexical-selection", "english:concept:collocation", "english:concept:valency-and-argument-structure", "english:concept:derivation", "english:concept:inflection", "english:concept:compounding", "english:concept:productivity-and-lexicalization", "english:concept:head-and-dependent", "english:concept:object-and-pp-complement", "english:concept:semantic-predicate"]
uses_models: ["english:model:english-morphology-system", "english:model:english-syntax-system", "english:model:english-semantics-system"]
system_domain: "lexicon"
---

# English lexicon system

## Key takeaway
The lexicon connects lexical identity, form, senses and combinatorial possibilities; it is not merely a list of spellings and translations.

## Summary
A lexical entry associates a lexeme with its forms, category, senses and relevant distribution. This Model separates those fields, shows why the same spelling can participate in different entries or senses, and explains selection and lexical relations. The entry format below is an analytical working tool, not a claim that a dictionary or the brain uses this exact schema. Interfaces with Morphology, Syntax and Semantics explain how word structure, complement frames and sense contributions interact. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked entry](#worked-entry)
- [Interfaces](#interfaces)
- [Interface with Morphology](#interface-with-morphology)
- [Interface with Syntax](#interface-with-syntax)
- [Interface with Semantics](#interface-with-semantics)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

## Purpose
Given a word in an utterance, determine which lexical use is relevant before assigning complements or meaning. Keep ordinary vocabulary description separate from an individual's private associations and from a complete mental-lexicon theory.

## Representation

| Entry field | What to record | Why it matters |
|---|---|---|
| Identity and forms | Lexeme, written forms and variety-labeled pronunciation | A lexeme can have several grammatical forms |
| Category | Noun, verb, adjective or another justified category in this use | Distribution is not determined by translation alone |
| Sense | A conventional meaning contribution in the intended use | Different senses can license different constructions |
| Combinatorial frame | Categories and forms of associated complements | A participant is not automatically a direct object |
| Relations and usage | Meaning relations, collocation, register and variation | Near synonyms may differ in constraints and contexts |

These fields are related but not reducible to one another. Spelling alone neither selects a sense nor determines a construction.

## Essential distinctions
A **lexeme** is a lexical identity abstracting over grammatical forms. A **word form** is a particular realization. **Polysemy** concerns related senses; **homonymy** concerns distinct lexical identities with the same form. The boundary can be contested, so a useful entry records the distinction needed for the present analysis instead of claiming an infallible dictionary partition.

A word's **sense** is not the particular individual it refers to on one occasion. A noun can contribute a property while a full noun phrase identifies an individual or quantifies over a set. Lexical meaning also includes relations such as hyponymy, antonymy and partial synonymy; synonymy rarely licenses replacement in every construction and register.

**Selection** concerns the kinds of complements licensed in a use. **Valency** describes the associated participant or complement pattern under a stated convention. **Collocation** is a recurring combination preference; an observed preference is different from a categorical grammatical requirement. Corpus frequency claims require an actual corpus and counts, neither supplied here.

## Worked entry
For a dependence use of DEPEND, record a verb frame containing a Subject and an *on*-PP: *The outcome depends on the weather*. Here *on the weather* is the verb's PP complement, while *the weather* is the NP complement of the preposition *on*. Flattening both levels into a generic verb-object list loses the local structure.

For RUN, compare *Maya runs every morning* with *Maya runs a company*. The locomotion and management uses differ in their ordinary participant structure. This does not mean a word's category alone supplies the whole frame, or that all information must reside in an isolated lexical entry. A constructional account may distribute some licensing information across constructions.

## Interfaces
**Lexicon Morphology:** a lexeme connects to inflected and derived forms. **Lexicon Syntax:** a sense and construction constrain permitted complement structures. **Lexicon Semantics:** lexical senses contribute to interpretations composed with other expressions. Pronunciation belongs to a variety-labeled form, while phonetic details still require token evidence.

### Interface with Morphology

Word-formation structure and stored lexical knowledge jointly constrain a complex word’s interpretation without making every meaning predictable from its parts.

Keep a stored sense and lexical identity separate from word-internal structure and grammatical forms. The counterpart is explained in [Morphology](english-morphology-system.md#interface-with-lexicon).

#### Interface with Morphology representation

| Morphological analysis | Lexical question | Boundary |
|---|---|---|
| Base plus derivational affix | Does a corresponding lexeme exist and which senses are conventional? | Structural possibility is not attested use. |
| Compound constituents | Which relation between the constituents is conventional here? | The relation may not be uniquely determined by the parts. |
| Inflectional paradigm | Which forms realize a lexeme’s grammatical contrasts? | A form is not necessarily a new lexeme. |

#### Interface with Morphology worked analysis

For printer, one working analysis combines print with agent/instrument-forming -er. The suffix gives a useful interpretation cue, but does not by itself choose between a person and a device. In printers, plural -s changes grammatical number rather than resolving that lexical sense. Store the word structure, the selected sense and the plural form separately.

#### Interface with Morphology evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Morphology assumptions and limits

The balance between lexical storage and productive formation is theory-dependent. Apparent segmentability is not proof of a synchronically productive rule; historical etymology is a separate claim. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Morphology evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Syntax

Lexical senses and constructions constrain the category and form of licensed syntactic complements.

Record the sense-specific complement possibilities that a construction must account for. The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-lexicon).

#### Interface with Syntax representation

| Lexical sense | Working frame | Local distinctions |
|---|---|---|
| DEPEND dependence | Subject + V + on-PP | NP inside PP complements ON |
| DISCUSS transitive | Subject + V + NP | NP is Direct Object |
| PUT placement | Subject + V + NP + location complement | Location is not another Object |
| RUN management | Subject + V + NP | Different from locomotion use |

#### Interface with Syntax worked interpretation

For "The result depends on the weather", on the weather is a PP complement of DEPEND; the weather is an NP complement of ON. The grammar is not a generic SVO template followed by an unrelated lexical pass. Selection information participates in grammatical licensing.

#### Interface with Syntax assumptions and limits

The frames are sense-specific working descriptions. Constructional theories may locate some information outside an item-specific entry; dialectal data can change the relevant permitted forms.

#### Interface with Syntax evaluation and counterevidence

Compare attested frames, accepted omission and meaning shifts. Count semantic arguments separately from overt NP objects. A frame must explain local hierarchy rather than infer functions from participant importance.

#### Interface with Syntax evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

### Interface with Semantics

A sense-specific lexical entry constrains an interpretation without making a spelling identify one context-independent predicate.

Separate the selected lexical sense from its contribution to the complete expression’s interpretation. The counterpart is explained in [Semantics](english-semantics-system.md#interface-with-lexicon).

#### Interface with Semantics representation

| Endpoint | Schematic fields |
|---|---|
| lexical sense entry | lexeme, sense, selection |
| predicate interpretation | predicate, arguments, contextual_restrictions |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Semantics essential terms

A **lexical sense entry** records a word's category, a conventional meaning contribution and relevant combinatorial restrictions. A **predicate interpretation** characterizes a property, relation or situation and its participants under the selected reading. Choosing a sense is not merely choosing a spelling. Compositional structure and context constrain how the contribution combines with other expressions; this bridge does not reduce complete sentence meaning to a dictionary gloss.

#### Interface with Semantics worked interpretation

In *Maya runs every morning*, a locomotion use of RUN characterizes an activity involving Maya. In *Maya runs a company*, a management use relates Maya to the company she manages. Keeping the same spelling while selecting the locomotion contribution for the second sentence would fail to capture its ordinary intended reading. A constructional or coercion account can distribute the explanation differently; the record should state which analysis is being used instead of assuming one location for all meaning.

#### Interface with Semantics assumptions and limits

The location of lexical and constructional information differs among theories. This bridge is schematic and does not establish an exhaustive sense inventory, an automatic disambiguator or full claim-level support.

#### Interface with Semantics evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Semantics evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Evaluation and counterevidence
Compare attested uses where available, substitution possibilities, complement omission and meaning shifts. Keep an unfamiliar but possible use distinct from an ungrammatical one. State the variety and register before judging a frame unavailable. A new contextual use may reveal coercion or a lexical innovation rather than a failure of all existing entries.

Diagnostic: if *discuss* and *talk about* can concern the same subject matter, must they take the same complements? No. Similar meaning does not erase their different category and frame structure.

## Assumptions and limits
The entry fields are an authored description format. No complete dictionary, corpus frequency, diachronic explanation or neural storage mechanism is claimed. Detailed lexical relations and register restrictions need additional source-specific study.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) supports bounded distinctions involving word meaning and syntactic analysis. The DEPEND and RUN entries are constructed working descriptions; they are not newly extracted corpus records.

## Related knowledge
[Lexeme and word form](../concepts/lexeme-and-word-form.md), [lexical entry](../concepts/lexical-entry.md), [sense and lexical ambiguity](../concepts/sense-and-lexical-ambiguity.md), [lexical selection](../concepts/lexical-selection.md), [collocation](../concepts/collocation.md) and [valency and argument structure](../concepts/valency-and-argument-structure.md) elaborate the fields. [Lexicon Syntax interface](#interface-with-syntax) gives additional examples.
