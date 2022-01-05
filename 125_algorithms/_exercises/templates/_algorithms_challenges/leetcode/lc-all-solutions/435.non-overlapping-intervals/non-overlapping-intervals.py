# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

c_ Solution(o..):
  ___ eraseOverlapIntervals  intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.s..(key=l.... i: i.end)
    ans = 0
    end = float("-inf")
    ___ interval __ intervals:
      # print interval.start, interval.end
      __ interval.start >= end:
        ans += 1
        end = interval.end
    r.. l..(intervals) - ans
