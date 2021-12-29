'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object):
    ___ multiply(self, A, B):
        m, n = len(A), len(A[0])
        nB = len(B[0])
        res = [[0]*nB for _ in range(m)]
        for i in range(m):
            for k in range(n):
                __ A[i][k]:
                    for j in range(nB):
                        __ B[k][j]:
                            res[i][j] += A[i][k]*B[k][j]
        return res
    
    ___ multiply_own(self, A, B):
        __ not A or not B:
            return A __ not A else B
        mA, nA = len(A), len(A[0])
        mB, nB = len(B), len(B[0])
        colSumB = []
        for j in range(nB):
            tmp = 0
            for i in range(mB):
                tmp+=B[i][j]
            colSumB.append(tmp)
        result = [[0]*nB for i in range(mA)]
        for i in range(mA):
            for j in range(nB):
                __ colSumB[j]:
                    for i0 in range(nA):
                        result[i][j] += A[i][i0]*B[i0][j]
        return result
