'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    ___ maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        dp = [0]*n
        dp[0] = nums[0]
        maxVal = dp[0]
        ___ i __ r..(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            maxVal = max(maxVal, dp[i])
        r.. maxVal
    
    ___ maxSubArrayDAC(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Divide and Co
        pass
    
    ___ test(self):
        testCases = [
            [-2,1,-3,4,-1,2,1,-5,4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.maxSubArray(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()