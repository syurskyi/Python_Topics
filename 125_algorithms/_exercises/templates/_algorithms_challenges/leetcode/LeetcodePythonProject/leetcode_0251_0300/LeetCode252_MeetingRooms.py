'''
Created on Mar 1, 2017

@author: MT
'''

# Definition for an interval.
class Interval(object
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e

class Solution(object
    ___ canAttendMeetings(self, intervals
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)
        length = le.(intervals)
        for i in range(length-1
            curr = intervals[i]
            nextInter = intervals[i+1]
            __ curr.end > nextInter.start:
                r_ False
        r_ True
