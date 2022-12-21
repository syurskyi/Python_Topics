#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


c.. Solution o..
    ___ insert  intervals, newInterval
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        merged_list   # list
        length = l..(intervals)

        # Insert the newInterval to the right position
        index = 0
        _____ index < length:
            __ intervals[index].start >= newInterval.start:
                intervals.insert(index, newInterval)
                ______
            index += 1
        __ index __ length:
            intervals.append(newInterval)

        i = 0
        length += 1
        # Scan every interval and merge the overlapping intervals.
        _____ i < length:
            j = i + 1
            _____ j < length a.. intervals[j].start <= intervals[i].end:
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
[5,7]
[[1,4],[6,8],[7,8]]
[3,10]
[[1,5]]
[6,8]
"""
