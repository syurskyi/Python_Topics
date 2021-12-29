'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object):
    ___ rob(self, nums):
        __ n.. nums: r.. 0
        __ l..(nums) __ 1: r.. nums[0]
        r.. max(self.robHelper(nums, 0, l..(nums)-2),\
                   self.robHelper(nums, 1, l..(nums)-1))
    
    ___ robHelper(self, nums, lo, hi):
        include, exclude = 0, 0
        ___ i0 __ r..(lo, hi+1):
            i, e = include, exclude
            include = e+nums[i0]
            exclude = max(i, e)
        r.. max(include, exclude)
    
    ___ robSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        __ l..(nums) < 2: r.. nums[0]
        dp0 = [0]*l..(nums)
        dp1 = [0]*l..(nums)
        ___ i __ r..(l..(nums)-1):
            __ i __ 0:
                dp0[i] = nums[0]
            ____ i __ 1:
                dp0[i] = max(nums[i], nums[i-1])
            ____:
                dp0[i] = max(dp0[i-1], dp0[i-2] + nums[i])
        ___ i __ r..(1, l..(nums)):
            __ i __ 1:
                dp1[i] = nums[i]
            ____ i __ 2:
                dp1[i] = max(nums[i], nums[i-1])
            ____:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        r.. max(dp0[-2], dp1[-1])
    
    ___ test(self):
        testCases = [
            [1, 1, 1],
#             [1, 1],
            [1, 2, 3, 9],
            [2, 1, 1, 2]
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.rob(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
