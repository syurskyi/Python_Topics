'''
Created on Mar 30, 2018

@author: tongq
'''
# Definition for an interval.
class Interval(object
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e

class Solution(object
    ___ employeeFreeTime(self, schedule
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        ______ heapq
        heap = []
        ___ arr in schedule:
            ___ inter in arr:
                heapq.heappush(heap, [inter.start, inter.end])
        temp = heapq.heappop(heap)
        res = []
        w___ heap:
            __ temp[1] < heap[0][0]:
                res.append(Interval(temp[1], heap[0][0]))
                temp = heapq.heappop(heap)
            ____
                __ temp[1] < heap[0][1]:
                    temp = heap[0]
                heapq.heappop(heap) 
        r_ res
    
    ___ test(self
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
        ___ schedule in testCases:
            print('schedule: %s' % schedule)
            arr = []
            ___ arr0 in schedule:
                arr.append([Interval(inter[0], inter[1]) ___ inter in arr0])
            schedule = arr
            result = self.employeeFreeTime(schedule)
            res = [[inter.start, inter.end] ___ inter in result]
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
