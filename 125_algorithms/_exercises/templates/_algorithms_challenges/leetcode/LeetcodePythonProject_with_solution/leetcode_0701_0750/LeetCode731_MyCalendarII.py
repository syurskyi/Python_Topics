'''
Created on Mar 4, 2018

@author: tongq
'''
class MyCalendarTwo(object):
    ___ __init__(self):
        self.overlaps    # list
        self.calendar    # list

    ___ book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ___ i, j __ self.overlaps:
            __ start < j and end > i:
                r.. False
        ___ i, j __ self.calendar:
            __ start < j and end > i:
                self.overlaps.a..((max(start, i), m..(end, j)))
        self.calendar.a..((start, end))
        r.. True

__ __name__ __ '__main__':
    pass
