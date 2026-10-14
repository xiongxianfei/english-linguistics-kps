---
id: "english:model:english-semantics-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["semantics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:richards-2022-semantics", "english:reference:yablo-2015-modal-semantics", "english:reference:british-council-undated-grammar-reference", "english:reference:bhatt-2003-implicature", "english:reference:fox-menendez-benito-2006-presupposition"]
uses_concepts: ["english:concept:compositionality", "english:concept:reference-and-denotation", "english:concept:semantic-role", "english:concept:quantification-and-scope", "english:concept:negation-and-entailment", "english:concept:tense-and-aspect", "english:concept:modality", "english:concept:semantic-predicate", "english:concept:situation-type", "english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:lexical-selection", "english:concept:object-and-pp-complement", "english:concept:valency-and-argument-structure", "english:concept:contextual-resolution", "english:concept:implicature", "english:concept:presupposition", "english:concept:common-ground"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-syntax-system", "english:model:english-pragmatics-system"]
system_domain: "semantics"
---

# English semantics system

Semantics explains how expressions contribute meaning, how those contributions combine, and what follows under a stated interpretation. A reader should be able to distinguish two readings, represent their truth conditions, and find a counterexample to an unsupported inference. Understanding what a sentence means is different from knowing whether it is true in the actual world.

This Model connects composition, predication, reference, quantification, time and modality. The recurring report-reading example shows how those distinctions work together. The finite representations are teaching models; their logical behavior does not establish which readings English speakers accept in every context. Examples are constructed, and the source support and remaining gaps are identified below.

## Contents

- [Meaning and composition](#meaning-and-composition)
- [Reference and denotation](#reference-and-denotation)
- [Predication and participants](#predication-and-participants)
- [Quantification](#quantification)
- [Quantifier scope](#quantifier-scope)
- [Negation and entailment](#negation-and-entailment)
- [Temporal reference](#temporal-reference)
  - [Situation types](#situation-types)
- [Modality](#modality)
- [Following one interpretation](#following-one-interpretation)
- [Interfaces](#interfaces)
  - [Interface with Lexicon](#interface-with-lexicon)
  - [Interface with Syntax](#interface-with-syntax)
  - [Interface with Pragmatics](#interface-with-pragmatics)
- [Evidence and open questions](#evidence-and-open-questions)
- [Related knowledge](#related-knowledge)

## Meaning and composition

A **proposition** is a content that can be evaluated as true or false. A truth-conditional analysis states what would have to be the case for that content to be true; it need not establish that those conditions actually hold. Questions and commands also have meaning, so truth conditions for declaratives are a starting point rather than an account of all language use.

**Composition** connects the meanings of parts with their arrangement. *Maya admires Ravi* and *Ravi admires Maya* contain the same words, but exchanging their positions changes who admires whom. A list of dictionary meanings would miss this difference. In a simple representation, `admire(Maya, Ravi)` and `admire(Ravi, Maya)` can have different truth values.

| Contribution | What the analysis records | Example |
|---|---|---|
| Lexical meaning | The selected conventional sense | READ as engaging with written content |
| Composition | How interpreted parts combine through structure | READ combines with its participants |
| Reference and denotation | Values assigned under an interpretation | Maya denotes an individual; report denotes a set in a simple extensional account |
| Predication | A property, relation or situation attributed to participants | `read(Anna, report_A)` |
| Operators and scope | How quantification, negation or modality applies | EVERY outside an existential report expression |
| Time and aspect | Temporal location, viewpoint and situation structure | HAD READ relates reading to a later past reference time |

Composition is not always set intersection. In a simplified reading, a *red book* is both red and a book. A *former teacher* need not be a current teacher: FORMER changes how the property is evaluated over time. Idioms can supply conventional meaning at a larger unit, so finding an idiom does not by itself refute every compositional account. The analysis must say which units contribute meaning and how they combine.

**Lexical ambiguity** involves distinct senses, such as a financial versus river-edge use of *bank*. **Structural ambiguity** involves distinct combinations: in *Maya saw the student with binoculars*, the PP can modify the seeing or the student. **Vagueness** concerns borderline cases within an interpretation: a person may be a borderline case of *tall* under a given comparison standard. Different senses, different structures and uncertain boundaries call for different explanations. The selected Anderson material supports the ambiguity distinction; the broader composition and vagueness account remains an authored synthesis.

## Reference and denotation

**Denotation** is the semantic value assigned to an expression under an interpretation. In the simple extensional account used here, a name can denote an individual, a common noun a set, and a two-place verb a relation. **Reference** concerns identifying what an expression picks out in a use. These are connected notions, but not every meaningful expression is a label for one physical object.

For example, *report* can denote the set of reports in a model. *Every report* does not name a special object called “every report”; it combines with a property to make a quantified claim. *A report* in *Every student read a report* need not select the same report for each student. The structure of the claim determines that dependency.

An expression's conventional contribution can also require context. In a constructed utterance by Maya, *I* identifies Maya through its speaker-related rule. A different speaker changes the value without requiring a new dictionary sense for each person. *Here* requires a contextually determined location whose extent may be a desk, room or wider place. Resolving such values does not make all meaning unconstrained by words.

A sense is not identical to its current extension: two descriptions could happen to apply to the same individuals while presenting different properties. The account must also distinguish a fixed-world extension from a contribution evaluated across times or possibilities. This introductory representation does not resolve competing theories of names, definites, kinds or nonexistent entities.

## Predication and participants

A **semantic predicate** characterizes a property, relation or situation. Its **arguments** fill the positions that its interpretation requires. In the deliberately simple relation `read(x, y)`, `x` is the reader and `y` the text read. Reversing the arguments changes the claim. An event-based analysis could additionally represent a reading event and connect its participants to it; the two-place notation here leaves that detail implicit.

Participant labels explain how an entity is involved. An **Agent** is an initiator or actor under the adopted account; a **Theme** is an entity involved, moved or characterized; a **Patient** undergoes an effect or change; a **Recipient** receives something; an **Experiencer** has a perception or psychological state. A **Stimulus** occasions such a state. These are working descriptions, not a universally agreed inventory with mechanically decidable boundaries. Not every predicate denotes an intentional action: *Maya knows Ravi* describes a state.

Semantic roles differ from grammatical functions. In *Maya received a report*, Maya is Subject while a recipient analysis is plausible. Subject therefore does not mean Agent. Likewise, a semantic predicate is not the same object as the syntactic Predicate phrase. The [Syntax interface](#interface-with-syntax) shows how constructions redistribute grammatical functions while preserving or changing participant relations.

## Quantification

A quantifier makes a claim about how many or which members of a domain satisfy a condition. For a basic quantified sentence, separate the **restrictor**, which identifies the relevant set, from the **nuclear scope**, which supplies the property attributed to its members. In *Every student passed*, STUDENT restricts the quantifier and PASSED supplies that property. The relevant students may be those in a particular class, rather than all students everywhere.

Let `S` be the relevant students and `P` those who passed. Under the classical finite interpretation used here:

| Expression | Truth condition |
|---|---|
| Every student passed | Every member of S belongs to P: S is a subset of P |
| Some student passed | S and P share at least one member |
| No student passed | S and P share no members |

*Some* supplies an existential condition here, not “some but not all.” Whether a speaker suggests the stronger reading depends on conversational assumptions. Also distinguish a quantifier's restrictor from its scope relative to another operator. The first asks which students count; the second asks how two operations combine.

Selected Richards lecture passages support these elementary quantifier conditions and a scope contrast. Their application to the constructed domains below is local analysis, not an observation of English speakers.

## Quantifier scope

Consider *Every student read a report*. Two schematic interpretations differ in whether a report may depend on the student:

```text
EVERY > A:
  for every student x, some report y satisfies read(x,y)

A > EVERY:
  some report y satisfies read(x,y) for every student x
```

In a constructed domain with students Anna and Ben and reports A and B, Anna reads A and Ben reads B; neither reads the other report. EVERY > A is true, while A > EVERY is false. The first representation allows different reports, but does not require them to be different. If both students read A, both representations are true. The second does not say that exactly one report exists or that the students read no additional reports.

The same distinction applies to the retained teacher-and-book representation:

```text
EVERY > A:
  for every x in teachers, some y in books satisfies recommend(x,y)
A > EVERY:
  some y in books satisfies recommend(x,y) for every x in teachers

NOT > EVERY:
  not all relevant individuals satisfy P
EVERY > NOT:
  all relevant individuals fail to satisfy P
```

Three teachers with nonoverlapping recommendations satisfy EVERY > A but not A > EVERY; a common recommended book satisfies both. These are differences between formulas. They do not show that every context freely permits both readings of the corresponding English sentence. Lexical, structural, discourse and prosodic conditions can matter to reading availability.

Empty domains expose another assumption. With no teachers, the universal claim is vacuously true. The shared-book claim then depends on whether any books exist: it is true if there is a book and false if there are none. Thus EVERY > A does not in general entail A > EVERY. A > EVERY does entail EVERY > A under these classical definitions. Ordinary uses can carry additional existence expectations; those expectations are not silently built into this toy model. Existing regression tests check the declared formulas, including empty domains, rather than validating natural-language scope judgments.

## Negation and entailment

Negation reverses the truth value of the proposition within its scope in this classical account. Moving its scope changes what is denied. *Not every student passed* denies universal success. *No student passed* denies that any student succeeded. With exactly two relevant students:

| Outcome | Every passed | Not every passed | No student passed |
|---|---|---|---|
| Anna and Ben passed | True | False | False |
| Anna passed; Ben failed | False | True | False |
| Both failed | False | True | True |

Consequently, *not every* does not entail that someone passed. The last row is a counterexample to that proposed conclusion. With an empty student domain, EVERY is true, NOT EVERY false and NO true; any inference from NO to NOT EVERY must therefore assume a nonempty restrictor.

**Entailment** holds when a conclusion is true in every interpretation where its premise is true, holding the intended meanings and relevant background assumptions fixed. To defeat an entailment claim, supply one coherent **countermodel** with a true premise and false conclusion. Checking only a case in which both statements are true cannot establish entailment.

For example, *Maya read report A and report B* entails *Maya read report A* under the ordinary conjunctive interpretation. It does not entail that she read only those two reports: a case where she also read C defeats that added restriction. Two claims are contradictory when they cannot both be true or both false under the fixed interpretation; mere difference in wording or conversational tension is insufficient. Whether a sentence presupposes background information is a separate issue from whether its asserted content entails a conclusion.

## Temporal reference

**Tense** relates temporal interpretation to reference points. **Aspect** concerns how a situation is presented or internally organized. A **reference time** is the time from which a situation is viewed. Speech time, reference time and event time can differ:

```text
Bounded past-perfect example:
E: finish report < R: Ravi arrives < S: speech time

Progressive example:
work interval: [--------- R ---------]

Continuing present-perfect example:
residence: [prior interval ----- now ---- possible continuation]
```

In the constructed *Maya had finished when Ravi arrived*, finishing precedes the past arrival, which precedes speech time. Here E marks the completion, R the arrival and S the utterance. In *Maya was finishing when Ravi arrived*, the progressive presents an internal phase: she may subsequently finish or be interrupted. Actual completion does not follow from that progressive statement.

A **perfect** relates a situation to a reference time through a retrospective perspective; it is not simply a completed-event marker. *Maya has lived here for years* allows residence to continue now. Selected British Council explanations support looking back from present or past reference times and include continuing situations. A strict point diagram E < R is therefore useful for the bounded finishing example, but inadequate for every perfect. A past participle by itself does not establish actual-world completion.

Tense forms also need not map one-to-one to chronological labels: schedules and historical presents illustrate why present morphology is not simply “happening now.” These broader uses remain outside the selected source support. For each analysis, distinguish an ordering required by the chosen reading from one merely favored by context or left unspecified.

### Situation types

**Situation type**, often called lexical aspect, concerns temporal organization. It differs from the grammatical viewpoint contributed by constructions such as the progressive. A familiar introductory classification distinguishes:

| Type | Organizing distinction | Constructed example |
|---|---|---|
| State | A condition holds rather than an unfolding activity | Maya owns a flat |
| Activity | A dynamic situation has no inherent endpoint in this reading | Maya walked |
| Accomplishment | A process develops toward an inherent endpoint | Maya wrote a report |
| Achievement | A transition is presented without an extended preparatory process in its basic characterization | The glass broke |

The classification concerns a predicate in a reading, not a permanent label attached to a spelling. *Walk* and *walk to the station* can differ in whether an endpoint is supplied. **Telicity** concerns an inherent endpoint; **boundedness** concerns how an occurrence is delimited. Walking for ten minutes has a time limit without making reaching a destination part of WALK's meaning. Lexical sense, complements, quantity and context interact with grammatical aspect, so the table is an analytical starting point rather than a complete classifier. Detailed diagnostics and competing event accounts remain source gaps.

## Modality

Modality evaluates a proposition relative to relevant alternatives. An introductory possible-world representation interprets **necessity** as truth in all relevant alternatives and **possibility** as truth in at least one. A possible world here is a representation of how things might be, not an additional observed place. Yablo's selected modal-logic pages support this formal core; they do not establish a full semantics of English modal verbs.

The source of the alternatives matters:

| Reading | What makes alternatives relevant | Constructed example |
|---|---|---|
| Epistemic | Available evidence or knowledge | Maya must be home, given the evidence |
| Deontic | Rules, duties or permissions | Maya must submit the report under the course rules |
| Circumstantial | Relevant abilities or circumstances | With the repaired lift, Maya can reach the upper floor |

The same modal form can serve different readings. *May* can concern possibility or permission; *must* can concern an inference or an obligation. Necessity alone does not identify the source. For deontic readings, rule-compliant alternatives need not include the actual situation: a duty can be violated. English modality can also involve ordering alternatives by ideals or likelihood; the elementary all/some representation does not capture all that structure.

In a constructed model with two accessible alternatives, Maya has read the report in one and has not read it in the other. Reading is possible but not necessary relative to that set. Neither evaluation tells us what actually happened unless the model also connects the actual situation to those alternatives. No numerical probability follows from counting these illustrative alternatives. An epistemic *must* is likewise not a guarantee that the speaker's evidence is complete or correct.

Negation can interact with modality as it does with quantification: “not necessary that p” differs from “necessary that not p.” This logical distinction does not make every English modal-plus-negation construction freely ambiguous; conventional patterns and context constrain interpretation.

## Following one interpretation

Consider the constructed sentence:

> When Maya arrived, every student had read a report.

Fix the relevant students as Anna and Ben, the reports as A and B, and Maya's arrival as yesterday afternoon. Anna finished reading A and Ben finished reading B before the arrival; neither read the other report. No actual learner or observed reading event is being reported.

| Step in the explanation | Contribution to the chosen reading |
|---|---|
| Reference and domain | Maya identifies the stipulated individual; STUDENT ranges over Anna and Ben |
| Predication | READ relates each reader to a report; the arguments are not interchangeable |
| Composition | The quantified Subject combines with a reading description; the WHEN clause supplies the reference time |
| Scope | EVERY > A allows A for Anna and B for Ben |
| Time | In this bounded reading, the reading completions precede arrival, which precedes speech time |
| Truth conditions | The described situation satisfies this reading, but not a reading requiring one shared report |

The result depends on the stipulated interpretation and facts. The surface sentence does not itself identify Anna, Ben, A and B, or demonstrate which scope readings speakers prefer. The interpretation should expose these inputs rather than present them as discoveries from the words alone.

Small changes isolate different contributions. Replacing *had read* with *was reading* presents reading in progress and removes the completion commitment. Replacing *every student* with *not every student* denies the corresponding universal claim and is compatible with no student having read a report. Replacing *had read* with *may have read* introduces modal alternatives rather than asserting actual reading. None of these changes is merely a different grammatical label for the same truth conditions.

## Interfaces

Lexical senses supply contributions, syntax organizes combinations, and context helps resolve values and interpret communicative use. These connections do not form a compulsory processing pipeline. Information structure and prosody can affect salient alternatives without erasing lexical and structural constraints.

### Interface with Lexicon

A **lexical sense entry** supplies a conventional meaning contribution, category and combinatorial restrictions. A **predicate interpretation** characterizes a property, relation or situation under a selected reading. The mapping is constraining rather than a spelling-to-meaning lookup:

| Endpoint | Schematic fields |
|---|---|
| Lexical sense entry | lexeme, sense, selection |
| Predicate interpretation | predicate, arguments, contextual_restrictions |

The relationship uses `kps:constrains`: the entry restricts possible interpretations, while construction and context help determine the result. These fields are analytical records, not measured quantities or a full formal theory.

In *Maya runs every morning*, a locomotion use of RUN characterizes an activity. In *Maya runs a company*, a management use relates Maya to the company. Treating the second sentence as ordinary locomotion merely because the spelling is unchanged would miss the intended interpretation. A constructional or coercion account may distribute the explanation differently; the chosen analysis should state where its meaning contributions come from.

This bridge does not establish an exhaustive sense inventory or an automatic disambiguator. Selected word-meaning and ambiguity support informs the distinction; the specific RUN mapping remains authored analysis. The [Lexicon counterpart](english-lexicon-system.md#interface-with-semantics) explains the same connection from the entry side.

### Interface with Syntax

The syntactic representation records phrases and grammatical functions. The semantic representation records predicates and participants. Construction-sensitive mappings connect them without making them identical. In this table, NP means noun phrase and PP means preposition phrase. Subject and Object are grammatical functions, while Giver, Recipient and Theme describe involvement in giving:

| Construction | Giver | Recipient | Theme |
|---|---|---|---|
| Leo gave Maya a prize | Subject | Indirect Object | Direct Object |
| Leo gave a prize to Maya | Subject | NP inside to-PP | Direct Object |
| Maya was given a prize by Leo | NP inside by-PP | Subject | Retained Object |

The passive preserves the basic participant relations while redistributing grammatical functions. In contrast, *The glass broke / Leo broke the glass* introduces a Causer in the second construction. A psychological predicate such as *The noise frightened Maya* can have a Stimulus Subject and Experiencer Object without passive morphology. Changing a grammatical function alone does not prove that a new participant role has been added.

Keep explicit, omitted and inferred participants separate. The dative comparison does not establish unrestricted alternation or complete synonymy: lexical, semantic and discourse restrictions matter. Role inventories also differ across frameworks. Anderson's selected participant and passive passages support the basic distinction, not all these mappings or a universal role theory. The [Syntax counterpart](english-syntax-system.md#interface-with-semantics) explains the grammatical side.

### Interface with Pragmatics

Conventional contributions and contextual values constrain what is said; additional conversational reasoning can suggest more. Context-sensitive semantics is possible, so the boundary is not simply “meaning without context” versus “meaning with context.”

```text
I -> speaker-related interpretation rule -> Maya in this utterance
here -> contextually anchored location -> the desk in this situation
some -> existential contribution -> possible not-all implicature
stop -> background prior activity -> accommodation or challenge
```

Resolving *I* to Maya supplies a value needed for interpretation. In *Maya read some reports*, inferring “not all” adds a possible **implicature**, a defeasible conversational inference. The continuation *in fact, she read all of them* cancels that inference without contradicting the existential contribution. Its derivation needs suitable relevance and speaker-knowledge assumptions; a speaker might simply lack evidence about the remaining reports. Bhatt's selected handout supports those qualifications.

A **presupposition** is background information that an expression or use presents as already available. *Maya stopped reading* backgrounds prior reading; *Maya did not stop reading* can retain that background. A listener may accept it into the shared assumptions, a process called **accommodation**, or challenge it. Projection through negation is a useful comparison, not an infallible definition: embeddings and local context affect what survives. Fox and Menéndez-Benito's selected notes support this background-and-projection account.

The **common ground** is what interlocutors treat as shared for the conversation, not necessarily what is objectively true. Presuppositions, contextual reference and implicature can interact; they are not three mutually exclusive word lists. Annotate which contribution the expression supplies, what context resolves and which conclusion remains defeasible. These constructed examples do not establish a speaker's actual intention or a listener's observed response. The [Pragmatics counterpart](english-pragmatics-system.md#semantics-pragmatics-interface) develops the discourse side.

## Evidence and open questions

**Provisional; independent review pending.** This is an introductory synthesis with constructed examples, not a comprehensive formal semantics or an empirical study. Source support is bounded:

- [Anderson](../references/anderson-2018-essentials-of-linguistics.md): selected lexical/structural ambiguity, word meaning and participant-role passages.
- [Richards](../references/richards-2022-semantics.md): selected elementary quantifier and scope explanations; not every English scope judgment or a commitment to the lecture's derivational theory.
- [British Council](../references/british-council-undated-grammar-reference.md): selected perfect-aspect and possibility explanations; not a full tense/aspect theory.
- [Yablo](../references/yablo-2015-modal-semantics.md): the elementary alternatives-based modal representation, not a lexical semantics of every English modal.
- [Bhatt](../references/bhatt-2003-implicature.md) and [Fox and Menéndez-Benito](../references/fox-menendez-benito-2006-presupposition.md): selected distinctions at the Pragmatics interface.

Full composition rules, vagueness diagnostics, competing reference theories, plural and distributive interpretations, event structure, detailed aspect diagnostics and richer modal bases remain gaps. Source support attached here does not silently close separate gaps in the reusable Concepts. The scope of participant labels and the semantics–pragmatics boundary remain theory-dependent.

For a proposed inference, state the reading, domain and background assumptions, then seek a true-premise/false-conclusion countermodel. Small-domain enumeration checks a formal claim; acceptability judgments, corpus evidence or experiments are needed to investigate actual English reading availability. Structural publication checks do not establish linguistic truth, independent review or teaching effectiveness.

## Related knowledge

[Compositionality](../concepts/compositionality.md), [reference and denotation](../concepts/reference-and-denotation.md), [semantic role](../concepts/semantic-role.md), [quantification and scope](../concepts/quantification-and-scope.md), [negation and entailment](../concepts/negation-and-entailment.md), [tense and aspect](../concepts/tense-and-aspect.md) and [modality](../concepts/modality.md) give reusable definitions. The core explanations and representations needed for the worked analysis are contained above.
