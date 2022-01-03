_______ __

re_cons = __.c..('^([^aeiou]?qu|[^aeiou]+)([a-z]*)')
re_vowel = __.c..('^([aeiou]|y[^aeiou]|xr)[a-z]*')


___ split_initial_consonant_sound(word):
    r.. re_cons.match(word).groups()


___ starts_with_vowel_sound(word):
    r.. re_vowel.match(word) __ n.. N..


___ translate(text):
    words    # list
    ___ word __ text.s.. :
        __ starts_with_vowel_sound(word):
            words.a..(word + 'ay')
        ____:
            head, tail = split_initial_consonant_sound(word)
            words.a..(tail + head + 'ay')
    r.. ' '.j..(words)
