# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
  ___ merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    ans    # list
    ___ intv __ s..(intervals, key=l.... x: x.start):
      __ ans and ans[-1].end >= intv.start:
        ans[-1].end = max(ans[-1].end, intv.end)
      ____:
        ans.a..(intv)
    r.. ans
