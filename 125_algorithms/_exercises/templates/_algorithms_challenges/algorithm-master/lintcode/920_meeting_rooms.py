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
c_ Solution:
    ___ canAttendMeetings  intervals
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        timeline    # list

        ___ interval __ intervals:
            timeline.a..((interval.start, T..
            timeline.a..((interval.end, F..

        timeline.s..()

        cnt = 0

        ___ time, is_start __ timeline:
            __ is_start:
                cnt += 1
            ____
                cnt -= 1

            __ cnt > 1:
                r.. F..

        r.. T..


"""
Sorting
time: O(nlogn)
space: O(1)
"""
c_ Solution:
    ___ canAttendMeetings  intervals
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        intervals.s..(key=l.... x: (x.start, x.end

        ___ i __ r..(1, l..(intervals:
            __ intervals[i].start < intervals[i - 1].end:
                r.. F..

        r.. T..
