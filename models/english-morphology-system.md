---
id: "english:model:english-morphology-system"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
domains: ["morphology"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:morpheme", "english:concept:root-base-and-stem", "english:concept:inflection", "english:concept:derivation", "english:concept:compounding", "english:concept:allomorphy", "english:concept:paradigm-and-syncretism"]
uses_models: ["english:model:morphology-lexicon-interface", "english:model:morphology-syntax-interface", "english:model:morphology-phonology-interface"]
system_domain: "morphology"
---

# English morphology system

## Key takeaway
Morphology relates word-internal structure, grammatical features and lexical identity without equating morphemes with letters or syllables.

## Summary
This Model organizes lexemes, word forms, roots, affixes, inflection, derivation, compounding and allomorphy. It explains their relationships and applies them to *reports*, *teacher* and *sent*. The analyses are constructed, introductory and theory-aware; no word-list completeness or new empirical observation is claimed.

## Purpose
Given a word form in context, identify its lexical identity, grammatical features and any supported internal structure. Do not split a word merely because a letter sequence resembles an affix.

## Representation

| Component | Distinction | Working example |
|---|---|---|
| Lexeme and word form | Vocabulary identity versus grammatical realization | REPORT and its forms *report*, *reports* |
| Root, base and stem | Lexical core versus the form an operation takes as input | A suffix attaches to a base; an inflectional stem need not be a bare root |
| Inflection | Grammatical realization within a paradigm | Singular/plural or present/past distinctions |
| Derivation | Formation of a lexical item through a word-building operation | TEACH to TEACHER in a productive analysis |
| Compounding | Combination of lexical bases | A compound is not simply any adjacent pair of words |
| Allomorphy and suppletion | Alternative realizations associated with a morphological identity | Regular plural variants; SEND and past *sent* |

The representation is relational: lexical identity, feature specification, structural analysis and pronounced form are recorded separately.

## Essential distinctions
A **morpheme** is a minimal unit in a particular form-meaning or grammatical analysis; it is not necessarily a single syllable or a visible string. An **affix** combines with a base. A **root** is the lexical core in the chosen analysis; **base** names the input to an operation; **stem** is used for the form to which inflection applies. These labels may pick out the same span in a simple word but need not do so in a complex word.

An inflectional **paradigm** organizes forms of a lexeme by grammatical features. One form may occupy several cells, called syncretism. Different lexemes can also share a surface form. Consequently, identical spelling does not guarantee identical grammatical analysis.

Derivation may change category or meaning, but category change is not required. Productivity is the availability of a pattern for new formations, not proof that every imaginable form is conventional. Lexicalization can make an established item's meaning or behavior less predictable from its parts. Compounds require evidence about their structure and use; spacing alone is not decisive.

## Worked analysis
In *the reports*, *reports* is a plural word form of the noun REPORT. In *she reports*, the same spelling can be a present-tense verb form. Context therefore precedes the choice of analysis.

For the ordinary noun use, a working segmentation is report + plural exponent. Its usual final stem phoneme /t/ conditions the nonsyllabic /s/ variant in this example. The morphological feature plural is not itself the sound /s/. Other regular stems select /z/ or a syllabic variant, and irregular nouns require separate treatment.

*Teacher* can be analyzed as teach + -er in a person-denoting derivation. That does not license the same segmentation or meaning for every word ending in the letters *er*. *Sent* is the past form of SEND; treating it as send + an overt regular -ed suffix would misdescribe the surface form. The exact analysis of stem alternation and suppletion depends on the framework.

## Interfaces
**Morphology Lexicon:** paradigms connect word forms with lexemes; lexicalized derivatives need lexical information. **Morphology Syntax:** number and finiteness features participate in agreement and construction licensing. **Morphology Phonology:** exponents and stems receive sound-conditioned realizations. These links do not imply that word formation always occurs before syntactic or phonological processing in time.

## Evaluation and counterevidence
Compare related forms and contexts. A good analysis predicts at least one contrast and states where it fails. Check whether a proposed piece recurs with a relevant contribution, whether a rival segmentation is possible, and whether the pattern is regular or lexically restricted.

Diagnostic: does every final written *s* express plural? No. The string can occur within a stem or realize a different grammatical function; pronunciation and context must be distinguished.

## Assumptions and limits
This is a descriptive working framework rather than a commitment to one morpheme-based theory. Word-and-paradigm and constructional accounts can organize the same evidence differently. Historical etymology, complete paradigms and detailed dialectal variation require further evidence.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) identifies inspected allomorphy and inflection passages. Examples and the overall component map are an authored synthesis, not the source's endorsement of this repository.

## Related knowledge
[Morpheme](../concepts/morpheme.md), [root base and stem](../concepts/root-base-and-stem.md), [inflection](../concepts/inflection.md), [derivation](../concepts/derivation.md), [compounding](../concepts/compounding.md), [allomorphy](../concepts/allomorphy.md) and [paradigm and syncretism](../concepts/paradigm-and-syncretism.md) provide reusable distinctions. [Word formation hierarchy](word-formation-hierarchy.md) develops internal structure.
