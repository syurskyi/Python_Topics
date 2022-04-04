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
        ans = 0

        __ n.. intervals:
            r.. ans

        time    # list

        ___ x __ intervals:
            time.a..((x.start, T..
            time.a..((x.end, F..

        time.s..()

        cnt = 0

        ___ t, is_start __ time:
            __ is_start:
                cnt += 1
            ____:
                cnt -= 1

            __ cnt > ans:
                ans = cnt

        r.. ans
