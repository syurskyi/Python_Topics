"""
Premium Question
Find the maximum number of overlapped intervals
"""
_______ heapq
_______ operator


__author__ = 'Daniel'


c_ Interval:
    ___ - , s=0, e=0):
        start = s
        end = e


c_ Solution(object):
    ___ minMeetingRooms  intervals):
        """

        :type intervals: list[Interval]
        :rtype: int
        """
        maxa = 0

        intervals.s..(key=operator.attrgetter("start"))
        h_end    # list
        ___ itvl __ intervals:
            heapq.heappush(h_end, itvl.end)
            w.... h_end a.. h_end[0] <= itvl.start:
                heapq.heappop(h_end)

            maxa = m..(maxa, l..(h_end))

        r.. maxa