---
id: "english:model:english-lexicon-system"
type: "model"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
domains: ["lexicon"]
evidence_status: "provisional"
source_status: "selected-support-only"
basis_kind: "Authored foundational synthesis and constructed examples; independent review pending"
reviewed: null
references: ["english:reference:anderson-2018-essentials-of-linguistics", "english:reference:princeton-undated-wordnet", "english:reference:british-council-undated-lexical-combinations"]
uses_concepts: ["english:concept:lexeme-and-word-form", "english:concept:lexical-entry", "english:concept:sense-and-lexical-ambiguity", "english:concept:lexical-selection", "english:concept:collocation", "english:concept:valency-and-argument-structure", "english:concept:derivation", "english:concept:inflection", "english:concept:compounding", "english:concept:productivity-and-lexicalization", "english:concept:head-and-dependent", "english:concept:object-and-pp-complement", "english:concept:semantic-predicate"]
uses_models: ["english:model:english-morphology-system", "english:model:english-syntax-system", "english:model:english-semantics-system"]
system_domain: "lexicon"
---

# English lexicon system

The lexicon connects a word's identity and forms with its senses, grammatical possibilities and conventional uses. This Model helps a reader explain why knowing a translation or a spelling is not enough to use or analyze a word. It connects lexical entries, ambiguity, categories, selection, meaning relations, combinations and register through worked examples and interfaces with Morphology, Syntax and Semantics.

The entry format is an analytical tool, not a claim that dictionaries or brains store information in these exact fields. The coverage is introductory; its organization is an authored synthesis of selected sources and existing explanations. Examples are constructed for ordinary standard-English readings unless stated otherwise. The Model remains provisional and independently unreviewed.

## Contents

- [Lexemes and lexical entries](#lexemes-and-lexical-entries)
- [Senses and lexical ambiguity](#senses-and-lexical-ambiguity)
- [Lexical categories](#lexical-categories)
- [Selection and argument structure](#selection-and-argument-structure)
- [Lexical relations](#lexical-relations)
- [Collocations and idioms](#collocations-and-idioms)
- [Register and variation](#register-and-variation)
- [Worked entry](#worked-entry)
- [Interfaces](#interfaces)
  - [Interface with Morphology](#interface-with-morphology)
  - [Interface with Syntax](#interface-with-syntax)
  - [Interface with Semantics](#interface-with-semantics)
- [Evidence and open questions](#evidence-and-open-questions)

## Lexemes and lexical entries

A **lexeme** is a lexical identity abstracting over grammatical forms. RUN, in capitals to name the lexeme, has forms including *run*, *runs*, *ran* and *running*. A **word form** is one realization in that grammatical pattern. A **lemma** is a conventional lookup form, such as *run*; it is not the entire lexeme or an exhaustive account of its uses.

A **lexical entry** records information relevant to an item or sense. An entry can describe a conventional multiword expression as well as a single written word. The record below separates questions that a single translation tends to hide.

| Entry field | What to record | Why it matters |
|---|---|---|
| Identity and forms | Lexeme, written forms and variety-labeled pronunciation | A lexeme can have several grammatical forms |
| Category | Noun, verb, adjective or another justified category in this use | Distribution is not determined by translation alone |
| Sense | A conventional meaning contribution in the intended use | Different senses can license different constructions |
| Combinatorial frame | Categories and forms of associated complements | A participant is not automatically a direct object |
| Relations and usage | Meaning relations, collocation, register and variation | Near synonyms may differ in constraints and contexts |

For *Maya ran a company*, the form is *ran*, the category is verb, and the intended sense concerns managing. Identifying past tense does not identify that sense. Conversely, recognizing management does not tell us which past form English uses. Record the source of a proposed entry and distinguish an attested example from a constructed illustration. Unrecorded fields remain unknown rather than being filled from intuition alone.

## Senses and lexical ambiguity

A **sense** is a conventional meaning associated with an item in an analysis. **Polysemy** concerns related senses; **homonymy** concerns distinct lexical identities sharing a form. The locomotion and management uses of RUN illustrate a working sense distinction. The financial-institution and river-edge readings of *bank* illustrate a familiar homonymy analysis. Spelling alone cannot establish either relationship, and dictionaries can differ over how finely to divide senses.

In the constructed sentence *Maya approached the bank*, the broad clause structure stays the same under those two readings. The ambiguity is lexical. Adding *to deposit a cheque* favors the financial reading. Context helps choose an interpretation; it does not mean every contextual inference must become another dictionary sense. [Anderson's ambiguity discussion](../references/anderson-2018-essentials-of-linguistics.md#editing-ambiguity-passage) supports distinguishing lexical alternatives from alternative syntactic structures.

A sense is also different from a **referent**, the entity identified on an occasion. In *Maya runs the company*, the noun's contribution does not identify which company the speaker means without context. Understanding a word's meaning and resolving a particular reference are separate analytical tasks. Anderson's [word-meaning passage](../references/anderson-2018-essentials-of-linguistics.md#additional-foundation-passages) supports this distinction without settling every theory of sense.

## Lexical categories

A word's **category** concerns its grammatical behavior. In *They run*, *run* is a verb; in *a short run*, it is a noun. The shared spelling and related meaning do not make those uses grammatically interchangeable. Inflection and distribution together supply evidence: *ran* contrasts with *run*, while the noun can occur after *a* and take plural *runs*.

Category differs from **function**: noun is a category, whereas Subject and Object name relationships within a construction. Nor is a category a meaning class: an expression describing an event need not be a verb. [Anderson 7.1](../references/anderson-2018-essentials-of-linguistics.md#lexical-category-and-selection-passages) supports using behavior rather than meaning alone. No single diagnostic works for every member of a category.

Open classes readily admit new members; more restricted grammatical classes organize functions such as determination and connection. This introductory distinction does not exclude function words from lexical description. The [Syntax Model](english-syntax-system.md) supplies the package's wider category and function account; competing category inventories remain possible.

## Selection and argument structure

**Selection** concerns the complements and semantic properties licensed in a particular use. **Argument structure** describes participants associated with a predicate and their grammatical realization. **Valency** counts or characterizes arguments or complements under a stated convention; say whether the Subject is included before comparing counts.

A frame is not supplied by the label “verb” alone. Compare *Maya discussed the decision* with *Maya talked about the decision*. Similar subject matter does not make their complement structures identical. In *The outcome depends on the weather*, DEPEND takes an *on*-prepositional phrase (PP); *the weather* is a noun phrase (NP) inside that PP, complementing ON. It is not DEPEND's Direct Object.

[Anderson 8.6](../references/anderson-2018-essentials-of-linguistics.md#lexical-category-and-selection-passages) supports complement-sensitive subcategorization. The local frames below are authored applications. We do not adopt its complete X-bar theory or infer semantic participant counts simply from overt objects.

**Semantic compatibility** is another question. *Maya drank the chair* has an available Subject–Verb–Object shape but conflicts with the ordinary literal expectation of something drinkable. A special fictional or metaphorical context can change the interpretation. Conversely, understanding the intended message does not license every complement form.

Test a proposed frame against the intended sense, variety and construction. Omission alone is insufficient: *Maya ate* can leave what was eaten unexpressed. A missing phrase does not prove that a participant is absent from the interpretation or that every optional phrase is an adjunct. The [Syntax interface](#interface-with-syntax) keeps local structure explicit.

## Lexical relations

Meaning relations connect **particular senses**, not undifferentiated spellings. A relation involving RUN as locomotion need not hold for RUN as management. [Princeton WordNet](../references/princeton-undated-wordnet.md) illustrates a sense-based organization with named relations. The following constructed examples explain a selected subset:

| Relation | What it distinguishes | Example |
|---|---|---|
| Synonymy or near synonymy | Similar meaning, with possible usage differences | *begin* and *start* overlap in starting an activity; substitution still needs checking |
| Hyponymy and hypernymy | A more specific kind and its broader kind | A dog is a kind of animal; DOG is the hyponym |
| Meronymy | Part and whole | A bicycle wheel is part of a bicycle, not a kind of bicycle |
| Antonymy | Opposition on a relevant dimension | *hot* and *cold* contrast in temperature |

Keep the relation label with the pair. A vague “related words” list loses the difference between kind, part and opposite. WordNet's organization is one resource's representation, not a complete theory of lexical meaning or an exhaustive account of English vocabulary.

## Collocations and idioms

A **collocation** is a conventional co-occurrence pattern. In *Maya made a difficult decision*, MAKE with DECISION is the lexical combination; an NP functioning as Object is the syntactic pattern. *Heavy rain* supplies another familiar example. A preference does not make every alternative ungrammatical. The [British Council account](../references/british-council-undated-lexical-combinations.md) distinguishes more restricted and freer combinations; it supplies no corpus counts for these examples.

An **idiom** has a conventional interpretation that cannot be recovered just by composing the ordinary literal meanings. In the constructed *During the argument, Maya lost her head*, the intended idiomatic reading concerns losing control, not physical separation of a head. The British Council's idiom explanation supports this distinction. A recurring combination need not be opaque: knowing that *heavy rain* is conventional does not require treating it as an idiom.

Conventional meaning and fixed wording are separate questions. Record an expression's allowed variation rather than assuming every idiom is frozen: *lose my head* and *lost her head* change tense and person while retaining the intended idiom. This is an authored illustration, not a comprehensive idiom grammar. Keep longer expressions visible in lexical description without creating a separate subsystem for each phrase.

For a frequency claim, identify a corpus, its variety and genre, the query and counts. None were collected here. The present distinction between combination preference and complement licensing is an analytical choice; it is not a claim that all traditions use the term collocation identically.

## Register and variation

**Register** concerns language choices associated with a situation or activity, including formality and specialist usage. **Dialectal variation** concerns patterns associated with communities or regions. These dimensions can interact, but a technical expression is not automatically formal in every setting, and a regional form is not automatically an error.

A useful lexical record distinguishes meaning from appropriateness. For an authored comparison, *kids* and *children* can refer to the same young people while suggesting different styles in a particular document. Whether either fits depends on the speaker, audience, purpose and genre. This is a provisional illustration, not a measured universal ranking or a source-verified register label.

**Connotation** concerns associated attitudes or evaluations, rather than simply the entities a word can describe. Anderson's selected word-meaning discussion supports distinguishing associations from reference. A synonym substitution may preserve a basic description yet change its tone. Do not silently promote an individual association into a community-wide convention.

To substantiate a usage label, inspect a named dictionary's labeling policy or comparable passages from a declared variety and genre. A fuller account of register, regional lexical variation, frequency and changing usage remains an evidence gap. This section gives the reader the distinctions needed to record that gap; it does not complete sociolinguistics within Lexicon.

## Worked entry

Consider the constructed sentence:

> After the meeting, Maya made a decision to run the company.

The lexical analysis connects several kinds of information:

| Expression | Working account | What that account does not settle |
|---|---|---|
| *made* | Past form of MAKE, verb, in MAKE A DECISION | Its spelling alone does not explain the conventional combination |
| *a decision* | NP containing the noun DECISION; Object of MADE | Its importance in the event does not establish its function without structure |
| *run* | Verb RUN in a management use | The locomotion interpretation is not selected merely because the spelling is unchanged |
| *the company* | NP complement of RUN under this reading | The intended organization's identity still needs context |

The *to run the company* clause elaborates the decision's content in this working analysis. It is not another object of RUN. Compare *Maya runs every morning*: the locomotion reading has a different ordinary participant pattern. Compare *Maya ran the company*: tense changes while the management reading can remain. Compare *Maya lost her head*: an idiomatic expression requires conventional knowledge beyond the literal component meanings.

For DEPEND, the entry must retain local hierarchy: *The outcome depends [on [the weather]]*. The outer brackets delimit DEPEND's PP complement; the inner brackets delimit ON's NP complement. Replacing this structure with a list of two objects would misrepresent the construction.

These comparisons explain what the record is for: preserve identity, form, sense, structure and usage as connected but distinct information. They are analytical walkthroughs, not corpus observations or learner results.

## Interfaces

Lexicon overlaps with other subsystems because the same expression has internal form, grammatical behavior and an interpreted contribution. The correspondences below are explanatory constraints, not sequential processing stages. Pronunciation belongs to a variety-labeled form; phonetic detail still requires evidence about actual tokens.

### Interface with Morphology

Morphology describes word-internal structure and grammatical forms. Lexical knowledge supplies conventional identities and senses that those structures do not uniquely determine. The counterpart is explained in [Morphology](english-morphology-system.md#interface-with-lexicon).

| Morphological analysis | Lexical question | Boundary |
|---|---|---|
| Base plus derivational affix | Does a corresponding lexeme exist and which senses are conventional? | Structural possibility is not attested use |
| Compound constituents | Which relation between the constituents is conventional here? | The relation may not be uniquely determined by the parts |
| Inflectional paradigm | Which forms realize a lexeme's grammatical contrasts? | A form is not necessarily a new lexeme |

For *printer*, a working analysis combines *print* with agent/instrument-forming *-er*. The suffix is an interpretation cue, but does not alone choose between a person and a device. In *printers*, plural *-s* changes number without resolving that lexical sense. Keep structure, sense and grammatical form separate.

Compare the predicted structure with attested uses and alternative senses. The balance between lexical storage and productive formation is theory-dependent. Segmentability does not prove current productivity, and lexicalization is not an etymological explanation. This interface retains an authored synthesis; no newly inspected passage establishes all of its claims.

### Interface with Syntax

A lexical sense and its construction constrain the form and category of complements. Syntax represents their local hierarchical relationships. The counterpart is explained in [Syntax](english-syntax-system.md#interface-with-lexicon).

| Lexical sense | Working frame | Local distinctions |
|---|---|---|
| DEPEND dependence | Subject + V + on-PP | NP inside PP complements ON |
| DISCUSS transitive | Subject + V + NP | NP is Direct Object |
| PUT placement | Subject + V + NP + location complement | Location is not another Object |
| RUN management | Subject + V + NP | Different from locomotion use |

For *The result depends on the weather*, *on the weather* is DEPEND's PP complement, while *the weather* is ON's NP complement. Selection information contributes to grammatical licensing; a generic SVO template cannot replace it. For placement PUT, *Maya put the book on the table* distinguishes the Object from a location complement despite both contributing to the described event.

Compare attested frames, omission and meaning shifts, counting semantic participants separately from overt NP objects. Constructional theories can place some licensing information outside an isolated entry; different senses and varieties can permit different patterns. Anderson 8.6 supports the general complement-sensitive distinction, not independent verification of every frame here.

### Interface with Semantics

Lexical analysis identifies a conventional sense; Semantics describes how its contribution combines with other expressions. The counterpart is explained in [Semantics](english-semantics-system.md#interface-with-lexicon).

| Endpoint | Schematic fields |
|---|---|
| Lexical sense entry | Lexeme, sense, selection |
| Predicate interpretation | Predicate, arguments, contextual restrictions |

A **predicate interpretation** characterizes a property, relation or situation and its participants. The mapping uses `kps:constrains`: a sense-specific entry constrains the interpretation without making a spelling identify one context-independent predicate. These fields are analytical records, not measured values or a complete formal theory.

In *Maya runs every morning*, the locomotion use characterizes Maya's activity. In *Maya runs a company*, the management use relates her to the organization. Selecting locomotion solely because the spelling matches fails to capture the intended management reading. Conversely, a dictionary gloss alone cannot determine complete sentence meaning or contextual reference.

Sense, compositional structure and context must be considered together. A constructional or coercion account can distribute the explanation differently; identify the adopted analysis rather than assuming all meaning resides in the entry. Anderson supports bounded ambiguity and meaning/reference distinctions. The particular mappings remain provisional, not an exhaustive sense inventory or automatic disambiguator. Predictions still require comparison with observations and competing analyses.

## Evidence and open questions

Selected [Anderson passages](../references/anderson-2018-essentials-of-linguistics.md), [WordNet documentation](../references/princeton-undated-wordnet.md) and [British Council explanations](../references/british-council-undated-lexical-combinations.md) support the bounded contributions identified above. The entry schema, topic organization and examples are authored applications. Sources attached here do not automatically close the separate evidence gaps in linked Concepts.

This Model does not supply a complete dictionary, corpus frequencies, a historical explanation or a neural storage mechanism. Difficult sense boundaries, register labels, productive versus stored expressions and competing argument-structure accounts need stronger source-specific treatment. An unfamiliar use may be an innovation or contextual extension rather than an error. No independent expert review, speaker study or learning outcome is claimed.

Reusable definitions include [lexeme and word form](../concepts/lexeme-and-word-form.md), [lexical entry](../concepts/lexical-entry.md), [sense and lexical ambiguity](../concepts/sense-and-lexical-ambiguity.md), [lexical selection](../concepts/lexical-selection.md), [collocation](../concepts/collocation.md) and [valency and argument structure](../concepts/valency-and-argument-structure.md). The Model explains their connections locally so these links are optional depth rather than prerequisites for following the examples.
