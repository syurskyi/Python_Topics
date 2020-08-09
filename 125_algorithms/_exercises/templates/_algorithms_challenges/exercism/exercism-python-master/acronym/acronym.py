from re ______ split

___ abbreviate(phrase
    """abbreviate creates an acronym for a phrase"""
    r_ ''.join(abbreviate_word(word) for word in split('\W+', phrase))

___ abbreviate_word(word
    """abbreviate_word selects the letters in a word to use for abbriviation"""
    __ all(letter.isupper() for letter in word
        r_ word[0]
    r_ word[0].upper() + ''.join(letter for letter in word[1:] __ letter.isupper())
