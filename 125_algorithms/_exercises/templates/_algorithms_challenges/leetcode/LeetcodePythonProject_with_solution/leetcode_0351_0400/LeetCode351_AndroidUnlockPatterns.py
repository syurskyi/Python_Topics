'''
Created on Mar 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ numberOfPatterns  m, n
        skip = [[0]*10 ___ _ __ r..(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = \
            skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        result = 0
        ___ i __ r..(m, n+1
            p.. = s..()
            result += helper(p.., 1, i-1)*4
            result += helper(p.., 2, i-1)*4
            result += helper(p.., 5, i-1)
        r.. result
    
    ___ helper  p.., curr, remain
        __ remain < 0: r.. 0
        __ remain __ 0: r.. 1
        p...add(curr)
        result = 0
        ___ to __ r..(1, 10
            __ to n.. __ p.. a.. (skip[curr][to]__0 o. skip[curr][to] __ p..
                result += helper(p.., to, remain-1)
        p...remove(curr)
        r.. result