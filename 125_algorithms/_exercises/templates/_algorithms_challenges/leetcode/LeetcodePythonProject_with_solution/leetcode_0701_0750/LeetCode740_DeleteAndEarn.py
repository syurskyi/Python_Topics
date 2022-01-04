'''
Created on Mar 14, 2018

@author: tongq
'''
c_ Solution(object):
    ___ deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]*10001
        ___ num __ nums:
            count[num] += num
        dp = [0]*10003
        ___ i __ r..(10000, -1, -1):
            dp[i] = max(count[i]+dp[i+2], dp[i+1])
        r.. dp[0]
    
    ___ test
        testCases = [
            [3, 4, 2],
            [2, 2, 3, 3, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = deleteAndEarn(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
