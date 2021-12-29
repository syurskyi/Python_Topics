"""
Write a function to determine if a word (or phrase) is a palindrome.

Then write a second function to receive a word (or phrase) list and determine which word is the
longest palindrome.

See the template code / docstrings below for further requirements as well as the tests.

A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward.

"""

import os
import urllib.request
import string
import re

DICTIONARY = os.path.join(os.getenv('temp'), 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)

# How come it's a generator, if it doesn't have yield statement?
# It's a generator expression
# What is the memory requirement for this code?
#
___ load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


___ is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    stripped = re.sub(r'[^a-z]', '', word.lower())
    i, j = 0, len(stripped) - 1
    while i < j:
        __ stripped[i] != stripped[j]:
            return False
        i, j = i + 1, j - 1
    return True

___ is_palindrome_pybites_solution(word):
    word = re.sub(r'\W+', '', word.lower())
    return word == word[::-1]

# jak to elegancko przerobic, zeby spelnic kryterium zadania?
___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    max_pal = 0
    pal = ""
    __ words:
        for word in words:
            __ is_palindrome(word):
                __ len(word) > max_pal:
                    max_pal = len(word)
                    pal = word
    else:
        for word in load_dictionary():
            __ is_palindrome(word):
                __ len(word) > max_pal:
                    max_pal = len(word)
                    pal = word

    return pal

___ get_longest_palindrome(words_ N..

    __ not words:
        words = load_dictionary()
    palindromes = (word for word in words __ is_palindrome(word))
    return max(palindromes, key=len)

print(get_longest_palindrome())
