"""
Premium Question
https://leetcode.com/problems/sparse-matrix-multiplication/
"""
__author__ = 'Daniel'


class Solution(object):
    ___ multiply(self, A, B):
        """
        Brute force O(n^3)
        O(n^2 k) HashMap
        Posting list
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = l..(A), l..(A[0])
        A1 = [{} ___ _ __ xrange(m)]
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ A[i][j] != 0:
                    A1[i][j] = A[i][j]

        m, n = l..(B), l..(B[0])
        B1 = [{} ___ _ __ xrange(n)]
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ B[i][j] != 0:
                    B1[j][i] = B[i][j]

        ret = [[0 ___ _ __ xrange(l..(B[0]))] ___ _ __ xrange(l..(A))]
        ___ i, row __ e..(A1):
            ___ j, col __ e..(B1):
                s = 0
                ___ k __ row.keys():
                    __ k __ col:
                        s += row[k]*col[k]
                ret[i][j] = s

        r.. ret

__ __name__ __ "__main__":
    A = [
        [1, 0, 0],
        [-1, 0, 3]
    ]

    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    ... Solution().multiply(A, B) __ [[7, 0, 0], [-7, 0, 3]]

