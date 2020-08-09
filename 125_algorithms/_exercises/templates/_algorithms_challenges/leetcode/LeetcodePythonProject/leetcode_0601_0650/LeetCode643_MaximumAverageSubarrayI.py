'''
Created on Sep 27, 2017

@author: MT
'''
class Solution(object
    ___ findMaxAverage(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        __ k <= 0: r_ 0
        sumVal = 0
        maxVal = float('-inf')
        for i, num in enumerate(nums
            sumVal += num
            __ i >= k-1:
                maxVal = max(maxVal, sumVal)
                sumVal -= nums[i-k+1]
        r_ float(maxVal)/k
    
    ___ test(self
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
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.findMaxAverage(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
