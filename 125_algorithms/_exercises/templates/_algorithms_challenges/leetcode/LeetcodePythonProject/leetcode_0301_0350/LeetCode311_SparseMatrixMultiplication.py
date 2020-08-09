'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object
    ___ multiply(self, A, B
        m, n = le.(A), le.(A[0])
        nB = le.(B[0])
        res = [[0]*nB ___ _ in range(m)]
        ___ i in range(m
            ___ k in range(n
                __ A[i][k]:
                    ___ j in range(nB
                        __ B[k][j]:
                            res[i][j] += A[i][k]*B[k][j]
        r_ res
    
    ___ multiply_own(self, A, B
        __ not A or not B:
            r_ A __ not A else B
        mA, nA = le.(A), le.(A[0])
        mB, nB = le.(B), le.(B[0])
        colSumB = []
        ___ j in range(nB
            tmp = 0
            ___ i in range(mB
                tmp+=B[i][j]
            colSumB.append(tmp)
        result = [[0]*nB ___ i in range(mA)]
        ___ i in range(mA
            ___ j in range(nB
                __ colSumB[j]:
                    ___ i0 in range(nA
                        result[i][j] += A[i][i0]*B[i0][j]
        r_ result
