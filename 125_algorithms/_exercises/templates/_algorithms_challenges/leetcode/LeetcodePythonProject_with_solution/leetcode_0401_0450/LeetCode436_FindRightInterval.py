'''
Created on Apr 16, 2017

@author: MT
'''

# Definition for an interval.
c_ Interval(object):
    ___ - , s=0, e=0):
        start = s
        end = e

c_ Solution(object):
    ___ findRightInterval(self, intervals):
        sortedList = [(interval.start, i) ___ i, interval __ e..(intervals)]
        sortedList.s..()
        result    # list
        ___ i, interval __ e..(intervals):
            ind = binary_search(interval.end, sortedList)
            __ ind != i:
                result.a..(ind)
            ____:
                result.a..(-1)
        r.. result
    
    ___ binary_search(self, target, sortedList):
        start, end = 0, l..(sortedList)
        w.... start < end:
            mid = (start+end)//2
            __ sortedList[mid][0] < target:
                start = mid+1
            ____:
                end = mid
        __ end __ l..(sortedList): r.. -1
        r.. sortedList[end][1]
    
    ___ findRightInterval_short(self, intervals):
        _______ bisect
        l = s..((e.start, i) ___ i, e __ e..(intervals))
        res    # list
        ___ e __ intervals:
            r = bisect.bisect_left(l, (e.end,))
            res.a..(l[r][1] __ r < l..(l) ____ -1)
        r.. res
    
    ___ test
        testCases = [
            [ [1,2] ],
            [ [3,4], [2,3], [1,2] ],
            [ [1,4], [2,3], [3,4] ],
        ]
        ___ intervals __ testCases:
            intervals = [Interval(x[0], x[1]) ___ x __ intervals]
            result = findRightInterval(intervals)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
