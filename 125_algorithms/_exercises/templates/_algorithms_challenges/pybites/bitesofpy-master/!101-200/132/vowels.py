VOWELS = list('aeiou')


___ _count(w: str
    r_ le.([l for l in w __ l in VOWELS])


___ get_word_max_vowels(text
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    words = [(w, _count(w)) for w in text.split(' ')]
    r_ sorted(words, key=lambda x: -x[1])[0]
