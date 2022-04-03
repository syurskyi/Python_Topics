____ difflib _______ get_close_matches
____ __ _______ p..
____ u__.r.. _______ u..

DICTIONARY = p...j..('/tmp', 'dictionary.txt')
__ n.. p...isfile(DICTIONARY
    u..('http://bit.ly/2iQ3dlZ', DICTIONARY)


___ load_words
    """Return a set of words from DICTIONARY"""
    w__ o.. DICTIONARY) __ f:
        r.. {word.s...l.. ___ word __ f.r..}


___ suggest_word(misspelled_word: s.., words: s.. = N..) __ s..:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    __ words __ N..
        words = load_words()

    r.. get_close_matches(misspelled_word, words, n=1)[0]
