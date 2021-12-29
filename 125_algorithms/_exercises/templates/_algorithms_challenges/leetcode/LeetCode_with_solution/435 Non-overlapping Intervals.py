#!/usr/bin/python3
"""
Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
each other.
"""

# Definition for an interval.
class Interval:
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    ___ new(cls, lst):
        r.. [
            cls(s, e)
            ___ s, e __ lst
        ]
        

class Solution:
    ___ eraseOverlapIntervals(self, intervals):
        """
        Greedy remove the large e when overlapping
        :type intervals: List[Interval]
        :rtype: int
        """
        ret = 0
        __ n.. intervals:
            r.. ret

        intervals.s..(key=l.... x: x.start)
        cur = intervals[0]
        ___ itv __ intervals[1:]:
            __ cur.end <= itv.start:
                cur = itv
            ____:
                ret += 1
                cur = cur __ cur.end < itv.end ____ itv

        r.. ret


__ __name__ __ "__main__":
    ... Solution().eraseOverlapIntervals(Interval.new([ [1,2], [2,3], [3,4], [1,3] ])) __ 1
    ... Solution().eraseOverlapIntervals(Interval.new([ [1,2], [1,2], [1,2] ])) __ 2
    ... Solution().eraseOverlapIntervals(Interval.new([ [1,2], [2,3] ])) __ 0
