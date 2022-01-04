'''
Created on Apr 12, 2017

@author: MT
'''

c_ Solution(object):
    ___ canPartition(self, nums):
        sumVal = s..(nums)
        __ sumVal%2 != 0:
            r.. F..
        target = sumVal//2
        dp = [F..]*(target+1)
        dp[0] = T..
        ___ num __ nums:
            ___ i __ r..(target, -1, -1):
                __ i-num >= 0 a.. dp[i-num]:
                    dp[i] = T..
        r.. dp[-1]
    
    ___ test
        testCases = [
            [1, 2, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = canPartition(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
