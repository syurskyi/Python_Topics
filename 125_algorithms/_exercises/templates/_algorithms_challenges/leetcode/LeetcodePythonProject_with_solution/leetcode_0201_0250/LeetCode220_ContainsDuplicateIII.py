'''
Created on Feb 20, 2017

@author: MT
'''
c_ Solution(object):
    ___ containsNearbyAlmostDuplicate  nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        __ t < 0: r.. F..
        w = t+1
        hashmap    # dict
        ___ i, num __ e..(nums):
            m = num//w
            __ m __ hashmap:
                r.. T..
            __ m+1 __ hashmap a.. abs(hashmap[m+1]-num) < w:
                r.. T..
            __ m-1 __ hashmap a.. abs(hashmap[m-1]-num) < w:
                r.. T..
            hashmap[m] = num
            __ i>=k:
                del hashmap[nums[i-k]//w]
        r.. F..
