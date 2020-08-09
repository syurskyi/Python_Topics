'''
Created on Mar 7, 2017

@author: MT
'''

class Solution(object
    ___ findDuplicate(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ le.(nums) > 1:
            slow, fast = nums[0], nums[nums[0]]
            w___ slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            w___ fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            r_ slow
        r_ -1
    