VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    for char in input_str.casefold():
        if char not in VOWELS:
            return False
        else:
            return True


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for char in input_str.casefold():
        if char in PYTHON:
            return True
        elif char is None:
            return False
        else:
            return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    digits = []
    for char in input_str:
        if char.isdigit():
            digits.append(char)
    if len(digits) > 0:
        return True
    else:
        return False