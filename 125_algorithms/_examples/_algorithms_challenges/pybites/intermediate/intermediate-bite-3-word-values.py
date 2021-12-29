"""
Calculate the dictionary word that would have the most value in Scrabble.

There are 3 tasks to complete for this Bite:

First write a function to read in the dictionary.txt file (= DICTIONARY constant),
returning a list of words (note that the words are separated by new lines).

Second write a function that receives a word and calculates its value.
Use the scores stored in LETTER_SCORES.
Letters that are not in LETTER_SCORES should be omitted (= get a 0 score).

With these two pieces in place, write a third function that takes a list
of words and returns the word with the highest value.
Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
print(TMP)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
print(DICTIONARY)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words_v1():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    l = []
    with open(DICTIONARY) as file:
        for line in file:
            l.append(line.strip())
    return l

def load_words_v2():

    with open(DICTIONARY) as file:
        return [word.strip() for word in file.read().split()]

def calc_word_value_v1(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    value = 0
    for char in word.upper():
        try:
            value += LETTER_SCORES[char]
        except:
            value = 0
    return value

def calc_word_value_v2(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    max = ()
    for word in words:
        value = calc_word_value(word)
        if max == ():
            max = (word, value)
        else:
            if value > max[1]:
                max = (word, value)
    return max[0]

def max_word_value_v2(words):
    return max(words, key=calc_word_value)

print(max_word_value(['zime', 'fgrtgtrtvv']))