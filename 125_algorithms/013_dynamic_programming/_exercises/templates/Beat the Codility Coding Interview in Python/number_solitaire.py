# # This is the solution for Dynamic programming > NumberSolitaire
# #
# # This is marked as RESPECTABLE difficulty
# # Note here we have the evolution of the algorithm. Only the last function is the correct one.
#
# ___ solutionRecursive A
#     r_ m.. ? 0
#
#
# ___ max_sum_six_distances a position
#     __ ? __ le. ? - 1
#         r_ ?|?
#     ____
#         max_forward _ mi. le. ? - ? 6
#         current_max _ -100000
#         ___ i __ ra.. 1 m..
#             local_max _ m.. a ? + ?
#             current_max _ ma. c.. ?
#         r_ ? + a|?
#
#
# ___ solutionMemoize A
#     values _ |-100000 * le. ?
#     r_ m.. ? 0, v..
#
#
# ___ max_sum_six_distancesMem a position values
#     __ ? __ le. ? - 1
#         r_ ?|?
#     __ v..|? __ -100000
#         max_forward _ mi. le. ? - ?, 6
#         current_max _ -100000
#         ___ i __ ra.. 1 m_f..
#             local_max _ m.. a ? + ? v..
#             current_max _ ma. c_m.0 l..
#         v..|? _ c_m.. + a|?
#     r_ ?|?
#
#
# ___ solution A
#     values _ |0 * le. ?
#     ?|le. ? - 1 _ ?|le. ? - 1
#     ___ i __ ra.. le. ? - 2 -1 -1)
#         v..|? _ ?|? + f.. v.. ? + 1 6
#     r_ v..|0
#
#
# ___ find_max_between values start length
#     max _ v..|s..
#     upto _ mi. s.. + l.. le. v..
#     ___ i __ ra.. s.. u..
#         __ v..|? > m..
#             m.. _ v..|?
#     r_ max
#
#
# print(sR.. 1, -2, 0, 9, -1, -2, 5, -4
# print(sR.. 1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2
#
# print(sM.. 1, -2, 0, 9, -1, -2, 5, -4
# print(sM.. 1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2
#
# print(s.. 1, -2, 0, 9, -1, -2, 5, -4
# print(s.. 1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2
