'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object
    ___ firstMissingPositive(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n = le.(nums)
        dp = [0]*n
        for num in nums:
            __ 0 <= num-1 < n:
                dp[num-1] += 1
        for i, val in enumerate(dp
            __ val __ 0:
                r_ i+1
        r_ le.(nums)+1
