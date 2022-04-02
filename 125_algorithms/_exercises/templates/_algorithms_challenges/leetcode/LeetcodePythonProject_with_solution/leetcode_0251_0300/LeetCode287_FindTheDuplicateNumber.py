'''
Created on Mar 7, 2017

@author: MT
'''

c_ Solution(o..
    ___ findDuplicate  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) > 1:
            slow, fast = nums[0], nums[nums[0]]
            w.... slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            w.... fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            r.. slow
        r.. -1
    