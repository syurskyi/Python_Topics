# # Knight's Tour Code
# #
# # ** Below is th ecode referenced in the video lecture. Please refer to the video lectures for full explanation.**
#
# ___ knightGraph bdSize
#     ktGraph _ Graph()
#     ___ row __ ra.. ?
#         ___ col __ ra.. ?
#             nodeId _ p.. ? ? ?
#             newPositions _ g.. ? ? ?
#             ___ e __ ?
#                 nid _ p.. ?|0 ?|1 ?
#                 k__.aE.. n.. nid)
#     r_ ?
#
# ___ posToNodeId row column board_size
#     r_ |r.. * b.| + c..
#
# ___ genLegalMoves x y bdSize
#     newMoves _   # list
#     moveOffsets _ [(-1,-2),(-1,2),(-2,-1),(-2,1),
#                    ( 1,-2),( 1,2),( 2,-1),( 2,1)]
#     ___ i __ m..
#         newX _ x + i[0]
#         newY _ y + i[1]
#         __ l.. |_X b.. an. \
#                         l.. _Y b..
#             n__.ap..||_X _Y
#     r_ ?
#
# ___ legalCoord x bdSize
#     __ ? >_ 0 an. ? < ?
#         r_ T..
#     ____
#         r_ F..
#
# ___ knightTour n path u limit
#         u.s.. 'gray'
#         p__.ap.. u
#         __ n < l..
#             nbrList _ li.. u.g..
#             i _ 0
#             done _ F..
#             w___ i < le. ? an. no. d..
#                 __ ?|? .gC.. __ 'white'
#                     d.. _ ? ?+1 p.. n..|? l..
#                 i _ ? + 1
#             __ no. d..  # prepare to backtrack
#                 p__.po.
#                 u.sC.. 'white'
#         ____
#             d.. _ T..
#         r_ ?