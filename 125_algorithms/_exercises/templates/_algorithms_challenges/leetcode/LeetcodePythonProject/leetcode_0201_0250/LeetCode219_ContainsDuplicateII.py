'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object
    ___ containsNearbyDuplicate(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        ___ i, num in enumerate(nums
            __ num not in hashmap or i - hashmap[num] > k:
                hashmap[num] = i
            ____
                r_ True
        r_ False
    