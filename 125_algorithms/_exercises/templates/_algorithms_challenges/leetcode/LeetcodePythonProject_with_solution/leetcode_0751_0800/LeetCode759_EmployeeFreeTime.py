'''
Created on Mar 30, 2018

@author: tongq
'''
# Definition for an interval.
class Interval(object):
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    ___ employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        _______ heapq
        heap    # list
        ___ arr __ schedule:
            ___ inter __ arr:
                heapq.heappush(heap, [inter.start, inter.end])
        temp = heapq.heappop(heap)
        res    # list
        while heap:
            __ temp[1] < heap[0][0]:
                res.a..(Interval(temp[1], heap[0][0]))
                temp = heapq.heappop(heap)
            ____:
                __ temp[1] < heap[0][1]:
                    temp = heap[0]
                heapq.heappop(heap) 
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [[1,2],[5,6]],
                [[1,3]],[[4,10]],
            ],
            [
                [[1,3],[6,7]],[[2,4]],
                [[2,5],[9,12]],
            ],
        ]
        ___ schedule __ testCases:
            print('schedule: %s' % schedule)
            arr    # list
            ___ arr0 __ schedule:
                arr.a..([Interval(inter[0], inter[1]) ___ inter __ arr0])
            schedule = arr
            result = self.employeeFreeTime(schedule)
            res = [[inter.start, inter.end] ___ inter __ result]
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
