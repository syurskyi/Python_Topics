# -*- coding: utf-8 -*0
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in 
linear time and in O(1) space.
"""
__author__ 'Daniel'
____ c.. _______ d..


c_ Solution:
    ___ majorityElement  nums
        """
        Since majority elements appears more than ⌊ n/3 ⌋ times, there are at most 2 majority number
        :type nums: list[int]
        :rtype: list[int]
        """
        cnt d..(i..)
        ___ num __ nums:
            __ num __ cnt:
                cnt[num] += 1
            ____
                __ l..(cnt) < 3-1:
                    cnt[num] += 1
                ____
                    ___ k __ cnt.k..:
                        cnt[k] -_ 1
                        __ cnt[k] __ 0:
                            del cnt[k]

        ret    # list
        ___ k __ cnt.k..:
            __ l..(f.. l.... x: x __ k, nums > l..(nums)/2:
                ret.a..(k)

        r.. ret

