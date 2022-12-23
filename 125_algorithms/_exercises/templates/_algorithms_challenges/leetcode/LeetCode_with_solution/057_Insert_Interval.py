# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

c_ Solution o..
    ___ insert  intervals, newInterval
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        __ intervals is N.. or l.. intervals) __ 0:
            r_ [newInterval]
        intervals.s.. k.._l... x:x.start)
        pos = 0
        w.. pos < l.. intervals
            # left of pos
            __ newInterval.end < intervals[pos].start:
                intervals.insert(pos, newInterval)
                r_ intervals
            # overlap with pos
            __ check_overlap(intervals[pos], newInterval
                temp = intervals.pop(pos)
                newInterval = merge_intervals(temp, newInterval)
            ____
                pos += 1
        __ l.. intervals) __ 0 or pos __ l.. intervals
            intervals.a.. newInterval)
        r_ intervals

    ___ check_overlap  curr_int, new_int
        __ curr_int.start <= new_int.start:
           __ curr_int.end > new_int.start:
               r_ T..
        ____
            __ curr_int.start <= new_int.end:
                r_ T..
        r_ F..

    ___ merge_intervals  int1, int2
        temp_int = Interval()
        temp_int.start = m.. [int1.start, int2.start])
        temp_int.end = m..([int1.end, int2.end])
        r_ temp_int


