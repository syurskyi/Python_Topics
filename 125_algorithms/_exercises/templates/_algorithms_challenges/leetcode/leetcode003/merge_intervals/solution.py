# Definition for an interval.
# class Interval:
#     ___ __init__(self, s=0, e=0
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    ___ merge(self, intervals
        __ not intervals:
            r_ []
        n = le.(intervals)
        __ n __ 1:
            r_ intervals
        ____
            # Sort the intervals by start value
            intervals.sort(key=lambda x: x.start)
            res = []
            res.append(intervals[0])
            cur_end = intervals[0].end
            cur_index = 0
            for interval in intervals[1:]:
                __ interval.start <= cur_end:
                    __ interval.end > cur_end:
                        res[cur_index].end = interval.end
                        cur_end = interval.end
                ____
                    # Added a non-overlapping interval
                    res.append(interval)
                    cur_end = interval.end
                    cur_index += 1
            r_ res
