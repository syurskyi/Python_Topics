'''
Created on Mar 1, 2017

@author: MT
'''
# Definition for an interval.
c_ Interval(object):
    ___ - , s=0, e=0):
        start = s
        end = e

c_ Solution(object):
    ___ minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        _______ heapq
        intervals.s..(key=l.... x: x.start)
        heap    # list
        maxLen = 0
        ___ interval __ intervals:
            w.... heap a.. heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            maxLen = max(maxLen, l..(heap))
        r.. maxLen
     
    ___ test
        testCases = [
            [[0, 30], [5, 10], [15, 20]],
            [[0, 50], [5, 10], [15, 20], [17, 23], [19, 30]],
            [[13, 15], [0, 13]],
            [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]],
        ]
        ___ intervals __ testCases:
            print('intervals: %s' % (intervals))
            intervals = [Interval(inter[0], inter[1]) ___ inter __ intervals]
            result = minMeetingRooms(intervals)
            print('result: %s' % result)
            print('-='*20+'-')

___ main
    Solution().test()

__ _____ __ _____
    main()

