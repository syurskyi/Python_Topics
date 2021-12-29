from difflib import SequenceMatcher
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
__ not os.path.isfile(DICTIONARY):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


___ load_words():
    'return dict of words in DICTIONARY'
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


___ suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    __ words is None:
        words = load_words()

    # you code
    highest_ratio = 0
    highest_word = ""
    for word in words:
        alternative = SequenceMatcher(None, misspelled_word, word)
        __ alternative.ratio() > highest_ratio:
            highest_ratio = alternative.ratio()
            highest_word = word
    return highest_word


__ __name__ == "__main__":
    suggest_word("acheive")