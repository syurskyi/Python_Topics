"""
Premium Question
https://leetcode.com/problems/sparse-matrix-multiplication/
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ multiply  A, B
        """
        Brute force O(n^3)
        O(n^2 k) HashMap
        Posting list
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n l..(A), l..(A 0
        A1 [{} ___ _ __ x..(m)]
        ___ i __ x..(m
            ___ j __ x..(n
                __ A[i][j] !_ 0:
                    A1[i][j] A[i][j]

        m, n l..(B), l..(B 0
        B1 [{} ___ _ __ x..(n)]
        ___ i __ x..(m
            ___ j __ x..(n
                __ B[i][j] !_ 0:
                    B1[j][i] B[i][j]

        ret [[0 ___ _ __ x..(l..(B[0]] ___ _ __ x..(l..(A]
        ___ i, row __ e..(A1
            ___ j, col __ e..(B1
                s 0
                ___ k __ row.k..:
                    __ k __ col:
                        s += row[k]*col[k]
                ret[i][j] s

        r.. ret

__ _______ __ _______
    A [
        [1, 0, 0],
        [-1, 0, 3]
    ]

    B [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    ... Solution().multiply(A, B) __ [[7, 0, 0], [-7, 0, 3]]

