"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
__author__ 'Daniel'
_______ h__
____ c.. _______ d..


c_ Solution:
    ___ containsNearbyDuplicate  nums, k
        """
        hash with heap

        :rtype: bool
        """
        d d.. l..
        ___ i, v __ e..(nums
            h__.heappush(d[v], i)

        ___ v __ d.v..
            __ l..(v) > 1:
                pre h__.heappop(v)
                w.... v:
                    cur h__.heappop(v)
                    __ cur-pre <_ k:
                        r.. T..
                    pre cur

        r.. F..