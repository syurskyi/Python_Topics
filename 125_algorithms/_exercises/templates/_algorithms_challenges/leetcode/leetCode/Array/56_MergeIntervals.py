# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
# # Definition for an interval.
# # class Interval(object):
# #     def __init__(self, s=0, e=0):
# #         self.start = s
# #         self.end = e
#
#
# c.. Solution o..
#     ___ merge  intervals
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         merged_list   # list
#         length _ l.. ?
#         ?.s.. k.._l... interval| ?.s..
#         i _ #
#
#         # Scan every interval and merge the overlapping intervals.
#         _____ i < l..
#             j = ? + 1
#             _____ ? < l.. a.. ?|?.s.. _ ?|?.e..
#                 ?|?.s.. = m.. ?|?.s..
#                                          ?|?.s..
#                 ?|?.e.. = m..(?|?.e..,
#                                        ?|?.e..
#                 j +_ #
#
#             m__.a.. ?|?
#             ? _ ?
#
#         r_ ?
#
# """
# []
# [[1,4],[4,5]]
# [[1,3],[2,6],[8,10],[15,18]]
# [[12,13],[1,3],[5,8],[2,6],[6,7]]
# """
