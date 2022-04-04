#!/usr/bin/python3
"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you
can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the
memory at once?
"""
____ t___ _______ L..


c_ Solution:
    ___ isToeplitzMatrix  matrix: L..[L..[i..]]) __ b..:
        m, n = l..(matrix), l..(matrix[0])
        ___ i __ r..(1, m
            ___ j __ r..(1, n
                __ matrix[i][j] != matrix[i-1][j-1]:
                    r.. F..

        r.. T..

    ___ isToeplitzMatrix_complex  matrix: L..[L..[i..]]) __ b..:
        """
        Brute force iteration will work

        need a good way to go through the matrix
        """
        m, n = l..(matrix), l..(matrix[0])
        ___ j __ r..(n
            r = 0
            c = j
            cur = matrix[r][c]
            w.... r < m a.. c < n:
                __ cur != matrix[r][c]:
                    r.. F..
                r += 1
                c += 1

        ___ i __ r..(1, m
            r = i
            c = 0
            cur = matrix[r][c]
            w.... r < m a.. c < n:
                __ cur != matrix[r][c]:
                    r.. F..

                r += 1
                c += 1

        r.. T..
