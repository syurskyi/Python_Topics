# # This is the solution for Sorting > NumberOfDiscIntersections
# #
# # This is marked as RESPECTABLE difficulty
#
# c_ Disc
#     ___ - low_x high_x
#         ? ?
#         ? ?
#
# ___ index_less_than sortedDiscList i start last
#     mid _ s.. + |l.. - s.. // 2
#     __ l.. <_ s.. an. s.. |m__.l.. > i
#         r_ m.. - 1
#     ____ l.. <_ s..
#         r_ m..
#     ____ s..|m...l.. > i
#         r_ ?|s.. i s.. m.. - 1
#     ____
#         r_ ? s.. i m.. + 1 l..
#
# ___ solution A
#     discs    # dict
#     ___ i in ra.. le. ?
#         ?.ap.. ? i - ?|? i + ?|i
#     discs _ so.. ? key_l__ d; ?.l..
#     total _ 0
#     ___ i __ ra.. le. ?
#         t.. += ? d.. d..|? .h.. + 0.5, 0, le. d.. - 1) - i
#         __ ? > 10000000
#             ? _ -1
#             b..
#     r_ ?
#
# print(solution([1, 5, 2, 1, 4, 0]))
#
# print(solution([0] * 100000))
