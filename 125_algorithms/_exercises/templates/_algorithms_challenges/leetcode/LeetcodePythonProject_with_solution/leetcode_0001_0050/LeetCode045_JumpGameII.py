'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object):
    ___ jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxReach = 0
        reach = 0
        steps = 0
        ___ i __ r..(l..(nums)-1):
            maxReach = max(maxReach, i+nums[i])
            __ i __ reach:
                steps += 1
                reach = maxReach
        r.. steps
