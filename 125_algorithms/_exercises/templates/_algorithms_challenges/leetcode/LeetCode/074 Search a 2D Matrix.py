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


class Solution(object
    ___ searchMatrix(self, mat, target
        """
        binary search. Two exactly the same binary search algorithm
        :param mat: a list of lists of integers
        :param target: an integer
        :return: a boolean
        """
        __ not mat:
            r_ False

        m = le.(mat)
        n = le.(mat[0])

        # binary search
        lo = 0
        hi = m  # [0, m)
        w___ lo < hi:
            mid = (lo+hi)/2
            __ mat[mid][0] __ target:
                r_ True
            ____ mat[mid][0] < target:
                lo = mid+1
            ____
                hi = mid

        lst = mat[lo-1]  # <=

        # binary search
        lo = 0
        hi = n  # [0, n)
        w___ lo < hi:
            mid = (lo+hi)/2
            __ lst[mid] __ target:
                r_ True
            ____ lst[mid] < target:
                lo = mid+1
            ____
                hi = mid

        r_ False


__ __name__ __ "__main__":
    assert Solution().searchMatrix([[1], [3]], 3) __ True