# KPS 12 validation boundaries

## Key takeaway
Executable invariants, preserved source content and scientific truth are different questions.

## Summary
The active suite validates the entity-centric KPS 12 profile, domain and interface semantics, claim ownership, evidence limitations, relative links and deterministic views. The original KPS 9 suite remains runnable against the preserved baseline. Test success does not certify linguistic truth or the effectiveness of pronunciation Practices.

## Recorded execution
Run `python3 tools/run_checks.py` to execute active and historical suites, verify exact first-migration reproducibility, and write `validation-evidence.json` with actual outcomes and a SHA-256 input manifest. CI uploads its newly executed report rather than claiming the committed local report was a CI run. For future content releases, replace the first-migration reproduction gate with a reviewed new fixture; do not regenerate an old migration to overwrite later authored changes.

## Active checks
```bash
python3 validate.py .
python3 test_validate.py
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
python3 tools/check_preservation.py
```

The active tests include destructive mutations in temporary copies: unknown domains and predicates, dangling targets, alias collisions, domain and composition cycles, malformed interfaces, claim version drift, unsupported evidence promotion, stale views and pending dependency reviews. The General American policy, phone/word Practice contracts and constructed linguistic fixtures are also tested on active KPS 12 content.

## Historical regression checks
```bash
cd legacy/kps9
python3 validate.py .
python3 test_validate.py
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

Historical tests describe the old profile only. The preservation checker verifies the exact baseline hashes and the migrated body transformations, rather than treating historical tests as evidence of active-profile correctness.

## Dependency review
Ordinary validation and view generation never accept a changed dependency baseline. Write a review record containing `reviewer`, `date`, `findings`, `before_sha256`, `after_sha256`, `changed_entities` and `affected_dependents`, then run:

```bash
python3 tools/accept_dependency_review.py --record reviews/your-editorial-review.json
python3 tools/build_navigation.py
python3 validate.py .
```

The hashes are SHA-256 of the canonical sorted JSON serialization used by the tool for the complete previous and proposed snapshot. The acceptance tool requires an exact matching change set and affected-dependent set; it does not perform the human or editorial review. No such acceptance belongs in CI, and no scientific status changes as a side effect.

## Reproducibility and security
The permanent GitHub Actions workflow has `contents: read`, does not retain credentials and has no deployment or branch-writing step. Temporary migration/export workflows are removed before the final pull request is ready. Validation reports identify their input tree or payload manifest; no old validation report is relabelled as a new execution.

## Limits
JSON validation cannot prove a publication was read, a reviewer performed a review, a linguistic claim is true, a waveform was measured or a learner improved. The package remains scientifically provisional. Missing atomic-claim decomposition and unrepresented subdomains are explicit review work.
