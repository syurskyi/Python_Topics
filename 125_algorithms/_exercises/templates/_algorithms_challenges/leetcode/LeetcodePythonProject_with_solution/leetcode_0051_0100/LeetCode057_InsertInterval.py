'''
Created on Jan 21, 2017

@author: MT
'''

# Definition for an interval.
c_ Interval(object):
    ___ - , s=0, e=0):
        start = s
        end = e
    
    ___ __str__
        r.. '<s: %s, e: %s>' % (start, end)
    
    ___ __repr__
        r.. __str__()

c_ Solution(object):
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
    
    ___ test
        testCases = [
            ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]),
            ([[1,2],[3,5],[6,7],[8,10],[12,16],[15,23]], [4,9]),
            ([[1,2],[2,5],[6,7],[8,10],[12,16],[15,23]], [7,9]),
        ]
        ___ intervals, newInterval __ testCases:
            intervals = [Interval(x[0], x[1]) ___ x __ intervals]
            newInterval = Interval(newInterval[0], newInterval[1])
            print('intervals: %s' % (intervals))
            result = insert(intervals, newInterval)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()