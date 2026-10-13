#!/usr/bin/env python3
"""Check the English package's declared ten-domain scope."""
from pathlib import Path
from kps12 import load, validate, dump

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'phonetics', 'phonology', 'morphology', 'lexicon', 'syntax', 'semantics',
            'pragmatics', 'discourse', 'information-structure', 'prosody'}
if __name__ == '__main__':
    result = validate(ROOT)
    records, _ = load(ROOT)
    actual = {r['id'].split(':')[-1] for r in records.values() if r['kind'] == 'domain' and r.get('top_level')}
    if actual != EXPECTED:
        result['ok'] = False
        result['errors'].append({'code': 'english-domains', 'message': 'Expected exactly the ten declared primary domains.'})
    print(dump(result))
    raise SystemExit(not result['ok'])
