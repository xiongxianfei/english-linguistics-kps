from __future__ import annotations
import pathlib,re,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from kpslib import build_state

class PracticePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.state=build_state(ROOT)

    def test_general_american_policy_preserved(self):
        text=(ROOT/'PRONUNCIATION.md').read_text()
        self.assertIn('General American',text)
        self.assertIn('/si/',text)
        self.assertIn('/kɑr/',text)
        self.assertIn('sources/',text)

    def test_practice_stages_and_labels(self):
        labels=['Goal','Why','What to do','What to observe','Success signal','Next']
        for doc in [d for d in self.state['knowledge'] if d.role=='practice']:
            stages=re.findall(r'^## Stage(\d+) (.+)$',doc.body,re.M)
            self.assertTrue(stages,doc.relpath)
            self.assertEqual([int(x[0]) for x in stages],list(range(1,len(stages)+1)))
            for label in labels:
                self.assertRegex(doc.body,rf'\*\*{re.escape(label)}(?::)?\*\*')

    def test_pronunciation_practices_stay_provisional(self):
        for ident in ['english:learn-word-pronunciation','english:classify-and-produce-phone']:
            doc=self.state['by_id'][ident]
            self.assertEqual(doc.meta['evidence_status'],'provisional')
            self.assertIn('learner',doc.body.lower())

if __name__=='__main__':unittest.main(verbosity=2)
