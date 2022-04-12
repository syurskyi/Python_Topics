'''
Created on Jan 24, 2017

@author: MT
'''

c_ Solution(o..
    ___ removeDuplicates  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) <_ 2:
            r.. l..(nums)
        prev, curr 1, 2
        w.... curr < l..(nums
            __ nums[curr] !_ nums[prev] o. nums[curr] !_ nums[prev-1]:
                prev += 1
                nums[prev] nums[curr]
            curr += 1
        r.. prev + 1
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()
