'''
Created on Mar 1, 2017

@author: MT
'''

# Definition for an interval.
c_ Interval(o..
    ___ - , s=0, e=0
        start = s
        end = e

c_ Solution(o..
    ___ canAttendMeetings  intervals
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.s..(key=l.... x: x.start)
        length = l..(intervals)
        ___ i __ r..(length-1
            curr = intervals[i]
            nextInter = intervals[i+1]
            __ curr.end > nextInter.start:
                r.. F..
        r.. T..
