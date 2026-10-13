from __future__ import annotations
import json, pathlib, sys, tempfile, shutil, unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from kpslib import build_state, check_generated, parse_document, validate, ROLE_FOLDERS

class StructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=validate(ROOT)
        cls.state=build_state(ROOT)

    def test_repository_validates(self):
        self.assertTrue(self.result['ok'], self.result['errors'])
        self.assertEqual(self.result['errors'], [])

    def test_foundation_counts(self):
        self.assertEqual(self.result['stats']['knowledge_items'],127)
        self.assertEqual(self.result['stats']['interfaces'],13)
        self.assertEqual(self.result['stats']['sources'],10)
        self.assertEqual(self.result['stats']['sequences'],1)

    def test_exactly_one_role_from_folder(self):
        for doc in self.state['knowledge']:
            self.assertIn(doc.role, ROLE_FOLDERS)
            self.assertNotIn('role',doc.meta)
            self.assertNotIn('roles',doc.meta)
            self.assertNotIn('type',doc.meta)

    def test_forbidden_stores_absent(self):
        for name in ['entities','ontology','knowledge','references']:
            self.assertFalse((ROOT/name).exists(),name)

    def test_source_not_reference_folder(self):
        self.assertTrue((ROOT/'sources').is_dir())
        for doc in self.state['sources']:
            self.assertTrue(doc.meta['id'].startswith('source:'))

    def test_required_domains(self):
        pub=json.loads((ROOT/'publication.json').read_text())
        top={d.split(':',1)[0] for d in self.state['all_domains']}
        self.assertTrue(set(pub['foundation_domains']) <= top)
        for domain in pub['foundation_domains']:
            self.assertTrue((ROOT/'views/domains'/f'{domain}.md').is_file())

    def test_open_vocabulary_is_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=pathlib.Path(tmp)/'repo'
            shutil.copytree(ROOT,target)
            p=target/'concepts'/'temporary-open-vocabulary-test.md'
            p.write_text('''---\nid: "english:temporary-open-vocabulary-test"\naliases: []\nversion: "1.0.0-draft.1"\nlanguage: "KPS 12.x"\nstatus: "draft"\ndomains: ["experimental-domain"]\nevidence_status: "provisional"\nsource_status: "external-support-pending"\nbasis_kind: "Constructed test"\nreviewed: null\nclaims: [{"id":"key-takeaway","statement":"A temporary object tests open vocabulary.","scope":"Test only.","evidence_status":"provisional"}]\nrelations: [{"predicate":"newly-relates-to","target":"english:morpheme","layer":"semantic","claim":"key-takeaway"}]\nsources: []\n---\n\n# Temporary open vocabulary test\n\n## Key takeaway\nA temporary object tests open vocabulary.\n\n## Summary\nTest only.\n\n## Definition\nTest.\n\n## Distinctions\nTest.\n\n## Scope and limits\nTest.\n\n## Evidence status\nProvisional.\n''')
            # Generated views are intentionally stale, so exclude that check.
            r=validate(target,check_views=False)
            self.assertTrue(r['ok'],r['errors'])

    def test_generated_views_are_fresh(self):
        self.assertEqual(check_generated(ROOT),[])

if __name__=='__main__':unittest.main(verbosity=2)
