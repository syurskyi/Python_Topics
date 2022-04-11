"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


c_ Solution:
    ___ minMeetingRooms  intervals
        """
        :type intervals: list[Interval]
        :rtype: int
        """
        ans 0

        __ n.. intervals:
            r.. ans

        t__    # list

        ___ x __ intervals:
            t__.a..((x.start, T..
            t__.a..((x.end, F..

        t__.s..()

        cnt 0

        ___ t, is_start __ t__:
            __ is_start:
                cnt += 1
            ____
                cnt -_ 1

            __ cnt > ans:
                ans cnt

        r.. ans
