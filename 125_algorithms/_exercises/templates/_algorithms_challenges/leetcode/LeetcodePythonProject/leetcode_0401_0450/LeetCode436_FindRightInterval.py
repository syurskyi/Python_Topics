'''
Created on Apr 16, 2017

@author: MT
'''

# Definition for an interval.
class Interval(object
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e

class Solution(object
    ___ findRightInterval(self, intervals
        sortedList = [(interval.start, i) for i, interval in enumerate(intervals)]
        sortedList.sort()
        result = []
        for i, interval in enumerate(intervals
            ind = self.binary_search(interval.end, sortedList)
            __ ind != i:
                result.append(ind)
            ____
                result.append(-1)
        r_ result
    
    ___ binary_search(self, target, sortedList
        start, end = 0, le.(sortedList)
        w___ start < end:
            mid = (start+end)//2
            __ sortedList[mid][0] < target:
                start = mid+1
            ____
                end = mid
        __ end __ le.(sortedList r_ -1
        r_ sortedList[end][1]
    
    ___ findRightInterval_short(self, intervals
        ______ bisect
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e.end,))
            res.append(l[r][1] __ r < le.(l) else -1)
        r_ res
    
    ___ test(self
        testCases = [
            [ [1,2] ],
            [ [3,4], [2,3], [1,2] ],
            [ [1,4], [2,3], [3,4] ],
        ]
        for intervals in testCases:
            intervals = [Interval(x[0], x[1]) for x in intervals]
            result = self.findRightInterval(intervals)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
