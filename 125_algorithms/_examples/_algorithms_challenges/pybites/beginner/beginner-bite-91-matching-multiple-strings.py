'''
Catching up after #PyCon2018 ... in this Bite you do multiple string matching. Complete contains_only_vowels,
contains_any_py_chars, and contains_digits below. See more info in the docstrings and the tests. Have fun!

'''


VOWELS = 'aeiou'
PYTHON = 'python'
import string

def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    lower = input_str.lower()
    vowels = "aeoiu"
    for c in lower:
        if c not in vowels:
            return False
    return True

def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    chars = "PYTHON".lower()
    lower = input_str.lower()
    for c in lower:
        if c in chars:
            return True
    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for c in input_str:
        if c in string.digits:
            return True
    return False


