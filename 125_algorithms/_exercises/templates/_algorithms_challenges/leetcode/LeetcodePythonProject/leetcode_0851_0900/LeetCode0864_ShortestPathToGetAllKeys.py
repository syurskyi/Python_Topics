'''
Created on Sep 24, 2019

@author: tongq
'''
class Solution(object
    ___ shortestPathAllKeys(self, grid
        """
        :type grid: List[str]
        :rtype: int
        """
        m, n = le.(grid), le.(grid[0])
        numOfKeys = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        moves = set()
        for i in range(m
            for j in range(n
                __ grid[i][j] __ '@':
                    starti = i
                    startj = j
                ____ grid[i][j] in 'abcdef':
                    numOfKeys += 1
        deque = []
        deque.append([starti, startj, 0, '.@abcdef', 0])
        w___ deque:
            i, j, steps, keys, collectedKeys = deque.pop(0)
            __ grid[i][j] in 'abcdef' and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collectedKeys += 1
            __ collectedKeys __ numOfKeys:
                r_ steps
            for x, y in dirs:
                ni = i+x
                nj = j+y
                __ 0<=ni<m and 0<=nj<n and grid[ni][nj] in keys:
                    __ (ni, nj, keys) not in moves:
                        moves.add((ni, nj, keys))
                        deque.append([ni, nj, steps+1, keys, collectedKeys])
        r_ -1
    
    ___ test(self
        testCase = [
            
        ]
        for grid in testCase:
            res = self.shortestPathAllKeys(grid)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
