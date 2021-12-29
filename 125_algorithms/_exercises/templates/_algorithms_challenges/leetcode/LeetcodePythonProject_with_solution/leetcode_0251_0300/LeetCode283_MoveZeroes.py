'''
Created on Mar 6, 2017

@author: MT
'''

class Solution(object):
    ___ moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        ___ num __ nums:
            __ num != 0:
                nums[j] = num
                j+=1
        ___ i __ r..(j, l..(nums)):
            nums[i] = 0
