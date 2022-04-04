#!/usr/bin/python3
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""


c_ Solution:
    ___ findDisappearedNumbers  A
        """
        You can use hash map with extra space O(n).
        To use without extra space, notice the additional constraints that:
            1. 1 ≤ a[i] ≤ n
            2. appear twice or once
        => use original array as storage with a[i] (- 1) as the index
        :type A: List[int]
        :rtype: List[int]
        """
        ___ idx __ r..(l..(A:
            w... T...
                target = A[idx] - 1
                __ idx __ target o. A[idx] __ A[target]:
                    _____ 
                A[idx], A[target] = A[target], A[idx]

        missing    # list
        ___ idx, elm __ e..(A
            __ idx != elm - 1:
                missing.a..(idx + 1)
        r.. missing


__ _______ __ _______
    ... Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) __ [5, 6]
