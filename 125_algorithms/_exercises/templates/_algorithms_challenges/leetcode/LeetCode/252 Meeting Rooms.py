"""
Premium Question
"""
______ operator

__author__ = 'Daniel'


class Interval:
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e


class Solution:
    ___ canAttendMeetings(self, intervals
        """

        :type intervals: list[Interval]
        :rtype: bool
        """
        intervals.sort(key=operator.attrgetter("start"))
        for i in xrange(le.(intervals)-1
            __ intervals[i].end > intervals[i+1].start:
                r_ False

        r_ True

