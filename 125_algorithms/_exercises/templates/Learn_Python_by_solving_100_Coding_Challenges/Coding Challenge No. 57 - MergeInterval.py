# # Merge Intervals
# # Question: Given a collection of intervals, merge all overlapping intervals.
# # For example:
# # Given [1,3],[2,6],[8,10],[15,18],
# # return [1,6],[8,10],[15,18].
# # Solutions:
#
#
# c_ Interval
#     ___  -  s_0 e_0
#         start _ ?
#         end _ ?
#     ___ printIn i
#         print  "[@ ,@]"  ?.s.. ?.e..
#
#
# c_ Solution
#     # @param intervals, a list of Interval
#     # @return a list of Interval
#     ___ merge  intervals
#         ?.s.. key _ l___ x ?.s..
#         length _ le. ?
#         res_  # list
#         ___ i __ ra.. l..
#             __ ? __  # list:
#                 ?.ap.. ? ?
#             ____
#                 size_len ?
#                 __ ? ? - 1 .s.. <_ ? ? .s.. <_ ? ? - 1 .e..
#                     ? ?-1 .end _ ma. ? ? .e.. ? ? - 1 .e..
#                 ____
#                     ?.ap.. ? ?
#         r_ ?
#
#
# i1 _ ? 1,3
# i2 _ ? 2,6
# i3 _ ? 8,10
# i4 _ ? 15,18
# result _ ? .? ? ? ? ?
# ___ i __ ?
#     ? . ? ?