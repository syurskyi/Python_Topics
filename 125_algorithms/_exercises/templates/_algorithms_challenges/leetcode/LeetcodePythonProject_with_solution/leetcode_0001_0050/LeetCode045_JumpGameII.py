'''
Created on Jun 5, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ jump  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxReach = 0
        reach = 0
        steps = 0
        ___ i __ r..(l..(nums)-1):
            maxReach = m..(maxReach, i+nums[i])
            __ i __ reach:
                steps += 1
                reach = maxReach
        r.. steps
