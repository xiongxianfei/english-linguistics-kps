---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# KPS compatibility

## Key takeaway
The domain versions its own content separately from the KPS authoring language and tested upstream release.

## Summary
The domain versions its own content separately from the KPS authoring language and tested upstream release. The initial broad release remains provisional; supporting links and checks do not constitute independent scientific review.

## Declaration

```json
{"kps_language":"9.x","validated_with":"9.0.1","markdown_profile":"practical-markdown-v1","upstream_commit":"60972c57199ae8bc21d4b7a00ac55552b4105277"}
```

The authoring contract, validator and regression suite are pinned, not dynamically installed from a changing branch. See [lock metadata](upstream-lock.json). The exact validation execution is recorded separately in validation-evidence.json after checks actually run.

## Independent package

The five knowledge folders and reference records are readable locally with no sibling package. Knowledge objects retain stable IDs independently of path changes. Domain version 0.1.0 does not pretend to be KPS release 0.1.0; language and content versions answer different questions.

## Review on update

Compare a candidate upstream release against AUTHORING.md, inspect changed validation behavior, review affected content and rerun the suites. Do not infer future compatibility from a matching major numeral alone. Upstream updates should use a separate reviewed PR and update attribution and lock hashes.

## Limitations

Compatibility is a structural and authoring claim. It is not factual certification, expert approval, verified learning benefit or a literal processing architecture. The current upstream validator uses a deliberately restricted Markdown and JSON-compatible YAML profile.
