'''
Created on Mar 22, 2017

@author: MT
'''
class Interval(object):
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):
    ___ __init__(self):
        self.intervals    # list
    
    ___ addNum(self, val):
        __ n.. self.intervals:
            self.intervals.a..(Interval(val, val))
        ____:
            result    # list
            newInterval = Interval(val, val)
            ___ interval __ self.intervals:
                __ newInterval.end < interval.start-1:
                    result.a..(newInterval)
                    newInterval = interval
                ____ newInterval.start <= interval.end+1:
                    newInterval = Interval(m..(interval.start, newInterval.start),\
                        max(interval.end, newInterval.end))
                ____:
                    result.a..(interval)
            result.a..(newInterval)
            self.intervals = result
    
    ___ getIntervals(self):
        r.. self.intervals
