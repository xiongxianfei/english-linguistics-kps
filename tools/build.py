#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
from kpslib import check_generated, write_generated

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    parser = argparse.ArgumentParser(description="Build deterministic KPS 12 views and JSON projections.")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        stale = check_generated(ROOT)
        if stale:
            print("Stale generated files:")
            for item in stale: print(" -", item)
            return 1
        print("Generated views are fresh")
        return 0
    files = write_generated(ROOT)
    print(f"Wrote {len(files)} generated files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
