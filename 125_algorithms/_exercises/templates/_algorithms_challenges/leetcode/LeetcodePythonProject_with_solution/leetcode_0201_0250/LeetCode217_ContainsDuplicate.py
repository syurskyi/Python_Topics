'''
Created on Feb 20, 2017

@author: MT
'''

class Solution(object):
    ___ containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            __ num in s:
                return True
            s.add(num)
        return False