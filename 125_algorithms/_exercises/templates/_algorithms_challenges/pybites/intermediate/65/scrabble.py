_______ i..
_______ os
_______ urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.j..(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

w__ open(DICTIONARY) __ f:
    dictionary = set([word.s...l.. ___ word __ f.read().s.. ])

print(dictionary)
___ get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    r.. (word ___ word __ _get_permutations_draw(draw) __ word __ dictionary)


___ _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    
    ___ i __ r..(1,l..(draw) + 1):
        ___ word __ i...permutations(draw,i):
            y.. ''.j..(word).l..






__ _______ __ _______

    DRAW = l..('GARYTEV')

    print(l..(_get_permutations_draw(DRAW)))



