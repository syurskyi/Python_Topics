_______ ___
_______ i..
_______ __
_______ u__.r..

# PREWORK
TMP __.g.. TMP  /tmp
DICT 'dictionary.txt'
DICTIONARY __.p...j..(TMP, DICT)
u__.r...u..(
    _*https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

w__ o.. ? __ f
    dictionary s..([word.s...l.. ___ word __ f.r...s.. ])


___ get_possible_dict_words(draw
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    perms _get_permutations_draw(draw)
    r.. l..(f.. l.... x: x __ dictionary, perms


___ _get_permutations_draw(draw
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw ''.j..(draw).l..
    ___ k __ r..(1, l..(draw)+1
        ___ perm __ i...p.. draw, r=k
            y.. ''.j..(perm)
