'''
Created on Mar 4, 2018

@author: tongq
'''
class MyCalendarTwo(object):
    ___ __init__(self):
        self.overlaps = []
        self.calendar = []

    ___ book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlaps:
            __ start < j and end > i:
                return False
        for i, j in self.calendar:
            __ start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True

__ __name__ == '__main__':
    pass
