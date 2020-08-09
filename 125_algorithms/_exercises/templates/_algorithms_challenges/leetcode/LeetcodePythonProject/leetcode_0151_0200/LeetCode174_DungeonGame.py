'''
Created on Feb 14, 2017

@author: MT
'''

class Solution(object
    ___ calculateMinimumHP(self, dungeon
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = le.(dungeon), le.(dungeon[0])
        tbl = [[0]*n ___ _ in range(m)]
        __ dungeon[-1][-1] > 0:
            tbl[-1][-1] = 1
        ____
            tbl[-1][-1] = 1-dungeon[-1][-1]
        ___ i in range(m-1, -1, -1
            ___ j in range(n-1, -1, -1
                __ i __ m-1 and j __ n-1:
                    continue
                __ i __ m-1:
                    right = tbl[i][j+1] - dungeon[i][j]
                    tbl[i][j] = max(1, right)
                __ j __ n-1:
                    down = tbl[i+1][j] - dungeon[i][j]
                    tbl[i][j] = max(1, down)
                __ i != m-1 and j != n-1:
                    right = tbl[i][j+1] - dungeon[i][j]
                    down = tbl[i+1][j] - dungeon[i][j]
                    tbl[i][j] = max(1, min(right, down))
        r_ tbl[0][0]
