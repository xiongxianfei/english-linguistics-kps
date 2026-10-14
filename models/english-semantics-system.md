---
id: "english:model:english-semantics-system"
type: "model"
version: "0.4.0"
language: "KPS 9.x"
status: "draft"
domains: ["semantics"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:coppock-champollion-2026-formal-semantics", "english:reference:anderson-2018-essentials-of-linguistics", "english:reference:richards-2022-semantics", "english:reference:yablo-2015-modal-semantics", "english:reference:british-council-undated-grammar-reference", "english:reference:bhatt-2003-implicature", "english:reference:fox-menendez-benito-2006-presupposition"]
uses_concepts: ["english:concept:compositionality", "english:concept:reference-and-denotation", "english:concept:semantic-role", "english:concept:quantification-and-scope", "english:concept:negation-and-entailment", "english:concept:tense-and-aspect", "english:concept:modality", "english:concept:semantic-predicate", "english:concept:situation-type", "english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:lexical-selection", "english:concept:object-and-pp-complement", "english:concept:valency-and-argument-structure", "english:concept:contextual-resolution", "english:concept:implicature", "english:concept:presupposition", "english:concept:common-ground"]
uses_models: ["english:model:english-lexicon-system", "english:model:english-syntax-system", "english:model:english-pragmatics-system"]
system_domain: "semantics"
---

# English semantics system

Semantics explains how expressions contribute meaning, how those contributions combine, and what follows under a stated interpretation. A reader should be able to distinguish two readings, represent their truth conditions, and find a counterexample to an unsupported inference. Understanding what a sentence means is different from knowing whether it is true in the actual world.

Thirteen visible topics connect meaning and reference, semantic building blocks, events and roles, composition, operators, time and the Syntax interface. Their order supports reading; the topics overlap and do not form a compulsory processing sequence. The recurring report-reading example shows how those distinctions work together. The finite representations are teaching models; their logical behavior does not establish which readings English speakers accept in every context. Examples are constructed, and the source support and remaining gaps are identified below.

## Contents

- [Meaning and reference](#meaning-and-reference)
  - [Truth conditions](#truth-conditions)
- [Entities properties and relations](#entities-properties-and-relations)
- [Predicates and arguments](#predicates-and-arguments)
- [Events and states](#events-and-states)
  - [Situation types](#situation-types)
- [Semantic roles](#semantic-roles)
- [Compositionality](#compositionality)
  - [Building an interpretation](#building-an-interpretation)
- [Quantification](#quantification)
- [Negation and entailment](#negation-and-entailment)
- [Scope](#scope)
  - [Quantifier scope](#quantifier-scope)
- [Ambiguity](#ambiguity)
- [Tense and aspect semantics](#tense-and-aspect-semantics)
- [Modality](#modality)
- [Syntax Semantics interface](#syntax-semantics-interface)
  - [Structure and interpretation](#structure-and-interpretation)
  - [Grammatical functions and participant roles](#grammatical-functions-and-participant-roles)
- [Following one interpretation](#following-one-interpretation)
- [Other interfaces](#other-interfaces)
  - [Interface with Lexicon](#interface-with-lexicon)
  - [Interface with Pragmatics](#interface-with-pragmatics)
- [Evidence and open questions](#evidence-and-open-questions)
- [Related knowledge](#related-knowledge)

## Meaning and reference

**Denotation** is the semantic value assigned to an expression under an interpretation. In the simple extensional account used here, a name can denote an individual, a common noun a set, and a two-place verb a relation. **Reference** concerns identifying what an expression picks out in a use. These are connected notions, but not every meaningful expression is a label for one physical object.

For example, *report* can denote the set of reports in a model. *Every report* does not name a special object called “every report”; it combines with a property to make a quantified claim. *A report* in *Every student read a report* need not select the same report for each student. The structure of the claim determines that dependency.

An expression's conventional contribution can also require context. In a constructed utterance by Maya, *I* identifies Maya through its speaker-related rule. A different speaker changes the value without requiring a new dictionary sense for each person. *Here* requires a contextually determined location whose extent may be a desk, room or wider place. Resolving such values does not make all meaning unconstrained by words.

A sense is not identical to its current extension: two descriptions could happen to apply to the same individuals while presenting different properties. The account must also distinguish a fixed-world extension from a contribution evaluated across times or possibilities. This introductory representation does not resolve competing theories of names, definites, kinds or nonexistent entities.

Consider a constructed context in which Maya is the only editor of a particular report. *Maya* and *the editor of the report* identify the same person in that context. The expressions still contribute differently: the description characterizes a role, and a different person could become the editor. Shared reference in this case does not establish sameness of meaning. This is an introductory comparison, not a settled theory of names or descriptions.

### Truth conditions

A **proposition** is a content that can be evaluated as true or false. A truth-conditional analysis states what would have to be the case for that content to be true; it need not establish that those conditions actually hold. Questions and commands also have meaning, so truth conditions for declaratives are a starting point rather than an account of all language use.

## Entities properties and relations

To interpret a sentence, first distinguish the kinds of values in the representation. A **domain** is the collection of entities the model considers. Here an **individual** is a particular member, such as Maya or report A. A **property** characterizes an individual; a **relation** connects ordered participants. These are semantic distinctions, not word classes.

Use a constructed domain containing Maya, Ravi, report A and report B. Suppose Maya has read A and Ravi has read B:

| Kind | Representation in this interpretation | How to use it |
|---|---|---|
| Individual | `Maya` | Identify one participant |
| Property | `REPORT = {A, B}` | Ask whether a candidate belongs to the set of reports |
| Two-place relation | `READ = {(Maya, A), (Ravi, B)}` | Ask whether an ordered reader–text pair belongs to the relation |
| Truth value | `read(Maya, A)` is true; `read(Maya, B)` is false | Evaluate a claim against the stipulated relation |

Braces list set members; parentheses in READ group ordered pairs. The pair `(Maya, A)` differs from `(A, Maya)`. A property can be represented extensionally by a set, or by a function that returns true for members and false for nonmembers. A relation similarly classifies tuples. This does not reduce a property's meaning across all times and possibilities to one current set.

In a basic typed account, `e` labels individual-denoting values and `t` truth values; `〈e,t〉` labels a function from individuals to truth values. A **semantic type** describes a contribution's inputs and outputs. It is different from a grammatical category such as noun or verb: a noun and a verb phrase can both express properties. These type labels are introduced for orientation; the worked calculations below can be followed without typed lambda notation.

Events can also count as entities in a broad semantic ontology. Some theories distinguish an event domain from an individual domain. The local `e` type label above must not be confused with an event variable named `e` in a formula. The next sections use names and plain-language functions to keep that distinction visible. [Coppock and Champollion](../references/coppock-champollion-2026-formal-semantics.md) supply selected support for the typed account; this tiny domain is an authored illustration.

## Predicates and arguments

A **semantic predicate** characterizes a property, relation or situation. Its **arguments** fill the positions that its interpretation requires. In the deliberately simple relation `read(x, y)`, `x` is the reader and `y` the text read. Reversing the arguments changes the claim. An event-based analysis could additionally represent a reading event and connect its participants to it; the two-place notation here leaves that detail implicit.

The number of participant positions in an analysis is its **arity**. Keep that number and their order explicit:

| Working predicate | Positions | Constructed clause |
|---|---|---|
| `sleep(x)` | One: sleeper | Maya sleeps |
| `read(x, y)` | Two: reader, text | Maya read report A |
| `give(x, y, z)` | Three: giver, recipient, transferred item | Maya gave Ravi report A |

The formulas temporarily omit tense and other contributions. *Maya read quietly* can leave the text unexpressed; it does not make QUIETLY the missing text argument. Semantic participation, syntactic complement requirements and the number of overt phrases are distinct. Conversely, an event analysis can distribute participant information over separate relations rather than encode all participants as positions of one verb predicate. State the adopted representation before comparing argument counts.

An argument to a semantic function is also a broader notion than a participant in an event. A quantifier can take a property as its input. We therefore distinguish READ's reader/text participants from the function inputs used to calculate a sentence's meaning.

## Events and states

An event or state representation identifies the situation being described, so its participants, time and modifiers can be connected. An **event**, in a narrow use, unfolds or involves change; a **state** is a condition holding over an interval. *Maya read a report* describes an event on the reading used here; *Maya knows Ravi* describes a state. Neither the word *event* nor a past-tense form by itself means an intentional or completed action. **Eventuality** is a useful cover term for events and states; some sources use *event* in that broader sense instead.

Compare two schematic representations of *Maya read report A quietly*:

```text
Participant relation, leaving the event implicit:
  read(Maya, A)

Event representation:
  there is an event ev such that
    reading(ev)
    reader(ev, Maya)
    text(ev, A)
    quiet(ev)
```

Here `ev` identifies the same event in every line, and all lines must hold together. QUIET characterizes the reading event, rather than asserting that Maya is always a quiet person or that the report is quiet. Maya could read another report noisily in a different event without contradicting this description. Removing the quietness condition leaves a reading-event claim; adding it back requires more than the bare claim supplies. This inference is for the stated conjunctive manner analysis, not a rule allowing every adverb to be removed in every construction.

The representation separates participants from the event instead of treating its time or manner as another text being read. A state can likewise be represented as a holding situation: a KNOWING state connects an experiencer, what is known and the interval over which it holds. Exactly which state predicates introduce situation variables, and how events are individuated, vary across theories. The local reading representation illustrates a Neo-Davidsonian approach; it does not silently replace every simpler participant formula in this Model. Selected [event-semantics passages](../references/coppock-champollion-2026-formal-semantics.md) motivate the connection.

### Situation types


**Situation type**, often called lexical aspect, concerns temporal organization. It differs from the grammatical viewpoint contributed by constructions such as the progressive. A familiar introductory classification distinguishes:

| Type | Organizing distinction | Constructed example |
|---|---|---|
| State | A condition holds rather than an unfolding activity | Maya owns a flat |
| Activity | A dynamic situation has no inherent endpoint in this reading | Maya walked |
| Accomplishment | A process develops toward an inherent endpoint | Maya wrote a report |
| Achievement | A transition is presented without an extended preparatory process in its basic characterization | The glass broke |

The classification concerns a predicate in a reading, not a permanent label attached to a spelling. *Walk* and *walk to the station* can differ in whether an endpoint is supplied. **Telicity** concerns an inherent endpoint; **boundedness** concerns how an occurrence is delimited. Walking for ten minutes has a time limit without making reaching a destination part of WALK's meaning. Lexical sense, complements, quantity and context interact with grammatical aspect, so the table is an analytical starting point rather than a complete classifier. Detailed diagnostics and competing event accounts remain source gaps.

## Semantic roles

Participant labels explain how an entity is involved. An **Agent** is an initiator or actor under the adopted account; a **Theme** is an entity involved, moved or characterized; a **Patient** undergoes an effect or change; a **Recipient** receives something; an **Experiencer** has a perception or psychological state. A **Stimulus** occasions such a state. These are working descriptions, not a universally agreed inventory with mechanically decidable boundaries. Not every predicate denotes an intentional action: *Maya knows Ravi* describes a state.

Semantic roles differ from grammatical functions. In *Maya received a report*, Maya is Subject while a recipient analysis is plausible. Subject therefore does not mean Agent. Likewise, a semantic predicate is not the same object as the syntactic Predicate phrase. The [Syntax Semantics interface](#syntax-semantics-interface) shows how constructions redistribute grammatical functions while preserving or changing participant relations.

In *Maya gave Ravi report A*, a basic transfer analysis assigns Maya Giver, Ravi Recipient and A Theme. Calling Maya Agent additionally adopts an actor/initiator analysis; it should not be inferred solely from Subject position. In *Ravi received report A*, Ravi is still a recipient although now Subject. In *The noise frightened Maya*, Maya is Experiencer, while the noise is Stimulus; a noise need not intentionally act.

The READ example identifies Reader and Text with deliberately predicate-specific labels. A broader role inventory might group the reader under Agent and the text under Theme, but the label Theme does not establish that reading physically changes the text. Explain which relation a label captures, and preserve uncertainty when broader inventories classify a case differently.

## Compositionality

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

### Building an interpretation

Start with *Maya read report A*, temporarily leaving tense aside. Let `a` denote report A and `m` denote Maya. Here VP means verb phrase. Interpret READ as a function that first takes a text and then takes a reader:

| Expression or combination | Interpretation | What is still needed |
|---|---|---|
| READ | Given a text `y`, return the property “read y” | A text, then a reader |
| report A | The individual `a` | No participant slot |
| read report A | Given a reader `x`, evaluate `read(x, a)` | A reader |
| Maya | The individual `m` | No participant slot |
| Maya + read report A | Evaluate `read(m, a)` | No unfilled participant position in this simple claim |

This stepwise combination is **function application**: apply a contribution to an input of the appropriate kind. Supplying the object first does not reverse the argument convention; `read(x, y)` still lists reader before text. A completed formula has a truth value in the fixed model. Across possible situations, its truth conditions tell us when the claim would hold.

Now replace *report A* with *a report*. Under the local existential reading, the resulting VP contributes a property:

```text
read a report:
  given a reader x, true if some y is a report and read(x,y)

Maya read a report:
  true if some y is a report and read(Maya,y)
```

This step does not assign *a report* the value of a named individual. It states how an existential condition contributes to the VP. A complete formal derivation for quantified objects needs additional type choices or composition rules; this explanatory paraphrase is not a claim that the earlier individual-object application rule handles every expression unchanged. Replacing Maya with *every student* then applies universal quantification to that VP property, giving the EVERY > A reading.

The function-application explanation follows selected [Coppock and Champollion passages](../references/coppock-champollion-2026-formal-semantics.md); the report example is authored. Different frameworks distribute lexical, constructional and compositional information differently. The objective is an explicit interpretation, not adoption of a universal tree or one rule for every construction.

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

## Scope

**Scope** is the part of an interpretation over which an operator acts, including its relation to other operators. It concerns interpreted structure, not just which word appears first. Once quantification, negation and modality are distinguished, compare how their contributions nest:

| Operators | One interpretation | Contrasting interpretation |
|---|---|---|
| Universal and existential | Each student has a potentially different report | One report is shared by every student |
| Negation and universal | It is not the case that all passed | Each student did not pass |
| Negation and necessity | It is not required that Maya leave | It is required that Maya not leave |

The formulas below make the first two contrasts precise. The modal contrast concerns different requirements; it does not claim that a particular English modal construction freely expresses both. [Modality](#modality) explains the relevant alternatives.

### Quantifier scope

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

## Ambiguity

**Lexical ambiguity** involves distinct senses, such as a financial versus river-edge use of *bank*. **Structural ambiguity** involves distinct combinations: in *Maya saw the student with binoculars*, the PP can modify the seeing or the student. **Vagueness** concerns borderline cases within an interpretation: a person may be a borderline case of *tall* under a given comparison standard. Different senses, different structures and uncertain boundaries call for different explanations. The selected Anderson material supports the ambiguity distinction; the broader composition and vagueness account remains an authored synthesis.

Scope can introduce another interpretive contrast even when the words and overt grouping stay fixed. In the report example, the student-dependent and shared-report representations differ in operator nesting. To make an ambiguity claim useful, show the candidate interpretations and a situation in which their truth conditions differ. Then distinguish that formal contrast from evidence that speakers actually permit both readings in a specified context.

| Question | Distinction to investigate |
|---|---|
| Which conventional sense is selected? | Lexical ambiguity |
| Which expressions form a constituent or modify which other expression? | Structural ambiguity |
| Which operator applies within another? | Scope ambiguity |
| Where are the borderline cases under the selected meaning? | Vagueness |

These distinctions can interact. Context may resolve a sense or favor an attachment; that does not turn every contextual inference into another lexical sense. A short expression being underspecified is also not enough to establish a fixed inventory of distinct readings.

## Tense and aspect semantics

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


The [event/state representation](#events-and-states) gives temporal interpretation something to locate. For a bounded reading event, one can relate its runtime to a past reference interval. A state such as knowing Ravi may hold throughout that interval, without a completion point. Grammatical aspect describes how the situation is viewed; situation type describes its internal temporal organization. These dimensions interact, but neither replaces the other.

The **perfect** and **perfective** are distinct terms. Perfect constructions concern a retrospective relation to a reference time; perfective viewpoint presents a situation as a whole in an adopted account. The present explanation is not a complete mapping between English forms and cross-linguistic aspect categories. Selected Coppock and Champollion text supports the distinction; fuller interval derivations and habitual interpretations remain beyond this introductory account.

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

## Syntax Semantics interface

The interface connects grammatical grouping with the construction of interpretations, as well as grammatical functions with participant roles. A syntactic tree specifies which expressions combine; a semantic account must explain what their contributions produce at those combinations.

### Structure and interpretation

In the simplified grouping `[Maya [read [report A]]]`, READ first combines with its Object, giving the property of reading A; that property combines with Maya. This is the [compositional calculation](#building-an-interpretation) expressed as a structure. It is not a claim about the chronological order of mental processing.

Attachment can change the contribution being composed:

```text
[Maya [saw [the student [with binoculars]]]]
  WITH BINOCULARS helps identify the student.

[Maya [[saw the student] [with binoculars]]]
  WITH BINOCULARS describes the means of seeing.
```

These are abbreviated grouping sketches, not complete phrase-structure trees. The first reading does not require Maya to use binoculars; the second does not require the student to possess them. The same sequence can therefore support different truth conditions through different attachment. Context and lexical meaning still constrain plausible analyses.

Overt structure also does not transparently determine every scope reading. The report example keeps the surface wording fixed while comparing two operator nestings. Frameworks differ over how they derive such readings; no particular movement or type-shifting theory is established here. Selected source support covers function application and attachment, while the reading availability and full syntax-to-semantics mapping remain open.

### Grammatical functions and participant roles

The syntactic representation records phrases and grammatical functions. The semantic representation records predicates and participants. Construction-sensitive mappings connect them without making them identical. In this table, NP means noun phrase and PP means preposition phrase. Subject and Object are grammatical functions, while Giver, Recipient and Theme describe involvement in giving:

| Construction | Giver | Recipient | Theme |
|---|---|---|---|
| Leo gave Maya a prize | Subject | Indirect Object | Direct Object |
| Leo gave a prize to Maya | Subject | NP inside to-PP | Direct Object |
| Maya was given a prize by Leo | NP inside by-PP | Subject | Retained Object |

The passive preserves the basic participant relations while redistributing grammatical functions. In contrast, *The glass broke / Leo broke the glass* introduces a Causer in the second construction. A psychological predicate such as *The noise frightened Maya* can have a Stimulus Subject and Experiencer Object without passive morphology. Changing a grammatical function alone does not prove that a new participant role has been added.

Keep explicit, omitted and inferred participants separate. The dative comparison does not establish unrestricted alternation or complete synonymy: lexical, semantic and discourse restrictions matter. Role inventories also differ across frameworks. Anderson's selected participant and passive passages support the basic distinction, not all these mappings or a universal role theory. The [Syntax counterpart](english-syntax-system.md#interface-with-semantics) explains the grammatical side.

## Following one interpretation

Consider the constructed sentence:

> When Maya arrived, every student had read a report.

Fix the relevant students as Anna and Ben, the reports as A and B, and Maya's arrival as yesterday afternoon. Anna finished reading A and Ben finished reading B before the arrival; neither read the other report. No actual learner or observed reading event is being reported.

| Step in the explanation | Contribution to the chosen reading |
|---|---|
| Reference and domain | Maya identifies the stipulated individual; STUDENT ranges over Anna and Ben |
| Entities and properties | Anna and Ben are individuals in the student set; A and B are individuals in the report set |
| Predication and roles | READ relates each reader to a report; the arguments are not interchangeable |
| Events | Anna's reading of A and Ben's reading of B are distinct situations, each with its own participants and runtime |
| Composition | The quantified Subject combines with a reading description; the WHEN clause supplies the reference time |
| Scope | EVERY > A allows A for Anna and B for Ben |
| Time | In this bounded reading, the reading completions precede arrival, which precedes speech time |
| Truth conditions | The described situation satisfies this reading, but not a reading requiring one shared report |

The result depends on the stipulated interpretation and facts. The surface sentence does not itself identify Anna, Ben, A and B, or demonstrate which scope readings speakers prefer. The interpretation should expose these inputs rather than present them as discoveries from the words alone.

Small changes isolate different contributions. Replacing *had read* with *was reading* presents reading in progress and removes the completion commitment. Replacing *every student* with *not every student* denies the corresponding universal claim and is compatible with no student having read a report. Replacing *had read* with *may have read* introduces modal alternatives rather than asserting actual reading. None of these changes is merely a different grammatical label for the same truth conditions.

## Other interfaces

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

- [Coppock and Champollion](../references/coppock-champollion-2026-formal-semantics.md): selected typed-denotation, function-application, event and aspect passages; the local progression, report calculations and event record are authored adaptations.
- [Anderson](../references/anderson-2018-essentials-of-linguistics.md): selected lexical/structural ambiguity, word meaning and participant-role passages.
- [Richards](../references/richards-2022-semantics.md): selected elementary quantifier and scope explanations; not every English scope judgment or a commitment to the lecture's derivational theory.
- [British Council](../references/british-council-undated-grammar-reference.md): selected perfect-aspect and possibility explanations; not a full tense/aspect theory.
- [Yablo](../references/yablo-2015-modal-semantics.md): the elementary alternatives-based modal representation, not a lexical semantics of every English modal.
- [Bhatt](../references/bhatt-2003-implicature.md) and [Fox and Menéndez-Benito](../references/fox-menendez-benito-2006-presupposition.md): selected distinctions at the Pragmatics interface.

The Model now explains elementary composition and an event representation. A complete formal grammar, vagueness diagnostics, competing reference theories, plural and distributive interpretations, richer event structure, detailed aspect diagnostics and modal bases remain gaps. Source support attached here does not silently close separate gaps in the reusable Concepts. The scope of participant labels and the semantics–pragmatics boundary remain theory-dependent.

For a proposed inference, state the reading, domain and background assumptions, then seek a true-premise/false-conclusion countermodel. Small-domain enumeration checks a formal claim; acceptability judgments, corpus evidence or experiments are needed to investigate actual English reading availability. Structural publication checks do not establish linguistic truth, independent review or teaching effectiveness.

## Related knowledge

[Compositionality](../concepts/compositionality.md), [reference and denotation](../concepts/reference-and-denotation.md), [semantic role](../concepts/semantic-role.md), [quantification and scope](../concepts/quantification-and-scope.md), [negation and entailment](../concepts/negation-and-entailment.md), [tense and aspect](../concepts/tense-and-aspect.md) and [modality](../concepts/modality.md) give reusable definitions. The core explanations and representations needed for the worked analysis are contained above.
