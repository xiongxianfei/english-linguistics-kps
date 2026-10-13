#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from kpslib import validate
r=validate(ROOT)
print(f"Domain checks: {r['stats']['knowledge_items']} knowledge items; {r['stats']['interfaces']} interfaces; {len(r['errors'])} errors; no factual certification")
for e in r['errors']: print(e)
raise SystemExit(0 if r['ok'] else 1)
