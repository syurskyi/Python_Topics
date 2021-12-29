import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

___ load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    text = open(DICTIONARY, 'r').read()
    return [word for word in text.splitlines()]


___ calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    scores = dict(scrabble_scores)
    final_score = []
    for ch in word.upper():
        for key, value in scores.items():
            __ ch in list(value):
                final_score.append(key)
    return sum(final_score)


___ max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    key_list = [word for word in words]
    value_list = [calc_word_value(word) for word in words]
    d = dict(zip(key_list, value_list))
    return max(d, key=d.get)