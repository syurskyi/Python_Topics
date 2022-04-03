_______ __
_______ u__.r..

# PREWORK
TMP = __.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = __.p...j..(TMP, DICT)
u__.r...u.. _*{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score ___ score, letters __ scrabble_scores
                 ___ letter __ letters.s.. }

# start coding

___ load_words
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""

    w__ o.. DICTIONARY _ __ f:
        content = f.r..
    

    r.. content.s.. 


___ calc_word_value(word
    """Given a word calculate its value using the LETTER_SCORES dict"""


    r.. s..(LETTER_SCORES.get(letter,0) ___ letter __ word.upper


___ max_word_value(words
    """Given a list of words calculate the word with the maximum value and return it"""
    
    max_word = N..
    max_score = f__("-inf")

    ___ word __ words:
        score = calc_word_value(word)
        __ score > max_score:
            max_score = score
            max_word = word


    r.. max_word








