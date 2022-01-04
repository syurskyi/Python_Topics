'''
Created on Sep 19, 2017

@author: MT
'''
c_ Solution(object):
    ___ smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        _______ heapq
        pq = [(arr[0], i, 0) ___ i, arr __ e..(nums)]
        heapq.heapify(pq)
        res = [float('-inf'), float('inf')]
        right = max([arr[0] ___ arr __ nums])
        w.... pq:
            left, i, j = heapq.heappop(pq)
            __ right-left < res[1]-res[0]:
                res = [left, right]
            __ j+1 __ l..(nums[i]):
                r.. res
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))
        r.. res
    
    ___ test
        testCases = [
            [
                [4, 10, 15, 24, 26],
                [0, 9, 12, 20],
                [5, 18, 22, 30],
            ],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = smallestRange(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
