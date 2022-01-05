'''
Created on Feb 16, 2017

@author: MT
'''

c_ Solution(o..):
    ___ rob  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        include, exclude = 0, 0
        ___ num __ nums:
            i, e = include, exclude
            include = e+num
            exclude = m..(i, e)
        r.. m..(include, exclude)
