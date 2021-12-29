'''
Created on Jan 21, 2017

@author: MT
'''

# Definition for an interval.
class Interval(object):
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    ___ __str__(self):
        r.. '<s: %s, e: %s>' % (self.start, self.end)
    
    ___ __repr__(self):
        r.. self.__str__()

class Solution(object):
    ___ insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result    # list
        ___ interval __ intervals:
            __ interval.end < newInterval.start:
                result.a..(interval)
            ____ interval.start > newInterval.end:
                result.a..(newInterval)
                newInterval = interval
            ____ interval.end >= newInterval.start o. interval.start <= newInterval.end:
                newInterval = Interval(\
                    m..(newInterval.start, interval.start),\
                    max(newInterval.end, interval.end))
        result.a..(newInterval)
        r.. result
    
    ___ test(self):
        testCases = [
            ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]),
            ([[1,2],[3,5],[6,7],[8,10],[12,16],[15,23]], [4,9]),
            ([[1,2],[2,5],[6,7],[8,10],[12,16],[15,23]], [7,9]),
        ]
        ___ intervals, newInterval __ testCases:
            intervals = [Interval(x[0], x[1]) ___ x __ intervals]
            newInterval = Interval(newInterval[0], newInterval[1])
            print('intervals: %s' % (intervals))
            result = self.insert(intervals, newInterval)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()