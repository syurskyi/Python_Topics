'''
Created on Mar 1, 2017

@author: MT
'''
# Definition for an interval.
class Interval(object):
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    ___ minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        _______ heapq
        intervals.sort(key=l.... x: x.start)
        heap    # list
        maxLen = 0
        ___ interval __ intervals:
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            maxLen = max(maxLen, l..(heap))
        r.. maxLen
     
    ___ test(self):
        testCases = [
            [[0, 30], [5, 10], [15, 20]],
            [[0, 50], [5, 10], [15, 20], [17, 23], [19, 30]],
            [[13, 15], [0, 13]],
            [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]],
        ]
        ___ intervals __ testCases:
            print('intervals: %s' % (intervals))
            intervals = [Interval(inter[0], inter[1]) ___ inter __ intervals]
            result = self.minMeetingRooms(intervals)
            print('result: %s' % result)
            print('-='*20+'-')

___ main():
    Solution().test()

__ __name__ __ '__main__':
    main()

