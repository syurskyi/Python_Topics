'''
Created on Sep 27, 2017

@author: MT
'''
c_ Solution(object):
    ___ findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        __ k <= 0: r.. 0
        sumVal = 0
        maxVal = float('-inf')
        ___ i, num __ e..(nums):
            sumVal += num
            __ i >= k-1:
                maxVal = max(maxVal, sumVal)
                sumVal -= nums[i-k+1]
        r.. float(maxVal)/k
    
    ___ test
        testCases = [
            [
                [1, 12, -5, -6, 50, 3],
                4,
            ],
            [
                [3, 3, 4, 3, 0],
                3,
            ],
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = findMaxAverage(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
