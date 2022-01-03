'''
Created on Feb 16, 2017

@author: MT
'''

c_ Solution(object):
    ___ rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        include, exclude = 0, 0
        ___ num __ nums:
            i, e = include, exclude
            include = e+num
            exclude = max(i, e)
        r.. max(include, exclude)
