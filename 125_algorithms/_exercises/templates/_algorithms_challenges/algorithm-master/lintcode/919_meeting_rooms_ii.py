"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    ___ minMeetingRooms(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: int
        """
        ans = 0

        __ n.. intervals:
            r.. ans

        time    # list

        ___ x __ intervals:
            time.a..((x.start, True))
            time.a..((x.end, False))

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
