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
from typing ______ List

class Solution:
    ___ matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = le.(nums), le.(nums[0])
        __ m * n != r * c:
            r_ nums

        ret = []
        for i in range(m
            for j in range(n
                __ (i * n + j) % c __ 0:
                    ret.append([])
                ret[-1].append(nums[i][j])

        r_ ret 
