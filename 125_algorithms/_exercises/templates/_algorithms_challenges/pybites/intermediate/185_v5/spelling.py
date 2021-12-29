from difflib import get_close_matches
from os import path
from urllib.request import urlretrieve

DICTIONARY = path.join('/tmp', 'dictionary.txt')
__ not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


___ load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


___ suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    __ words __ None:
        words = load_words()

    return get_close_matches(misspelled_word, words, n=1)[0]
