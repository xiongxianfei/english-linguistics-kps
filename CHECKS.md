# Checks

## Key takeaway
Validation establishes repository coherence and reproducibility, not linguistic truth.

## Commands

```bash
python3 tools/build.py --check
python3 validate.py .
python3 -m unittest discover -s tests -v
python3 tools/query.py --interfaces
```

## What is checked

Unique IDs and aliases; role/folder consistency; required sections; synchronized key-takeaway claims; resolvable relations and sources; open-vocabulary syntax; interface endpoint fields; sequence members; ten-domain foundation coverage; source inspection metadata; generated-view freshness; and selected constructed regression examples.

## What is not checked

Whether a linguistic claim is true, whether an example is frequent or acceptable across varieties, whether a source passage actually supports a claim beyond its recorded assessment, whether a reviewer performed a review, or whether a Practice improves learning.

## Generated files

`python3 tools/build.py` writes `views/`, `generated/`, `INDEX.md`, `COVERAGE.md` and `REVIEW-QUEUE.md`. `--check` compares without rewriting. CI must remain read-only after checkout.
