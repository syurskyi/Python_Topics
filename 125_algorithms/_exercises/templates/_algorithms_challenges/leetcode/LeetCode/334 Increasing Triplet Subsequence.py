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
______ sys

__author__ = 'Daniel'


class Solution(object
    ___ increasingTriplet(self, nums
        """
        Brute force: O(N^3)

        dp: O(N)
        :type nums: List[int]
        :rtype: bool
        """
        min1 = sys.maxint
        min2 = sys.maxint
        ___ e in nums:
            __ e < min1:
                min1 = e
            ____ e != min1 and e < min2:
                min2 = e
            ____ e > min2:
                r_ True

        r_ False

    ___ increasingTripletError(self, nums
        """
        use stack
        :type nums: List[int]
        :rtype: bool
        """
        stk = []
        ___ elt in nums:
            w___ stk and stk[-1] >= elt:
                stk.p..

            stk.append(elt)
            __ le.(stk) >= 3:
                r_ True

        r_ False
