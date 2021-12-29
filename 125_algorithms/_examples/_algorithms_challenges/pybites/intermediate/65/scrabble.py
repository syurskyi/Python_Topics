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

print(dictionary)
def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    return (word for word in _get_permutations_draw(draw) if word in dictionary)


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    
    for i in range(1,len(draw) + 1):
        for word in itertools.permutations(draw,i):
            yield ''.join(word).lower()






if __name__ == "__main__":

    DRAW = list('GARYTEV')

    print(list(_get_permutations_draw(DRAW)))



