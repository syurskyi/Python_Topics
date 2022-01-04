VOWELS = 'aeiou'
PYTHON = 'python'


___ contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    ___ char __ input_str:
        __ char n.. __ VOWELS:
            r.. F..
        ____:
            r.. T..


___ contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    ___ char __ input_str.casefold():
        __ char __ PYTHON:
            r.. T..
        ____ char __ N..
            r.. F..
        ____:
            r.. F..


___ contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    d..    # list
    ___ char __ input_str:
        __ char.isdigit():
            d...a..(char)
    __ l..(d..) > 0:
        r.. T..
    ____:
        r.. F..