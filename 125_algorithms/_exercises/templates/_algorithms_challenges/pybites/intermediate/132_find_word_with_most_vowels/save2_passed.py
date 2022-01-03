VOWELS = l..('aeiou')

___ get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    text = text.l...s..
    d.. = {word: s..(letter __ VOWELS ___ letter __ word) ___ word __ text}
    r.. max(d...i.., key=l.... x: x[1])