____ difflib _______ SequenceMatcher
_______ __
____ u__.r.. _______ u..

TMP = __.g..("TMP", "/tmp")
DICTIONARY = __.p...j..(TMP, 'dictionary.txt')
__ n.. __.p...isfile(DICTIONARY
    u..(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


___ load_words
    'return dict of words in DICTIONARY'
    w__ o.. DICTIONARY) __ f:
        r.. {word.s...l.. ___ word __ f.r..}


___ suggest_word(misspelled_word: s.., words: s.. = N..) __ s..:
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


__ _______ __ _______
    suggest_word("acheive")