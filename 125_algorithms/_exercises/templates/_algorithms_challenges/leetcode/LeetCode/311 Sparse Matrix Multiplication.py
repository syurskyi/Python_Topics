"""
Premium Question
https://leetcode.com/problems/sparse-matrix-multiplication/
"""
__author__ = 'Daniel'


class Solution(object
    ___ multiply(self, A, B
        """
        Brute force O(n^3)
        O(n^2 k) HashMap
        Posting list
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = le.(A), le.(A[0])
        A1 = [{} ___ _ in xrange(m)]
        ___ i in xrange(m
            ___ j in xrange(n
                __ A[i][j] != 0:
                    A1[i][j] = A[i][j]

        m, n = le.(B), le.(B[0])
        B1 = [{} ___ _ in xrange(n)]
        ___ i in xrange(m
            ___ j in xrange(n
                __ B[i][j] != 0:
                    B1[j][i] = B[i][j]

        ret = [[0 ___ _ in xrange(le.(B[0]))] ___ _ in xrange(le.(A))]
        ___ i, row in enumerate(A1
            ___ j, col in enumerate(B1
                s = 0
                ___ k in row.keys(
                    __ k in col:
                        s += row[k]*col[k]
                ret[i][j] = s

        r_ ret

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
    assert Solution().multiply(A, B) __ [[7, 0, 0], [-7, 0, 3]]

