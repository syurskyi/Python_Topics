'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object):
    ___ numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        __ k <= 1: r.. 0
        prod = 1
        left = 0
        count = 0
        ___ i, num __ enumerate(nums):
            prod *= num
            while left < i+1 and prod >= k:
                prod //= nums[left]
                left += 1
            count += i-left+1
        r.. count
    
    ___ test(self):
        testCases = [
            [
                [10, 5, 2, 6],
                100,
            ],
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.numSubarrayProductLessThanK(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
