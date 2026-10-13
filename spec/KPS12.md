# KPS 12 entity profile

## Key takeaway
A knowledge entity has stable identity independently of its role, domain, storage path, claims and relationships.

## Summary
This repository implements the local, experimental KPS 12 profile `12.0.0-draft.1`. It is the first English-domain implementation requested by the repository owner, not a claim that the separate upstream KPS project has published version 12. The domain package is version `0.2.0`. KPS 10 and KPS 11 releases are not implied.

## Identity and record kinds
Every canonical graph node is an entity in `entities/*.json`, with schema `kps:12:entity`, a namespaced stable `id`, `kind`, `label`, `version`, `status`, `roles`, `domains`, `aliases` and `relations`. Neither folder names nor substrings of an identifier determine its semantics. New IDs omit the old knowledge-role segment; old IDs remain resolvable aliases. Changing a role or a file path must not change the entity ID.

`kind` controls structural validation, not the five knowledge roles. Supported record kinds are `knowledge`, `interface`, `representation`, `claim`, `evidence`, `source`, `domain`, `role`, `relation-type` and `sequence`. They are all identifiable entities in the same store. The five familiar roles classify knowledge and interface records. This profile permits more than one role only when the content satisfies the union of their authoring obligations; migration does not invent extra roles.

## Storage and authoring
Structured facts about an entity are canonical JSON. Human explanations are ordinary UTF-8 Markdown under `knowledge/` or `sources/`, linked by an entity's `content` path. Each content file has exactly one owner. Markdown has one title, a Key takeaway and Summary, and the locally sufficient sections required by the assigned roles. JSON Schema describes serialization; the Python validator additionally checks graph, role, content, provenance and migration invariants.

Legacy `concepts/`, `principles/`, `models/`, `methods/`, `practices/` and `references/` paths are compatibility redirects, not competing knowledge stores. The immutable `legacy/kps9/` snapshot is historical input and is excluded from the active entity graph. Its original validation suites remain executable.

## Roles
Concept defines a distinction, Principle states and explains a scoped relationship, Model contains an explicit representation, Method gives an executable bounded operation, and Practice supplies locally sufficient operational stages. Role definitions are entities with section obligations. A command is not automatically a Principle; a bibliography record is not a sixth knowledge role.

## Domains and internal structure
Domain memberships are many-to-many. Domains have stable IDs, explicit scope and zero or more broader parents. The parent graph must be acyclic. A broader-domain edge is classification, not a causal claim or a universally accepted linguistic `is-a` relation. The English package supplies ten independently navigable domains and provisional subdomain scopes. Prosody and Information Structure remain visible without being isolated from neighboring domains. The KPS core does not hard-code their names.

Coverage means explicitly classified content, not exhaustive or scientifically adequate treatment. A registered subdomain with zero objects must appear as an unrepresented coverage gap. Foundations and knowledge maintenance are supporting classifications, not additional primary linguistic subsystems.

## Relations and inference boundaries
Every authored predicate resolves to a `relation-type` entity with allowed source kinds, target kinds, a layer, a description and an explicit acyclicity policy. Migrated role-specific dependencies become `kps:uses` with an `expected_target_role` constraint, preserving the old type check. Document use, citation, navigation, classification and semantic mapping remain separate layers.

Relation instances have stable generated edge IDs. Semantic mappings must identify a versioned claim and scope. KPS 12 performs no automatic causal, symmetric, transitive or truth inference. It does not assume that arbitrary uses edges form an acyclic learning prerequisite graph. Only predicates declared acyclic, including Practice composition, are checked for cycles. Domain hierarchy is checked independently.

## Claims
A Claim entity has an owner, the exact owner version, a nonempty statement, scope, extraction provenance and evidence state. The owner declares its claim IDs. This migration exposes each knowledge object's Key takeaway as one **summary claim**, not an assertion that the summary is atomic. Other sentences in the body remain unextracted and are named as review work. Key-takeaway-derived claims must remain textually synchronized with that source section.

A statement in an entity record is an authored assertion, not an endorsement by the framework. Constructed examples remain constructed. Review status is not inferred from tests, citation count or a version increment.

## Sources and evidence
Source entities retain publication identity, date basis, historical inspection extent and nonclaims. Migration is not a new inspection of the publication. An Evidence entity identifies the source, its target and the assessment relation. `context-only` evidence preserves a legacy document citation without asserting support for an extracted claim.

`supports`, `qualifies` and `contradicts` require a specific Claim target, a located source passage, an explicit assessment and an inspection-extent statement. Legacy-citation migration cannot create those stronger relations. Reviewed status requires a version-specific record naming an actual reviewer and findings; a validator can check the declaration but cannot establish that the reviewer really performed the review. No independent review is claimed in this release.

## Representation interfaces
An interface is an entity with a Model role, a locally sufficient explanation and a `mapping` identifying source representation, target representation, predicate, claim, scope and cardinality. Endpoint representations are separate entities with domain membership and a schematic structure. Interface domains must include the endpoint domains.

A source/target ordering declares how a correspondence is documented; it does not establish a temporal processing order. Cardinality is `unspecified` until justified. The five pre-existing interface Models are migrated without changing their linguistic claims. Five additional bridge Models are explicitly authored, provisional, illustrative additions, not experimentally validated findings.

## Sequencing
The legacy Stage 0–7 route is a Sequence entity. Membership records identify positions in that route, not ontological identity or empirically necessary prerequisites. Local Practice Stage1, Stage2 and later steps remain distinct from the global route. Their complete maps, stage-local instructions and pending-outcome safeguards are retained.

## Dependency review
`summary-dependencies.json` records content hashes and explicit document dependencies. Ordinary validation and view generation never refresh it. A changed source or dependent summary requires an editorial review record identifying before and after snapshots, the changed entities and affected dependents, an actual reviewer, date and findings. The acceptance tool validates that record before recording a new baseline. It does not promote scientific evidence status.

The initial KPS 12 baseline is explicitly a mechanical migration baseline, not a claim of new independent scientific review. The migration manifest retains original file hashes and the exact content transformations.

## Version and compatibility
The schema is a breaking change from KPS 9. Old `type`, role-based IDs, role-specific dependency fields and root-level stages are migrated into independent dimensions. JSON entity records and a format-12 graph are the active contract. KPS 9 software is not expected to understand the new graph. The old package is preserved verbatim under `legacy/kps9/`, and original IDs and Markdown paths have mappings.

The first implementation uses `KPS 12.x` and profile `12.0.0-draft.1`. Stabilizing this generic profile in the separate KPS repository is future work, not a completed upstream release.
