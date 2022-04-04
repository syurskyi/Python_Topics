#!/usr/bin/python3
"""
Given a sorted array, two integers k and x, find the k closest elements to x in
the array. The result should also be sorted in ascending order. If there is a
tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""
____ t___ _______ L..
____ bisect _______ bisect_left
____ c.. _______ d..


c_ Solution:
    ___ findClosestElements  A: L..[i..], k: i.., x: i..) __ L..[i..]:
        """
        binary search without two pointers scanning
        """
        n = l..(A)
        lo = 0
        hi = n - k
        w.... lo < hi:
            mid = (lo + hi) // 2
            __ a..(x - A[mid]) > a..(A[mid + k] - x
                # better to have A[mid+k] rather than A[mid]
                lo = mid + 1
            ____
                hi = mid

        r.. A[lo:lo+k]

    ___ findClosestElements2  A: L..[i..], k: i.., x: i..) __ L..[i..]:
        """
        input sorted arrya
        two pointers
        """
        n = l..(A)
        idx = bisect_left(A, x)
        ret = d..()
        i = idx - 1
        j = idx
        w.... k:
            __ 0 <_ i < n a.. 0 <_ j < n:
                __ a..(A[i] - x) <_ a..(A[j] - x
                    ret.appendleft(A[i])
                    i -= 1
                ____
                    ret.a..(A[j])
                    j += 1
            ____ 0 <_ i < n:
                ret.appendleft(A[i])
                i -= 1
            ____ 0 <_ j < n:
                ret.a..(A[j])
                j += 1
            ____
                r..

            k -= 1

        r.. l..(ret)


__ _______ __ _______
    ... Solution().findClosestElements([1,2,3,4,5], 4, 3) __ [1,2,3,4]
    ... Solution().findClosestElements([1,2,3,4,5], 4, -1) __ [1,2,3,4]
