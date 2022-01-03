'''
Created on Mar 15, 2017

@author: MT
'''

c_ Solution(object):
    ___ multiply(self, A, B):
        m, n = l..(A), l..(A[0])
        nB = l..(B[0])
        res = [[0]*nB ___ _ __ r..(m)]
        ___ i __ r..(m):
            ___ k __ r..(n):
                __ A[i][k]:
                    ___ j __ r..(nB):
                        __ B[k][j]:
                            res[i][j] += A[i][k]*B[k][j]
        r.. res
    
    ___ multiply_own(self, A, B):
        __ n.. A o. n.. B:
            r.. A __ n.. A ____ B
        mA, nA = l..(A), l..(A[0])
        mB, nB = l..(B), l..(B[0])
        colSumB    # list
        ___ j __ r..(nB):
            tmp = 0
            ___ i __ r..(mB):
                tmp+=B[i][j]
            colSumB.a..(tmp)
        result = [[0]*nB ___ i __ r..(mA)]
        ___ i __ r..(mA):
            ___ j __ r..(nB):
                __ colSumB[j]:
                    ___ i0 __ r..(nA):
                        result[i][j] += A[i][i0]*B[i0][j]
        r.. result
