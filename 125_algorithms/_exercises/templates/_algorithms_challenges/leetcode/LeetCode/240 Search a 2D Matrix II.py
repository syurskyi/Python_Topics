"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
__author__ = 'Daniel'


class Solution(object
    ___ searchMatrix(self, mat, target
        """
        Manhattan work
        O(m+n) eliminate a row or a column at a time
        Practically: 112 ms

        :type mat: list[int][int]
        :type target: int
        :rtype: bool
        """
        m = le.(mat)
        n = le.(mat[0])

        i = 0
        j = n-1
        w___ i < m and 0 <= j:
            __ mat[i][j] __ target:
                r_ True
            ____ mat[i][j] > target:
                j -= 1
            ____
                i += 1

        r_ False


class SolutionBinSearch(object
    ___ searchMatrix(self, mat, target
        """
        Binary search

        Multiple round of binary search
        possible to swap m and n, depends on the size
        O(m log n) or O(n log m)
        Practically: 204 ms

        :type mat: list[int][int]
        :type target: int
        :rtype: bool
        """
        m = le.(mat)
        n = le.(mat[0])

        col = [mat[i][0] ___ i __ xrange(m)]
        row_by_first = self.bin_search(col, target)

        col = [mat[i][-1] ___ i __ xrange(m)]
        row_by_last = self.bin_search(col, target, False)

        ___ i __ range(row_by_first, row_by_last-1, -1
            col = self.bin_search(mat[i], target)
            __ mat[i][col] __ target:
                r_ True

        r_ False

    ___ bin_search(self, A, t, lower=True
        lo = 0
        hi = le.(A)
        w___ lo < hi:
            mid = (lo+hi)/2
            __ A[mid] __ t:
                r_ mid
            ____ A[mid] < t:
                lo = mid+1
            ____
                hi = mid

        __ lower:
            r_ lo-1
        ____
            r_ lo

__  -n __ "__main__":
    assert Solution().searchMatrix([[1, 4], [2, 5]], 4) __ True
    assert SolutionBinSearch().searchMatrix([[1, 4], [2, 5]], 4) __ True
