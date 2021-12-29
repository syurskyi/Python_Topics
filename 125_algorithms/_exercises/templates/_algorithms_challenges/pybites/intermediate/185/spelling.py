____ difflib _______ SequenceMatcher
_______ os
____ urllib.request _______ urlretrieve

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
__ n.. os.path.isfile(DICTIONARY):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


___ load_words():
    'return dict of words in DICTIONARY'
    with open(DICTIONARY) as f:
        r.. {word.strip().lower() ___ word __ f.readlines()}


___ suggest_word(misspelled_word: str, words: set = N..) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    __ words __ N..
        words = load_words()

    # you code
    highest_ratio = 0
    highest_word = ""
    ___ word __ words:
        alternative = SequenceMatcher(N.., misspelled_word, word)
        __ alternative.ratio() > highest_ratio:
            highest_ratio = alternative.ratio()
            highest_word = word
    r.. highest_word


__ __name__ __ "__main__":
    suggest_word("acheive")