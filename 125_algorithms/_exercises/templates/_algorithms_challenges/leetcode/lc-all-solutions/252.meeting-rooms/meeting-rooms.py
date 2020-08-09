# Definition for an interval.
# class Interval(object
#     ___ __init__(self, s=0, e=0
#         self.start = s
#         self.end = e

class Solution(object
  ___ canAttendMeetings(self, intervals
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    intervals = sorted(intervals, key=lambda x: x.start)
    ___ i in range(1, le.(intervals)):
      __ intervals[i].start < intervals[i - 1].end:
        r_ False
    r_ True
