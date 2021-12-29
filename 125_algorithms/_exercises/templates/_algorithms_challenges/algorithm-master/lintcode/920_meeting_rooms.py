"""
Definition of Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


"""
Sweep Line
time: O(n)
space: O(n)
"""
class Solution:
    ___ canAttendMeetings(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        timeline    # list

        ___ interval __ intervals:
            timeline.a..((interval.start, True))
            timeline.a..((interval.end, False))

        timeline.sort()

        cnt = 0

        ___ time, is_start __ timeline:
            __ is_start:
                cnt += 1
            ____:
                cnt -= 1

            __ cnt > 1:
                r.. False

        r.. True


"""
Sorting
time: O(nlogn)
space: O(1)
"""
class Solution:
    ___ canAttendMeetings(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        intervals.sort(key=l.... x: (x.start, x.end))

        ___ i __ r..(1, l..(intervals)):
            __ intervals[i].start < intervals[i - 1].end:
                r.. False

        r.. True
