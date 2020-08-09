'''
Created on Feb 20, 2017

@author: MT
'''

class Solution(object
    ___ containsDuplicate(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        ___ num in nums:
            __ num in s:
                r_ True
            s.add(num)
        r_ False