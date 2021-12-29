from difflib import SequenceMatcher
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
if not os.path.isfile(DICTIONARY):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


def load_words():
    'return dict of words in DICTIONARY'
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()
    

    return max(words,key=lambda x:SequenceMatcher(None,misspelled_word,x).ratio())
    best_word = None
    highest_ratio = float("-inf")
    for word in words:
        ratio = SequenceMatcher(None,misspelled_word,word).ratio()
        if ratio >highest_ratio:
            highest_ratio = ratio
            best_word = word


    return best_word 



