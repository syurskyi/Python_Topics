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
        self.intervals = []
    
    ___ addNum(self, val):
        __ not self.intervals:
            self.intervals.append(Interval(val, val))
        else:
            result = []
            newInterval = Interval(val, val)
            for interval in self.intervals:
                __ newInterval.end < interval.start-1:
                    result.append(newInterval)
                    newInterval = interval
                elif newInterval.start <= interval.end+1:
                    newInterval = Interval(min(interval.start, newInterval.start),\
                        max(interval.end, newInterval.end))
                else:
                    result.append(interval)
            result.append(newInterval)
            self.intervals = result
    
    ___ getIntervals(self):
        return self.intervals
