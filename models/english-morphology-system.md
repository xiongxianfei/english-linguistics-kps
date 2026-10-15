---
id: "english:model:english-morphology-system"
type: "model"
version: "0.3.1"
language: "KPS 9.x"
status: "draft"
domains: ["morphology"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:richards-2022-morphology", "english:reference:anderson-2018-essentials-of-linguistics"]
uses_concepts: ["english:concept:lexeme-and-word-form", "english:concept:suppletion", "english:concept:morpheme", "english:concept:root-base-and-stem", "english:concept:inflection", "english:concept:derivation", "english:concept:compounding", "english:concept:allomorphy", "english:concept:paradigm-and-syncretism", "english:concept:affix", "english:concept:consonant-articulation", "english:concept:representation-levels", "english:concept:lexical-entry", "english:concept:productivity-and-lexicalization", "english:concept:sense-and-lexical-ambiguity", "english:concept:finiteness", "english:concept:auxiliary-chain"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-syntax-system", "english:model:english-phonology-system"]
system_domain: "morphology"
---

# English morphology system

Morphology explains word-internal structure, grammatical forms and lexical identity. Use this Model to distinguish a new lexeme from a grammatical form, justify a proposed segmentation, and explain why the same grammatical contribution can have different realizations. Its introductory coverage follows the outline's five areas: word identity and form, internal structure, inflection and word formation, alternation and lexical limits, and allomorphy versus allophony. The examples are constructed analyses; a complete English morphological inventory and independent review remain outside the present scope.

## Contents

- [Word identity and form](#word-identity-and-form)
- [Internal word structure](#internal-word-structure)
  - [Morphemes and segmentation](#morphemes-and-segmentation)
  - [Roots bases stems and affixes](#roots-bases-stems-and-affixes)
- [Inflection and word formation](#inflection-and-word-formation)
  - [Inflection](#inflection)
  - [Derivation](#derivation)
  - [Compounding](#compounding)
- [Alternation and lexical limits](#alternation-and-lexical-limits)
  - [Allomorphy and suppletion](#allomorphy-and-suppletion)
  - [Productivity and lexicalization](#productivity-and-lexicalization)
- [Allomorphy vs allophony](#allomorphy-vs-allophony)
- [Worked analysis](#worked-analysis)
- [Word formation hierarchy](#word-formation-hierarchy)
- [Interfaces](#interfaces)
  - [Interface with Phonology](#interface-with-phonology)
  - [Interface with Lexicon](#interface-with-lexicon)
  - [Interface with Syntax](#interface-with-syntax)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)
- [Related knowledge](#related-knowledge)

## Word identity and form
A **lexeme** is a vocabulary identity abstracting over its grammatical forms; capital letters name one here, as in TEACH. A **word form** realizes that lexeme in a grammatical setting. *Teach*, *teaches*, *taught* and *teaching* belong to TEACH, while the person-denoting noun TEACHER is a different lexeme. Lexical identity, grammatical features, structure and pronunciation are separate descriptions.

A **paradigm** organizes a lexeme's forms by grammatical distinctions. **Syncretism** occurs when one form occupies more than one cell. In the working TEACH paradigm, *taught* serves as past tense in “They taught” and past participle in “They have taught.” The spelling alone does not choose the grammatical analysis. Identical forms can also belong to different lexemes: noun REPORT and verb REPORT both have *reports*. That is not automatically syncretism within one paradigm.

These are working lexeme-and-paradigm distinctions, not a claim that a speaker stores a table with these exact fields. Fuller source attachment for paradigm structure and syncretism remains needed; the local [Paradigm and syncretism explanation](../concepts/paradigm-and-syncretism.md) retains that gap.

## Internal word structure

### Morphemes and segmentation
A **morpheme** is a minimal unit pairing form with a meaning or grammatical contribution in the chosen analysis. **Free** morphemes can stand as words; **bound** morphemes require a host. In *teachers*, *teach* is free, while derivational *-er* and plural *-s* are bound. A morpheme is neither a letter nor necessarily a syllable.

A proposed segmentation needs recurring form-and-contribution evidence. Comparing *teach/teacher* and *work/worker* supports the person-denoting pattern; seeing the letters *er* at the end of another word is insufficient. Spelling adjustments must also be separated from morphological operations. Anderson 6.1 supports free/bound distinctions, but its wordhood diagnostics are introductory tendencies rather than universal tests for every construction.

### Roots bases stems and affixes
A **root** is a lexical core in an analysis. A **base** is the input to a word-building operation; a **stem** is the form to which inflection applies. In *restarted*, *start* is the root and the base for *re-*; *restart* is the stem for past inflection. One expression can serve different roles at different steps.

An **affix** is a bound element attached to a base: a prefix precedes it and a suffix follows it. Describe what kind of base an affix combines with and what it contributes. The same written sequence need not identify the same affix. Richards's selected lecture distinguishes reversal *un-* with verbs from negative *un-* with adjectives; this is evidence for looking at meaning and combination, not letters alone. The [word-formation hierarchy](#word-formation-hierarchy) shows how several operations can be nested.

## Inflection and word formation

### Inflection
**Inflection** realizes grammatical distinctions within a lexeme's paradigm. In the working noun analysis, *teacher/teachers* differs in number without creating a new lexeme. Verb forms can realize tense, agreement and participial distinctions. A grammatical distinction need not have a separate affix: *taught* cannot be described as an overt concatenation of *teach* and regular *-ed*.

Anderson 6.3 supports grammatical realization through affixes and other form changes. Context remains necessary: plural noun *reports* and present-tense verb *reports* do different grammatical work despite matching spelling. Detailed inventories, case analyses and the status of particular English constructions require a fuller account.

### Derivation
**Derivation** forms a lexeme from a base. In the selected analysis, TEACH → TEACHER changes a verb into a person-denoting noun. START → RESTART retains the verb category while adding meaning. Category change is therefore a possible result, not the definition of derivation.

Anderson 6.4 distinguishes these operations and shows that a derived form can become a further base. Record attachment order because different structures can imply different meanings. In *schoolteachers*, the plural applies to the compound SCHOOLTEACHER. That example does not prove an exceptionless law that every English word must be formed in the same sequence.

### Compounding
**Compounding** combines lexical bases, rather than attaching only a bound affix. In *schoolteacher*, both components contribute to the new lexical item; *teacher* is its **head**, the component determining the noun category and the relevant “kind of teacher” interpretation in this analysis.

An **endocentric** compound denotes a kind of its head; an **exocentric** interpretation lacks that straightforward relation. Anderson 7.2 presents this contrast. Meaning, grammatical behavior and pronunciation can inform a compound analysis; spacing or a single stress heuristic is insufficient. English compounds often have a right-hand head, but this is not a universal claim about every compound or language. The [Lexicon interface](#interface-with-lexicon) explains why conventional interpretation can exceed what structure supplies.

## Alternation and lexical limits

### Allomorphy and suppletion
**Allomorphs** are alternative forms associated with a morphological unit. In regular plurals, /s/, /z/ and a syllabic variant conventionally written /ɪz/ realize plural according to the stem's final sound. The vowel can differ by accent. The grammatical contribution is held apart from its pronounced exponent, the form that realizes it.

Other alternations are lexically restricted. *Sent* belongs to SEND; do not force its surface form into an overt regular *-ed* analysis. **Suppletion** is used for sharply different stems within one paradigm, illustrated here by GO and past *went*. This is distinct from predicting every irregular form by a general sound rule. Richards's pages 8–9 compare regular and idiosyncratic alternations; they do not settle the exact boundary between suppletion and other stem changes. Our GO example and terminology retain that theoretical limit.

### Productivity and lexicalization
**Productivity** concerns a pattern's availability for new formations. Knowing many existing members is not enough to show that any new base will work. The proposed test is whether speakers can form and interpret additional cases under stated conditions; this Model reports no such experiment.

**Lexicalization** concerns a form's established conventional identity and behavior. A word can remain structurally analyzable while its sense is not fully predictable from its parts. The person/device readings of *printer* illustrate why a suffix alone cannot select the intended sense. Richards's selected material motivates recording base-selection restrictions and idiosyncratic information. A comprehensive productivity measure or theory of lexical storage remains outside scope.

## Allomorphy vs allophony
Allomorphy relates forms of a morpheme; **allophony** relates phonetic realizations of a phoneme. Compare plural /s/ in *cats* with /z/ in *dogs*: the same grammatical contribution has different exponents. Compare /p/ in *pin* and *spin*: the contextual aspiration difference concerns realizations of a sound category, not a plural morpheme. Neither is a distinction between written letters.

These accounts interact. A phonological theory can derive several surface exponents from one proposed underlying exponent. That does not erase the morphological question about what grammatical unit is being realized. The [Phonology interface](#interface-with-phonology) gives the regular ending patterns and their boundaries.

## Worked analysis
Use the constructed sentence “The schoolteachers went home.” The nominal structure can be represented as `[[school [teach-er]]-s]`: a derivation supplies TEACHER, compounding supplies SCHOOLTEACHER, and inflection supplies plural *schoolteachers*. This is a structural analysis, not a measured sequence of mental processing.

| Comparison | What changes | What the analysis explains |
|---|---|---|
| *teach* → *teacher* | Derivation creates TEACHER | A word-building relation changes lexical identity |
| *teacher* → *teachers* | Plural inflection | Grammatical number changes within TEACHER |
| *schoolteacher* → *schoolteachers* | Plural applies to the compound | The internal structure identifies the relevant stem |
| *cat* → *cats* | Plural exponent /s/ after /t/ | Phonological context helps select an exponent; plural is not inherently the sound /s/ |
| *go* → *went* | An irregular past form | Lexical information is needed; a regular suffix rule does not predict this form |

Now compare “the reports” with “she reports.” The first has noun REPORT with plural inflection; the second has verb REPORT with present-tense agreement. Both usually end in /s/ after stem-final /t/. The sound pattern cannot decide which grammatical analysis is intended. Conversely, the feature plural does not determine a unique sound without stem and variety information.

These comparisons connect word identity, internal structure, grammatical features and realization. They do not establish that every final written *s* is an affix, every word ending in *er* contains the person-denoting suffix, or every unfamiliar word has a uniquely recoverable structure.

## Word formation hierarchy

Morphological analyses distinguish the element, the operation, its input base and the resulting lexeme or word form.

```text
TEACH --derivation with -er--> TEACHER
SCHOOL + TEACHER --compounding--> SCHOOLTEACHER
SCHOOLTEACHER --plural inflection--> schoolteachers

[[school [teach-er]]-s]

START --re- derivation--> RESTART --past inflection--> restarted
```

Teach is one root inside schoolteachers; school is another lexical root. Teacher is the head of the compound in this analysis. For restarted, the base for re- is start, while the stem for past -ed is restart. The suffix and the operation are not interchangeable answers.

The trees are synchronic working analyses of transparent examples. No general claim that every compound is right-headed or every historically complex form remains decomposable is made.

A competing analysis must preserve the actual morphological contributions and the distinction between derivation and inflection. Test analogous forms, and flag lexicalization or spelling adjustments rather than inventing extra morphemes.

Anderson 6.4 and 7.2 supply selected support for successive derivation and compounding. The schoolteachers and restarted representations are authored applications, not source endorsements or observed processing sequences.

## Interfaces
**Morphology Lexicon:** paradigms connect word forms with lexemes; lexicalized derivatives need lexical information. **Morphology Syntax:** number and finiteness features participate in agreement and construction licensing. **Morphology Phonology:** exponents and stems receive sound-conditioned realizations. These links do not imply that word formation always occurs before syntactic or phonological processing in time.

### Interface with Phonology

Regular English inflection links morphological features to sound-conditioned exponents.

Explain how a grammatical exponent receives a sound-conditioned realization rather than a spelling-conditioned one. The counterpart is explained in [Phonology](english-phonology-system.md#interface-with-morphology).

| Morpheme | Special environment first | Voiceless remainder | Voiced remainder |
|---|---|---|---|
| Regular plural | Sibilants -> /ɪz/ | /s/ | /z/ |
| Regular past | /t,d/ -> /ɪd/ | /t/ | /d/ |

The weak vowel can differ across accents; /əz/ and /əd/ are relevant alternatives. Vowels are included in the voiced environments of this simplified model.

Watch ends in /tʃ/, not /h/, so watches selects the syllabic plural. Laugh ends in /f/, so laughs has /s/ and laughed /t/. DELIVER ends in a voiced vowel or rhotic realization in the accents at issue, so delivered has /d/.

These are regular-pattern models, not full lexical pronunciation tools. Irregular stems, lexicalized adjectives, suffix-conditioned stress and accent variation are outside the algorithm. A single-underlying-exponent analysis is a compatible alternative explanation of the surface variants.

Stem-final sounds, not English spellings, determine these regular variants. Checking sibilants and /t,d/ before the general voicing split prevents a general rule from incorrectly overriding the syllabic variants. The declared patterns do not predict every irregular word.

Anderson 6.2 supports selected regular-plural conditioning. The complete past-tense pattern and interface schema require broader claim-specific evidence; independent review remains pending.

### Interface with Lexicon

Word-formation structure and stored lexical knowledge jointly constrain a complex word’s interpretation without making every meaning predictable from its parts.

Distinguish a word-building operation from the conventional senses and uses associated with its result. The counterpart is explained in [Lexicon](english-lexicon-system.md#interface-with-morphology).

| Morphological analysis | Lexical question | Boundary |
|---|---|---|
| Base plus derivational affix | Does a corresponding lexeme exist and which senses are conventional? | Structural possibility is not attested use. |
| Compound constituents | Which relation between the constituents is conventional here? | The relation may not be uniquely determined by the parts. |
| Inflectional paradigm | Which forms realize a lexeme’s grammatical contrasts? | A form is not necessarily a new lexeme. |

For printer, one working analysis combines print with agent/instrument-forming -er. The suffix gives a useful interpretation cue, but does not by itself choose between a person and a device. In printers, plural -s changes grammatical number rather than resolving that lexical sense. Store the word structure, the selected sense and the plural form separately.

The balance between lexical storage and productive formation is theory-dependent. Apparent segmentability is not proof of a synchronically productive rule; historical etymology is a separate claim. No recorded production, corpus sample or independent expert review is supplied for this interface account.

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Syntax

Word-form features and syntactic distributions must be represented separately even when an analysis connects them through agreement or finiteness.

Relate grammatical word-form features to agreement and finiteness without assuming one spelling realizes only one feature set. The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-morphology).

| Endpoint | Schematic fields |
|---|---|
| grammatical word features | lexeme, number, person, tense, word_form |
| agreement and finiteness pattern | construction, controller, agreement_form, finiteness |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

**Word-form features** such as number, person and tense describe grammatical distinctions realized by forms. **Agreement** is a correspondence between a controller and a form in a construction, not agreement between adjacent written words. **Finiteness** concerns clause licensing and verb form, not whether an event occurs now. **Syncretism** means that one form realizes more than one feature combination, so a feature distinction need not produce an overt spelling contrast.

In *This report is ready* and *These reports are ready*, singular versus plural nominal features correspond to *is* versus *are* in the illustrated construction. The head of *the report near the windows* is still singular REPORT, so *The report near the windows is ready* shows why the nearest plural noun is not a sufficient agreement rule. The examples are constructed descriptive contrasts, not a universal agreement algorithm; collective nouns and other constructions require variety-specific qualifications.

Agreement varies by construction and variety; syncretism can conceal feature differences. This is a proposed bridge based on existing distinctions, with external claim support pending.

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Evaluation and counterevidence
Compare related forms and contexts. A good analysis predicts at least one contrast and states where it fails. Check whether a proposed piece recurs with a relevant contribution, whether a rival segmentation is possible, and whether the pattern is regular or lexically restricted.

Diagnostic: does every final written *s* express plural? No. The string can occur within a stem or realize a different grammatical function; pronunciation and context must be distinguished.

## Assumptions and limits
This is a descriptive working framework rather than a commitment to one morpheme-based theory. Word-and-paradigm and constructional accounts can organize the same evidence differently. Historical etymology, complete paradigms and detailed dialectal variation require further evidence.

## Evidence status
**Provisional; independent review pending.** The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md#morphology-coverage-passages) identifies selected morpheme, allomorphy, inflection, derivation and compound passages. [Richards](../references/richards-2022-morphology.md) supports selected affix-selection and alternation distinctions. Paradigm/syncretism detail, productivity measurement and full accounts of conversion, clitics, nonconcatenative patterns and morphological theory remain gaps. The current outline is an introductory selection, not an exhaustive taxonomy. Examples and the overall component map are an authored synthesis, not the source's endorsement of this repository.

## Related knowledge
[Morpheme](../concepts/morpheme.md), [root base and stem](../concepts/root-base-and-stem.md), [inflection](../concepts/inflection.md), [derivation](../concepts/derivation.md), [compounding](../concepts/compounding.md), [allomorphy](../concepts/allomorphy.md) and [paradigm and syncretism](../concepts/paradigm-and-syncretism.md) provide reusable distinctions. [Word formation hierarchy](#word-formation-hierarchy) develops internal structure.
