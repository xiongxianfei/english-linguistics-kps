# KPS 12 repository mechanism

## Key takeaway
Primary role determines storage; metadata expresses subject and relationships; build tools derive every alternate view.

## Summary
This repository uses one canonical Markdown file for each knowledge item. Concept, Principle, Model, Method and Practice are mutually exclusive primary roles. Domains and relation predicates are open author vocabulary constrained only by stable kebab-case syntax and resolvable targets. Sources are external provenance records; references are links from knowledge to those sources.

## Canonical mechanism

1. **Identify** a reusable knowledge item and assign one primary role.
2. **Assert** one or more scoped claims in its metadata and explanation.
3. **Relate** it to other items using the most specific responsible predicate available.
4. **Ground** claims in inspected sources or leave evidence explicitly pending.
5. **Classify** it in any relevant domains; membership is many-to-many.
6. **Project** domain, relation, interface, review, search and sequence views from canonical Markdown.

## Five roles

- **Concept:** defines and distinguishes a reusable thing or analytical distinction.
- **Principle:** states and explains a scoped general relationship.
- **Model:** supplies an explicit representation, including cross-domain interfaces.
- **Method:** specifies a bounded repeatable analytical operation.
- **Practice:** coordinates knowledge and operations for a recurring goal through locally sufficient stages.

Folder location supplies the role; a redundant `role` field is forbidden.

## Open vocabulary

Authors may introduce a domain or relation predicate when existing terms are inadequate. IDs use lower-case kebab-case, with colon-separated subdomains such as `phonology:phonotactics`. Predicates such as `uses`, `constrains`, `maps-to` or `updates-and-constrains` carry no automatic causal, symmetric or transitive inference. The generated vocabulary views expose collisions for editorial review.

## Claims and sources

Claims are embedded in their owning file and receive derived identities such as `english:allomorphy#key-takeaway`. `sources/` records what external material was actually inspected and what it does not establish. Evidence assessments target a claim; a source mention marked `context-only` is not claim support.

## Interfaces

An interface is a Model with explicit source and target domains, representation labels, mapping predicate, scope, cardinality and claim. Domain overlap alone is not an interface, and source-to-target ordering is documentation rather than a temporal processing claim.

## Sequences

Sequences are optional authored routes over canonical knowledge. They are pedagogical or operational recommendations, not ontology, causal order or proof of mastery.

## Generated material

Everything under `views/` and `generated/`, plus root compatibility indexes, is derived. Deleting and rebuilding it must not lose unique knowledge.
