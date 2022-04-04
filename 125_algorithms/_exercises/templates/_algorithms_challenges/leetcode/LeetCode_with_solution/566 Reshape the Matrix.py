#!/usr/bin/python3
"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a
matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive
integers r and c representing the row number and column number of the wanted
reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original
matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output
the new reshaped matrix; Otherwise, output the original matrix.
"""
____ t___ _______ List

c_ Solution:
    ___ matrixReshape  nums: List[List[i..]], r: i.., c: i..) __ List[List[i..]]:
        m, n = l..(nums), l..(nums[0])
        __ m * n != r * c:
            r.. nums

        ret    # list
        ___ i __ r..(m
            ___ j __ r..(n
                __ (i * n + j) % c __ 0:
                    ret.a..([])
                ret[-1].a..(nums[i][j])

        r.. ret
