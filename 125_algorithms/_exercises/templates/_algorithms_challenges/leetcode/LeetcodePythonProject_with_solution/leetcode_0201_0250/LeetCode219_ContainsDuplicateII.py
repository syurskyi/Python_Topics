'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    ___ containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        ___ i, num __ e..(nums):
            __ num n.. __ hashmap o. i - hashmap[num] > k:
                hashmap[num] = i
            ____:
                r.. True
        r.. False
    