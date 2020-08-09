'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object
    ___ rob(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        include, exclude = 0, 0
        ___ num in nums:
            i, e = include, exclude
            include = e+num
            exclude = max(i, e)
        r_ max(include, exclude)
