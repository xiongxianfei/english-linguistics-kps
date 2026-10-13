# KPS 12 navigation

## Key takeaway
Browse one canonical knowledge graph by role, domain, interface, claim, evidence or sequence.

## Summary
INDEX.md, DOMAINS.md, INTERFACES.md, COVERAGE.md, SOURCES.md, REVIEW-QUEUE.md, views/domains and knowledge-graph.json are generated from canonical entity records. File hierarchy is not the ontology.

## Commands
```bash
python3 tools/build_navigation.py
python3 tools/build_navigation.py --check
python3 tools/kps12.py query --domain linguistics:prosody
python3 tools/kps12.py query --role kps:role:model --interfaces
python3 tools/kps12.py query --id english:concept:prosody
python3 tools/kps12.py query --claim english:prosody:claim:key-takeaway
```

An empty claim-evidence result means no substantive evidence record targets that claim; it does not mean the owner has no bibliography links. Use the explicit graph layers to distinguish citations, classifications, document dependencies and semantic mappings.

## Paths and anchors
Canonical Markdown under knowledge and sources uses ordinary relative links. Old paths contain compatibility redirects and preserve original heading anchors. Entity IDs are not Markdown anchors. Sequence positions are navigation choices, not intrinsic linguistic levels.
