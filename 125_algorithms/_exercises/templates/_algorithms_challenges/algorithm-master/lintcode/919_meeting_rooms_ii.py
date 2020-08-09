"""
Definition of Interval.
class Interval(object
    ___ __init__(self, start, end
        self.start = start
        self.end = end
"""


class Solution:
    ___ minMeetingRooms(self, intervals
        """
        :type intervals: list[Interval]
        :rtype: int
        """
        ans = 0

        __ not intervals:
            r_ ans

        time = []

        for x in intervals:
            time.append((x.start, True))
            time.append((x.end, False))

        time.sort()

        cnt = 0

        for t, is_start in time:
            __ is_start:
                cnt += 1
            ____
                cnt -= 1

            __ cnt > ans:
                ans = cnt

        r_ ans
