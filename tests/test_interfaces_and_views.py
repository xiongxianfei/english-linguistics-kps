from __future__ import annotations
import json,pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from kpslib import build_state

class InterfaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.state=build_state(ROOT)

    def test_required_interface_pairs(self):
        required={tuple(x) for x in json.loads((ROOT/'publication.json').read_text())['required_interfaces']}
        actual={(x['source_domain'],x['target_domain']) for x in self.state['interfaces']}
        self.assertEqual(required,actual)

    def test_interface_claims_exist(self):
        for item in self.state['interfaces']:
            doc=self.state['by_id'][item['id']]
            self.assertIn(item['claim'],{c['id'] for c in doc.meta['claims']})
            self.assertIn(item['source_domain'],doc.meta['domains'])
            self.assertIn(item['target_domain'],doc.meta['domains'])

    def test_gap_filling_items_exist(self):
        expected={
            'english:dialogue-and-turn-taking','english:information-packaging-constructions',
            'english:lexical-relations','english:lexical-variation-and-register',
            'english:phonological-analysis-frameworks','english:politeness-and-social-meaning',
            'english:plural-and-collective-interpretation','english:ellipsis-and-discontinuity',
            'english:annotate-and-measure-prosody',
        }
        self.assertTrue(expected <= set(self.state['by_id']))

    def test_claims_are_embedded_not_files(self):
        self.assertFalse((ROOT/'claims').exists())
        for doc in self.state['knowledge']:
            self.assertTrue(doc.meta['claims'])

    def test_machine_graph_matches_state(self):
        graph=json.loads((ROOT/'generated/knowledge-graph.json').read_text())
        knowledge_nodes=[n for n in graph['nodes'] if n['kind']=='knowledge']
        interface_nodes={i['id'] for i in self.state['interfaces']}
        self.assertEqual(len(knowledge_nodes),len(self.state['knowledge']))
        self.assertEqual(len(interface_nodes),13)

if __name__=='__main__':unittest.main(verbosity=2)
