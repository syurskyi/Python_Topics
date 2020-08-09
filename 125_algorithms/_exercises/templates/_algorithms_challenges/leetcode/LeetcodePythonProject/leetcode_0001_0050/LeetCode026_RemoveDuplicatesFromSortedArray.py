'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object
    ___ removeDuplicates(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        ___ i, num in enumerate(nums
            __ i __ 0 or nums[i-1] != num:
                nums[j] = num
                j += 1
        r_ j
