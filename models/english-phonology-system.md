---
id: "english:model:english-phonology-system"
type: "model"
version: "0.2.4"
language: "KPS 9.x"
status: "draft"
domains: ["phonology"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:international-phonetic-association-undated-ipa-chart"]
uses_concepts: ["english:concept:phone-phoneme-and-allophone", "english:concept:contrast-and-distribution", "english:concept:syllable-structure", "english:concept:phonotactics", "english:concept:stress", "english:concept:consonant-articulation", "english:concept:vowel-articulation", "english:concept:connected-speech", "english:concept:representation-levels", "english:concept:prosody", "english:concept:allomorphy", "english:concept:inflection"]
uses_models: ["english:model:english-morphology-system", "english:model:english-phonetics-system", "english:model:english-prosody-system"]
system_domain: "phonology"
uses_principles: ["english:principle:realization-varies-with-environment"]
---

# English phonology system

## Key takeaway
Phonology models contrast, distribution and the organization of sound patterns within a specified language variety.

## Summary
English phonology distinguishes meaning-changing sound categories from contextually distributed realizations and organizes segments into larger structures. This Model explains vowel and consonant attributes, then uses them to explain contrast, allophony and natural classes alongside syllables and phonotactics. It does not treat spelling, phonological representation and actual pronunciation as identical. The phonological-word account and interfaces with Morphology, Phonetics and Prosody are included locally. Source limits remain specific to each explanation.

## Contents

- [Purpose](#purpose)
- [Representation](#representation)
- [Essential distinctions](#essential-distinctions)
- [Worked example](#worked-example)
- [Connected speech patterns](#connected-speech-patterns)
- [Phonological word](#phonological-word)
- [Interfaces](#interfaces)
- [Interface with Phonetics](#interface-with-phonetics)
- [Interface with Prosody](#interface-with-prosody)
- [Interface with Morphology](#interface-with-morphology)
- [Evaluation and counterevidence](#evaluation-and-counterevidence)
- [Assumptions and limits](#assumptions-and-limits)
- [Evidence status](#evidence-status)

## Purpose
For a sound difference, ask whether it distinguishes words, follows an environment-sensitive pattern or remains unresolved. The aim is a testable analysis of distributions, not a list of IPA symbols.

## Representation

| Component | What it contributes | Example question |
|---|---|---|
| Contrast | Language-specific distinctions between phonological categories | Can replacing one sound distinguish words? |
| Distribution | Environments in which realizations occur | Is a difference predictable in this context? |
| Features and natural classes | Shared properties used to state generalizations | Does the pattern affect voiceless stops rather than arbitrary letters? |
| Syllables and phonotactics | Structural positions and restrictions on sequences | Which sounds occupy onset, nucleus and coda? |
| Processes and constraints | Explicit descriptions of alternation and licensing | Under what conditions is aspiration expected? |

An inventory, a distribution table and a rule make different claims. A proposed rule must fit the data and its exceptions rather than replace them.

## Essential distinctions
A **phone** is a phonetic sound category used in describing realizations. A **phoneme** is a contrastive category in an analysis of a particular language variety. **Allophones** are realizations associated with a phoneme. A minimal pair differs at one corresponding sound position while the relevant environment is held constant; a meaning distinction can motivate a contrastive analysis.

Complementary distribution means two realizations do not occur in the same examined environments. It is evidence to investigate, not an automatic proof that any two sounds belong to one phoneme. Phonetic relationships, the completeness of the sample and alternative analyses matter.

A syllable can be represented as onset plus rhyme, with the rhyme divided into nucleus and coda. In /spɪn/, /sp/ is the onset, /ɪ/ the nucleus and /n/ the coda in this working analysis. These are structural positions, not spaces in the written word. **Phonotactics** concerns permitted patterns; absence from a small word list does not prove that a sequence is impossible.

A natural class groups sounds by shared relevant features. A rule or constraint can use such a class and state an environment. Rules, constraints and usage-based generalizations are alternative representational approaches; this foundation does not choose a universal theory of mental computation.

### Consonant attributes

Phonetics describes how sounds are produced; phonology asks which differences distinguish words or help explain patterns in a language. The following attributes provide the descriptive starting point. They describe sounds, not alphabet letters: the letters *th* can represent different sounds in *thin* and *this*.

| Attribute | Meaning | Useful categories and examples |
|---|---|---|
| Voicing | Whether the vocal folds vibrate during the relevant sound interval | [s] is voiceless; [z] is voiced |
| Place | Where the vocal tract is constricted | Bilabial: both lips, as in [p]; labiodental: lower lip against upper teeth, as in [f]; alveolar: tongue near the ridge behind the upper teeth, as in [t]; velar: tongue back against the soft palate, as in [k] |
| Manner | How the constriction directs or restricts airflow | Stop: oral airflow is blocked, as in [p]; fricative: a narrow passage produces friction, as in [s]; nasal: oral closure with airflow through the nose, as in [m] |

An affricate, such as [tʃ], combines a closure with a fricated release. An approximant has a more open constriction without the friction characteristic of a fricative; [j], the initial sound in *yes*, is an example. A lateral approximant such as [l] allows airflow around the tongue's sides. Thus the labels say what the articulators and airflow are doing.

| Phone category | Voicing | Place | Manner |
|---|---|---|---|
| [p] | Voiceless | Bilabial | Stop |
| [b] | Voiced | Bilabial | Stop |
| [t] | Voiceless | Alveolar | Stop |
| [k] | Voiceless | Velar | Stop |
| [s] | Voiceless | Alveolar | Fricative |
| [z] | Voiced | Alveolar | Fricative |
| [m] | Voiced | Bilabial | Nasal |
| [n] | Voiced | Alveolar | Nasal |
| [ŋ] | Voiced | Velar | Nasal |

These are introductory IPA categories, written in square brackets. The English phonemes /p/ and /b/ have several realization cues, including aspiration and timing; an English /b/ token need not be fully voiced throughout. The broad category label is not a measurement of every production.

### Vowel attributes

Vowels are described by the shape of the relatively open vocal tract. **Height** places the tongue body relatively high (close) or low (open); **backness** distinguishes front, central and back positions; **rounding** describes the lips. These dimensions are separate: a front vowel is not necessarily unrounded in every language.

| Phone category | Height | Backness | Lips |
|---|---|---|---|
| [i] | Close (high) | Front | Unrounded |
| [ɪ] | Near-close | Near-front | Unrounded |
| [ɛ] | Open-mid | Front | Unrounded |
| [æ] | Near-open | Front | Unrounded |
| [u] | Close (high) | Back | Rounded |
| [ʊ] | Near-close | Near-back | Rounded |
| [ə] | Mid | Central | Neutral or unrounded in the working English description |

In broad General American notation, *see*, *sit* and *sat* illustrate /i/, /ɪ/ and /æ/. Their quality differences involve more than simply holding one sound for longer. /u/ in *food* conventionally uses the symbol for a close back rounded vowel, but actual American realizations may be farther forward. A diphthong, such as /aɪ/ in *my*, involves movement in quality rather than one fixed position. Stress, duration, nasalization and rhoticity can require further description; none should be inferred from a vowel letter alone.

### From attributes to sound patterns

Compare [p] with [b]: place and manner match in these categories, while voicing differs. Compare [p] with [t]: both are voiceless stops, but their places differ. The English phonemes /p t k/ therefore form a useful **natural class of voiceless stops** for discussing aspiration, although they use different constriction locations. /m n ŋ/ form a nasal class across those locations. Whether a class explains a particular pattern still needs distributional evidence.

To describe a target, first identify its sound and notation, then fill in the appropriate attributes. Finally ask a separate phonological question: does the difference distinguish words, or is it a contextual realization? Feature similarity alone cannot decide that. For vowels, *sit* /sɪt/ and *sat* /sæt/ provide a constructed lexical comparison: the matching consonant environment helps isolate the vowel contrast. These word examples are illustrations, not recorded speaker observations.

## Worked example
The words *pin* and *bin* illustrate a broad /p/ versus /b/ contrast in a matched environment. *Pin* and *spin* instead help investigate the distribution of aspiration associated with /p/: the added /s/ changes the environment, so they are not a minimal pair differing only in aspiration.

The table applies a bounded aspiration generalization to constructed General American examples. A stressed syllable is relatively prominent within its word; its onset is the consonant material before its nucleus. Aspiration is the interval of voiceless airflow after a stop release, written with [ʰ].

| Word and broad form | Target and environment | Predicted target realization | What the comparison shows |
|---|---|---|---|
| *pin* /pɪn/ | /p/ begins a stressed syllable, without preceding /s/ | [pʰ] | Voiceless stop aspiration is expected here |
| *spin* /spɪn/ | /p/ follows /s/ in the stressed syllable's onset | [p], with less aspiration | Stress alone does not specify the realization |
| *bin* /bɪn/ | /b/ in the matched word-initial environment | [b] as a broad phone label; voicing timing varies | /b/ falls outside the voiceless-stop class |

The generalization links **category + environment** to a predicted realization: English /p t k/ commonly have aspiration at the beginning of a stressed syllable, while a preceding /s/ in the same onset blocks that usual pattern. It applies across different places because the shared voiceless-stop properties matter here. /s/ is also voiceless, but it is a fricative, so it does not belong to this stop class. Choosing only the feature "voiceless" would make the proposed class too broad.

The /p/–/b/ distinction can distinguish words; the [pʰ]–[p] difference illustrated here is a contextual realization difference associated with /p/. These are distinct conclusions. No recording has been examined, so the table predicts target phones only. It does not transcribe complete productions or specify all realizations in unstressed, final or other environments. The [inspected aspiration passage](../references/anderson-2018-essentials-of-linguistics.md#aspiration) supports the bounded pattern, not a universal timing threshold.

## Connected speech patterns

**Elision**, also called segment deletion, relates a fuller form to a realization lacking a segment. A possible *asked* comparison is /æskt/ with [æst]: the /k/ has no separate segment in that surface analysis. This is a context-sensitive realization proposal, not a new lexical item or proof that /k/ is absent from the language's inventory. The [inspected casual-speech passage](../references/anderson-2018-essentials-of-linguistics.md#connected-speech-passages) supplies the example; it is not a recording examined here.

To turn such a comparison into a phonological generalization, specify the target segment, neighboring categories, relevant stress or boundary conditions, variety, and whether the pattern is optional. Compare retained as well as omitted realizations. One example does not license a rule deleting every stop in every cluster, and an absent audible release alone does not prove segment deletion.

Other [connected-speech processes](../concepts/connected-speech.md) make different claims: assimilation changes a property toward that of a neighbor; reduction weakens a realization without necessarily removing it; linking connects articulation across a boundary without necessarily changing the segment sequence. These distinctions let an analysis state what changes before asking why it is distributed that way.

## Phonological word

Segment categories, syllable organization, stress and phonetic realization provide distinct descriptions of a sound pattern.

### Phonological word representation

```text
spin /spɪn/
Syllable
  Onset: /sp/
  Rhyme
    Nucleus: /ɪ/
    Coda: /n/

Orthography: <pin>
Phonology: /pɪn/
Possible phonetic form: [pʰɪn]
```

### Phonological word primary general american examples

The package default for a new lexical example is a **General American broad transcription**, as set out in [PRONUNCIATION](../docs/PRONUNCIATION.md). Typical authored examples include *see* /si/, *food* /fud/ and rhotic *car* /kɑr/. Existing phonological examples such as *pin* /pɪn/ and [pʰɪn] remain usable at their stated levels. Do not convert earlier non-rhotic or British-style lexical transcriptions by replacing symbols mechanically; dialect-specific lexical incidence and stress must be checked. None of the illustrative square-bracket forms is a measured token.

### Phonological word worked interpretation

The /sp/ onset is licensed in ordinary English; /ŋl/ is not an ordinary native initial onset. Primary stress is ˈ and secondary stress ˌ. A written vowel sequence can represent one nucleus, while some consonants can be syllabic.

### Phonological word assumptions and limits

The model uses an onset-rhyme organization and conventional broad English symbols. Phonemic symbols do not promise exact cardinal vowel qualities, and a phone label is not a waveform measurement.

### Phonological word evaluation and counterevidence

Inspect a recording before making token-specific phonetic claims. Check transcription level, accent and syllable boundaries. Use possible nonwords as structural illustrations without asserting universal lexical nonexistence.

### Phonological word evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Interfaces
**Morphology Phonology:** regular inflection connects number or tense features with exponents whose form depends partly on stem sounds. **Phonology Prosody:** segment organization interacts with syllables, stress and larger prosodic domains. **Phonology Phonetics:** an abstract category is realized under contextual and speaker-specific conditions; a broad form does not uniquely determine a waveform.

### Interface with Phonetics

Phonological representations constrain possible phonetic analyses without uniquely specifying an observed speech token.

Relate sound categories and environments to possible realizations while keeping contrast distinct from physical difference. The counterpart is explained in [Phonetics](english-phonetics-system.md#interface-with-phonology).

#### Interface with Phonetics representation

| Endpoint | Schematic fields |
|---|---|
| phonological form | segments, syllables, stress |
| phonetic realization | transcription_level, context, observed_or_predicted, recording_id |

The mapping uses `kps:constrains`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

#### Interface with Phonetics essential terms

A **phonological form** describes language-specific categories and structural positions. A **phonetic realization** describes speech production or the resulting sound in a particular context. Slashes conventionally mark a phonemic analysis; square brackets mark a phonetic description. Neither notation by itself identifies a recording. Stress, neighboring sounds, rate and speaker variety can condition realization, so a phonological string need not determine one narrow transcription.

#### Interface with Phonetics worked interpretation

Broad /pɪn/ and /spɪn/ both contain /p/. A stressed onset in *pin* can be aspirated, represented schematically as [pʰ], while the post-/s/ realization in *spin* is commonly less aspirated. The phonological environment helps explain a predicted difference without changing /p/ into a different phoneme merely because the phones differ. No token has been recorded here. To claim an observed difference, identify recordings and the criteria used to inspect the realization.

#### Interface with Phonetics assumptions and limits

A variety, stress and segmental context must be stated. This bridge does not assert a universal phonetics–phonology boundary or an executable production model. No audio has been recorded or inspected during migration.

#### Interface with Phonetics evaluation and counterevidence

Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

#### Interface with Phonetics evidence status

**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

### Interface with Prosody

Syllable organization and lexical stress constrain prosodic realization, but do not uniquely determine phrasal prominence or grouping.

Relate syllables and lexical stress to possible utterance prominence without rewriting lexical entries for every sentence accent. The counterpart is explained in [Prosody](english-prosody-system.md#interface-with-phonology).

#### Interface with Prosody representation

Keep a segment string and syllable parse, lexical stress positions, proposed phrasal accents, and phrase-edge annotations in different fields. A word can contain a lexically stressed syllable even when that word does not receive the strongest prominence in an utterance. Prosody is independently browsable here but overlaps phonological analysis; the domain boundary is an organizing convention.

#### Interface with Prosody worked analysis

In a constructed “The students repaired the printers,” lexical word forms remain the same across a who-question and a what-question context. A proposed accent can shift from students to printers, while each word retains its lexical stress organization. Do not rewrite the lexical entry to encode every sentence-specific accent.

#### Interface with Prosody evaluation and counterevidence

Record the source and target analyses separately. Vary one relevant condition while preserving the others, compare the proposed mapping with an alternative, and record mismatches. A shared domain tag is not evidence for the mapping. No result is assumed to be uniquely recoverable from the other representation.

#### Interface with Prosody assumptions and limits

This does not assign a complete metrical or tonal analysis. Stress, reduction, syllabification and phrasing vary with variety, rate and theoretical assumptions. No recorded production, corpus sample or independent expert review is supplied for this interface account.

#### Interface with Prosody evidence status

**Provisional; not independently reviewed.** No newly inspected external passage is asserted to verify this summary claim. Internal links provide explanatory context, not independent evidence.

### Interface with Morphology

Regular English inflection links morphological features to sound-conditioned exponents.

Use stem-final sound classes to describe the distribution of inflectional variants, keeping the grammatical feature distinct from its exponent. The counterpart is explained in [Morphology](english-morphology-system.md#interface-with-phonology).

#### Interface with Morphology representation

| Morpheme | Special environment first | Voiceless remainder | Voiced remainder |
|---|---|---|---|
| Regular plural | Sibilants -> /ɪz/ | /s/ | /z/ |
| Regular past | /t,d/ -> /ɪd/ | /t/ | /d/ |

The weak vowel can differ across accents; /əz/ and /əd/ are relevant alternatives. Vowels are included in the voiced environments of this simplified model.

#### Interface with Morphology worked interpretation

Watch ends in /tʃ/, not /h/, so watches selects the syllabic plural. Laugh ends in /f/, so laughs has /s/ and laughed /t/. DELIVER ends in a voiced vowel or rhotic realization in the accents at issue, so delivered has /d/.

#### Interface with Morphology assumptions and limits

These are regular-pattern models, not full lexical pronunciation tools. Irregular stems, lexicalized adjectives, suffix-conditioned stress and accent variation are outside the algorithm. A single-underlying-exponent analysis is a compatible alternative explanation of the surface variants.

#### Interface with Morphology evaluation and counterevidence

The supplied pure functions accept final phonemes, not English spellings; tests include sibilants, vowels and /t,d/. Passing proves implementation agreement with these declared cases, not scientific completeness.

#### Interface with Morphology evidence status

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Evaluation and counterevidence
Collect positive, negative and untested environments; compare competing classifications; separate accent-specific patterns from claims about all English. A counterexample may reveal a missing condition, a different lexical class or a faulty transcription. It should not be silently deleted.

Diagnostic: a phone occurs only word-finally in a small sample. Has it been proved to be an allophone of a different word-initial phone? No. Distribution alone does not establish that relationship, and the sample may omit relevant environments.

## Assumptions and limits
The onset-rhyme representation and examples are working analyses. English varieties differ in inventories and realizations. A complete variety-specific inventory, loanword phonotactics, rule interactions and empirical processing evidence remain outside this foundational Model.

## Evidence status
**Provisional; independent review pending.** Selected passages on contrast, natural classes, allomorphy, connected speech and aspiration are identified in the [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md). The [IPA chart record](../references/international-phonetic-association-undated-ipa-chart.md) supports the symbol classifications; it does not establish a complete English inventory or measured realizations. The inline feature explanations summarize the local articulation Concepts. These sources support bounded distinctions, not every generalization or the particular framework used here.

## Related knowledge
[Phone phoneme and allophone](../concepts/phone-phoneme-and-allophone.md) and [contrast and distribution](../concepts/contrast-and-distribution.md) deepen the category distinction. [Syllable structure](../concepts/syllable-structure.md), [phonotactics](../concepts/phonotactics.md) and [stress](../concepts/stress.md) expand structural details. [Phonological word](#phonological-word) provides another worked representation.

[Vowel articulation](../concepts/vowel-articulation.md) and [consonant articulation](../concepts/consonant-articulation.md) expand the feature descriptions. [Classify and produce a phone](../practices/classify-and-produce-phone.md) connects classification with listening, production and verification.
