'''
Created on Mar 7, 2017

@author: MT
'''

class Solution(object):
    ___ findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) > 1:
            slow, fast = nums[0], nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            r.. slow
        r.. -1
    