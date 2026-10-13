#!/usr/bin/env python3
"""Generate KPS 12 views without accepting dependency or evidence changes."""
import argparse
from pathlib import Path
from kps12 import build

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        stale = build(Path(__file__).resolve().parents[1], args.check)
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + '\n')
    print('Stale views: ' + ', '.join(stale) if stale else 'KPS 12 navigation views checked' if args.check else 'KPS 12 navigation views generated')
    raise SystemExit(bool(stale))
