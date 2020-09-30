______ itertools
______ os
______ urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() ___ word __ f.read().split()])


___ get_possible_dict_words(draw
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    r_ [word ___ word __ _get_permutations_draw(draw) __ word __ dictionary]


___ _get_permutations_draw(draw
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    r_ [''.join(x).lower() ___ r __ range(le.(draw)) ___ x __ itertools.permutations(draw, r + 1)]
