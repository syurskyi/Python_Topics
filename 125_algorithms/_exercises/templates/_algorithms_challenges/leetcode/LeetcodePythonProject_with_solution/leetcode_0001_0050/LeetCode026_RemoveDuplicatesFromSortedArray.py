'''
Created on Nov 2, 2017

@author: MT
'''
c_ Solution(object):
    ___ removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        ___ i, num __ e..(nums):
            __ i __ 0 o. nums[i-1] != num:
                nums[j] = num
                j += 1
        r.. j
