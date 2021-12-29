'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    ___ containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        __ t < 0: r.. False
        w = t+1
        hashmap = {}
        ___ i, num __ enumerate(nums):
            m = num//w
            __ m __ hashmap:
                r.. True
            __ m+1 __ hashmap and abs(hashmap[m+1]-num) < w:
                r.. True
            __ m-1 __ hashmap and abs(hashmap[m-1]-num) < w:
                r.. True
            hashmap[m] = num
            __ i>=k:
                del hashmap[nums[i-k]//w]
        r.. False
