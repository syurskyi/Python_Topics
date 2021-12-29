# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    ___ merge(self, intervals):
        __ n.. intervals:
            r.. []
        n = l..(intervals)
        __ n __ 1:
            r.. intervals
        ____:
            # Sort the intervals by start value
            intervals.s..(key=l.... x: x.start)
            res    # list
            res.a..(intervals[0])
            cur_end = intervals[0].end
            cur_index = 0
            ___ interval __ intervals[1:]:
                __ interval.start <= cur_end:
                    __ interval.end > cur_end:
                        res[cur_index].end = interval.end
                        cur_end = interval.end
                ____:
                    # Added a non-overlapping interval
                    res.a..(interval)
                    cur_end = interval.end
                    cur_index += 1
            r.. res
