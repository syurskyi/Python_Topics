VOWELS = 'aeiou'
PYTHON = 'python'


___ contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    vowel_count = []
    for char in input_str.casefold():
        __ char in VOWELS:
            vowel_count.append(char)
    __ len(vowel_count) == len(input_str):
        return True
    else:
        return False


___ contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    python_count = []
    for char in input_str.casefold():
        __ char in PYTHON:
            python_count.append(char)
    __ len(python_count) > 0:
        return True
    else:
        return False


___ contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    digits = []
    for char in input_str:
        __ char.isdigit():
            digits.append(char)
    __ len(digits) > 0:
        return True
    else:
        return False