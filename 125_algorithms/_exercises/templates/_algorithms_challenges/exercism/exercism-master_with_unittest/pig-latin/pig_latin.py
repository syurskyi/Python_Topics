_______ s__


c_ PigLatinTranslator:

    alpha s..(s__.a..)
    vowels s..( 'a', 'e', 'i', 'o', 'u' )
    consonants alpha - vowels

    @classmethod
    ___ translate_phrase(cls, phrase
        r.. ' '.j..([cls.translate(word) ___ word __ phrase.s.. ])

    @classmethod
    ___ translate(cls, word
        __ (word[0] __ cls.vowels o.
            word.s.. 'yt') o.
                word.s.. 'xr':
            r.. word + 'ay'
        ____ (word.s.. 'squ') o.
                word.s.. 'sch') o.
                word.s.. 'thr':
            r.. word[3:] + word[0:3] + 'ay'
        ____ ((word[0] __ cls.consonants a..
                word[1] __ cls.consonants) o.
                word.s.. 'qu':
            r.. word[2:] + word[0:2] + 'ay'
        ____ (word[0] __ cls.consonants
            r.. word[1:] + word[0] + 'ay'


___ translate(phrase
    print((PigLatinTranslator.alpha
    print((PigLatinTranslator.vowels
    print((PigLatinTranslator.consonants
    r.. PigLatinTranslator.translate_phrase(phrase)
