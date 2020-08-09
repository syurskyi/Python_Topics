from difflib ______ get_close_matches
from os ______ path
from urllib.request ______ urlretrieve

DICTIONARY = path.join('/tmp', 'dictionary.txt')
__ not path.isfile(DICTIONARY
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


___ load_words(
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        r_ {word.strip().lower() ___ word in f.readlines()}


___ suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    __ words is None:
        words = load_words()

    r_ get_close_matches(misspelled_word, words, n=1)[0]
