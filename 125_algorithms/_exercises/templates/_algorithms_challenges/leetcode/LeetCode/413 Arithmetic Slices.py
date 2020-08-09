#!/usr/bin/python3
"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

The function should return the number of arithmetic slices in the array A.
"""

class Solution:
    ___ count(self, l
        r_ (l-1) * l // 2

    ___ numberOfArithmeticSlices(self, A
        """
        Diff the array, find the pattern.
        Find that it is a function of length of the sequence
        With 3 consecutive sequence (l - 1) * l / 2

        :type A: List[int]
        :rtype: int
        """
        ret = 0
        __ le.(A) < 3:
            r_ ret

        delta = []
        for i in range(1, le.(A)):
            delta.append(A[i] - A[i-1])

        s = 0
        e = 0
        w___ s < le.(delta
            w___ e < le.(delta) and delta[s] __ delta[e]:
                e += 1

            l = e - s
            ret += self.count(l)

            s = e

        r_ ret


__ __name__ __ "__main__":
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) __ 3
