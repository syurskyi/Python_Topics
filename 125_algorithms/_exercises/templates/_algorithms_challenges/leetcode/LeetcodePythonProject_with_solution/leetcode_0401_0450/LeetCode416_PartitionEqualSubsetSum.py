'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object):
    ___ canPartition(self, nums):
        sumVal = s..(nums)
        __ sumVal%2 != 0:
            r.. False
        target = sumVal//2
        dp = [False]*(target+1)
        dp[0] = True
        ___ num __ nums:
            ___ i __ r..(target, -1, -1):
                __ i-num >= 0 a.. dp[i-num]:
                    dp[i] = True
        r.. dp[-1]
    
    ___ test(self):
        testCases = [
            [1, 2, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.canPartition(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
