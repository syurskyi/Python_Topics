"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
__author__ = 'Danyang'


c_ Solution(o..
    ___ searchMatrix  mat, target
        """
        binary search. Two exactly the same binary search algorithm
        :param mat: a list of lists of integers
        :param target: an integer
        :return: a boolean
        """
        __ n.. mat:
            r.. F..

        m = l..(mat)
        n = l..(mat[0])

        # binary search
        lo = 0
        hi = m  # [0, m)
        w.... lo < hi:
            mid = (lo+hi)/2
            __ mat[mid][0] __ target:
                r.. T..
            ____ mat[mid][0] < target:
                lo = mid+1
            ____:
                hi = mid

        lst = mat[lo-1]  # <=

        # binary search
        lo = 0
        hi = n  # [0, n)
        w.... lo < hi:
            mid = (lo+hi)/2
            __ lst[mid] __ target:
                r.. T..
            ____ lst[mid] < target:
                lo = mid+1
            ____:
                hi = mid

        r.. F..


__ _______ __ _______
    ... Solution().searchMatrix([[1], [3]], 3) __ T..