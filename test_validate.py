#!/usr/bin/env python3
"""Run KPS 12 core invariants. KPS 9 tests remain in the preserved snapshot."""
import unittest
from pathlib import Path
if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root / 'tests'), pattern='test_kps12.py')
    raise SystemExit(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())
