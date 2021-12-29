"""
Premium Question
"""
_______ operator

__author__ = 'Daniel'


class Interval:
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    ___ canAttendMeetings(self, intervals):
        """

        :type intervals: list[Interval]
        :rtype: bool
        """
        intervals.s..(key=operator.attrgetter("start"))
        ___ i __ xrange(l..(intervals)-1):
            __ intervals[i].end > intervals[i+1].start:
                r.. False

        r.. True

