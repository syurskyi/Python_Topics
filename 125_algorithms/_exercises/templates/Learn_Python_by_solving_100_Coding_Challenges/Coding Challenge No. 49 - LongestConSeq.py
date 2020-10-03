# # Longest Consecutive Sequence
# # Question: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# # For example,
# # Given [100, 4, 200, 1, 3, 2],
# # The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# # Your algorithm should run in O(n) complexity.
# # Solutions:
#
#
# c_ Solution
#     # @param num, a list of integer
#     # @return an integer
#
#     ___ longestConsecutive  num
#         startToEnd _  # dict
#         endToStart _ # dict
#         longest _ 0
#         ___ i __ ra.. 0 le. ?
#             start _ ? ?
#             end _ ? ?
#             __ ? ? __ ?
#                 e.. _ ? ? ?
#                 ? ? ? ?
#                 ? ? ?
#             __ ? ? __ e..
#                 s.. _ ? ? ?
#                 ? ? ? ?
#                 ? ? ? ?
#             __ ? ? - 1 __ e..
#                 s.. _ mi. s.. e.. ? ? - 1
#                 ? s.. e.. ? ? - 1
#                 ? e... ? ?-1
#             __ ? ? + 1 __ s..
#                 e.. _ ma. e.. s.. ? ? + 1
#                 ? e.. ? ? ? ? + 1
#                 ? s.. ? ? + 1
#             s.. ? _ e..
#             e.. ? _ ?
#             l.. _ ma. ? e.. - ? + 1
#         r_ ?
#
# ? .?  [100, 4, 200, 1, 3, 2]