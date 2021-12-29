# # Edit Distance
# # Question: Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# # (Each operation is counted as 1 step.)
# # You have the following 3 operations permitted on a word:
# # a) Insert a character
# # b) Delete a character
# # c) Replace a character
# # Solutions:
#
#
# c_ Solution
#     # @return an integer
#     ___ minDistance word1 word2
#         m _ len ? + 1; n _ len ? + 1
#         dp _ 0 ___ i __ ra.. n ___ j __ ra.. m
#         ___ i __ ra.. n
#             ? 0 ? _ ?
#         ___ i __ ra.. m
#             ? ? 0 _ ?
#         ___ i __ ra.. 1 m
#             ___ j __ ra.. 1 n
#                 ? ? ? _ min ? ? - 1 ? + 1, ? ? ? - 1 + 1 ? ? - 1 ? - 1+ 0 __ _1 ? - 1 __ _2 ? - 1 ____ 1
#         r_ ? ? - 1 ? - 1
#
#
# ?.? "Freebirds", "Dinner"