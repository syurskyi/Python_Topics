# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
  ___ insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    s, e = newInterval.start, newInterval.end
    left = filter(lambda x: x.end < newInterval.start, intervals)
    right = filter(lambda x: x.start > newInterval.end, intervals)
    __ left + right != intervals:
      s = min(intervals[len(left)].start, s)
      e = max(intervals[~len(right)].end, e)
    return left + [Interval(s, e)] + right
