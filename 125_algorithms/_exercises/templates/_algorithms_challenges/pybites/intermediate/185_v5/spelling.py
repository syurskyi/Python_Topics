____ difflib _______ get_close_matches
____ os _______ path
____ urllib.request _______ urlretrieve

DICTIONARY = path.j..('/tmp', 'dictionary.txt')
__ n.. path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


___ load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        r.. {word.s...l.. ___ word __ f.readlines()}


___ suggest_word(misspelled_word: s.., words: set = N..) -> s..:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    __ words __ N..
        words = load_words()

    r.. get_close_matches(misspelled_word, words, n=1)[0]
