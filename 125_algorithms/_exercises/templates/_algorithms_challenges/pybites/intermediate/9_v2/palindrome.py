"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import re

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


___ load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


___ is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""

    
    
    word = re.sub(r'\W','',word).lower()

    low,high = 0,len(word) - 1


    while low < high:
        __ word[low] != word[high]:
            return False

        low += 1
        high -= 1

    return True



___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    
    __ not words:
        words = load_dictionary()
    
    longest_length = float("-inf")
    longest = None
    for word in words:
        __ is_palindrome(word):
            __ len(word) > longest_length:
                longest_length = len(word)
                longest_word = word

    return longest_word

