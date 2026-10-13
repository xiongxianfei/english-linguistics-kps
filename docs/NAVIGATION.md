---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# Navigation conventions

## Key takeaway
Read self contained Models for understanding and use catalogs only to locate additional detail.

## Summary
README and the ten English subsystem Models are the reader entry points. Each Model includes the terms, structure, worked example and limitations needed for its own purpose. Links deepen the explanation; neither a graph nor a sequence engine is needed.

## Files and headings
Use ordinary relative Markdown links to real files. Heading fragments match the full heading in lowercase with hyphens; metadata identities do not create anchors. When a heading changes, update its stage map and incoming links.

## Optional catalogs
[Knowledge index](INDEX.md) summarizes each canonical item by role. [Review priorities](REVIEW.md#priority-evidence-gaps) describe remaining evidence work and coverage limits. The index is generated from canonical Markdown with `python3 tools/build_navigation.py` from the repository root; the generator does not alter knowledge or dependency fingerprints.

The old global stages metadata retained in unchanged inherited notes is historical classification only and is not used for navigation. Numbered stages inside a Practice are actions within that Practice, not a course sequence. There is no sequences/ folder.

## Reader checks
Hide links and attempt the file's intended task. Check that a Model explains the relationship instead of telling the reader to consult another file. Follow at least one real link in the intended reader when a click test is available; structural validation alone does not prove viewer behavior.
