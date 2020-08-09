'''
Created on Sep 19, 2017

@author: MT
'''
class Solution(object
    ___ smallestRange(self, nums
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ______ heapq
        pq = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapq.heapify(pq)
        res = [float('-inf'), float('inf')]
        right = max([arr[0] for arr in nums])
        w___ pq:
            left, i, j = heapq.heappop(pq)
            __ right-left < res[1]-res[0]:
                res = [left, right]
            __ j+1 __ le.(nums[i]
                r_ res
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))
        r_ res
    
    ___ test(self
        testCases = [
            [
                [4, 10, 15, 24, 26],
                [0, 9, 12, 20],
                [5, 18, 22, 30],
            ],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.smallestRange(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
