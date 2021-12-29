import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    possible_word = {}
    in_str = ''.join([letter for letter in draw if letter.isalpha()])
    permute_list = _get_permutations_draw(in_str)
    for word in permute_list:
        temp_word = ''.join(word)
        if temp_word.lower() in dictionary: 
            possible_word[temp_word.lower()] = calc_word_value(temp_word.lower())
    listOfKeys = list()
    max_value = max(possible_word.values())
    for key, value in possible_word.items():
        if value == max_value:
            listOfKeys.append(key)
    return listOfKeys

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    """     
    permute_words_list = []
    for i in range(len(draw)):
        permute_words = list(itertools.permutations(draw, i+1))
        permute_words_list += permute_words
    return permute_words_list
     """
    lowered = ''.join(draw).lower()
    for i in range(1, len(draw) + 1):
        yield from itertools.permutations(lowered, i)
