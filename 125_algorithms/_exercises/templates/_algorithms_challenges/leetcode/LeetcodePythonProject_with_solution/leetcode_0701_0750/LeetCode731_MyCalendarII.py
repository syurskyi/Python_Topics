'''
Created on Mar 4, 2018

@author: tongq
'''
c_ MyCalendarTwo(object):
    ___ - ):
        overlaps    # list
        calendar    # list

    ___ book  start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ___ i, j __ overlaps:
            __ start < j a.. end > i:
                r.. F..
        ___ i, j __ calendar:
            __ start < j a.. end > i:
                overlaps.a..((m..(start, i), m..(end, j)))
        calendar.a..((start, end))
        r.. T..

__ _____ __ _____
    p..
