______ string


class PigLatinTranslator:

    alpha = set(string.ascii_lowercase)
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = alpha - vowels

    @classmethod
    ___ translate_phrase(cls, phrase
        r_ ' '.join([cls.translate(word) for word in phrase.split()])

    @classmethod
    ___ translate(cls, word
        __ (word[0] in cls.vowels or
            word.startswith('yt') or
                word.startswith('xr')):
            r_ word + 'ay'
        ____ (word.startswith('squ') or
                word.startswith('sch') or
                word.startswith('thr')):
            r_ word[3:] + word[0:3] + 'ay'
        ____ ((word[0] in cls.consonants and
                word[1] in cls.consonants) or
                word.startswith('qu')):
            r_ word[2:] + word[0:2] + 'ay'
        ____ (word[0] in cls.consonants
            r_ word[1:] + word[0] + 'ay'


___ translate(phrase
    print((PigLatinTranslator.alpha))
    print((PigLatinTranslator.vowels))
    print((PigLatinTranslator.consonants))
    r_ PigLatinTranslator.translate_phrase(phrase)
