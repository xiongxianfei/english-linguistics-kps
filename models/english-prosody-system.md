---
id: "english:model:english-prosody-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["prosody"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:roberts-2012-information-structure", "english:reference:mit-2006-tobi-tutorial", "english:reference:krifka-2008-information-structure"]
uses_concepts: ["english:concept:stress", "english:concept:prosody", "english:concept:connected-speech", "english:concept:syllable-structure", "english:concept:phonotactics", "english:concept:constituency", "english:concept:relative-clause", "english:concept:phrase-and-clause", "english:concept:focus-topic-and-qud"]
uses_models: ["english:model:english-phonology-system", "english:model:english-syntax-system", "english:model:english-information-structure-system", "english:model:english-phonetics-system"]
system_domain: "prosody"
uses_methods: ["english:method:analyze-sound-realization"]
---

# English prosody system

Prosody explains how speech groups material and makes some parts relatively prominent through stress, pitch organization and timing. It helps explain why the same words can support different spoken contributions, while keeping grammatical structure, contextual interpretation and acoustic measurements distinct.

This Model develops seven introductory areas and connects them through a constructed printer-repair example. Its accent-and-boundary vocabulary draws on selected Mainstream American English ToBI materials, without claiming to supply a full annotation course or a universal prosodic grammar. General American is the convention for new lexical transcriptions. No recording, acoustic measurement or listener response is supplied.

## Contents

- [Lexical stress and utterance prominence](#lexical-stress-and-utterance-prominence)
- [Pitch accents](#pitch-accents)
- [Phrasing and boundaries](#phrasing-and-boundaries)
- [Intonation and interpretation](#intonation-and-interpretation)
- [Rhythm and timing](#rhythm-and-timing)
- [Connected speech and reduction](#connected-speech-and-reduction)
- [Prosodic representation and acoustic evidence](#prosodic-representation-and-acoustic-evidence)
- [Worked analysis](#worked-analysis)
- [Interfaces](#interfaces)
  - [Interface with Phonology](#interface-with-phonology)
  - [Interface with Phonetics](#interface-with-phonetics)
  - [Interface with Syntax](#interface-with-syntax)
  - [Interface with Information Structure](#interface-with-information-structure)
- [Evidence and limits](#evidence-and-limits)

## Lexical stress and utterance prominence

**Lexical stress** organizes relative prominence among syllables in a word. **Utterance prominence** concerns highlighting within a spoken contribution. The two interact, but changing the prominent word in a sentence does not ordinarily rewrite that word's lexical stress pattern.

In the broad General American form *printer* /ˈprɪntər/, primary stress falls on the first syllable. A response to *Who repaired the printer?* might give the main prominence to *Maya* in *MAYA repaired the printer*. A response to *What did Maya repair?* might instead give it to *printer*. In both proposed realizations, *printer* retains its first-syllable lexical stress. The primary mark ˈ and secondary mark ˌ identify stress positions in a stated lexical analysis; they are not measurements of loudness.

**Prominence** is relational: a syllable stands out against others in a particular domain. Duration, vowel quality, pitch-related movement and intensity can contribute. These cues do not have to increase together. A word can contain a lexically stressed syllable without receiving a pitch accent in a particular utterance.

Keep at least four locations explicit: the word's stress-bearing syllable, an utterance's accented syllable, the contextual focus span, and a phrase edge. A reader who treats all four as “the stressed word” loses the distinctions needed to interpret the next sections. [Phonology](english-phonology-system.md#lexical-stress) supplies the lexical organization; the selected [ToBI text](../references/mit-2006-tobi-tutorial.md) distinguishes prominence and phrasing.

## Pitch accents

A **pitch accent** is a tonal event associated with a prominent syllable under the adopted intonational analysis. It is different from a regional “accent,” a word's IPA stress mark, or any arbitrary high point in a pitch track.

The selected ToBI conventions use H and L for relatively high and low tonal targets, with a star marking the tone associated with an accented syllable. Thus H* and L* name different accent categories; a low target can still signal prominence. These are category labels interpreted in a speaker's range and context, not fixed frequencies in hertz. More complex accents and downstep exist, but are not derived or comprehensively catalogued here.

A phrase can contain more than one pitch accent. Its final pitch accent is often called the **nuclear accent** in descriptions of English intonation. That position is not necessarily the final word: a correction such as *MAYA repaired the printer* can leave later words without another accent. Do not identify the nucleus by selecting the largest numerical F0 value or by assuming it must occur at the rightmost written word.

Accent placement and accent type are separate decisions. Placing an accent on *Maya* says where an event belongs; deciding between a high, low or complex accent requires evidence about the realization and the adopted system. Without audio, the examples here propose locations and alternatives rather than claim exact ToBI labels.

## Phrasing and boundaries

**Prosodic phrasing** groups speech into units. Boundaries can be cued by tonal events, lengthening and sometimes pauses. No single cue is a necessary or sufficient universal boundary test: a boundary may lack silence, and a hesitation pause need not establish the intended syntactic grouping.

The selected ToBI account distinguishes an **intermediate phrase** from a larger **intonational phrase**. Phrase accents such as H- or L- mark an intermediate phrase's tonal ending; a full intonational phrase additionally has a boundary tone, conventionally marked with %. A pitch accent belongs at a prominent syllable, whereas these edge events concern phrase endings. Section 2.8 uses break index 3 for an intermediate-phrase boundary and 4 for a full intonational-phrase boundary. The numbers are annotation categories, not a count of words or seconds of silence.

A schematic organization is:

```text
Full intonational phrase
  Intermediate phrase: one or more pitch accents + phrase accent
  Optional further intermediate phrases
  Final boundary tone
```

This describes the selected framework, not a universal hierarchy or a transcription of the examples. A final pitch accent can precede unaccented words before the phrase ends. Separating the accent from the edge explains why a high final pitch need not identify a high accent on the final word.

Syntactic structure helps constrain grouping without determining it uniquely. In *The report that Maya prepared arrived*, the Subject includes the relative clause. Length, rate and context can support different spoken groupings of that Subject. Written brackets and commas do not supply measured pauses. The Syntax interface below retains this distinction locally.

## Intonation and interpretation

**Intonation** is the organization of pitch over a phrase or utterance. An accent-and-boundary analysis describes it as a configuration of events rather than one label attached to a whole sentence. The ending and an earlier accent can differ: a low accent can be followed by a high ending, and a high accent by a low ending.

Intonational form does not have a one-to-one relation with sentence type or speaker intention. A declarative *Maya repaired the printer?* can be used to seek confirmation; an information-seeking *Who repaired the printer?* can have a falling ending. Neither example licenses “rise means question” or “fall means statement” as universal decoding rules.

For a constructed comparison, hold *Maya repaired the printer* fixed and vary one proposed property. Moving prominence from *Maya* to *printer* can change the salient alternatives. Changing the ending while holding the prominent word fixed can contribute to a different conversational stance or continuation pattern. The context and variety must still be supplied; these schematic changes do not establish one emotion, attitude or illocution for every speaker.

The [ToBI overview](../references/mit-2006-tobi-tutorial.md#additional-overview-and-phrasing-passages) explicitly treats the mapping from prosodic categories to functions as an object of investigation. Full intonational meaning, voice-quality effects and comparisons across English varieties remain further work.

## Rhythm and timing

**Rhythm** concerns patterns of timing and prominence across speech. Describing English as stress-timed does not mean that all intervals between stresses are exactly equal. Segment identities, syllable structure, speaking rate, phrase position and communicative context affect timing.

Compare the constructed strings *Maya sent reports* and *Maya could have sent the reports*. The second has more syllables that could occur between prominent positions. A speaker might compress some material, lengthen the interval, or use different grouping. A label such as stress-timed cannot choose among those realizations or justify deleting sounds from a transcription.

Keep several comparisons apart:

| Timing question | Relevant observation | Invalid shortcut |
|---|---|---|
| Is a particular syllable longer? | Duration of matched tokens in a stated context | Assuming its stress mark supplies milliseconds |
| Is phrase-final material lengthened? | Comparable segments in phrase-final and other positions | Treating every long vowel as a boundary |
| Are intervals between prominences similar? | Defined landmarks across identified utterances | Assuming an exactly periodic beat |
| Does faster speech change the pattern? | Matched recordings with rate and context recorded | Prescribing one obligatory reduction |

The inspected ToBI phrasing prose supports considering phrase-final lengthening alongside tonal cues. A full theory of English rhythm, numerical thresholds and empirical rate effects are not supplied. These are questions for comparing evidence, not measurements made in this repository.

## Connected speech and reduction

Prosodic organization conditions the environments in which segmental changes are investigated. **Reduction** can make a sound less fully articulated while retaining it; **elision** proposes that a segment lacks a separate realization in a reduced analysis; **assimilation** changes a property toward that of a neighbor. **Linking** concerns continuity across a boundary and does not itself imply deletion.

For a schematic General American comparison, unstressed *you* may be [jə] rather than [ju]. A vowel remains, so the comparison illustrates reduction rather than deletion. In a possible *asked* comparison [æskt] versus [æst], [k] is absent from the second segmental representation. Stress, rate and phrase context are conditions to investigate, not proof that either change occurred in a particular token.

**Coarticulation** is overlap among speech gestures. A weak or inaudible release can arise while a closure remains; failure to hear a burst therefore does not by itself establish elision. Separate the prosodic hypothesis about prominence from the phonetic hypothesis about what was produced. The [Anderson passages](../references/anderson-2018-essentials-of-linguistics.md#connected-speech-passages) support selected reduction and omission examples. No elision is required merely to force the words into an assumed rhythm.

## Prosodic representation and acoustic evidence

A useful representation keeps the wording, lexical stress, proposed accents, phrase edges, context and measurements in separate layers. The [ToBI overview](../references/mit-2006-tobi-tutorial.md#additional-overview-and-phrasing-passages) describes time-aligned annotation tiers and the recording underlying them. Our plain-language table is a teaching aid, not a completed ToBI annotation.

| Layer | What it represents | Evidence boundary |
|---|---|---|
| Words and syllables | Segment sequence and proposed lexical organization | Spelling is not an exact sound transcript |
| Stress and accents | Lexical prominence and utterance tonal events | A proposed label is not a measured peak |
| Phrasing | Group spans and edge events | Punctuation does not specify every boundary |
| Context | Current question, intended alternatives and use | A written sentence may leave these unresolved |
| Acoustic description | F0 in voiced intervals, duration, intensity and method | An identified recording is required |

**Fundamental frequency**, F0, describes periodic repetition in the signal; perceived pitch is related to it but not identical. **Duration** measures an interval; **intensity** is a different physical property. High F0, greater intensity and perceived prominence are not interchangeable. Voiceless intervals, irregular voicing and tracking errors can complicate a pitch trace. A missing or doubled track is not automatically an intended tonal event.

A complete observational record identifies speaker or variety, context, recording, annotated span, measurement method and uncertainty. In this document the recording and measured-value fields remain absent. They cannot be filled by capitalizing a word or drawing an attractive contour.

## Worked analysis

Hold *Maya repaired the printer* constant. Bold marks a possible main accented word, not a measured loudness or full contour.

| Contextual question | Possible response | Intended focus span |
|---|---|---|
| Who repaired the printer? | **Maya** repaired the printer. | Maya, among possible repairers |
| What did Maya repair? | Maya repaired the **printer**. | The printer, among possible objects |
| What did Maya do? | Maya repaired the **printer**. | Repaired the printer, among possible activities |

For the second response, a locally complete schematic account is:

| Layer | Constructed analysis |
|---|---|
| Word stress | *Printer* /ˈprɪntər/ has primary stress on its first syllable |
| Pitch accent location | Proposed main accent on that first syllable |
| Focus | The NP *the printer* answers the stated question |
| Grouping | One proposed phrase containing the response |
| Intonation | A falling ending is one candidate, not dictated by the transcript |
| Timing and signal | No recorded durations, intensity values or pitch track |

Changing the question to *Who repaired the printer?* can shift the main accent to Maya without shifting printer's lexical stress. Changing it to *What did Maya do?* can expand focus to the VP while keeping the proposed accent on printer. Changing the response into a confirmation request can motivate a different ending without changing which word is intended to contrast. Those changes affect distinct layers.

Now add an already established object: *The printer was broken. What did Maya do with it?* The answer *She REPAIRED the printer* can make the action contrast salient while the object is given. This possible pattern illustrates interaction between givenness and prominence, not a mandatory realization rule. [Krifka's selected discussion](../references/krifka-2008-information-structure.md#givenness-and-accent) supports the distinction; the particular examples remain authored and unrecorded.

## Interfaces

Prosody overlaps phonological organization, syntactic grouping, contextual interpretation and physical realization. These correspondences are constraints to investigate, not a sequence of independent processing modules.

### Interface with Phonology

Phonology supplies segment categories, syllable structure and lexical stress; Prosody relates them to utterance accents and phrasing. Keep a segment string, syllable parse, lexical stress positions, proposed accents and edges in separate fields. The counterpart is explained in [Phonology](english-phonology-system.md#interface-with-prosody).

In *The students repaired the printers*, a who-question and a what-question can favor prominence on different words while their lexical forms stay the same. A lexically stressed syllable need not receive the strongest utterance prominence. Stress, reduction and boundary organization can interact, but this does not supply a complete metrical theory or a universal realization algorithm. Compare the same words across contexts instead of rewriting lexical entries for every sentence accent.

### Interface with Phonetics

Prosody proposes accent and grouping categories; Phonetics investigates their signal realization. Represent `prominence pattern {accent_location, phrasing, variety}` as constraining `prosodic acoustic description {pitch_pattern, duration, intensity, measurement_method, recording_id}`. The relation uses `kps:constrains`; it does not predict numerical values. The counterpart is explained in [Phonetics](english-phonetics-system.md#interface-with-prosody).

For *Who repaired the printer? — Nina repaired the printer*, an analyst might predict prominence on Nina. A recording could realize that prominence through several cues. Capitalization does not specify an F0 contour. Preserve the question and token identity, compare the annotation with the signal, and retain uncertainty where cues disagree. The selected ToBI prose supports separating labels and realization; no measurements of this example are claimed.

### Interface with Syntax

Syntax supplies constituents, dependencies and clause structure; Prosody supplies candidate spoken groups. In `[The report that Maya prepared] [arrived]`, the first bracket is a Subject NP containing a relative clause. A proposed realization can group the whole Subject or use finer phrasing depending on length, context and rate. Neither brackets nor a written comma establish a pause duration.

The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-prosody). Compare syntactic and prosodic spans separately; a pause after *report* would need to be heard and interpreted in context before drawing a grammatical conclusion. The selected ToBI overview motivates a structure–grouping connection, but this particular analysis remains authored. It does not establish one-to-one constituency or deterministic recovery of syntax from acoustics.

### Interface with Information Structure

Information Structure supplies the current issue and focus alternatives; Prosody supplies possible prominence and phrasing. In *Nina repaired the printer*, focus can be Nina under *Who repaired it?*, the printer under *What did Nina repair?*, or the VP under *What did Nina do?* The latter two may share a main accent on printer. The counterpart and full comparison are explained in [Information Structure](english-information-structure-system.md#interface-with-prosody).

A focus span, an accented syllable and the highest measured pitch are three different things. Given expressions can also be accented contrastively, and a wider focus domain can contain deaccented given material. Krifka's inspected passages add selected support for these interactions; Roberts remains abstract-only. No full focus-projection derivation, fixed contour-to-meaning dictionary or recorded response is provided.

## Evidence and limits

The [MIT ToBI Reference](../references/mit-2006-tobi-tutorial.md) records the selected overview, accent and phrasing passages. [Anderson](../references/anderson-2018-essentials-of-linguistics.md) supplies selected suprasegmental and connected-speech support. [Krifka](../references/krifka-2008-information-structure.md) supplies selected givenness/focus distinctions; [Roberts](../references/roberts-2012-information-structure.md) supplies only the abstract-level QUD connection. The seven-area organization and comparisons are authored synthesis.

This Model remains **provisional and independently unreviewed**. It does not provide all ToBI labels, a full metrical or rhythm theory, a complete intonational semantics, cross-variety inventories or measured speech. For actual data, inspect competing annotations and preserve uncertain boundaries. The highest F0 alone cannot prove focus: speaker range, edge tones, segmental context and tracking error may matter.

[Stress](../concepts/stress.md), [prosody and intonation](../concepts/prosody.md), [connected speech](../concepts/connected-speech.md) and [analyze sound realization](../methods/analyze-sound-realization.md) provide optional detail and a procedure for investigation.
