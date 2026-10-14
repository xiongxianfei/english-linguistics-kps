---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# Navigation conventions

## Key takeaway
Use the body of knowledge outline to find a topic, read its explanations and follow a Practice for a target task.

## Summary
The README links to the authored body of knowledge outline and target Practices. The body of knowledge outline organizes topics and their relationships; the role index catalogs files; Practices organize activities. The linked knowledge remains locally sufficient for its own purpose.

## Files and headings
Use ordinary relative Markdown links to real files. Heading fragments match the full heading in lowercase with hyphens; metadata identities do not create anchors. When a heading changes, update its stage map and incoming links.

## Subject navigation

[English Linguistics Body of Knowledge Outline](body-of-knowledge-outline.md) is the subject coverage guide for this package. Its six areas and 39 topics include foundations of analysis and thirteen sound-system topics, alongside word structure, syntax, meaning and context. Each topic states required understanding, intended capability and existing explanations or gaps. A topic may refer to several files, and a file may support several topics. Keep this authored outline and its overview illustration aligned; no generator or new knowledge type is required. Practices and the README own task navigation.

[Learn English linguistics](../practices/learn-english-linguistics.md) selects from the outline and adds a learning route. Other Practices can use the same subject structure for different targets. Keep one shared subject outline rather than copying it into each Practice.

## Optional catalogs
[Knowledge index](INDEX.md) summarizes each canonical item by role. [Review priorities](REVIEW.md#priority-evidence-gaps) describe remaining evidence work and coverage limits. The index is generated from canonical Markdown with `python3 tools/build_navigation.py` from the repository root; the generator does not alter knowledge or dependency fingerprints.

The old global stages metadata retained in unchanged inherited notes is historical classification only and is not used for navigation. Numbered stages inside a Practice are actions within that Practice, not a course sequence. There is no sequences/ folder.

## Reader checks
Hide links and attempt the file's intended task. Check that a Model explains the relationship instead of telling the reader to consult another file. Follow at least one real link in the intended reader when a click test is available; structural validation alone does not prove viewer behavior.
