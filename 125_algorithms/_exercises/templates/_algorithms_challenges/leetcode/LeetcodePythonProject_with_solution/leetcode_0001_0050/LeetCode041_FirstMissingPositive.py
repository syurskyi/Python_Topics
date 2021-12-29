'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    ___ firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        dp = [0]*n
        ___ num __ nums:
            __ 0 <= num-1 < n:
                dp[num-1] += 1
        ___ i, val __ enumerate(dp):
            __ val __ 0:
                r.. i+1
        r.. l..(nums)+1
