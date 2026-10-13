from __future__ import annotations
import json,pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import linguistic_examples as examples

class LinguisticFixtureTests(unittest.TestCase):
    def test_plural_regular_patterns(self):
        for sound,out in [('t','s'),('k','s'),('g','z'),('eɪ','z'),('f','s'),('tʃ','ɪz'),('s','ɪz'),('z','ɪz'),('ʃ','ɪz'),('dʒ','ɪz')]:
            with self.subTest(sound=sound):self.assertEqual(examples.plural_ending(sound),out)

    def test_past_regular_patterns(self):
        for sound,out in [('f','t'),('k','t'),('eɪ','d'),('l','d'),('t','ɪd'),('d','ɪd')]:
            with self.subTest(sound=sound):self.assertEqual(examples.past_ending(sound),out)

    def test_spelling_is_not_sound_input(self):
        for sound in ['gh','tch','h','',None]:
            with self.subTest(sound=sound),self.assertRaises(ValueError):examples.plural_ending(sound)

    def test_scope_readings(self):
        people=['a','b'];things=['x','y'];separate={('a','x'),('b','y')};shared={('a','x'),('b','x')}
        self.assertTrue(examples.every_some(people,things,separate))
        self.assertFalse(examples.some_every(people,things,separate))
        self.assertTrue(examples.some_every(people,things,shared))

    def test_integrated_fixture(self):
        d=json.loads((ROOT/'data/integrated-example.json').read_text())
        self.assertEqual(len(d['clauses']),5)
        self.assertEqual(d['roles']['Leo'],'Recipient')
        self.assertEqual(d['focus']['domain'],'Anna')
        self.assertFalse(d['observed_audio'])

if __name__=='__main__':unittest.main(verbosity=2)
