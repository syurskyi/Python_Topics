# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# c.. Solution o..
#     ___ generateMatrix  n
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         __ n.. ?
#             r_ # list
#
#         matrix = ||-1 ___ row __ r..?| ___ col __ r..?
#         current_num = #
#         step _ #
#         _____ ? < n / 2
#             edge_len = ? - 1 - 2 * s..
#
#             # Get number from left to right(up edge)
#             ___ i __ r.. ?
#                 m..|s..|? + s.. _ c..
#                 c.. +_ 1
#
#             # Get number from up to down(right edge)
#             ___ i __ r.. e..
#                 m..|? + s..|? - 1 - s.. _ c..
#                 c.. +_ #
#
#             # Get number from right to left(down edge)
#             ___ i __ r.. e..
#                 m..|? - 1 - s..|? - 1 - s.. - ? _ c..
#                 c.. +_ #
#
#             # Get number from down to up(left edge)
#             ___ i __ r.. e..
#                 m..|? - 1 - s.. - ?|s.. _ c..
#                 c.. +_ #
#             s.. +_ #
#
#         __ n % 2 __ 1
#             m..|?/2|?/2 _ c..
#         r_ ?
#
# """
# 0
# 1
# 3
# 4
# """
