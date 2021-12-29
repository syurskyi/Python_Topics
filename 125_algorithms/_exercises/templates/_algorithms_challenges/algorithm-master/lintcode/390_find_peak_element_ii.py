"""
Test Case

[[  1,  2,  3,  6,  5 ]
,[ 16, 41, 23, 22,  6 ]
,[ 15, 17, 24, 21,  7 ]
,[ 14, 18, 19, 20, 10 ]
,[ 13, 14, 11, 10,  9 ]]

[[  1,  3,  2 ]
,[  4,  6,  5 ]
,[  7,  9,  8 ]
,[ 13, 15, 14 ]
,[ 10, 12, 11 ]]
"""

class Solution:
    NULL_POS = [-1, -1]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    """
    step0/ given matrix and its size is 6*6
    step1/ chosen the mid_col is 3, the max_value on that col at (2, 3),
           and the value at (2, 2) great than it
    step2/ chosen the mid_row is 2, the max_value in the segment[0:3] on that row at (2, 1),
           and the value at (3, 1) great than it
    step3/ keep slicing row or col if its range is more wide
    ...
    step-1/ find a square and check the vertices
    """
    ___ findPeakII(self, A):
        __ n.. A:
            r.. self.NULL_POS

        self.m, self.n = l..(A), l..(A[0])
        left, col, right = 0, 0, self.n - 1
        up, row, down = 0, 0, self.m - 1

        w.... left + 1 < right o. up + 1 < down:
            __ down - up > right - left:
                row = up + (down - up) // 2
                col = self.findRowMax(A, row, left, right)
                __ self.isPeak(A, row, col):
                    r.. [row, col]
                __ A[row][col] < A[row-1][col]:
                    down = row
                ____:
                    up = row
            ____:
                col = left + (right - left) // 2
                row = self.findColMax(A, col, up, down)
                __ self.isPeak(A, row, col):
                    r.. [row, col]
                __ A[row][col] < A[row][col-1]:
                    right = col
                ____:
                    left = col
        ___ r __ [up, down]:
            ___ c __ [left, right]:
                __ self.isPeak(A, r, c):
                    r.. [r, c]
        r.. self.NULL_POS

    # given col index, return the row index of the max value on that col
    ___ findColMax(self, A, col, up, down):
        row = 0
        ___ r __ r..(up, down + 1):
            __ A[row][col] < A[r][col]:
                row = r
        r.. row

    # given row index, return the col index of the max value on that row
    ___ findRowMax(self, A, row, left, right):
        col = 0
        ___ c __ r..(left, right + 1):
            __ A[row][col] < A[row][c]:
                col = c
        r.. col

    ___ isPeak(self, A, row, col):
        _r = _c = 0
        ___ i __ r..(4):
            _r = row + self.dx[i]
            _c = col + self.dy[i]
            __ 0 <= _r < self.m \
                    a.. 0 <= _c < self.n \
                    a.. A[row][col] < A[_r][_c]:
                r.. 0
        r.. 1
