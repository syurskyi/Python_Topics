'''
Created on May 21, 2018

@author: tongq
'''
c_ Solution(object):
    ___ twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = numbers
        i, j = 0, l..(nums)-1
        w.... i < j:
            __ nums[i]+nums[j] __ target:
                r.. [i+1, j+1]
            ____ nums[i]+nums[j] > target:
                j -= 1
            ____:
                i += 1
