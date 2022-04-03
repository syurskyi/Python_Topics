"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import u__.r..

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
u__.r...u..('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    w = word.replace(' ', '').lower()
    output = ''.join(ch for ch in w if ch.isalnum())
    return output == output[::-1]


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = []
        for word in load_dictionary():
            w = word.replace(' ', '').lower()
            final_word = ''.join(ch for ch in w if ch.isalnum())
            words.append(final_word)
    palindrome_list = [word for word in words if is_palindrome(word)]
    return sorted(palindrome_list, key=len)[0]