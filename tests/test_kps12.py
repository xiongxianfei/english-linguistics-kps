"""Structural and adversarial regressions for the actual KPS 12 package."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'tools'))
from tools import kps12 as k
from tools.check_preservation import check as preservation
from tools.accept_dependency_review import accept

class KPS12Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records,cls.paths=k.load(ROOT)

    def copy_package(self):
        tmp=tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        dest=Path(tmp.name)/'package'
        # Copy the legacy files as well because active documentation links to them.
        shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
        return dest

    def write(self,root,ident,record):
        (root/self.paths[ident]).write_text(k.dump(record),encoding='utf-8')

    def check_mutation(self,ident,mutate,code):
        root=self.copy_package();r=copy.deepcopy(self.records[ident]);mutate(r);self.write(root,ident,r)
        result=k.validate(root,check_views=False,check_dependencies=False)
        self.assertFalse(result['ok'],result)
        self.assertIn(code,{e['code'] for e in result['errors']},result['errors'])

    def test_01_complete_package_validates(self):
        result=k.validate(ROOT);self.assertTrue(result['ok'],result['errors'])
        self.assertEqual(result['stats']['knowledge_entities'],115)
        self.assertEqual(result['stats']['sources'],10)
        self.assertEqual(result['stats']['interfaces'],10)
        self.assertEqual(result['stats']['claims'],115)
        self.assertEqual(result['stats']['top_level_linguistic_domains'],10)

    def test_02_all_legacy_records_have_aliases(self):
        m=k.read_json(ROOT/'migration/manifest.json')
        self.assertEqual(len(m['identity_map']),120)
        for old,new in m['identity_map'].items():
            self.assertIn(old,self.records[new]['aliases'])

    def test_03_roles_are_not_structural_kinds(self):
        r=self.records['english:prosody'];self.assertEqual(r['kind'],'knowledge')
        self.assertEqual(r['roles'],['kps:role:concept'])
        self.assertTrue(r['content'].startswith('knowledge/'))
        self.assertNotIn('type',r)
        self.assertNotIn('stages',r)

    def test_04_domain_overlap_is_explicit(self):
        domains=self.records['english:prosody']['domains']
        for d in ['linguistics:prosody','linguistics:phonology','linguistics:phonetics','linguistics:information-structure']:
            self.assertIn(d,domains)

    def test_05_hierarchy_is_acyclic(self):
        adjacency={i:r['parents'] for i,r in self.records.items() if r['kind']=='domain'}
        self.assertEqual(k.cycle_nodes(adjacency),[])

    def test_06_unknown_domain_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['domains'].append('missing:domain'),'unresolved')

    def test_07_role_as_domain_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['domains'].append('kps:role:model'),'endpoint-kind')

    def test_08_domain_cycle_rejected(self):
        self.check_mutation('linguistics:language',lambda r:r['parents'].append('linguistics:prosody'),'domain-cycle')

    def test_09_alias_collision_rejected(self):
        self.check_mutation('english:stress',lambda r:r['aliases'].append('english:concept:prosody'),'alias')

    def test_10_alias_shadowing_rejected(self):
        self.check_mutation('english:stress',lambda r:r['aliases'].append('english:prosody'),'alias')

    def test_11_missing_target_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['relations'].append({'predicate':'kps:uses','target':'missing:thing'}),'unresolved')

    def test_12_unknown_predicate_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['relations'].append({'predicate':'unknown:predicate','target':'english:stress'}),'unresolved')

    def test_13_bad_predicate_endpoints_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['relations'].append({'predicate':'kps:cites','target':'english:stress'}),'relation-endpoint')

    def test_14_old_target_role_constraint_preserved(self):
        self.check_mutation('english:prosody',lambda r:r['relations'][0].update(expected_target_role='kps:role:method'),'target-role')

    def test_15_composition_cycle_rejected(self):
        self.check_mutation('english:classify-and-produce-phone',lambda r:r['relations'].append({'predicate':'kps:composes','target':'english:learn-word-pronunciation'}),'relation-cycle')

    def test_16_composition_needs_practice_roles(self):
        self.check_mutation('english:prosody',lambda r:r['relations'].append({'predicate':'kps:composes','target':'english:stress'}),'composition')

    def test_17_claim_version_mismatch_rejected(self):
        self.check_mutation('english:prosody:claim:key-takeaway',lambda r:r.update(owner_version='99.0.0'),'claim-version')

    def test_18_claim_owner_mismatch_rejected(self):
        self.check_mutation('english:prosody:claim:key-takeaway',lambda r:r.update(owner='english:stress'),'claim-owner')

    def test_19_claim_statement_drift_rejected(self):
        self.check_mutation('english:prosody:claim:key-takeaway',lambda r:r.update(statement='Changed without editing the source'),'claim-drift')

    def test_20_no_review_promotion(self):
        self.check_mutation('english:prosody',lambda r:r.update(evidence_status='reviewed'),'review')

    def test_21_no_reviewed_date_on_provisional_item(self):
        self.check_mutation('english:prosody',lambda r:r.update(reviewed='2026-10-13'),'review')

    def test_22_evidence_is_context_only_after_migration(self):
        evidence=[r for r in self.records.values() if r['kind']=='evidence']
        self.assertGreater(len(evidence),0)
        self.assertTrue(all(r['assessment_relation']=='context-only' for r in evidence))
        self.assertTrue(all(self.records[r['about']]['kind'] in k.KNOWLEDGE for r in evidence))

    def test_23_citation_cannot_be_auto_promoted(self):
        ident=next(i for i,r in self.records.items() if r['kind']=='evidence')
        self.check_mutation(ident,lambda r:r.update(assessment_relation='supports'),'evidence-promotion')

    def test_24_support_requires_a_claim_target(self):
        ident=next(i for i,r in self.records.items() if r['kind']=='evidence')
        self.check_mutation(ident,lambda r:r.update(assessment_relation='supports',record_origin='authored'),'evidence-target')

    def test_25_support_requires_a_located_passage(self):
        ident=next(i for i,r in self.records.items() if r['kind']=='evidence')
        self.check_mutation(ident,lambda r:r.update(about=r['about']+':claim:key-takeaway',assessment_relation='supports',record_origin='authored'),'evidence-locator')

    def test_26_interface_requires_representation_endpoints(self):
        self.check_mutation('english:focus-prosody-interface',lambda r:r['mapping'].update(source='linguistics:information-structure'),'endpoint-kind')

    def test_27_interface_requires_endpoint_domains(self):
        self.check_mutation('english:focus-prosody-interface',lambda r:r.update(domains=['linguistics:prosody']),'interface-domains')

    def test_28_interface_claim_must_be_owned(self):
        self.check_mutation('english:focus-prosody-interface',lambda r:r['mapping'].update(claim='english:stress:claim:key-takeaway'),'interface-claim')

    def test_29_interface_cannot_use_document_dependency_predicate(self):
        self.check_mutation('english:focus-prosody-interface',lambda r:r['mapping'].update(predicate='kps:uses'),'interface-predicate')

    def test_30_interface_requires_scope(self):
        self.check_mutation('english:focus-prosody-interface',lambda r:r['mapping'].update(scope=''),'serialization')

    def test_31_representation_requires_structure(self):
        self.check_mutation('english:representation:focus-domain',lambda r:r.update(structure={}),'serialization')

    def test_32_sequence_is_not_ontological_type(self):
        r=self.records['english:prosody'];self.assertEqual(r['sequences'][0]['scheme'],'english:legacy-route')
        self.assertEqual(r['sequences'][0]['positions'],[6])
        self.assertEqual(self.records['english:legacy-route']['kind'],'sequence')

    def test_33_unknown_sequence_position_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['sequences'][0].update(positions=[900]),'sequence')

    def test_34_boolean_is_not_sequence_integer(self):
        self.check_mutation('english:prosody',lambda r:r['sequences'][0].update(positions=[True]),'serialization')

    def test_35_stale_views_rejected(self):
        root=self.copy_package();(root/'DOMAINS.md').write_text('stale',encoding='utf-8')
        result=k.validate(root);self.assertIn('stale-view',{e['code'] for e in result['errors']})

    def test_36_body_change_requires_dependency_review(self):
        root=self.copy_package();p=root/'knowledge/prosody.md';p.write_text(p.read_text()+'\nChanged body.\n')
        result=k.validate(root,check_views=False);self.assertIn('dependency-review',{e['code'] for e in result['errors']})

    def test_37_build_never_accepts_changed_baseline(self):
        root=self.copy_package();before=(root/'summary-dependencies.json').read_bytes()
        p=root/'knowledge/prosody.md';p.write_text(p.read_text()+'\nChanged body.\n')
        with self.assertRaises(ValueError):k.build(root)
        self.assertEqual((root/'summary-dependencies.json').read_bytes(),before)

    def test_38_dependency_acceptance_requires_exact_review(self):
        root=self.copy_package();p=root/'knowledge/prosody.md';p.write_text(p.read_text()+'\nChanged body.\n')
        record=root/'review.json';record.write_text(k.dump({'reviewer':'test fixture','date':'2026-10-13','findings':'synthetic test only'}))
        with self.assertRaises(ValueError):accept(root,record)

    def test_39_views_are_reproducible(self):
        a=k.generated(ROOT);b=k.generated(ROOT);self.assertEqual(a,b)
        for path,text in a.items():self.assertEqual((ROOT/path).read_text(encoding='utf-8'),text)

    def test_40_graph_has_qualified_semantic_edges(self):
        g=k.graph(self.records,self.paths)
        self.assertEqual(g['format'],12)
        semantic=[e for e in g['edges'] if e['layer']=='semantic']
        self.assertEqual(len(semantic),10)
        self.assertTrue(all(e.get('claim') and e.get('scope') and e.get('owner') for e in semantic))
        self.assertEqual(len({e['id'] for e in g['edges']}),len(g['edges']))

    def test_41_alias_lookup_returns_canonical_entity(self):
        self.assertEqual(k.query(ROOT,ident='english:concept:prosody')[0]['id'],'english:prosody')

    def test_42_domain_and_role_query(self):
        found=k.query(ROOT,domain='linguistics:prosody',role='kps:role:model',interfaces=True)
        self.assertGreaterEqual(len(found),2)
        self.assertTrue(all(r['kind']=='interface' for r in found))

    def test_43_no_claim_support_inferred_from_citation(self):
        self.assertEqual(k.query(ROOT,claim='english:focus-prosody-interface:claim:key-takeaway'),[])
        self.assertGreater(len(k.targets(self.records['english:focus-prosody-interface'],'kps:cites')),0)

    def test_44_unknown_query_identity_errors(self):
        with self.assertRaises(ValueError):k.query(ROOT,ident='missing:entity')

    def test_45_schema_has_all_record_kinds(self):
        s=k.read_json(ROOT/'schema/entity.schema.json')
        self.assertEqual(set(s['properties']['kind']['enum']),k.KINDS)

    def test_46_baseline_and_transform_hashes_preserved(self):
        result=preservation(ROOT);self.assertTrue(result['ok'],result['errors'])
        self.assertEqual(result['baseline_files'],157);self.assertEqual(result['migrated_records'],120)

    def test_47_legacy_relation_count_preserved(self):
        original=k.read_json(ROOT/'legacy/kps9/knowledge-graph.json')
        migrated=sum('legacy_predicate' in rel for r in self.records.values() for rel in r.get('relations',[]))
        self.assertEqual(migrated,len(original['edges']))

    def test_48_historical_inspection_dates_unchanged(self):
        for r in self.records.values():
            if r['kind']=='source':
                old=r['migration']['legacy_metadata']
                for key in ['creator','publication','publication_date','date_basis','accessed','access_extent','reviewed']:
                    self.assertEqual(r[key],old[key])

    def test_49_new_bridges_remain_provisional(self):
        added=[r for r in self.records.values() if r['kind']=='interface' and not r.get('migration')]
        self.assertEqual(len(added),5)
        for r in added:
            self.assertEqual(r['evidence_status'],'provisional')
            self.assertEqual(k.targets(r,'kps:cites'),[])
            self.assertIn('No new external source inspection',(ROOT/r['content']).read_text())

    def test_50_canonical_content_is_role_neutral(self):
        for r in self.records.values():
            if r['kind'] in k.KNOWLEDGE:
                self.assertTrue(r['content'].startswith('knowledge/'))
                self.assertFalse((ROOT/r['content']).read_text().startswith('---'))

    def test_51_unknown_subdomain_does_not_silently_pass(self):
        self.check_mutation('english:prosody',lambda r:r['domains'].append('linguistics:prosody:unregistered'),'unresolved')

    def test_52_unrepresented_scopes_are_visible_gaps(self):
        text=(ROOT/'views/domains/phonology.md').read_text()
        self.assertIn('Unrepresented; content needed',text)
        self.assertIn('theory alternatives',text.lower())

    def test_53_claims_are_honestly_summary_only(self):
        for r in self.records.values():
            if r['kind'] in k.KNOWLEDGE:
                self.assertIn('other body assertions',r['claim_extraction'])
            if r['kind']=='claim':
                self.assertEqual(r['granularity'],'summary-not-assumed-atomic')

    def test_54_missing_content_rejected(self):
        self.check_mutation('english:prosody',lambda r:r.update(content='knowledge/missing.md'),'content')

    def test_55_path_escape_rejected(self):
        self.check_mutation('english:prosody',lambda r:r.update(content='../outside.md'),'content')

    def test_56_duplicate_json_keys_rejected(self):
        root=self.copy_package();p=root/self.paths['english:prosody'];p.write_text('{"id":"a:b","id":"a:c"}')
        self.assertFalse(k.validate(root)['ok'])

    def test_57_unique_content_ownership_enforced(self):
        self.check_mutation('english:stress',lambda r:r.update(content='knowledge/prosody.md'),'content-owner')

    def test_58_duplicate_relation_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['relations'].append(copy.deepcopy(r['relations'][0])),'serialization')

    def test_59_malformed_relation_rejected(self):
        self.check_mutation('english:prosody',lambda r:r['relations'].append({'target':False}),'serialization')

    def test_60_role_section_contract_is_active(self):
        self.check_mutation('english:prosody',lambda r:r['roles'].append('kps:role:method'),'role-contract')

    def test_61_package_does_not_claim_upstream_release(self):
        p=k.read_json(ROOT/'publication.json');self.assertEqual(p['kps_language'],'12.x')
        self.assertIn('local',p['profile_status'])
        self.assertFalse(k.read_json(ROOT/'upstream-lock.json')['upstream_kps12_release_claimed'])

    def test_62_semantic_claim_not_implied_by_uses(self):
        g=k.graph(self.records,self.paths)
        uses=[e for e in g['edges'] if e['predicate']=='kps:uses']
        self.assertTrue(uses);self.assertTrue(all(e['layer']=='document' for e in uses))


    def test_63_positive_claim_evidence_is_supported_by_schema(self):
        root=self.copy_package()
        ident=next(i for i,r in self.records.items() if r['kind']=='evidence')
        record=copy.deepcopy(self.records[ident])
        owner=self.records[record['about']]
        record.update(about=owner['claims'][0],assessment_relation='qualifies',record_origin='test-fixture',
                      locator='Constructed test passage, not a real source inspection',
                      inspection_extent='Synthetic schema fixture only',assessment='Tests allowed record structure, not empirical support')
        self.write(root,ident,record)
        result=k.validate(root,check_views=False,check_dependencies=False)
        self.assertTrue(result['ok'],result['errors'])

    def test_64_nonfinite_json_rejected(self):
        root=self.copy_package();p=root/'bad-json.json';p.write_text('{"x":NaN}')
        with self.assertRaises(ValueError):k.read_json(p)
        with self.assertRaises(ValueError):k.dump({'x':float('inf')})

    def test_65_permanent_ci_is_read_only(self):
        text=(ROOT/'.github/workflows/checks.yml').read_text()
        self.assertIn('contents: read',text)
        self.assertIn('persist-credentials: false',text)
        self.assertNotIn('contents: write',text)
        self.assertNotIn('git push',text)
        self.assertNotIn('accept_dependency_review',text)

    def test_66_interface_checks_predicate_signature(self):
        self.check_mutation('kps:maps-to',lambda r:r.update(source_kinds=['knowledge']),'interface-predicate')

if __name__=='__main__':unittest.main(verbosity=2)
