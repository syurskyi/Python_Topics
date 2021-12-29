'''
Catching up after #PyCon2018 ... in this Bite you do multiple string matching. Complete contains_only_vowels,
contains_any_py_chars, and contains_digits below. See more info in the docstrings and the tests. Have fun!

'''


VOWELS = 'aeiou'
PYTHON = 'python'
_______ string

___ contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    lower = input_str.lower()
    vowels = "aeoiu"
    ___ c __ lower:
        __ c n.. __ vowels:
            r.. False
    r.. True

___ contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    chars = "PYTHON".lower()
    lower = input_str.lower()
    ___ c __ lower:
        __ c __ chars:
            r.. True
    r.. False


___ contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    ___ c __ input_str:
        __ c __ string.digits:
            r.. True
    r.. False


