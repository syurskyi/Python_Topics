'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object
    ___ containsNearbyAlmostDuplicate(self, nums, k, t
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        __ t < 0: r_ False
        w = t+1
        hashmap = {}
        ___ i, num in enumerate(nums
            m = num//w
            __ m in hashmap:
                r_ True
            __ m+1 in hashmap and abs(hashmap[m+1]-num) < w:
                r_ True
            __ m-1 in hashmap and abs(hashmap[m-1]-num) < w:
                r_ True
            hashmap[m] = num
            __ i>=k:
                del hashmap[nums[i-k]//w]
        r_ False
