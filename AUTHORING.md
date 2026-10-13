# KPS 12 authoring contract

## Key takeaway
Author canonical entity records and self-contained explanations; generate all alternate views from them.

## Summary
The repository-local [KPS 12 specification](spec/KPS12.md) replaces the active KPS 9 contract. Its five knowledge roles retain their explanatory and operational responsibilities but no longer define entity identity or storage folders. The upstream KPS 9 contract remains unchanged in the historical snapshot.

## Canonical edits
Edit `entities/*.json` and its uniquely owned Markdown `content` file. Assign stable, role-independent IDs and only registered role/domain/predicate IDs. A role or domain change does not rename an identity. Add aliases only when they are globally unambiguous. Do not edit generated indexes, redirects or `knowledge-graph.json` as if they were canonical knowledge.

## Local completeness
Use one title, Key takeaway and Summary. Concept needs Definition, Distinctions and Scope and limits; Principle needs Statement, Explanation and Scope and counterevidence; Model needs Purpose, Representation, Assumptions and limits, and Evaluation and counterevidence; Method needs Objective, Inputs and prerequisites, Rationale, Procedure, Expected effect and Validation and counterevidence. Knowledge roles can overlap only when every applicable obligation is fulfilled.

Practice retains consecutively numbered `## Stage1 Name` headings, a complete stage map and local Goal, Why, What to do, What to observe, Success signal and Next fields in every stage. Keep executable procedures, fallbacks and current-outcome uncertainty. A list of links cannot replace stage content.

## Claims and evidence
Synchronize extracted summary claims with their source Key takeaway. Name the exact owner version. Add atomic claim records only after identifying their actual scope. Preserve constructed examples, alternative analyses and historical source-access limits. An entity citation is not evidence for every claim. Substantive evidence must target a Claim, identify a source passage and explain its contribution. Never fabricate a locator, reviewer, source inspection or learner result.

## Interfaces
Specify representations, not merely domain names. Provide a mapping predicate, owned claim, scope, cardinality and a locally explained example. Keep observation separate from prediction. Semantic edges do not establish a neural pipeline, and classification overlap is not a causal connection.

## Change workflow
Read [CHECKS](CHECKS.md), [SCOPE](SCOPE.md), direct dependencies and source nonclaims. Update the canonical content and corresponding claims/versions together. When a dependency baseline changes, inspect affected summaries and provide an editorial review record using [the migration guide](MIGRATION.md). Then regenerate views, run tests and open a bounded pull request. Neither baseline refresh nor graph generation is scientific review.
