"""Tests of declared repository policy, not pronunciation or phonetic truth."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GeneralAmericanPolicyTests(unittest.TestCase):
    def text(self, p):
        return (ROOT / p).read_text(encoding="utf-8")

    def test_general_american_is_primary(self):
        self.assertIn("General American", self.text("SCOPE.md"))
        self.assertIn("primary reference", self.text("SCOPE.md"))
        self.assertIn("PRONUNCIATION.md", self.text("README.md"))

    def test_transcription_levels_are_distinct(self):
        s = self.text("PRONUNCIATION.md")
        self.assertIn("/pɪn/", s)
        self.assertIn("[pʰɪn]", s)
        self.assertIn("/si/", s)
        self.assertIn("/kɑr/", s)
        self.assertIn("candidate", s.lower())

    def test_source_records_are_bounded(self):
        for filename in ("sounds-american-undated-chart-and-terms.md", 
                         "tophonetics-undated-english-transcription.md",
                         "international-phonetic-association-undated-interactive-chart.md"):
            s = self.text("references/" + filename)
            self.assertIn("access_extent:", s)
            self.assertIn("## Nonclaims", s)
            self.assertIn('reviewed: null', s)

    def test_no_automatic_scientific_promotion(self):
        for filename in ("concepts/vowel-articulation.md",
                         "concepts/consonant-articulation.md",
                         "concepts/representation-levels.md",
                         "methods/analyze-sound-realization.md"):
            s = self.text(filename)
            self.assertIn('evidence_status: "provisional"', s)
            self.assertIn("PRONUNCIATION", s)
            self.assertIn('reviewed: null', s)

if __name__ == "__main__":
    unittest.main()
