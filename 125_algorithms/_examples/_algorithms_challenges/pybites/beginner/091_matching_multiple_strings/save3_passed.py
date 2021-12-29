VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    vowel_count = []
    for char in input_str.casefold():
        if char in VOWELS:
            vowel_count.append(char)
    if len(vowel_count) == len(input_str):
        return True
    else:
        return False


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    python_count = []
    for char in input_str.casefold():
        if char in PYTHON:
            python_count.append(char)
    if len(python_count) > 0:
        return True
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