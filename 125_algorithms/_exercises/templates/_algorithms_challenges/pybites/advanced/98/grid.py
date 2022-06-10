# _______ __
# DOWN, UP, LEFT, RIGHT '⇓', '⇑', '⇐', '⇒'
# START_VALUE 1
#
#
# ___ print_sequence_route grid, start_coordinates_ N..
#     """Receive grid string, convert to 2D matrix of ints, find the
#        START_VALUE coordinates and move through the numbers in order printing
#        them.  Each time you turn append the grid with its corresponding symbol
#        (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
#
#
#
#     matrix    # list
#     ___ i,line __ e.. g__.s..
#         __ i % 2 __ 1
#             values l.. m.. i.. __.s.. _ \D+ l..
#             __ S.. __ ?
#                 start_row l.. m..
#                 start_col v__.i.. S..
#             m__.a.. v..
#
#
#     length l.. m..
#
#     goal ?**2
#     current_row current_col start_row start_col
#     current_value S..
#
#     previous_direction N..
#
#
#     print c.. e.._' '
#     w.... c.. !_ g..
#         directions c.. + 1 c.. D.. c.. - 1,c.. U. c.. c.. + 1 R.. c.. c.. -1 L..
#
#
#         ___ neighbor_x,neighbor_y,direction __ ?
#             __ 0 <_ _x < l.. a.. 0 <_ _y < l..
#                 __ m.. _x _y __ c.. + 1
#                     __ p.. __ n.. N.. a.. d.. !_ p..
#                         print d..
#                         p.. d..
#                     ____ p..__ N..
#                         p.. d..
#                     print c.. + 1 e.._' '
#
#                     _____
#
#         c..,c.. _x _y
#         c.. +_ 1
#
# __ _______ __ _______
#
#
#     small_grid """
# 21 - 22 - 23 - 24 - 25
#  |
# 20    7 -  8 -  9 - 10
#  |    |              |
# 19    6    1 -  2   11
#  |    |         |    |
# 18    5 -  4 -  3   12
#  |                   |
# 17 - 16 - 15 - 14 - 13"""
#
#
#     ? ?
#
#
#
#
