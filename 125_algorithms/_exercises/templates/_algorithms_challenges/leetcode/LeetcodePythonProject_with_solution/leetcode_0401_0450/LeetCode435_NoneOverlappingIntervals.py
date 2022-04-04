'''
Created on Apr 15, 2017

@author: MT
'''

# Definition for an interval.
c_ Interval(o..
    ___ - , s=0, e=0
        start = s
        end = e

c_ Solution(o..
    ___ eraseOverlapIntervals  intervals
        __ n.. intervals: r.. 0
        intervals.s..(key=l.... x: (x.end, x.start
        maxLen = intervals[0].end
        count = 0
        ___ i __ r..(1, l..(intervals:
            __ intervals[i].start >_ maxLen:
                maxLen = intervals[i].end
            ____
                count += 1
        r.. count
    
    ___ test
        testCases = [
            [[1, 2], [2, 3], [3, 4], [1, 3]],
            [[1, 2], [1, 2], [1, 2]],
            [[1, 2], [2, 3]],
        ]
        ___ intervals __ testCases:
            print('intervals: %s' % intervals)
            intervals = [Interval(interval[0], interval[1]) ___ interval __ intervals]
            result = eraseOverlapIntervals(intervals)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
