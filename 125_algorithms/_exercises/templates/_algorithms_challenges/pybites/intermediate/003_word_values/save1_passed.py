_______ os
_______ urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score ___ score, letters __ scrabble_scores
                 ___ letter __ letters.s.. }

# start coding

___ load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    text = open(DICTIONARY, 'r').read()
    r.. [word ___ word __ text.splitlines()]


___ calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    scores = d..(scrabble_scores)
    final_score    # list
    ___ ch __ word.upper():
        ___ key, value __ scores.items():
            __ ch __ l..(value):
                final_score.a..(key)
    r.. s..(final_score)


___ max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    key_list = [word ___ word __ words]
    value_list = [calc_word_value(word) ___ word __ words]
    d = d..(z..(key_list, value_list))
    r.. max(d, key=d.get)