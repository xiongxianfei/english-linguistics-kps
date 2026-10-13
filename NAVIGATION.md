---
language: "KPS 12.x"
package_version: "0.1.0"
status: "draft"
---

# Navigation conventions

## Key takeaway
Portable relative Markdown links and stable metadata IDs serve different jobs.

## Summary
Portable relative Markdown links and stable metadata IDs serve different jobs. The initial broad release remains provisional; supporting links and checks do not constitute independent scientific review.

## Files and headings

Use [the system model](models/english-system-architecture.md) as an ordinary relative link. Use conservative ASCII words in headings under the current upstream validator. Heading fragments derive from the full heading text, not from metadata IDs. Do not create custom HTML anchors or use Obsidian wikilinks.

## Generated views

INDEX.md, COVERAGE.md, REVIEW-QUEUE.md and knowledge-graph.json are generated from canonical object metadata. Edit source objects and run python3 tools/build_navigation.py. CI --check detects drift without rewriting files. Stages 0 through 7 provide coverage navigation, while Practice stages are local numbered execution steps.

## Reader limits

Markdown rendering and IPA font appearance vary by application. Ordinary text and relative links remain usable without optional graph plugins. Generated views are not additional authoritative definitions.
