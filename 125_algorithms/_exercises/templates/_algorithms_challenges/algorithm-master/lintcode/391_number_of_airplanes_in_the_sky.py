"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    ___ countOfAirplanes(self, airplanes):
        ans = 0
        __ n.. airplanes:
            r.. ans
        cnt = 0
        timeline    # list
        ___ interval __ airplanes:
            timeline.a..((interval.start, 1))
            timeline.a..((interval.end, 0))
        timeline.s..()
        ___ _, in_sky __ timeline:
            __ in_sky:
                cnt += 1
            ____:
                cnt -= 1
            ans = max(ans, cnt)
        r.. ans
