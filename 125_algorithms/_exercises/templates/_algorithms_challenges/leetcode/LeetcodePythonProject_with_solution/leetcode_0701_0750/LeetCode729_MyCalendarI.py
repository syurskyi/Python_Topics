'''
Created on Mar 4, 2018

@author: tongq
'''
c_ Interval(object):
    ___ - , start, end):
        start = start
        end = end

c_ MyCalendar(object):

    ___ - ):
        intervals    # list

    ___ book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        newInterval = Interval(start, end)
        ___ i, interval __ e..(intervals):
            __ newInterval.end <= interval.start:
                intervals.insert(i, newInterval)
                r.. T..
            ____ newInterval.start >= interval.end:
                _____
            ____:
                r.. F..
        intervals.a..(newInterval)
        r.. T..

__ _____ __ _____
    cal = MyCalendar()
    print(cal.book(10, 20))
    print(cal.book(15, 25))
    print(cal.book(20, 30))
