# Representation interfaces

## Key takeaway
Interface Models connect explicit representation labels through scoped, provisional mappings.

## Summary
Generated from canonical KPS 12 Markdown. Views are navigation artifacts, not independent knowledge or scientific review.

| Interface | Source | Predicate | Target | Cardinality |
|---|---|---|---|---|
| [Discourse Information Structure interface](../models/discourse-information-structure-interface.md) | discourse / discourse-context | `constrains` | information-structure / focus-domain | unspecified |
| [Information Structure Prosody interface](../models/focus-prosody-interface.md) | information-structure / focus-domain | `constrains` | prosody / prominence-pattern | unspecified |
| [Lexicon Morphology interface](../models/lexicon-morphology-interface.md) | lexicon / lexical-entry | `constrains` | morphology / morphological-structure | many-to-many |
| [Lexicon Semantics interface](../models/lexicon-semantics-interface.md) | lexicon / lexical-sense-entry | `constrains` | semantics / predicate-interpretation | unspecified |
| [Lexicon Syntax interface](../models/lexicon-syntax-interface.md) | lexicon / lexical-selection-frame | `constrains` | syntax / syntactic-complement-structure | unspecified |
| [Morphology Phonology interface](../models/morphology-phonology-interface.md) | morphology / inflection-features | `maps-to` | phonology / phonological-exponent | unspecified |
| [Morphology Syntax interface](../models/morphology-syntax-interface.md) | morphology / grammatical-word-features | `constrains` | syntax / agreement-and-finiteness-pattern | unspecified |
| [Phonology Phonetics interface](../models/phonology-phonetics-interface.md) | phonology / phonological-form | `constrains` | phonetics / phonetic-realization | unspecified |
| [Pragmatics Discourse interface](../models/pragmatics-discourse-interface.md) | pragmatics / utterance-interpretation | `updates-and-constrains` | discourse / discourse-context | many-to-many |
| [Prosody Phonetics interface](../models/prosody-phonetics-interface.md) | prosody / prominence-pattern | `constrains` | phonetics / prosodic-acoustic-description | unspecified |
| [Semantics Pragmatics interface](../models/semantics-pragmatics-interface.md) | semantics / conventional-contribution | `constrains` | pragmatics / utterance-interpretation | unspecified |
| [Syntax Prosody interface](../models/syntax-prosody-interface.md) | syntax / syntactic-structure | `constrains` | prosody / prosodic-phrasing | many-to-many |
| [Syntax Semantics interface](../models/syntax-semantics-interface.md) | syntax / clause-functions | `maps-to` | semantics / participant-roles | unspecified |

## Limits

An interface is an authored Model, not an automatic causal or processing edge. All mappings remain provisional unless their claim evidence says otherwise.
