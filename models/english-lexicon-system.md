---
id: "english:model:english-lexicon-system"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["lexicon"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:lexeme-and-word-form", "english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:lexical-selection", "english:concept:collocation", "english:concept:valency-and-argument-structure"]
uses_models: ["english:model:morphology-lexicon-interface", "english:model:lexicon-syntax-interface", "english:model:lexicon-semantics-interface"]
system_domain: "lexicon"
---

# English lexicon system

## Key takeaway
The lexicon connects lexical identity, form, senses and combinatorial possibilities; it is not merely a list of spellings and translations.

## Summary
A lexical entry associates a lexeme with its forms, category, senses and relevant distribution. This Model separates those fields, shows why the same spelling can participate in different entries or senses, and explains selection and lexical relations. The entry format below is an analytical working tool, not a claim that a dictionary or the brain uses this exact schema.

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

## Evaluation and counterevidence
Compare attested uses where available, substitution possibilities, complement omission and meaning shifts. Keep an unfamiliar but possible use distinct from an ungrammatical one. State the variety and register before judging a frame unavailable. A new contextual use may reveal coercion or a lexical innovation rather than a failure of all existing entries.

Diagnostic: if *discuss* and *talk about* can concern the same subject matter, must they take the same complements? No. Similar meaning does not erase their different category and frame structure.

## Assumptions and limits
The entry fields are an authored description format. No complete dictionary, corpus frequency, diachronic explanation or neural storage mechanism is claimed. Detailed lexical relations and register restrictions need additional source-specific study.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) supports bounded distinctions involving word meaning and syntactic analysis. The DEPEND and RUN entries are constructed working descriptions; they are not newly extracted corpus records.

## Related knowledge
[Lexeme and word form](../concepts/lexeme-and-word-form.md), [lexical entry](../concepts/lexical-entry.md), [sense and lexical ambiguity](../concepts/sense-and-lexical-ambiguity.md), [lexical selection](../concepts/lexical-selection.md), [collocation](../concepts/collocation.md) and [valency and argument structure](../concepts/valency-and-argument-structure.md) elaborate the fields. [Lexicon Syntax interface](lexicon-syntax-interface.md) gives additional examples.
