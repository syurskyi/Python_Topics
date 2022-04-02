#!/usr/bin/python3
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


c_ Solution:
    ___ idx  a
        r.. a - 1

    ___ findDuplicates  A
        """
        Normally: hashmap
        Without extra space
        Extra constraint: 1 ≤ a[i] ≤ n

        :type A: List[int]
        :rtype: List[int]
        """
        ___ i __ r..(l..(A)):
            t = idx(A[i])
            w.... i != t:
                __ A[i] __ A[t]:
                    _____
                ____:
                    A[i], A[t] = A[t], A[i]
                    t = idx(A[i])

        ret    # list
        ___ i __ r..(l..(A)):
            __ idx(A[i]) != i:
                ret.a..(A[i])

        r.. ret


__ _______ __ _______
    ... s..(Solution().findDuplicates([4,3,2,7,8,2,3,1])) __ s..([2,3])
