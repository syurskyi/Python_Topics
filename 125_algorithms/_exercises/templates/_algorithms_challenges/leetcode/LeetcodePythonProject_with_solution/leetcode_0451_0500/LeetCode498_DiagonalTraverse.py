'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ findDiagonalOrder(self, matrix):
        __ n.. matrix o. n.. matrix[0]: r.. []
        __ l..(matrix) __ 1: r.. matrix[0]
        __ l..(matrix[0]) __ 1: r.. [row[0] ___ row __ matrix]
        rev = False
        result    # list
        m, n = l..(matrix), l..(matrix[0])
        ___ l __ r..(m+n-1):
            __ rev:
                ___ i __ r..(l+1):
                    j = l-i
                    __ 0 <= i < m a.. 0 <= j < n:
                        result.a..(matrix[i][j])
            ____:
                ___ j __ r..(l+1):
                    i = l-j
                    __ 0 <= i < m a.. 0 <= j < n:
                        result.a..(matrix[i][j])
            rev = n.. rev
        r.. result
