#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))
from kpslib import validate

def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    result = validate(root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
