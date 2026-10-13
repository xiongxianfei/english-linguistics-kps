"""Regression checks of declared conventions and constructed models, not empirical findings."""
import copy, importlib.util, json, pathlib, shutil, sys, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'tools'))
import validate as kps
import check_domain as domain
import linguistic_examples as examples
import build_navigation as navigation
class DomainTests(unittest.TestCase):
    def test_all_stages_and_provisional_metadata(self):
        errors,count=domain.inspect(ROOT);self.assertEqual(errors,[]);self.assertGreaterEqual(count,100)
    def test_navigation_fresh(self):
        for p,expected in navigation.generated().items():self.assertEqual((ROOT/p).read_text(encoding='utf-8'),expected)
    def test_plural_regular_patterns(self):
        for s,out in [('t','s'),('k','s'),('g','z'),('eɪ','z'),('f','s'),('tʃ','ɪz'),('s','ɪz'),('z','ɪz'),('ʃ','ɪz'),('dʒ','ɪz')]:
            with self.subTest(s=s):self.assertEqual(examples.plural_ending(s),out)
    def test_past_regular_patterns(self):
        for s,out in [('f','t'),('k','t'),('eɪ','d'),('l','d'),('t','ɪd'),('d','ɪd')]:
            with self.subTest(s=s):self.assertEqual(examples.past_ending(s),out)
    def test_unknown_spelling_is_not_a_sound(self):
        for s in ['gh','tch','h','',None]:
            with self.subTest(s=s),self.assertRaises(ValueError):examples.plural_ending(s)
    def test_distinct_books_need_not_be_shared(self):
        p=['a','b'];t=['x','y'];r={('a','x'),('b','y')}
        self.assertTrue(examples.every_some(p,t,r));self.assertFalse(examples.some_every(p,t,r))
    def test_shared_book_satisfies_both_readings(self):
        p=['a','b'];t=['x','y'];r={('a','x'),('b','x')}
        self.assertTrue(examples.every_some(p,t,r));self.assertTrue(examples.some_every(p,t,r))
    def test_empty_quantifier_domains(self):
        self.assertTrue(examples.every_some([],[],set()))
        self.assertFalse(examples.some_every([],[],set()))
        self.assertTrue(examples.some_every([],['x'],set()))
        self.assertFalse(examples.not_every([],lambda x:True))
        self.assertTrue(examples.no_member([],lambda x:True))
    def test_not_every_does_not_require_some_pass(self):
        self.assertTrue(examples.not_every(['a','b'],lambda x:False))
    def test_five_finite_clauses(self):
        d=json.loads((ROOT/'data/integrated-example.json').read_text());self.assertEqual(len(d['clauses']),5)
        self.assertEqual(sum(c['type']=='main' for c in d['clauses']),2)
        for c in d['clauses']:
            a,b=c['span'];self.assertIn(c['finite'],d['sentences'][c['sentence']][a:b])
    def test_relative_ends_before_recipient_pp(self):
        d=json.loads((ROOT/'data/integrated-example.json').read_text());r=next(c for c in d['clauses'] if c['type']=='relative')
        a,b=r['span'];self.assertEqual(d['sentences'][0][a:b],['that','Maya','had','prepared'])
        self.assertEqual(b,d['recipient_pp']['span'][0]);self.assertTrue(r['object_gap'])
    def test_spans_are_nested_or_disjoint(self):
        d=json.loads((ROOT/'data/integrated-example.json').read_text())
        for x in d['clauses']:
            for y in d['clauses']:
                if x['sentence']!=y['sentence']:continue
                a,b=x['span'];c,e=y['span'];self.assertFalse(a<c<b<e)
    def test_recipient_is_not_patient(self):
        d=json.loads((ROOT/'data/integrated-example.json').read_text());self.assertEqual(d['roles']['Leo'],'Recipient')
        self.assertEqual(d['recipient_pp']['head'],'to')
    def test_focus_is_answer_not_wh_word(self):
        d=json.loads((ROOT/'data/integrated-example.json').read_text());self.assertEqual(d['focus']['domain'],'Anna')
        self.assertFalse(d['observed_audio'])
    def test_provisional_label_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__','.bootstrap'))
            p=root/'concepts/morpheme.md';p.write_text(p.read_text().replace('## Evidence status','## Evidence note'))
            errors,_=domain.inspect(root);self.assertTrue(any('not visible' in x for x in errors))
    def test_no_reviewed_status_without_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__','.bootstrap'))
            p=root/'concepts/morpheme.md';p.write_text(p.read_text().replace('evidence_status: "provisional"','evidence_status: "reviewed"'))
            errors,_=domain.inspect(root);self.assertTrue(any('without review record' in x for x in errors))
if __name__=='__main__':unittest.main(verbosity=2)
