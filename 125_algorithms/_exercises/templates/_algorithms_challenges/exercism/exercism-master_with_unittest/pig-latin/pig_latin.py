_______ string


class PigLatinTranslator:

    alpha = set(string.ascii_lowercase)
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = alpha - vowels

    @classmethod
    ___ translate_phrase(cls, phrase):
        r.. ' '.join([cls.translate(word) ___ word __ phrase.s.. ])

    @classmethod
    ___ translate(cls, word):
        __ (word[0] __ cls.vowels o.
            word.startswith('yt') o.
                word.startswith('xr')):
            r.. word + 'ay'
        ____ (word.startswith('squ') o.
                word.startswith('sch') o.
                word.startswith('thr')):
            r.. word[3:] + word[0:3] + 'ay'
        ____ ((word[0] __ cls.consonants and
                word[1] __ cls.consonants) o.
                word.startswith('qu')):
            r.. word[2:] + word[0:2] + 'ay'
        ____ (word[0] __ cls.consonants):
            r.. word[1:] + word[0] + 'ay'


___ translate(phrase):
    print((PigLatinTranslator.alpha))
    print((PigLatinTranslator.vowels))
    print((PigLatinTranslator.consonants))
    r.. PigLatinTranslator.translate_phrase(phrase)
