# KPS 12 compatibility

## Key takeaway
The active entity/claim/interface schema is a breaking change from KPS 9; original identities and content are preserved through explicit mappings.

## Summary
The English package is 0.2.0 and uses KPS 12.x profile 12.0.0-draft.1. This is a local reference implementation, not a claim about the separate upstream KPS project's releases. The unchanged upstream tooling lock remains under legacy/kps9/upstream-lock.json.

## Boundaries
Old KPS 9 metadata and graph consumers are not compatible with active format 12. JSON canonical records replace role-frontmatter authority. Ordinary Markdown links remain portable; old role paths provide redirects and old IDs resolve through aliases. Source records retain their original publication names, access dates and licensing qualifications.

## Runtime
Python 3.10 or newer is required. The runtime uses only the standard library and no database, external ontology engine, Markdown plugin or network call. Schema validation is structural, with no implicit OWL/RDF, causal or transitive inference.

## Migration
See [MIGRATION](MIGRATION.md), [the specification](spec/KPS12.md) and [validation boundaries](CHECKS.md).
