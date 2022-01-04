_______ sys
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


___ get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    perms = _get_permutations_draw(draw)
    r.. l..(filter(l.... x: x __ dictionary, perms))


___ _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw = ''.j..(draw).l..
    ___ k __ r..(1, l..(draw)+1):
        ___ perm __ i...permutations(draw, r=k):
            y.. ''.j..(perm)
