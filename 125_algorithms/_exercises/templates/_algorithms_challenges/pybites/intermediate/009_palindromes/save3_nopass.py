"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


___ load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


___ is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    w = word.replace(' ', '').lower()
    output = ''.join(ch for ch in w __ ch.isalnum())
    return output == output[::-1]


___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    __ words is None:
        words = [word for word in load_dictionary()][0]
    words = words.replace(' ', '').lower()
    output = ''.join(ch for ch in words __ ch.isalnum())
    palindrome_list = ''.join(word for word in output __ is_palindrome(word))
    return sorted(palindrome_list, key=len)