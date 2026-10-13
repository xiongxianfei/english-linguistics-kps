"""Ported policy safeguards on active KPS 12 content and source entities."""
from pathlib import Path
import unittest
from tools.kps12 import load
ROOT=Path(__file__).resolve().parents[1]

class GeneralAmericanPolicyTests(unittest.TestCase):
    def text(self,path):return (ROOT/path).read_text(encoding='utf-8')
    def test_general_american_is_primary(self):
        self.assertIn('General American',self.text('SCOPE.md'))
        self.assertIn('primary reference',self.text('SCOPE.md'))
        self.assertIn('PRONUNCIATION.md',self.text('README.md'))
    def test_transcription_levels_are_distinct(self):
        s=self.text('PRONUNCIATION.md')
        for v in ['/pɪn/','[pʰɪn]','/si/','/kɑr/']:self.assertIn(v,s)
        self.assertIn('candidate',s.lower())
    def test_source_records_are_bounded(self):
        records,_=load(ROOT)
        for name in ['sounds-american-undated-chart-and-terms','tophonetics-undated-english-transcription','international-phonetic-association-undated-interactive-chart']:
            r=records['english:'+name];self.assertTrue(r['access_extent']);self.assertIsNone(r['reviewed'])
            self.assertIn('## Nonclaims',self.text(r['content']))
    def test_no_automatic_scientific_promotion(self):
        records,_=load(ROOT)
        for name in ['vowel-articulation','consonant-articulation','representation-levels','analyze-sound-realization']:
            r=records['english:'+name];self.assertEqual(r['evidence_status'],'provisional');self.assertIsNone(r['reviewed'])
            self.assertIn('PRONUNCIATION',self.text(r['content']))
