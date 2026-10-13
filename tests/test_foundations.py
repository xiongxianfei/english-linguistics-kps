"""Bounded structure/fixture checks, not proof of self-containedness or scientific truth."""
import hashlib
import json
import pathlib
import re
import shutil
import sys
import tempfile
import unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'tools'))
import validate as kps
import check_domain
import build_navigation

DOMAINS = {'phonetics', 'phonology', 'morphology', 'lexicon', 'syntax', 'semantics', 'pragmatics', 'discourse', 'information-structure', 'prosody'}

class FoundationTests(unittest.TestCase):
    def test_ten_subsystem_models(self):
        files = list((ROOT/'models').glob('english-*-system.md'))
        self.assertEqual(len(files), 10)
        self.assertEqual({kps.parse(p).meta['system_domain'] for p in files}, DOMAINS)

    def test_subsystem_sections_contain_local_explanations(self):
        for path in (ROOT/'models').glob('english-*-system.md'):
            doc=kps.parse(path)
            for heading in ['Purpose','Representation','Essential distinctions','Interfaces','Evaluation and counterevidence','Assumptions and limits','Evidence status']:
                with self.subTest(file=path.name, heading=heading):
                    self.assertTrue(kps.meaningful(kps.section(doc,heading)))
            self.assertTrue(re.search(r'^## Worked (?:example|analysis|entry)$',doc.live,re.M))

    def test_fourteen_interfaces_are_models(self):
        paths=list((ROOT/'models').glob('*-interface.md'))
        self.assertEqual(len(paths),14)
        for path in paths:
            doc=kps.parse(path)
            self.assertEqual(doc.meta['type'],'model')
            for heading in ['Purpose','Representation','Assumptions and limits','Evaluation and counterevidence']:
                # Representations may be locally complete fenced text diagrams.
                section=re.search(r'^## '+re.escape(heading)+r'\s*\n(.*?)(?=^## |\Z)',doc.body,re.M|re.S)
                self.assertIsNotNone(section,(path,heading))
                self.assertTrue(kps.meaningful(section[1]),(path,heading))


    def test_language_and_versions_are_distinct(self):
        pub=json.loads((ROOT/'publication.json').read_text())
        self.assertEqual(pub['kps_language'],'9.x')
        self.assertEqual(pub['version'],'0.2.0')
        self.assertEqual(pub['validated_with'],'9.1.0')
        self.assertEqual(pub['upstream_core'],'11.0.0')
        for folder in ['concepts','principles','models','methods','practices','references']:
            for path in (ROOT/folder).glob('*.md'):
                self.assertEqual(kps.parse(path).meta['language'],'KPS 9.x')

    def test_upstream_checker_is_byte_identical(self):
        data=(ROOT/'validate.py').read_bytes()
        actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        self.assertEqual(actual,lock['copied_files']['validate.py'])
        self.assertEqual(actual,'36ee1e7d6f991819d6d35b3764f7e16f8fb3fbc8')


    def test_build_does_not_accept_dependencies(self):
        path=ROOT/'summary-dependencies.json'
        before=path.read_bytes()
        build_navigation.generated()
        self.assertEqual(before,path.read_bytes())

    def test_missing_model_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=pathlib.Path(tmp)/'repo'
            shutil.copytree(ROOT,target,ignore=shutil.ignore_patterns('.git','__pycache__'))
            (target/'models/english-syntax-system.md').unlink()
            errors,_=check_domain.inspect(target)
            self.assertTrue(any('Ten subsystem' in e for e in errors))

    def test_domain_names_are_not_a_global_registry(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=pathlib.Path(tmp)/'repo'
            shutil.copytree(ROOT,target,ignore=shutil.ignore_patterns('.git','__pycache__'))
            path=target/'concepts/morpheme.md'
            text=path.read_text().replace('---\n','---\ndomains: ["new-author-defined-domain"]\n',1)
            path.write_text(text)
            errors,_=check_domain.inspect(target)
            self.assertEqual(errors,[])

    def test_source_support_is_not_independent_review(self):
        for role in ['concept','principle','model','method','practice']:
            for path in (ROOT/(role+'s')).glob('*.md'):
                m=kps.parse(path).meta
                self.assertEqual(m['evidence_status'],'provisional')
                self.assertIsNone(m['reviewed'])


    def test_reference_records_state_inspection_limits(self):
        refs=[p for p in (ROOT/'references').glob('*.md') if kps.parse(p).meta.get('type')=='reference']
        self.assertTrue(refs, 'No Reference records available to inspect')
        for path in refs:
            doc=kps.parse(path)
            self.assertTrue(doc.meta.get('access_extent'))
            self.assertTrue(kps.section(doc,'Nonclaims'))

    def test_steps_first_does_not_require_repeated_labels(self):
        self.assertTrue(kps.has_local_actions('1. Preserve the expression and context.\n2. Record the result.'))
        self.assertFalse(kps.has_local_actions('1. [Go elsewhere](../README.md)'))
        self.assertFalse(kps.has_local_actions('[Read more](../README.md)'))

    def test_read_only_hosting_workflow(self):
        text=(ROOT/'.github/workflows/checks.yml').read_text()
        self.assertIn('contents: read',text)
        self.assertNotIn('contents: write',text)
        self.assertNotIn('git push',text)

if __name__=='__main__':
    unittest.main(verbosity=2)
