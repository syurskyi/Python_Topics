'''
Created on May 29, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ generate  numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        __ numRows <= 0: r.. []
        res = [[1]]
        ___ i __ r..(1, numRows):
            tmp    # list
            ___ j __ r..(i+1):
                __ j __ 0 o. j __ i:
                    tmp.a..(1)
                ____:
                    tmp.a..(res[i-1][j] + res[i-1][j-1])
            res.a..(tmp)
        r.. res
