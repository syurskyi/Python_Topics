# Definition for an interval.
# class Interval(object
#     ___ __init__(self, s=0, e=0
#         self.start = s
#         self.end = e

class SummaryRanges(object

  ___ __init__(self
    """
    Initialize your data structure here.
    """
    self.intervals = []

  ___ insert(self, newInterval
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals = self.intervals
    # print intervals
    __ not intervals:
      intervals.append(newInterval)
      r_
    s, e = newInterval.start, newInterval.end
    left = filter(lambda x: x.end < newInterval.start, intervals)
    right = filter(lambda x: x.start > newInterval.end, intervals)
    # print left, right, (s, e)
    __ left + right != intervals:
      s = min(intervals[le.(left)].start, s)
      e = max(intervals[~le.(right)].end, e)
    newIntv = Interval(s, e)
    __ left and left[-1].end + 1 __ s:
      newIntv.start = left[-1].start
      left = left[:-1]
    __ right and right[0].start - 1 __ e:
      newIntv.end = right[0].end
      right = right[1:]
    self.intervals = left + [newIntv] + right

  ___ addNum(self, val
    """
    :type val: int
    :rtype: void
    """
    self.insert(Interval(val, val))

  ___ getIntervals(self
    """
    :rtype: List[Interval]
    """
    r_ self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
