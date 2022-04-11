_______ i..
_______ __
_______ u__.r..

# PREWORK
DICTIONARY __.p...j..('/tmp', 'dictionary.txt')
u__.r...u..('http://bit.ly/2iQ3dlZ', DICTIONARY)

w__ o.. ? __ f
    dictionary s..([word.s...l.. ___ word __ f.r...s.. ])


___ get_possible_dict_words(draw
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    r.. [word ___ word __ _get_permutations_draw(draw) __ word __ dictionary]


___ _get_permutations_draw(draw
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    r.. [''.j..(x).l.. ___ r __ r..(l..(draw ___ x __ i...p.. draw, r + 1)]
