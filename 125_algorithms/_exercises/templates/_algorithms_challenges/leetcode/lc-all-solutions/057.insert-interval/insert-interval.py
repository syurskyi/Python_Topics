# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

c_ Solution(o..
  ___ insert  intervals, newInterval
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    s, e newInterval.start, newInterval.end
    left f.. l.... x: x.end < newInterval.start, intervals)
    right f.. l.... x: x.start > newInterval.end, intervals)
    __ left + right !_ intervals:
      s m..(intervals[l..(left)].start, s)
      e m..(intervals[~l..(right)].end, e)
    r.. left + [Interval(s, e)] + right
