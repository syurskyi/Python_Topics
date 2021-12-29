VOWELS = 'aeiou'
PYTHON = 'python'


___ contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    #vowels = "AaEeIiOoUu"
    count = [letter ___ letter __ input_str __ letter __ "AaEeIiOoUu"]
    r.. True __ l..(count) __ l..(input_str) ____ False


___ contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    #PY = 'PYTHON'
    count = [letter ___ letter __ input_str.upper() __ letter __ 'PYTHON']
    r.. True __ l..(count) > 0 ____ False


___ contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    count = [letter ___ letter __ input_str __ letter.isdigit()]
    r.. True __ l..(count) > 0 ____ False

#print(contains_only_vowels('aeiou'))

#print(contains_any_py_chars('aaa'))

print(contains_digits('update'))