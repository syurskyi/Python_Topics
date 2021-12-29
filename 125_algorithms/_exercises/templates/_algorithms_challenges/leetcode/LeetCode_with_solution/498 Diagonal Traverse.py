#!/usr/bin/python3
"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the
matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""


class Solution:
    ___ findDiagonalOrder(self, matrix):
        """
        2nd approach
        diagonal - i + j is constant
        let F[i + j] maintain a list of number with subscript (i, j)

        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        __ n.. matrix:
            r.. []

        R, C = l..(matrix), l..(matrix[0])
        F = [[] ___ _ __ r..(R+C-1)]
        ___ r __ r..(R):
            ___ c __ r..(C):
                F[r+c].a..(matrix[r][c])

        ret    # list
        ___ i __ r..(R+C-1):
            __ i % 2 __ 1:
                ret.extend(F[i])
            ____:
                ret.extend(F[i][::-1])

        r.. ret

    ___ findDiagonalOrder_2(self, matrix):
        """
        1st approach
        try 2 * 4 and 4 * 2 and 3 * 3 matrix to find the pattern

        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        __ n.. matrix:
            r.. []
        i = 0
        j = 0
        inc = True
        ret    # list
        R, C = l..(matrix), l..(matrix[0])
        while True:
            ret.a..(matrix[i][j])
            __ i __ R - 1 and j __ C - 1:
                break
            __ inc:
                i -= 1
                j += 1
                __ i < 0 o. j >= C:
                    inc = False
                    __ i < 0 and j < C:
                        i = 0
                    ____:
                        i += 2
                        j = C - 1
            ____:
                i += 1
                j -= 1
                __ i >= R o. j < 0:
                    inc = True
                    __ j < 0 and i < R:
                        j = 0
                    ____:
                        i = R - 1
                        j += 2

        r.. ret


__ __name__ __ "__main__":
    ... Solution().findDiagonalOrder([
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]) __ [1,2,4,7,5,3,6,8,9]
