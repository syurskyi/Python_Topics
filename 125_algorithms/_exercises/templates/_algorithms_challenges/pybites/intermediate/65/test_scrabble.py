# _______ p__
#
# ____ ? _______ g..
#
# scrabble_scores [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
#                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
# LETTER_SCORES  letter| score ___ ? ? __ ?
#                  ___ ? __ ?.s..
#
#
# ___ calc_word_value word
#     """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
#     r.. s.. ?.g.. char.u.., 0 ___ ? __ ?
#
#
# ___ max_word_value words
#     """Calc the max value of a collection of words"""
#     r.. m.. ? k.._?
#
#
# ?p__.m__.p. "draw, expected", [
#     ('T, I, I, G, T, T, L', 'gilt'),
#     ('O, N, V, R, A, Z, H', 'zonar'),
#     ('E, P, A, E, I, O, A', ('apio', 'peai',
#     ('B, R, C, O, O, E, O', 'boce'),
#     ('G, A, R, Y, T, E, V', 'garvey'),
#
# ___ test_max_word ? e..
#     draw ?.s.. ', '
#     words ?
#     __ l.. e.. > 1
#         ... m.. ? __ e..
#     ____
#         ... m.. ? __ e..