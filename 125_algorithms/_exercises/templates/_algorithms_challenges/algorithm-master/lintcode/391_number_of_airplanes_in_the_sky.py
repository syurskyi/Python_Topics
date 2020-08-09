"""
Definition of Interval.
class Interval(object
    ___ __init__(self, start, end
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    ___ countOfAirplanes(self, airplanes
        ans = 0
        __ not airplanes:
            r_ ans
        cnt = 0
        timeline = []
        ___ interval in airplanes:
            timeline.append((interval.start, 1))
            timeline.append((interval.end, 0))
        timeline.sort()
        ___ _, in_sky in timeline:
            __ in_sky:
                cnt += 1
            ____
                cnt -= 1
            ans = max(ans, cnt)
        r_ ans
