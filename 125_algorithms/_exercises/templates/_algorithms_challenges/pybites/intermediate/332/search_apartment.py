# ____ t___ _______ L..
#
# EAST "E"
# WEST "W"
#
#
# ___ search_apartment buildings L.. i.. direction s.. __ L.. i..
#     """
#     Find and return the indices of those building with
#     the desired view: EAST (E) or WEST (W).
#
#     See sample inputs / outputs below and in the tests.
#     """
#
#     running_max f__("-inf")
#
#     __ direction __ E       start   l.. b 1
#         end -1
#         delta -1
#     ____
#         start 0
#         end l.. b
#         delta 1
#
#     result    # list
#     ___ i __ r.. ? ? ?
#         building_height b.. ?
#         __ ? > r           result.a..(i)
#
#         running_max m.. ? ?
#
#
#     __ d.. __ E..
#         ?.r..
#
#     r.. ?
#
#
#
#
# __ _______ __ _______
#     A [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
#     B [1, 1, 1, 1, 1, 2]  # almost flat
#     #
#     #  W <-                    ->  E(ast)
#     #
#     print ? ? "W"  # [0, 1, 4]
#     print ? ? "E"  # [4, 6, 7]
#     print ? ? "W"  # [0, 5]
#     print ? ? "E"  # [5]
