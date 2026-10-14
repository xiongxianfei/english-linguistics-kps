---
id: "english:model:english-morphology-system"
type: "model"
version: "0.2.1"
language: "KPS 9.x"
status: "draft"
domains: ["morphology"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:morpheme", "english:concept:root-base-and-stem", "english:concept:inflection", "english:concept:derivation", "english:concept:compounding", "english:concept:allomorphy", "english:concept:paradigm-and-syncretism", "english:concept:affix", "english:concept:consonant-articulation", "english:concept:representation-levels", "english:concept:lexical-entry", "english:concept:productivity-and-lexicalization", "english:concept:sense-and-lexical-ambiguity", "english:concept:finiteness", "english:concept:auxiliary-chain"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-syntax-system", "english:model:english-phonology-system"]
system_domain: "morphology"
---

# English morphology system

## Key takeaway
Morphology relates word-internal structure, grammatical features and lexical identity without equating morphemes with letters or syllables.

## Summary
This Model organizes lexemes, word forms, roots, affixes, inflection, derivation, compounding and allomorphy. It explains their relationships and applies them to *reports*, *teacher* and *sent*. The analyses are constructed, introductory and theory-aware; no word-list completeness or new empirical observation is claimed. A word-formation hierarchy and interfaces with Lexicon, Syntax and Phonology connect structure with lexical identity, grammatical features and realization. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked analysis](#worked-analysis)
- [Word formation hierarchy](#word-formation-hierarchy)
- [Interfaces](#interfaces)
- [Interface with Phonology](#interface-with-phonology)
- [Interface with Lexicon](#interface-with-lexicon)
- [Interface with Syntax](#interface-with-syntax)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

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

## Word formation hierarchy

Morphological analyses distinguish the element, the operation, its input base and the resulting lexeme or word form.

### Word formation hierarchy representation

```text
TEACH --derivation with -er--> TEACHER
SCHOOL + TEACHER --compounding--> SCHOOLTEACHER
SCHOOLTEACHER --plural inflection--> schoolteachers

[[school [teach-er]]-s]

START --re- derivation--> RESTART --past inflection--> restarted
```

### Word formation hierarchy worked interpretation

Teach is one root inside schoolteachers; school is another lexical root. Teacher is the head of the compound in this analysis. For restarted, the base for re- is start, while the stem for past -ed is restart. The suffix and the operation are not interchangeable answers.

### Word formation hierarchy assumptions and limits

The trees are synchronic working analyses of transparent examples. No general claim that every compound is right-headed or every historically complex form remains decomposable is made.

### Word formation hierarchy evaluation and counterevidence

A competing analysis must preserve the actual morphological contributions and the distinction between derivation and inflection. Test analogous forms, and flag lexicalization or spelling adjustments rather than inventing extra morphemes.

### Word formation hierarchy evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Interfaces
**Morphology Lexicon:** paradigms connect word forms with lexemes; lexicalized derivatives need lexical information. **Morphology Syntax:** number and finiteness features participate in agreement and construction licensing. **Morphology Phonology:** exponents and stems receive sound-conditioned realizations. These links do not imply that word formation always occurs before syntactic or phonological processing in time.

### Interface with Phonology

Regular English inflection links morphological features to sound-conditioned exponents.

Explain how a grammatical exponent receives a sound-conditioned realization rather than a spelling-conditioned one. The counterpart is explained in [Phonology](english-phonology-system.md#interface-with-morphology).

#### Interface with Phonology representation

| Morpheme | Special environment first | Voiceless remainder | Voiced remainder |
|---|---|---|---|
| Regular plural | Sibilants -> /ɪz/ | /s/ | /z/ |
| Regular past | /t,d/ -> /ɪd/ | /t/ | /d/ |

The weak vowel can differ across accents; /əz/ and /əd/ are relevant alternatives. Vowels are included in the voiced environments of this simplified model.

#### Interface with Phonology worked interpretation

Watch ends in /tʃ/, not /h/, so watches selects the syllabic plural. Laugh ends in /f/, so laughs has /s/ and laughed /t/. DELIVER ends in a voiced vowel or rhotic realization in the accents at issue, so delivered has /d/.

#### Interface with Phonology assumptions and limits

These are regular-pattern models, not full lexical pronunciation tools. Irregular stems, lexicalized adjectives, suffix-conditioned stress and accent variation are outside the algorithm. A single-underlying-exponent analysis is a compatible alternative explanation of the surface variants.

#### Interface with Phonology evaluation and counterevidence

The supplied pure functions accept final phonemes, not English spellings; tests include sibilants, vowels and /t,d/. Passing proves implementation agreement with these declared cases, not scientific completeness.

#### Interface with Phonology evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

### Interface with Lexicon

Word-formation structure and stored lexical knowledge jointly constrain a complex word’s interpretation without making every meaning predictable from its parts.

Distinguish a word-building operation from the conventional senses and uses associated with its result. The counterpart is explained in [Lexicon](english-lexicon-system.md#interface-with-morphology).

#### Interface with Lexicon representation

| Morphological analysis | Lexical question | Boundary |
|---|---|---|
| Base plus derivational affix | Does a corresponding lexeme exist and which senses are conventional? | Structural possibility is not attested use. |
| Compound constituents | Which relation between the constituents is conventional here? | The relation may not be uniquely determined by the parts. |
| Inflectional paradigm | Which forms realize a lexeme’s grammatical contrasts? | A form is not necessarily a new lexeme. |

#### Interface with Lexicon worked analysis

For printer, one working analysis combines print with agent/instrument-forming -er. The suffix gives a useful interpretation cue, but does not by itself choose between a person and a device. In printers, plural -s changes grammatical number rather than resolving that lexical sense. Store the word structure, the selected sense and the plural form separately.

#### Interface with Lexicon evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Lexicon assumptions and limits

The balance between lexical storage and productive formation is theory-dependent. Apparent segmentability is not proof of a synchronically productive rule; historical etymology is a separate claim. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Lexicon evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Syntax

Word-form features and syntactic distributions must be represented separately even when an analysis connects them through agreement or finiteness.

Relate grammatical word-form features to agreement and finiteness without assuming one spelling realizes only one feature set. The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-morphology).

#### Interface with Syntax representation

| Endpoint | Schematic fields |
|---|---|
| grammatical word features | lexeme, number, person, tense, word_form |
| agreement and finiteness pattern | construction, controller, agreement_form, finiteness |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Syntax essential terms

**Word-form features** such as number, person and tense describe grammatical distinctions realized by forms. **Agreement** is a correspondence between a controller and a form in a construction, not agreement between adjacent written words. **Finiteness** concerns clause licensing and verb form, not whether an event occurs now. **Syncretism** means that one form realizes more than one feature combination, so a feature distinction need not produce an overt spelling contrast.

#### Interface with Syntax worked interpretation

In *This report is ready* and *These reports are ready*, singular versus plural nominal features correspond to *is* versus *are* in the illustrated construction. The head of *the report near the windows* is still singular REPORT, so *The report near the windows is ready* shows why the nearest plural noun is not a sufficient agreement rule. The examples are constructed descriptive contrasts, not a universal agreement algorithm; collective nouns and other constructions require variety-specific qualifications.

#### Interface with Syntax assumptions and limits

Agreement varies by construction and variety; syncretism can conceal feature differences. This is a proposed bridge based on existing distinctions, with external claim support pending.

#### Interface with Syntax evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Syntax evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Evaluation and counterevidence
Compare related forms and contexts. A good analysis predicts at least one contrast and states where it fails. Check whether a proposed piece recurs with a relevant contribution, whether a rival segmentation is possible, and whether the pattern is regular or lexically restricted.

Diagnostic: does every final written *s* express plural? No. The string can occur within a stem or realize a different grammatical function; pronunciation and context must be distinguished.

## Assumptions and limits
This is a descriptive working framework rather than a commitment to one morpheme-based theory. Word-and-paradigm and constructional accounts can organize the same evidence differently. Historical etymology, complete paradigms and detailed dialectal variation require further evidence.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md) identifies inspected allomorphy and inflection passages. Examples and the overall component map are an authored synthesis, not the source's endorsement of this repository.

## Related knowledge
[Morpheme](../concepts/morpheme.md), [root base and stem](../concepts/root-base-and-stem.md), [inflection](../concepts/inflection.md), [derivation](../concepts/derivation.md), [compounding](../concepts/compounding.md), [allomorphy](../concepts/allomorphy.md) and [paradigm and syncretism](../concepts/paradigm-and-syncretism.md) provide reusable distinctions. [Word formation hierarchy](#word-formation-hierarchy) develops internal structure.
