"""
Premium Question
Find the maximum number of overlapped intervals
"""
______ heapq
______ operator


__author__ = 'Daniel'


class Interval:
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e


class Solution(object
    ___ minMeetingRooms(self, intervals
        """

        :type intervals: list[Interval]
        :rtype: int
        """
        maxa = 0

        intervals.sort(key=operator.attrgetter("start"))
        h_end =   # list
        ___ itvl __ intervals:
            heapq.heappush(h_end, itvl.end)
            w___ h_end and h_end[0] <= itvl.start:
                heapq.heappop(h_end)

            maxa = ma.(maxa, le.(h_end))

        r_ maxa