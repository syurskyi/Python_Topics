'''
Created on Mar 4, 2018

@author: tongq
'''
class Interval(object):
    ___ __init__(self, start, end):
        self.start = start
        self.end = end

class MyCalendar(object):

    ___ __init__(self):
        self.intervals    # list

    ___ book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        newInterval = Interval(start, end)
        ___ i, interval __ e..(self.intervals):
            __ newInterval.end <= interval.start:
                self.intervals.insert(i, newInterval)
                r.. True
            ____ newInterval.start >= interval.end:
                continue
            ____:
                r.. False
        self.intervals.a..(newInterval)
        r.. True

__ __name__ __ '__main__':
    cal = MyCalendar()
    print(cal.book(10, 20))
    print(cal.book(15, 25))
    print(cal.book(20, 30))
