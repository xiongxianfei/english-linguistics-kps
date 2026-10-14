---
id: "english:model:english-syntax-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["syntax"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:walter-2016-modal-verbs-basics", "english:reference:british-council-undated-grammar-reference"]
uses_concepts: ["english:concept:category-and-function", "english:concept:constituency", "english:concept:head-and-dependent", "english:concept:complement-and-modifier", "english:concept:finiteness", "english:concept:relative-clause", "english:concept:auxiliary-chain", "english:concept:tense-and-aspect", "english:concept:do-support-and-inversion", "english:concept:clause-architecture", "english:concept:inflection", "english:concept:paradigm-and-syncretism", "english:concept:lexical-selection", "english:concept:object-and-pp-complement", "english:concept:valency-and-argument-structure", "english:concept:semantic-role", "english:concept:phrase-and-clause", "english:concept:prosody", "english:concept:predicative-complement", "english:concept:complement-clause", "english:concept:coordination-and-subordination", "english:concept:wh-dependency"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-morphology-system", "english:model:english-semantics-system", "english:model:english-prosody-system"]
system_domain: "syntax"
---

# English syntax system

Syntax explains how words form phrases and clauses, which expressions depend on which, and how constructions organize grammatical functions. Use this Model to build and justify a structural analysis: identify complete units, distinguish their categories from their functions, explain verb forms and clause relationships, and compare alternative groupings. A connected student-and-printer example develops from a simple clause into a sentence with auxiliaries and embedded clauses.

The introductory coverage follows the outline's six areas: categories and functions, constituents and local dependencies, phrases and clauses, complement constructions, verb and auxiliary structure, and clause combination and dependencies. Interfaces connect these explanations with Morphology, Lexicon, Semantics and Prosody. The examples are constructed for ordinary standard-English readings. The account remains provisional; it uses NP terminology and a descriptive Subject/Predicate analysis rather than claiming one universal syntactic framework.

## Contents

- [Categories and functions](#categories-and-functions)
- [Constituents and local dependencies](#constituents-and-local-dependencies)
- [Phrases and clauses](#phrases-and-clauses)
  - [Clause types](#clause-types)
- [Complement constructions](#complement-constructions)
- [Finiteness and agreement](#finiteness-and-agreement)
- [Auxiliary selection](#auxiliary-selection)
- [Questions and negation](#questions-and-negation)
- [Clause combination and dependencies](#clause-combination-and-dependencies)
- [Worked analysis](#worked-analysis)
- [Nested clauses](#nested-clauses)
- [Interfaces](#interfaces)
  - [Interface with Morphology](#interface-with-morphology)
  - [Interface with Lexicon](#interface-with-lexicon)
  - [Interface with Semantics](#interface-with-semantics)
  - [Interface with Prosody](#interface-with-prosody)
- [Checking a proposed analysis](#checking-a-proposed-analysis)
- [Evidence and open questions](#evidence-and-open-questions)

## Categories and functions

A **category** identifies a kind of expression, such as noun, verb or noun phrase (NP). A **function** identifies its relationship within a construction, such as Subject, Object or modifier. In *The student repairs the printer*, both *the student* and *the printer* are NPs, but they have different functions. A noun is not automatically a Subject, and the Subject is the complete phrase rather than just its head noun.

| Dimension | Question | Example distinction |
|---|---|---|
| Category | What sort of expression is this? | Noun, verb, NP, PP, clause |
| Constituency | Which words form a structural unit? | The complete object NP versus only its head noun |
| Dependency | Which element locally licenses or modifies which? | A verb and its PP complement; the preposition and its NP |
| Function | What job does the unit perform here? | Subject, Object, complement, modifier |
| Clause architecture | How are predicates, auxiliaries and clauses related? | Finite auxiliary plus a selected nonfinite verb form |

Word categories are supported by grammatical behavior, including distribution and inflection, rather than meaning alone. The [Lexicon Model](english-lexicon-system.md#lexical-categories) explains why noun and verb uses of *run* need separate descriptions. Here the question is how a categorized expression participates in a larger structure. [Anderson 7.1 and 8.6](../references/anderson-2018-essentials-of-linguistics.md#lexical-category-and-selection-passages) provide selected background for behavioral categories and complement selection.

Function also differs from **semantic role**, a participant's relation to an event or state. In *The printer was repaired*, the Subject is what underwent repair, not its agent. The [Semantics interface](#interface-with-semantics) makes this distinction explicit.

## Constituents and local dependencies

A **constituent** is a unit within a proposed structure. A **head** organizes a headed phrase and helps determine its category and combination possibilities. **Dependents** stand in local relationships to that head. In *near the windows*, NEAR heads a prepositional phrase (PP), and *the windows* complements it. If that PP modifies *student*, the inner NP still depends on NEAR rather than directly becoming another Subject.

A **complement** is licensed by a head or construction's selection pattern; a **modifier** supplies a less selected elaboration. In *repairs the printer carefully*, the Object belongs to REPAIR's illustrated complement frame, while *carefully* modifies the manner of repair. Neither semantic importance nor whether a phrase can be omitted is a sufficient test: a complement can be left unexpressed in a suitable use, and a modifier can supply essential information for the speaker's purpose.

Groupings need evidence. [Anderson 8.3](../references/anderson-2018-essentials-of-linguistics.md#syntax-coverage-passages) presents replacement, movement and clefting as constituency diagnostics. For a constructed comparison:

| Candidate unit | Diagnostic | Result to interpret |
|---|---|---|
| *the printer* in *The student repaired the printer* | Replace it with *it* | *The student repaired it* preserves the Object position |
| The same candidate | Put it in a cleft | *It was the printer that the student repaired* highlights that unit |
| *after lunch* in *The student repaired the printer after lunch* | Front the phrase | *After lunch, the student repaired the printer* supports treating the time expression as a unit |

These are converging clues, not proofs of a unique tree. Replacement can fail because of the chosen substitute; fronting and clefting have contextual and grammatical restrictions. A proposed unit's failure on one test does not alone establish that it is not a constituent. The [constituency Method](../methods/analyze-constituency.md) develops the investigation procedure.

## Phrases and clauses

A **phrase** is a structural unit organized around a head in this working account. It can contain one word or several; length does not define it. Common labels include NP, verb phrase (VP), adjective phrase (AdjP), adverb phrase (AdvP) and PP. In *very careful*, CAREFUL heads an AdjP; in *quite carefully*, CAREFULLY heads an AdvP. A phrase can contain another phrase or a clause.

A **clause** has a predicational organization: it presents a property, situation or relation and associated grammatical structure. In the simple finite clause *The student repairs the printer*, the Subject NP combines with the Predicate VP *repairs the printer*. Here VP includes the verb and its dependents. Some teaching grammars use “verb phrase” more narrowly for a verb chain, so check the convention before comparing diagrams.

Not every clause has an overt Subject: *Repair the printer* is an imperative, and *to repair the printer* is a nonfinite clause in *The student hopes to repair the printer*. An understood repairer still needs interpretation. A complete theory of control and raising is beyond this introductory representation.

A **main clause** is not subordinate to another clause. A **subordinate clause** occurs dependently in a larger construction; it can itself contain a further clause. A written sentence can contain more than one clause. Conversely, a verb chain such as *may have been repairing* is not four independent clauses in the descriptive account used here.

### Clause types

Clause type describes grammatical organization, not a guaranteed communicative purpose. Compare these constructed forms:

| Type | Example | Structural point |
|---|---|---|
| Declarative | *The student repaired the printer.* | Ordinary Subject-before-finite-verb order in this example |
| Interrogative | *Did the student repair the printer?* | Auxiliary before Subject |
| Imperative | *Repair the printer.* | Plain verb with an understood addressee in this example |
| Exclamative | *What a careful repair the student made!* | An exclamative phrase is fronted; this is not an ordinary request for an answer |

An interrogative can serve as a request, as in *Could you repair the printer?* Pragmatics explains that use; syntactic form alone does not determine it. Embedded interrogatives, subject questions and marked constructions need their own patterns, so the table is an introduction rather than a transformation recipe for every clause.

## Complement constructions

Expressions following a verb do not all have the same function. The head, sense and construction matter as well as position.

| Constructed example | Complement analysis | Distinction preserved |
|---|---|---|
| *Maya repairs the printer.* | NP Direct Object of REPAIR | Object is the full NP |
| *The result depends on the weather.* | PP complement of DEPEND; NP complement of ON inside it | An NP inside a PP is not the higher verb's Object |
| *Maya became a technician.* | NP predicative complement | It classifies Maya rather than introducing an ordinary Object participant |
| *The printer seems unreliable.* | AdjP predicative complement | The property is attributed to the Subject |
| *Maya thinks that the printer works.* | Finite declarative complement clause | The embedded clause has its own Subject and Predicate |
| *Maya wonders whether the printer works.* | Finite interrogative complement clause | Embedded question type differs from a declarative complement |
| *Maya hopes to repair the printer.* | Nonfinite complement clause | The understood Subject needs interpretation; no overt tense is carried by REPAIR |

A **predicative complement** attributes a property, classification or identity to a **predicand**, the expression about which the predication is made. Compare *became a technician* with *met a technician*: the latter ordinarily introduces another participant. In *They painted the door blue*, *the door* is Object and *blue* is predicative of that Object. An NP after a verb is therefore not enough evidence to label it Object.

A complement clause's external function and internal structure must be recorded separately. In *Maya thinks that the student repaired the printer*, the whole subordinate clause complements THINK; inside it, *the printer* is REPAIR's Object, not THINK's NP Object. Anderson 8.6 supplies bounded support for complement-sensitive patterns, including clausal complements. The local predicative and nonfinite comparisons remain authored explanations with fuller claim-level support pending.

## Finiteness and agreement

**Finiteness** concerns verb form and clause licensing, not simply whether an event occurs now. Compare *The student repaired the printer* with *The student has repaired the printer*: REPAIRED is finite past in the first sentence and a past participle after finite HAS in the second. Identical spelling does not establish identical grammatical status. [Anderson 8.5](../references/anderson-2018-essentials-of-linguistics.md#syntax-coverage-passages) supports distinguishing forms whose spellings coincide.

In the ordinary finite declarative chains used here, the first verb is finite and later verbs have locally selected nonfinite forms. This does not mean every plain form is nonfinite: *They repair printers* contains finite present *repair*. Nor does finiteness guarantee a visible tense suffix: central modals and irregular forms require their own descriptions.

**Agreement** connects a controller's grammatical features with a form in a construction. In *The student near the windows repairs the printer*, singular STUDENT controls the illustrated third-person-singular agreement despite the nearer plural WINDOWS. Change the head to *students*, and the corresponding form is *repair*. This is a bounded standard-English contrast, not a universal nearest-noun rule or an exhaustive account of collective and notional agreement.

## Auxiliary selection

An **auxiliary** participates in grammatical constructions such as tense/aspect, voice, modality, inversion and negation. For a chain, distinguish each form from the construction it helps express:

| Selecting auxiliary | Selected form | Construction |
|---|---|---|
| Central modal | Plain | Modal |
| Perfect HAVE | Past participle | Perfect |
| Progressive BE | Ing form | Progressive |
| Passive BE | Past participle | Verbal passive |
| Support DO | Plain | Support for relevant finite constructions |

Read *may have been working* through its local connections: MAY selects plain HAVE; perfect HAVE selects the past participle BEEN; progressive BE, realized as BEEN, selects WORKING. In *has been reviewed*, perfect HAVE selects BEEN, but this occurrence of BE is passive and selects REVIEWED. The form BEEN does not by itself identify progressive or passive structure.

When these auxiliaries combine in the central patterns, the relative order is modal, perfect, progressive, passive, then lexical verb; particular chains use only some of those options. This is a description of the illustrated system, not an instruction to combine every option in every context. BE with an adjectival participle is not automatically a verbal passive, and a modal-like expression such as *ought to* does not follow every central-modal rule.

[Walter](../references/walter-2016-modal-verbs-basics.md#inspected-contribution) supports central-modal plain-form selection: *may deliver*, not *may delivers*, even with *she*. The [British Council verb-chain passage](../references/british-council-undated-grammar-reference.md#verb-chains) supplies selected support for perfect, progressive, passive and combined forms. Interpretation of tense, aspect and modality also requires Semantics; a construction label alone is not a complete account of meaning. Semi-auxiliaries, dialectal combinations and a full account of chain restrictions remain outside this introduction.

## Questions and negation

**Subject–auxiliary inversion** places the relevant finite auxiliary before the Subject in ordinary main-clause questions. **Do-support** supplies DO when the relevant construction needs an auxiliary and none is available. Tense and agreement are then carried by DO; the lexical verb is plain.

| Declarative | Main interrogative | Negative declarative |
|---|---|---|
| *The student repairs it.* | *Does the student repair it?* | *The student does not repair it.* |
| *The student repaired it.* | *Did the student repair it?* | *The student did not repair it.* |
| *The student has repaired it.* | *Has the student repaired it?* | *The student has not repaired it.* |
| *The student is ready.* | *Is the student ready?* | *The student is not ready.* |

The last row matters: BE can invert without another verb following it. In *may have been repairing*, the question begins *May the student have been repairing …?*; it does not move every verb before the Subject. [Anderson 8.11](../references/anderson-2018-essentials-of-linguistics.md#syntax-coverage-passages) supports the basic DO, auxiliary and BE contrasts. Its particular movement analysis is not required by this descriptive representation.

Compare *Who repaired the printer?* with *What did the student repair?* The first asks for the Subject and does not require ordinary do-support; the second asks for the Object. Compare the main question *Did Maya repair it?* with *I wonder whether Maya repaired it*: the embedded interrogative has its own pattern, without main-question inversion in this ordinary standard-English use. Emphatic questions and other varieties require separate treatment.

Negation is not confined to inserting NOT: *Nobody repaired it* is already negative without that operation. The table addresses selected clause-negation patterns, not every negative expression, scope reading or dialect. In particular, lexical HAVE and negative constructions vary; a source's judgment for one variety is not a universal ban.

## Clause combination and dependencies

**Coordination** links units of comparable structural status. In *The student [repaired the printer] and [tested the scanner]*, the two bracketed VPs share a Subject. In *[The student repaired the printer] and [Maya tested the scanner]*, whole clauses are coordinated. The word AND alone does not tell us which units are joined. Coordination with shared or omitted material needs more analysis than simply counting conjunctions.

**Subordination** places a clause dependently within another construction. A **complement clause** is selected by a head or construction; an **adjunct clause**, such as *because the printer was faulty*, adds a relation such as reason. A **relative clause** modifies a nominal expression in the account used here: *the printer [that Maya tested __]* identifies a printer through a relation to the testing event. The blank marks an understood Object dependency; it is notation, not a claim that speech contains an audible empty word.

A **wh-dependency** links an interrogative or relative expression to its grammatical role. In *Which printer did Maya repair __?*, the fronted expression is associated with REPAIR's Object. In *Who did Maya speak to __?*, the dependency is with the complement of TO. It must not be flattened into SPEAK's Direct Object. [Anderson 8.10](../references/anderson-2018-essentials-of-linguistics.md#syntax-coverage-passages) supports relating an interrogative expression to its role despite a different surface position.

A dependency can cross a clause boundary: *Which printer do you think Maya repaired __?* The associated Object position is inside the embedded clause. “Long-distance” does not mean unconstrained; extraction restrictions and competing analyses need further study. Relative marking also differs among frameworks: THAT is treated here as a relative marker without requiring the reader to settle whether it belongs to a pronoun or subordinator category.

Compare *the claim [that Maya repaired the printer]* with *the printer [that Maya repaired __]*. The first supplies the claim's content, with an overt Object inside the clause. The second contains a relative dependency involving the modified nominal. The initial word THAT alone cannot classify the clause. These relative, coordination and content-clause comparisons are constructed applications, not a complete source-verified inventory.

## Worked analysis

Begin with *The student repairs the printer*. Expand the Subject to *the student near the windows*:

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

The Subject is the whole NP *the student near the windows*. Singular STUDENT controls the illustrated form REPAIRS; WINDOWS is inside a modifier PP. *The windows* is not a second Subject, and the Object is *the printer*, not merely PRINTER. Replacing the whole Subject with *she* preserves the grouping; clefting the Object provides a second type of evidence for its span.

Now change one structural feature at a time:

| Development | Constructed sentence | What changes |
|---|---|---|
| Auxiliary chain | *The student near the windows may have been repairing the printer.* | MAY is finite; the remaining forms are locally selected |
| Relative modification | *The student near the windows may have been repairing the printer that Maya had tested.* | The Object NP contains a relative clause with an understood Object of TEST |
| Reason clause | *Because the printer was faulty, the student near the windows may have been repairing the printer that Maya had tested.* | A reason adjunct clause is added; it does not become another Object |

For the final sentence, the following bracketed account explicitly chooses the reason clause as an adjunct of the main clause:

```text
[Clause
  [Adjunct clause Because [NP the printer] [VP was [AdjP faulty]]]
  [Subject NP the student [Modifier PP near [NP the windows]]]
  [Predicate VP may have been repairing
    [Object NP the printer
      [Relative clause that [NP Maya] [VP had tested __]]]]]
```

The displayed analysis has three finite clauses, with finite WAS, MAY and HAD. REPAIR's Object is the entire NP *the printer that Maya had tested*. TEST's understood Object belongs inside the relative clause; it is not an extra overt Object of REPAIR. The auxiliary chain does not multiply the finite-clause count. The display simplifies internal VP structure and does not settle every possible scope of the reason relation.

A question changes another relationship: *Which printer may the student near the windows have been repairing __?* The complete Subject remains after MAY, while the questioned NP is associated with REPAIR's Object. In the passive comparison *The printer may have been repaired by the student*, PRINTER becomes Subject and the final verb is a past participle. The basic repair participants can remain, even though grammatical functions and auxiliary structure change.

These comparisons connect the explanations without claiming that one sentence demonstrates the whole grammar. Judgments, alternative attachments and the intended context must still be checked.

## Nested clauses

Retain a second, independently useful constructed passage:

> Although the roads were icy, Anna sent the reports that Maya had prepared to Leo. He thanked her because he needed them.

```text
[Clause
  [Adverbial Although the roads were icy]
  [NP Anna]
  [VP sent
      [NP the reports [Relative that Maya had prepared __]]
      [PP to [NP Leo]]]]
[Clause He [VP thanked her [Adverbial because he needed them]]]
```

In the intended reading, the *to*-PP attaches to SEND, not PREPARE. The full Object is *the reports that Maya had prepared*. Across both sentences this working account counts two main clauses, two finite adverbial clauses and one finite relative clause. *Had prepared* is one auxiliary chain. The relative ends before the recipient PP; simply counting verbs or attaching each PP to the nearest verb loses that structure.

The flat VP display and treatment of ALTHOUGH/BECAUSE as clause markers are declared simplifications. Alternative clause-layer analyses can differ while still needing to represent nesting. The companion constructed fixture records token spans: they must be nested or disjoint in this tree representation, not partially crossing. It is a consistency target for the selected reading, not corpus evidence or proof of a unique parse. Full claim-level support for this passage remains pending.

## Interfaces

Word forms, lexical senses, grammatical functions, participant roles and spoken grouping describe different aspects of the same expression. Their relationships constrain an analysis without collapsing those descriptions or defining a sequential processing pipeline.

### Interface with Morphology

Morphology describes grammatical forms and their features; Syntax identifies the construction and controller relevant to agreement and finiteness. The counterpart is explained in [Morphology](english-morphology-system.md#interface-with-syntax).

| Endpoint | Schematic fields |
|---|---|
| Grammatical word features | Lexeme, number, person, tense, word form |
| Agreement and finiteness pattern | Construction, controller, agreement form, finiteness |

This is a `kps:constrains` relationship, not a measured transfer operation. In *This report is ready* and *These reports are ready*, number corresponds to IS versus ARE. In *The report near the windows is ready*, singular REPORT remains the relevant head. **Syncretism**, where one form realizes different feature combinations, means a feature distinction need not produce a visible spelling contrast.

Compare forms while controlling construction and variety. Collective nouns and notional agreement need additional qualifications; the nearest written noun is not a general controller rule. The examples remain authored contrasts with independent support for a full agreement account pending.

### Interface with Lexicon

Sense-specific lexical information helps license complements; Syntax represents their local hierarchy. The counterpart is explained in [Lexicon](english-lexicon-system.md#interface-with-syntax).

| Lexical sense | Working frame | Local distinctions |
|---|---|---|
| DEPEND dependence | Subject + V + on-PP | NP inside PP complements ON |
| DISCUSS transitive | Subject + V + NP | NP is Direct Object |
| PUT placement | Subject + V + NP + location complement | Location is not another Object |
| RUN management | Subject + V + NP | Different from locomotion use |

For *The result depends on the weather*, DEPEND's complement is *on the weather*; ON's complement is *the weather*. For *Maya put the book on the table*, the Object and location complement play distinct grammatical roles. A generic SVO template cannot supply these distinctions.

Compare frames, omission and meaning shifts, counting semantic arguments separately from overt NP objects. Anderson 8.6 supports complement-sensitive subcategorization, not independent verification of every frame. Constructional accounts can locate some licensing information outside individual entries, and varieties or senses can differ.

### Interface with Semantics

Syntax identifies grammatical functions; Semantics describes participants and their relationships. A construction can preserve participant relations while changing their grammatical realization. The counterpart is explained in [Semantics](english-semantics-system.md#interface-with-syntax).

| Construction | Giver | Recipient | Theme |
|---|---|---|---|
| Leo gave Maya a prize | Subject | Indirect Object | Direct Object |
| Leo gave a prize to Maya | Subject | NP inside to-PP | Direct Object |
| Maya was given a prize by Leo | NP inside by-PP | Subject | Retained Object |

Here **Recipient** identifies the receiver and **Theme** the transferred item. The passive redistributes functions without requiring a different giver or recipient. Compare *The glass broke* with *Leo broke the glass*: this causative alternation adds a causer to the explicit description. In *The noise frightened Maya*, the Subject describes a stimulus and the Object an experiencer without passive morphology.

Ask which participants are explicit, implicit, added or redistributed. Dative alternation has lexical, semantic and discourse restrictions; the table does not claim complete synonymy. Anderson's recorded passive discussion supports separating functions and roles. The local dative, causative and experiencer comparisons remain provisional, and role inventories vary across theories.

### Interface with Prosody

Syntactic constituents constrain possible spoken grouping without being identical to prosodic phrases. The counterpart is explained in [Prosody](english-prosody-system.md#interface-with-syntax).

| Syntactic description | Prosodic description | Required distinction |
|---|---|---|
| NP or clause span | Candidate prosodic phrase span | Similar boundaries are not identity |
| Embedded relative clause | Possible grouping around the modifier | A pause does not prove a unique parse |
| Constituent length and embedding | Rate-sensitive phrasing options | Optional phrasing is not a new syntax by itself |

In *[The report that Maya prepared] [arrived]*, the Subject contains a relative clause. A spoken version might group the whole Subject or use finer phrasing depending on length, focus and rate. Written brackets specify neither silence durations nor exact intonation. A proposed pause after REPORT needs comparison with an actual spoken target before it can count as evidence.

Record both representations and compare plausible alternatives rather than inferring a unique parse from a pause. This remains a framework-sensitive authored interface account; no new recording, acoustic measurement or independent source verification is supplied.

## Checking a proposed analysis

Preserve the expression and intended reading, mark complete constituent spans, name their categories and functions, and compare at least one plausible alternative. Use appropriate diagnostics together; record what each actually supports. Auxiliary selection, grammatical function and semantic role should not silently substitute for one another.

If a constituent test fails, consider replacement choice and context before rejecting the unit. If a PP can attach at more than one level, retain the ambiguity until evidence or intent resolves it. Reject partially crossing spans for the simple tree representation used here, while recognizing that discontinuous constructions may require a different representation. A single analyst's acceptability judgment is not a speaker study.

## Evidence and open questions

The [Anderson Reference](../references/anderson-2018-essentials-of-linguistics.md#syntax-coverage-passages) records selected constituency, verb-form, question and negation passages alongside earlier complement, adjunct and function/role contributions. [Walter](../references/walter-2016-modal-verbs-basics.md) supplies bounded central-modal support; the [British Council record](../references/british-council-undated-grammar-reference.md#verb-chains) adds selected auxiliary combinations. These sources support particular distinctions, not every constructed example or the entire Model.

The category, phrase and clause framework is a declared working choice. NP versus DP accounts and analyses using tense/complementizer clause layers can differ. Ellipsis, extraction restrictions, control and raising, supplementary relatives, noncanonical word order, complex predication and dialect-sensitive agreement need fuller treatment. These are remaining depth and evidence gaps, not claims that the current outline exhausts English syntax. No independent expert review, observed learner result or corpus annotation study is claimed.

Reusable [category and function](../concepts/category-and-function.md), [constituency](../concepts/constituency.md), [head and dependent](../concepts/head-and-dependent.md), [complement and modifier](../concepts/complement-and-modifier.md), [finiteness](../concepts/finiteness.md) and [relative clause](../concepts/relative-clause.md) explanations provide optional depth. Source additions to this Model do not automatically validate those Concepts or the connected Methods and Practices.
