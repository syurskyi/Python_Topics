'''
Created on Jun 6, 2018

@author: tongq
'''
c_ Solution(o..
    ___ firstMissingPositive  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        dp = [0]*n
        ___ num __ nums:
            __ 0 <_ num-1 < n:
                dp[num-1] += 1
        ___ i, val __ e..(dp
            __ val __ 0:
                r.. i+1
        r.. l..(nums)+1
