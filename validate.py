#!/usr/bin/env python3
"""KPS 12 validator entrypoint; compatibility helpers serve ported content tests."""
import json
import sys
from pathlib import Path
from tools.kps12 import Document, parse, section, slug, meaningful, targets, validate

if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise SystemExit('Usage: python3 validate.py [ROOT]. Baseline refresh requires tools/accept_dependency_review.py --record PATH.')
    root = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).resolve().parent
    result = validate(root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['ok'] else 1)
