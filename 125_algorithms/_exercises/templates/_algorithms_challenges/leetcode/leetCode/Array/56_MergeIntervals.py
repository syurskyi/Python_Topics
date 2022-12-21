#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


c.. Solution o..
    ___ merge  intervals
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        merged_list   # list
        length = l..(intervals)
        intervals.sort(k.._l... interval: interval.start)
        i = 0

        # Scan every interval and merge the overlapping intervals.
        _____ i < length:
            j = i + 1
            _____ j < length and intervals[j].start <= intervals[i].end:
                intervals[i].start = min(intervals[i].start,
                                         intervals[j].start)
                intervals[i].end = m..(intervals[i].end,
                                       intervals[j].end)
                j += 1

            merged_list.append(intervals[i])
            i = j

        r_ merged_list

"""
[]
[[1,4],[4,5]]
[[1,3],[2,6],[8,10],[15,18]]
[[12,13],[1,3],[5,8],[2,6],[6,7]]
"""
