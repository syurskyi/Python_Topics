'''
Created on Mar 22, 2017

@author: MT
'''
c_ Interval(o..):
    ___ - , s=0, e=0):
        start = s
        end = e

c_ SummaryRanges(o..):
    ___ - ):
        intervals    # list
    
    ___ addNum  val):
        __ n.. intervals:
            intervals.a..(Interval(val, val))
        ____:
            result    # list
            newInterval = Interval(val, val)
            ___ interval __ intervals:
                __ newInterval.end < interval.start-1:
                    result.a..(newInterval)
                    newInterval = interval
                ____ newInterval.start <= interval.end+1:
                    newInterval = Interval(m..(interval.start, newInterval.start),\
                        m..(interval.end, newInterval.end))
                ____:
                    result.a..(interval)
            result.a..(newInterval)
            intervals = result
    
    ___ getIntervals
        r.. intervals
