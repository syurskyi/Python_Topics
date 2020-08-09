from string ______ ascii_lowercase as alphabet

___ is_pangram(phrase
    """is_pangram determines if every letter of the alphabet are in a phrase"""
    r_ all(letter in phrase or letter.upper() in phrase
               for letter in alphabet)
