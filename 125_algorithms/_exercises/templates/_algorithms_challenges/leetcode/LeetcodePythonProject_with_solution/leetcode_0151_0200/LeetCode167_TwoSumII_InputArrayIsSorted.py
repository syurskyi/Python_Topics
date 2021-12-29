'''
Created on May 21, 2018

@author: tongq
'''
class Solution(object):
    ___ twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = numbers
        i, j = 0, len(nums)-1
        while i < j:
            __ nums[i]+nums[j] == target:
                return [i+1, j+1]
            elif nums[i]+nums[j] > target:
                j -= 1
            else:
                i += 1
