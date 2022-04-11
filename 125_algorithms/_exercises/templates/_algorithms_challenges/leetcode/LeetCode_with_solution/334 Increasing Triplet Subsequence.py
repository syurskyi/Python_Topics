"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
_______ ___

__author__ 'Daniel'


c_ Solution(o..
    ___ increasingTriplet  nums
        """
        Brute force: O(N^3)

        dp: O(N)
        :type nums: List[int]
        :rtype: bool
        """
        min1 ___.maxint
        min2 ___.maxint
        ___ e __ nums:
            __ e < min1:
                min1 e
            ____ e != min1 a.. e < min2:
                min2 e
            ____ e > min2:
                r.. T..

        r.. F..

    ___ increasingTripletError  nums
        """
        use stack
        :type nums: List[int]
        :rtype: bool
        """
        stk    # list
        ___ elt __ nums:
            w.... stk a.. stk[-1] >_ elt:
                stk.p.. )

            stk.a..(elt)
            __ l..(stk) >_ 3:
                r.. T..

        r.. F..
