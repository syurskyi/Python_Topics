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


c_ Solution(object):
    ___ searchMatrix  mat, target):
        """
        Manhattan work
        O(m+n) eliminate a row or a column at a time
        Practically: 112 ms

        :type mat: list[int][int]
        :type target: int
        :rtype: bool
        """
        m = l..(mat)
        n = l..(mat[0])

        i = 0
        j = n-1
        w.... i < m a.. 0 <= j:
            __ mat[i][j] __ target:
                r.. T..
            ____ mat[i][j] > target:
                j -= 1
            ____:
                i += 1

        r.. F..


c_ SolutionBinSearch(object):
    ___ searchMatrix  mat, target):
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
        m = l..(mat)
        n = l..(mat[0])

        col = [mat[i][0] ___ i __ xrange(m)]
        row_by_first = bin_search(col, target)

        col = [mat[i][-1] ___ i __ xrange(m)]
        row_by_last = bin_search(col, target, F..)

        ___ i __ r..(row_by_first, row_by_last-1, -1):
            col = bin_search(mat[i], target)
            __ mat[i][col] __ target:
                r.. T..

        r.. F..

    ___ bin_search  A, t, lower=T..):
        lo = 0
        hi = l..(A)
        w.... lo < hi:
            mid = (lo+hi)/2
            __ A[mid] __ t:
                r.. mid
            ____ A[mid] < t:
                lo = mid+1
            ____:
                hi = mid

        __ lower:
            r.. lo-1
        ____:
            r.. lo

__ _______ __ _______
    ... Solution().searchMatrix([[1, 4], [2, 5]], 4) __ T..
    ... SolutionBinSearch().searchMatrix([[1, 4], [2, 5]], 4) __ T..
