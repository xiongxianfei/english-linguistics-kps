"""Toy implementations of declared examples, not a complete grammar or pronunciation engine."""
SIBILANTS = frozenset({'s', 'z', 'ʃ', 'ʒ', 'tʃ', 'dʒ'})
VOICELESS = frozenset({'p', 't', 'k', 'f', 'θ', 's', 'ʃ', 'tʃ'})
VOICED = frozenset({'b', 'd', 'g', 'v', 'ð', 'z', 'ʒ', 'dʒ', 'm', 'n', 'ŋ', 'l', 'r', 'ɹ', 'j', 'w', 'i', 'iː', 'ɪ', 'e', 'eɪ', 'æ', 'ɑ', 'ɑː', 'ɒ', 'ɔ', 'ɔː', 'ʊ', 'u', 'uː', 'ə', 'ɜː', 'ʌ', 'aʊ', 'aɪ', 'ɔɪ', 'oʊ', 'əʊ', 'ɚ'})

def _check(sound):
    if not isinstance(sound, str) or sound not in (VOICELESS | VOICED):
        raise ValueError('Supply a supported final phonological sound, not a spelling.')

def plural_ending(final_sound):
    _check(final_sound)
    if final_sound in SIBILANTS: return 'ɪz'
    return 's' if final_sound in VOICELESS else 'z'

def past_ending(final_sound):
    _check(final_sound)
    if final_sound in {'t', 'd'}: return 'ɪd'
    return 't' if final_sound in VOICELESS else 'd'

def every_some(people, things, relation):
    return all(any((p, t) in relation for t in things) for p in people)

def some_every(people, things, relation):
    return any(all((p, t) in relation for p in people) for t in things)

def not_every(people, predicate):
    return not all(predicate(p) for p in people)

def no_member(people, predicate):
    return not any(predicate(p) for p in people)
