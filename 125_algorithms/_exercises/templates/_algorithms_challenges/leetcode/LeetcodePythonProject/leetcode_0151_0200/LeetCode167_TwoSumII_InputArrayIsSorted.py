'''
Created on May 21, 2018

@author: tongq
'''
class Solution(object
    ___ twoSum(self, numbers, target
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = numbers
        i, j = 0, le.(nums)-1
        w___ i < j:
            __ nums[i]+nums[j] __ target:
                r_ [i+1, j+1]
            ____ nums[i]+nums[j] > target:
                j -= 1
            ____
                i += 1
