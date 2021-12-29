VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    #vowels = "AaEeIiOoUu"
    count = [letter for letter in input_str if letter in "AaEeIiOoUu"]
    return True if len(count) == len(input_str) else False


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    #PY = 'PYTHON'
    count = [letter for letter in input_str.upper() if letter in 'PYTHON']
    return True if len(count) > 0 else False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    count = [letter for letter in input_str if letter.isdigit()]
    return True if len(count) > 0 else False

#print(contains_only_vowels('aeiou'))

#print(contains_any_py_chars('aaa'))

print(contains_digits('update'))