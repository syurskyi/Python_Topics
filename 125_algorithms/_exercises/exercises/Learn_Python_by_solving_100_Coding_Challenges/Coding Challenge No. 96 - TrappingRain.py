# # Trapping Rain Water
# # Question: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# # For example,
# # Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# # Solutions:
#
#
# c_ Solution
#     # @param {integer[]} height
#     # @return {integer}
#     ___ trap  height
#         __ no. h.. o. le. h.. __ 1
#             r_ 0
#         max_left _ h.. 0
#         AddVolume _ ?
#
#         ___ i __ ra.. 1 le. h.. - 1
#             __ m.. < h.. ? - 1
#                 m.. _ h.. ? - 1
#             A__.ap.. m...
#
#         max_right _ h.. -1
#         A__.ap.. ?
#
#         ___ i __ r.. ra.. 1 le. h.. - 1
#             __ m.. < h.. ? + 1
#                     m.. _ h.. ? + 1
#             A.. ? _ mi. m.. A.. ?
#         ___ i __ ra.. le. A..
#             ? ? _ ma. ? ? - h.. ? 0
#         r_ su. ?
#
#
# ? .? [0,1,0,2,1,0,1,3,2,1,2,1]