"""
Definition of Interval.
class Interval:
    ___ __init__(self, start, end
        self.start = start
        self.end = end
"""


"""
Sweep Line
time: O(n)
space: O(n)
"""
class Solution:
    ___ canAttendMeetings(self, intervals
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        timeline = []

        for interval in intervals:
            timeline.append((interval.start, True))
            timeline.append((interval.end, False))

        timeline.sort()

        cnt = 0

        for time, is_start in timeline:
            __ is_start:
                cnt += 1
            ____
                cnt -= 1

            __ cnt > 1:
                r_ False

        r_ True


"""
Sorting
time: O(nlogn)
space: O(1)
"""
class Solution:
    ___ canAttendMeetings(self, intervals
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: (x.start, x.end))

        for i in range(1, le.(intervals)):
            __ intervals[i].start < intervals[i - 1].end:
                r_ False

        r_ True
