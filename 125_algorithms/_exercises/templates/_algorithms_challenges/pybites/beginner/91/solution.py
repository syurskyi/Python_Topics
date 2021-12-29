_______ re

VOWELS = 'aeiou'
PYTHON = 'python'


___ contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    r.. a..(c __ VOWELS ___ c __ input_str.lower())


___ contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    # return any(c in PYTHON for c in input_str.lower())
    r.. re.search(rf'[{PYTHON}]', input_str.lower())


___ contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    r.. re.search(r'\d+', input_str)