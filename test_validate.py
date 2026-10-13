#!/usr/bin/env python3
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tools'))
from kpslib import validate

class ValidationSmokeTest(unittest.TestCase):
    def test_valid(self):
        result=validate(ROOT)
        self.assertTrue(result['ok'],result['errors'])

if __name__=='__main__':unittest.main(verbosity=2)
