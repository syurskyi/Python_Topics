'''
Created on Feb 14, 2017

@author: MT
'''

c_ Solution(o..
    ___ calculateMinimumHP  dungeon
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n l..(dungeon), l..(dungeon 0
        tbl [[0]*n ___ _ __ r..(m)]
        __ dungeon[-1][-1] > 0:
            tbl[-1][-1] 1
        ____
            tbl[-1][-1] 1-dungeon[-1][-1]
        ___ i __ r..(m-1, -1, -1
            ___ j __ r..(n-1, -1, -1
                __ i __ m-1 a.. j __ n-1:
                    _____
                __ i __ m-1:
                    right tbl[i][j+1] - dungeon[i][j]
                    tbl[i][j] m..(1, right)
                __ j __ n-1:
                    down tbl[i+1][j] - dungeon[i][j]
                    tbl[i][j] m..(1, down)
                __ i !_ m-1 a.. j !_ n-1:
                    right tbl[i][j+1] - dungeon[i][j]
                    down tbl[i+1][j] - dungeon[i][j]
                    tbl[i][j] m..(1, m..(right, down
        r.. tbl 0 0 
