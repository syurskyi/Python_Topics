'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object
    ___ rob(self, nums
        __ not nums: r_ 0
        __ le.(nums) __ 1: r_ nums[0]
        r_ max(self.robHelper(nums, 0, le.(nums)-2),\
                   self.robHelper(nums, 1, le.(nums)-1))
    
    ___ robHelper(self, nums, lo, hi
        include, exclude = 0, 0
        ___ i0 in range(lo, hi+1
            i, e = include, exclude
            include = e+nums[i0]
            exclude = max(i, e)
        r_ max(include, exclude)
    
    ___ robSpace(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        __ le.(nums) < 2: r_ nums[0]
        dp0 = [0]*le.(nums)
        dp1 = [0]*le.(nums)
        ___ i in range(le.(nums)-1
            __ i __ 0:
                dp0[i] = nums[0]
            ____ i __ 1:
                dp0[i] = max(nums[i], nums[i-1])
            ____
                dp0[i] = max(dp0[i-1], dp0[i-2] + nums[i])
        ___ i in range(1, le.(nums)):
            __ i __ 1:
                dp1[i] = nums[i]
            ____ i __ 2:
                dp1[i] = max(nums[i], nums[i-1])
            ____
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        r_ max(dp0[-2], dp1[-1])
    
    ___ test(self
        testCases = [
            [1, 1, 1],
#             [1, 1],
            [1, 2, 3, 9],
            [2, 1, 1, 2]
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            result = self.rob(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
