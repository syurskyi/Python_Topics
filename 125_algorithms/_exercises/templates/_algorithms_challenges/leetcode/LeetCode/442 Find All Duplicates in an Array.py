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


class Solution:
    ___ idx(self, a
        r_ a - 1

    ___ findDuplicates(self, A
        """
        Normally: hashmap
        Without extra space
        Extra constraint: 1 ≤ a[i] ≤ n

        :type A: List[int]
        :rtype: List[int]
        """
        ___ i __ range(le.(A)):
            t = self.idx(A[i])
            w___ i != t:
                __ A[i] __ A[t]:
                    break
                ____
                    A[i], A[t] = A[t], A[i]
                    t = self.idx(A[i])

        ret =   # list
        ___ i __ range(le.(A)):
            __ self.idx(A[i]) != i:
                ret.append(A[i])

        r_ ret


__  -n __ "__main__":
    assert set(Solution().findDuplicates([4,3,2,7,8,2,3,1])) __ set([2,3])
