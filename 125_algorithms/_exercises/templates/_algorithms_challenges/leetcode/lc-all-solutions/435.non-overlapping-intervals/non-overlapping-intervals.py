# Definition for an interval.
# class Interval(object
#     ___ __init__(self, s=0, e=0
#         self.start = s
#         self.end = e

class Solution(object
  ___ eraseOverlapIntervals(self, intervals
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.sort(key=lambda i: i.end)
    ans = 0
    end = float("-inf")
    for interval in intervals:
      # print interval.start, interval.end
      __ interval.start >= end:
        ans += 1
        end = interval.end
    r_ le.(intervals) - ans
