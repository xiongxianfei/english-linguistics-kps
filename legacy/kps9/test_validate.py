#!/usr/bin/env python3
"""Regression tests for publication checks, not scientific/domain validity.
Run: python test_validate.py
Each test mutates a temporary copy, never the published knowledge.
"""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('publication_validator',HERE/'validate.py')
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)

class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/'package'
        shutil.copytree(HERE,self.root,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    def tearDown(self):self.temp.cleanup()
    def find(self,typ):
        return next(p for p in sorted(self.root.rglob('*.md')) if v.parse(p).meta.get('type')==typ)
    def meta(self,p,key,value):
        m,b=v.split_frontmatter(p.read_text());m[key]=value
        p.write_text('---\n'+'\n'.join(k+': '+json.dumps(x,ensure_ascii=False) for k,x in m.items())+'\n---\n\n'+b)
    def expect(self,code,manifest=False):
        r=v.validate(self.root,manifest=manifest)
        self.assertFalse(r['ok']); self.assertIn(code,[x['code'] for x in r['errors']],r['errors'])
    def add(self,p,text):p.write_text(p.read_text()+'\n'+text+'\n')
    def make_manifest(self):
        paths=v.manifest_payload_files(self.root)
        (self.root/'MANIFEST.sha256').write_text(''.join(v.sha(p)+'  '+p.relative_to(self.root).as_posix()+'\n' for p in paths))

    def test_01_clean_package(self):
        r=v.validate(self.root);self.assertTrue(r['ok'],r['errors'])
    def test_02_missing_summary(self):
        p=self.find('concept');p.write_text(p.read_text().replace('## Summary','## Overview',1));self.expect('local-summary')
    def test_03_empty_summary(self):
        p=self.find('concept');p.write_text(re.sub(r'(## Summary\n).*?(?=\n## )',r'\1\n',p.read_text(),count=1,flags=re.S));self.expect('local-summary')
    def test_04_imperative_principle(self):
        p=self.find('principle');p.write_text(re.sub(r'^# .+$','# Always obey this design',p.read_text(),count=1,flags=re.M));self.expect('imperative-principle')
    def test_05_missing_method_rationale(self):
        ps=[p for p in sorted(self.root.rglob('*.md')) if v.parse(p).meta.get('type')=='method' and '\n## Rationale\n' in p.read_text()]
        p=ps[0];p.write_text(p.read_text().replace('## Rationale','## Explanation',1));self.expect('method-rationale')
    def test_06_link_only_stage_action(self):
        p=self.find('practice');p.write_text(re.sub(r'(\*\*What to do:\*\*)[^\n]*',r'\1 [Read more](../README.md)',p.read_text(),count=1));self.expect('stage-local-card')
    def test_07_nonconsecutive_stage(self):
        p=self.find('practice');p.write_text(p.read_text().replace('## Stage2 ','## Stage99 ',1));self.expect('stage-order')
    def test_08_invented_ti_fragment(self):
        p=self.find('practice');self.add(p,'[Build the model](#ti-03)');self.expect('missing-fragment')
    def test_09_duplicate_heading(self):
        p=self.find('concept');self.add(p,'## Summary\nAnother summary.');self.expect('duplicate-heading')
    def test_10_missing_target(self):
        p=self.root/'README.md';self.add(p,'[Absent](missing-file.md)');self.expect('missing-target')
    def test_11_target_outside_package(self):
        p=self.root/'README.md';self.add(p,'[Sibling](../other-package/README.md)');self.expect('local-link')
    def test_12_duplicate_identity(self):
        a=self.find('concept');b=self.find('model');self.meta(b,'id',v.parse(a).meta['id']);self.expect('duplicate-id')
    def test_13_wrong_relationship_role(self):
        a=self.find('concept');b=self.find('method');self.meta(b,'uses_methods',[v.parse(a).meta['id']]);self.expect('relationship-type')
    def test_14_unknown_identity(self):
        p=self.find('method');self.meta(p,'uses_models',['missing:model']);self.expect('unresolved-id')
    def test_15_wrong_folder_role(self):
        p=self.find('principle');self.meta(p,'type','model');self.expect('type-folder')
    def test_16_recursive_composition_cycle(self):
        p=self.find('practice');self.meta(p,'composes',[v.parse(p).meta['id']]);self.expect('composition-cycle')
    def test_17_metadata_id_is_not_an_anchor(self):
        p=self.find('method');self.add(p,'[Object identity](#'+v.parse(p).meta['id']+')');self.expect('missing-fragment')
    def test_18_changed_dependency_needs_review(self):
        s=json.loads((self.root/'summary-dependencies.json').read_text())
        target=next(iter(next(iter(s['entries'].values())).keys()))
        self.add(self.root/target,'A changed source condition needs a deliberate review.');self.expect('stale-summary')
    def test_19_exact_version_not_major_line(self):
        p=self.root/'publication.json';d=json.loads(p.read_text());d['kps_language']='9.0.0';p.write_text(json.dumps(d));self.expect('compatibility')
    def test_20_wrong_language_in_file(self):
        self.meta(self.find('concept'),'language','KPS 8.x');self.expect('language')
    def test_21_custom_html_anchor(self):
        self.add(self.find('concept'),'<a id="hidden"></a>');self.expect('html-anchor')
    def test_22_application_wikilink(self):
        self.add(self.find('concept'),'[[A particular application link]]');self.expect('wikilink')
    def test_23_missing_reference_access_extent(self):
        self.meta(self.find('reference'),'access_extent','');self.expect('reference-access')
    def test_24_manifest_detects_tamper(self):
        self.make_manifest();self.add(self.root/'README.md','Changed after packaging.');self.expect('manifest-hash',True)
    def test_25_manifest_detects_unlisted_payload(self):
        self.make_manifest();(self.root/'unexpected.txt').write_text('unlisted');self.expect('manifest-coverage',True)
    def test_26_fenced_demonstration_is_not_live(self):
        self.add(self.root/'README.md','```markdown\n## TI-03\n[Not live](#missing)\n```')
        r=v.validate(self.root);self.assertTrue(r['ok'],r['errors'])
    def test_27_fresh_manifest_verifies(self):
        self.make_manifest();r=v.validate(self.root,manifest=True);self.assertTrue(r['ok'],r['errors'])
    def test_28_duplicate_metadata_key(self):
        p=self.find('concept');p.write_text(p.read_text().replace('---\n','---\ntype: "concept"\n',1));self.expect('parse')
    def test_29_missing_stage_map(self):
        p=self.find('practice');doc=v.parse(p);h=doc.meta['stage_titles'][0]
        p.write_text(p.read_text().replace('](#'+v.slug(h)+')','](../README.md)'));self.expect('stage-navigation')
    def test_30_review_refresh_does_not_hide_broken_links(self):
        self.add(self.root/'README.md','[Missing](does-not-exist.md)')
        old=(self.root/'summary-dependencies.json').read_bytes();r=v.validate(self.root,refresh=True)
        self.assertFalse(r['ok']);self.assertEqual(old,(self.root/'summary-dependencies.json').read_bytes())

    def test_31_manifest_ignores_checkout_and_caches(self):
        self.make_manifest()
        for name in ('.git/objects/fixture', '.pytest_cache/fixture', '__pycache__/fixture.pyc'):
            path=self.root/name
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(b'build tooling, not publication payload')
        result=v.validate(self.root,manifest=True)
        self.assertTrue(result['ok'],result['errors'])

if __name__=='__main__':unittest.main(verbosity=2)
