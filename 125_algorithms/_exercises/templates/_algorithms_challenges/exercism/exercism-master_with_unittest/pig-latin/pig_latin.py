_______ s__


c_ PigLatinTranslator:

    alpha s..(s__.a..)
    vowels s..( 'a', 'e', 'i', 'o', 'u' )
    consonants alpha - vowels

    ??
    ___ translate_phrase(cls, phrase
        r.. ' '.j..([ ?.translate(word) ___ word __ phrase.s.. ])

    ??
    ___ translate(cls, word
        __ (word[0] __  ?.vowels o.
            word.s.. 'yt') o.
                word.s.. 'xr':
            r.. word + 'ay'
        ____ (word.s.. 'squ') o.
                word.s.. 'sch') o.
                word.s.. 'thr':
            r.. word[3:] + word[0:3] + 'ay'
        ____ ((word[0] __  ?.consonants a..
                ? 1 __  ?.consonants) o.
                word.s.. 'qu':
            r.. word[2:] + word[0:2] + 'ay'
        ____ (word[0] __  ?.consonants
            r.. word[1:] + word[0] + 'ay'


___ translate(phrase
    print((PigLatinTranslator.alpha
    print((PigLatinTranslator.vowels
    print((PigLatinTranslator.consonants
    r.. PigLatinTranslator.translate_phrase(phrase)
