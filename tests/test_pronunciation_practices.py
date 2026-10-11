"""Document-contract tests, not speech recognition or evidence of learning outcomes."""
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate as kps

FILES = {
    'word': ROOT / 'practices/learn-word-pronunciation.md',
    'phone': ROOT / 'practices/classify-and-produce-phone.md',
}

class PronunciationPracticeTests(unittest.TestCase):
    def setUp(self):
        self.docs = {key: kps.parse(path) for key, path in FILES.items()}

    def test_two_real_practices_with_ga_scope(self):
        for doc in self.docs.values():
            self.assertEqual(doc.meta['type'], 'practice')
            self.assertEqual(doc.meta['reference_variety'], 'General American')
            self.assertEqual(doc.meta['stages'], [6, 7])
            self.assertEqual(doc.meta['status'], 'draft')

    def test_stage_maps_and_six_local_stages(self):
        for doc in self.docs.values():
            stages = [(n, h) for n, h in doc.headings if n == 2 and re.match(r'Stage\d+ ', h)]
            self.assertEqual(len(stages), 6)
            self.assertEqual([h for _, h in stages], doc.meta['stage_titles'])
            for i, (_, heading) in enumerate(stages, 1):
                self.assertTrue(heading.startswith(f'Stage{i} '))
                self.assertIn('#' + kps.slug(heading), doc.links)
                body = kps.section(doc, re.escape(heading))
                for label in ('Goal', 'Why', 'What to do', 'What to observe', 'Success signal', 'Next'):
                    self.assertRegex(body, r'\*\*' + re.escape(label) + r':\*\*\s+\S')
                self.assertIn('procedure', body.lower())
                self.assertIn('fallback', body.lower())
                self.assertGreater(len(kps.meaningful(body).split()), 110)

    def test_no_invented_review_or_performance(self):
        for doc in self.docs.values():
            self.assertEqual(doc.meta['evidence_status'], 'provisional')
            self.assertIsNone(doc.meta['reviewed'])
            self.assertIn('provisional', kps.section(doc, 'Evidence status').lower())
            self.assertIn('No learner application recorded', kps.section(doc, 'Current practice summary'))
            self.assertIn('not', kps.section(doc, 'Evidence status').lower())

    def test_analysis_listening_and_production_are_distinct(self):
        for doc in self.docs.values():
            for phrase in ('Perception status:', 'Production status:', 'pending'):
                self.assertIn(phrase, doc.body)
            self.assertIn('recording', doc.body.lower())
            self.assertIn('listener', doc.body.lower())
            self.assertIn('actual', doc.body.lower())

    def test_word_includes_retrieval_transfer_and_source_checks(self):
        s = self.docs['word'].body
        for phrase in ('unprompted', 'homographs', 'TTS', 'American', 'weak forms', 'dictionary', 'self-checked'):
            self.assertIn(phrase.lower(), s.lower())
        self.assertIn('Later retrieval and transfer status:', s)
        self.assertIn('/pɪn/', s)
        self.assertIn('[pʰɪn]', s)
        self.assertIn('/əˈbaʊt/', s)

    def test_phone_supports_both_input_routes_and_features(self):
        s = self.docs['phone'].body
        for phrase in ('Symbol-led route', 'Audio-led route', 'voicing', 'place', 'manner',
                       'height', 'backness', 'rounding', '[i̥]', '[n̩]', '[t͡ʃ]', '[ɾ]', 'unresolved'):
            self.assertIn(phrase, s)
        self.assertIn('not the consonant chart', s)
        self.assertIn('not itself', self.docs['word'].body)

    def test_composition_is_one_way(self):
        word, phone = self.docs['word'], self.docs['phone']
        self.assertEqual(word.meta['composes'], [phone.meta['id']])
        self.assertNotIn(word.meta['id'], phone.meta.get('composes', []))
        self.assertNotIn(word.meta['id'], phone.meta.get('uses_practices', []))

    def test_reuses_existing_methods_and_models(self):
        for doc in self.docs.values():
            self.assertIn('english:method:analyze-sound-realization', doc.meta['uses_methods'])
            self.assertIn('english:model:phonological-word-model', doc.meta['uses_models'])
            self.assertIn('../PRONUNCIATION.md', doc.links)

    def test_rights_privacy_and_discomfort_fallback(self):
        for doc in self.docs.values():
            text = doc.body.lower()
            self.assertIn('outside the public repository', text)
            self.assertIn('discomfort', text)
            self.assertIn('no', kps.section(doc, 'Evidence status').lower())
            self.assertFalse(any(link.endswith(('.mp3', '.wav', '.mp4')) for link in doc.links))

    def test_added_sources_state_actual_access_and_nonclaims(self):
        for file in ('merriam-webster-undated-pin-entry.md',
                     'international-phonetic-association-undated-diacritics-and-other-symbols.md'):
            doc = kps.parse(ROOT / 'references' / file)
            self.assertTrue(doc.meta['access_extent'])
            self.assertIsNone(doc.meta['reviewed'])
            self.assertTrue(kps.section(doc, 'Nonclaims').strip())

if __name__ == '__main__':
    unittest.main()
