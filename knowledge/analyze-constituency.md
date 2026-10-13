# Analyze constituency

## Key takeaway
Record candidate constituent boundaries and local relations using converging diagnostics.

## Summary
Record candidate constituent boundaries and local relations using converging diagnostics. The definitions and worked cases below state the intended analysis and its limits. This initial object is provisional; links deepen the explanation but do not replace it.

## Objective

Record candidate constituent boundaries and local relations using converging diagnostics.

## Inputs and prerequisites

A short expression with intended reading and enough surrounding context; familiarity with NP, PP, VP and clause labels. State whether the analysis adopts NP or DP and how auxiliary chains are treated.

## Rationale

A correct category label assigned to the wrong span still produces an incorrect analysis. Substitution, question-answer contexts and coordination can contribute evidence, but any one test can be confounded by grammar or discourse.

## Procedure

1. Preserve the original string and assign token indices.
2. Mark a complete candidate constituent, not just its head.
3. Apply at least two appropriate grouping diagnostics when available.
4. Draw nesting and state each local head and dependency.
5. Check whether a rival reading yields another legitimate grouping.
6. Record evidence, failed tests, framework choices and unresolved boundaries.

## Worked example

In "Anna sent the reports that Maya had prepared to Leo", the intended Object is "the reports that Maya had prepared". The relative is "that Maya had prepared __"; "to Leo" is a higher complement of SENT. A pronoun substitution for the full Object yields "Anna sent them to Leo".

## Expected effect

The output is an explicit, revisable analysis with its assumptions and uncertainties exposed. This is a design expectation, not a measured learning outcome.

## Validation and counterevidence

The replacement must preserve the intended function and meaning sufficiently for the test. Reject partially crossing constituent spans in this tree model. A failure of a single diagnostic is not decisive; retain alternative analyses when appropriate.

## Limits

This procedure produces a proposed analysis, not a universal syntactic tree. Discontinuous constructions, ellipsis and coordination can invalidate simple contiguous-span assumptions.

## Evidence status

**Provisional.** This is an AI-assisted authored draft, not independently reviewed linguistic science. Examples are constructed unless explicitly identified otherwise. No speaker study, corpus result, recorded pronunciation, learner outcome or expert approval is claimed.

Claim-level external source support has not yet been attached. Independent source review and counterexample checking are explicit next tasks, not completed work.

## Related knowledge

- [Constituency](constituency.md) provides a related distinction used in the local explanation.
- [Head and dependent](head-and-dependent.md) provides a related distinction used in the local explanation.
- [Relative clause](relative-clause.md) provides a related distinction used in the local explanation.
- [Object and PP complement](object-and-pp-complement.md) provides a related distinction used in the local explanation.
