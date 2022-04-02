'''
Created on Mar 4, 2018

@author: tongq
'''
c_ MyCalendarTwo(o..
    ___ -
        overlaps    # list
        ca__    # list

    ___ book  start, end
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ___ i, j __ overlaps:
            __ start < j a.. end > i:
                r.. F..
        ___ i, j __ ca__:
            __ start < j a.. end > i:
                overlaps.a..((m..(start, i), m..(end, j)))
        ca__.a..((start, end))
        r.. T..

__ _____ __ _____
    p..
