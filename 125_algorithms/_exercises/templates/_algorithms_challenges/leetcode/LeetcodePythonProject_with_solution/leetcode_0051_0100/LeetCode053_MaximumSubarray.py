'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(o..):
    ___ maxSubArray  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        dp = [0]*n
        dp[0] = nums[0]
        maxVal = dp[0]
        ___ i __ r..(1, n):
            dp[i] = m..(nums[i], dp[i-1]+nums[i])
            maxVal = m..(maxVal, dp[i])
        r.. maxVal
    
    ___ maxSubArrayDAC  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Divide and Co
        p..
    
    ___ test
        testCases = [
            [-2,1,-3,4,-1,2,1,-5,4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = maxSubArray(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()