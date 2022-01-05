# """
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
# drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
# container, such that the container contains the most water.
#
# Note: You may not slant the container.
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ maxArea  height
#         """
#         Two pointers scanning
#         starting from two ends since x-coordinate is maximized
#
#         Different from 041 Trapping Rain Water, since here it only considers two lines
#         :param height: array
#         :return: max area, integer
#         """
#         start = 0
#         end = l.. ? -1
#
#         max_area  -1 << 32
#         w.... ? < ?
#             area  m.. ? ? ? ? * ? - ?
#             max_area _ m.. ? ?
#
#             # move the shorter boarder
#             # move two pointers
#             __ ? ? < ? ?
#                 ? +_ 1
#             ____
#                 ? -_ 1
#
#         r.. ?
#
