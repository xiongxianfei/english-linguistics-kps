# Quantifier scope model

## Key takeaway
A finite-domain toy model makes scope differences explicit without claiming that logic alone predicts English reading availability.

## Summary
A finite-domain toy model makes scope differences explicit without claiming that logic alone predicts English reading availability. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Purpose

A finite-domain toy model makes scope differences explicit without claiming that logic alone predicts English reading availability.

## Representation

```text
EVERY > A:
  for every x in teachers, some y in books satisfies recommend(x,y)
A > EVERY:
  some y in books satisfies recommend(x,y) for every x in teachers

NOT > EVERY:
  not all relevant individuals satisfy P
EVERY > NOT:
  all relevant individuals fail to satisfy P
```

## Worked interpretation

Three teachers with nonoverlapping recommendations satisfy EVERY > A but not A > EVERY. A common recommended book satisfies both. A > EVERY does not mean that exactly one book exists or that nobody recommends additional books.

## Assumptions and limits

Classical quantification treats an empty universal restrictor vacuously. With no relevant teachers, shared-book claims also depend on whether the book domain is empty. These edge cases are retained in regression tests, not hidden behind informal some/not-all glosses.

## Evaluation and counterevidence

Enumerate small domains and relations to verify formal implications. Such tests validate only the explicit logical implementation. Actual acceptability and accessibility of inverse scope require linguistic evidence.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Related knowledge

- [Quantification and scope](quantification-and-scope.md) provides a related distinction used in the local explanation.
- [Negation and entailment](negation-and-entailment.md) provides a related distinction used in the local explanation.
- [Semantic predicate](semantic-predicate.md) provides a related distinction used in the local explanation.
