# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# c.. Solution o..
#     ___ spiralOrder  matrix
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         __ n.. ?
#             r_ # list
#
#         m_row _ l.. ?
#         n_col _ l.. ? 0
#         min_m_n _ m.. ? ?
#
#         spiral_order   # list
#         step _ #
#         _____ ? < (m.. + 1) / 2:
#             horizontal_len _ n.. - 1 - 2 * ?
#             vertical_len = m.. - 1 - 2 * ?
#             # print "step.._ |", step, horizontal_len, vertical_len
#
#             # Add the current up edge to spiral order.
#             __ ? __ 0 a.. ? > 0
#                 h.. +_ 1
#             ___ i __ r.. h..
#                 s__.a.. m..|s..| ? + s..
#
#             # Add the current right edge to spiral order.
#             __ ? __ 0 a.. ? > 0
#                 ? +_ 1
#             ___ i __ r.. v..
#                 s__.a.. m..|? + s..|n.. - 1 - s..
#
#             __ v.. > 0
#                 # Add the current down edge to spiral order.
#                 ___ i __ r.. h..
#                     s__.a..
#                         m..|m.. - 1 - s..|n.. - 1 - s.. - ?
#
#             __ h.. > 0
#                 # Add the current left edge to spiral order.
#                 ___ i __ r.. v..
#                     s__.a..
#                         m..|m.. - 1 - s.. - ?|s..
#
#             ? +_ 1
#
#         # For N * N matrix, where N is an odd number.
#         __ v.. __ h.. __ 0 a.. m.. __ n..
#             s__.a.. m..|m. / 2|n.. / 2
#
#         r_ ?
#
#
# """
# []
# [[1]]
# [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# [[1],[2],[3]]
# [[2,5],[8,4],[0,-1]]
# [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
# """
