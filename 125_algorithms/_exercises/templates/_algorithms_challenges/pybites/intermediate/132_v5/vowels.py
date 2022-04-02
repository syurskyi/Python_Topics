VOWELS = l..('aeiou')


___ _count(w: s..
    r.. l..([l ___ l __ w __ l __ VOWELS])


___ get_word_max_vowels(text
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    words = [(w, _count(w)) ___ w __ text.s..(' ')]
    r.. s..(words, key=l.... x: -x[1])[0]
