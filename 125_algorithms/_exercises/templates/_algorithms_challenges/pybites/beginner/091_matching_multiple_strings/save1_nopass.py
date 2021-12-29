VOWELS = 'aeiou'
PYTHON = 'python'


___ contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    ___ char __ input_str:
        __ char n.. __ VOWELS:
            r.. False
        ____:
            r.. True


___ contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    ___ char __ input_str.casefold():
        __ char __ PYTHON:
            r.. True
        ____ char __ N..
            r.. False
        ____:
            r.. False


___ contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    digits    # list
    ___ char __ input_str:
        __ char.isdigit():
            digits.a..(char)
    __ l..(digits) > 0:
        r.. True
    ____:
        r.. False