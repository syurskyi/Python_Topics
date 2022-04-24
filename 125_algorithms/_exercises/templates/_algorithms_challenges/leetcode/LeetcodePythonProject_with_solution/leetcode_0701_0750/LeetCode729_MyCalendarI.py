'''
Created on Mar 4, 2018

@author: tongq
'''
c_ Interval(o..
    ___ - , start, end
        start start
        end end

c_ MyCalendar(o..

    ___ -
        intervals    # list

    ___ book  start, end
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        newInterval Interval(start, end)
        ___ i, interval __ e..(intervals
            __ newInterval.end <_ interval.start:
                intervals.i.. i, newInterval)
                r.. T..
            ____ newInterval.start >_ interval.end:
                _____
            ____
                r.. F..
        intervals.a..(newInterval)
        r.. T..

__ _____ __ _____
    cal MyCalendar()
    print(cal.book(10, 20
    print(cal.book(15, 25
    print(cal.book(20, 30
