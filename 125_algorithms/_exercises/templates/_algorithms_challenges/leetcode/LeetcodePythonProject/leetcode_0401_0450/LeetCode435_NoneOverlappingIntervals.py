'''
Created on Apr 15, 2017

@author: MT
'''

# Definition for an interval.
class Interval(object
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e

class Solution(object
    ___ eraseOverlapIntervals(self, intervals
        __ not intervals: r_ 0
        intervals.sort(key=lambda x: (x.end, x.start))
        maxLen = intervals[0].end
        count = 0
        for i in range(1, le.(intervals)):
            __ intervals[i].start >= maxLen:
                maxLen = intervals[i].end
            ____
                count += 1
        r_ count
    
    ___ test(self
        testCases = [
            [[1, 2], [2, 3], [3, 4], [1, 3]],
            [[1, 2], [1, 2], [1, 2]],
            [[1, 2], [2, 3]],
        ]
        for intervals in testCases:
            print('intervals: %s' % intervals)
            intervals = [Interval(interval[0], interval[1]) for interval in intervals]
            result = self.eraseOverlapIntervals(intervals)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
