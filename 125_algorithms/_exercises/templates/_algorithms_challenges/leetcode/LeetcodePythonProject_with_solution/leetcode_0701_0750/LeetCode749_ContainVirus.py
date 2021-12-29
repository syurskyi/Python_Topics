'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object):
    ___ containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = [0]
        w.... self.check(grid, cost):
            continue
        r.. cost[0]
    
    ___ check(self, grid, cost):
        count = 1
        maxVal = -1
        flag = False
        info    # list
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    count += 1
                    walls = [[0]*n ___ _ __ r..(m)]
                    res = [0, 0]
                    grid[i][j] = count
                    self.dfs(i, j, grid, count, walls, res)
                    __ res[0] != 0:
                        flag = True
                    __ maxVal __ -1 o. res[0] > info[maxVal][0]:
                        maxVal = count-2
                    info.a..(l..(res))
        __ count __ 1:
            r.. False
        cost[0] += info[maxVal][1]
        self.update(grid, maxVal+2)
        r.. flag
    
    ___ dfs(self, row, col, grid, count, walls, res):
        shiftX = [1, 0, -1, 0]
        shiftY = [0, 1, 0, -1]
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(4):
            newRow = row+shiftX[i]
            newCol = col+shiftY[i]
            __ 0 <= newRow < m a.. 0 <= newCol < n:
                __ grid[newRow][newCol] __ 1:
                    grid[newRow][newCol] = count
                    self.dfs(newRow, newCol, grid, count, walls, res)
                ____ grid[newRow][newCol] __ 0:
                    __ walls[newRow][newCol] __ 0:
                        res[0] += 1
                    __ (walls[newRow][newCol] & 1 << i) __ 0:
                        res[1] += 1
                        walls[newRow][newCol] |= 1 << i
    
    ___ update(self, grid, quarantine):
        shiftX = [1, 0, -1, 0]
        shiftY = [0, 1, 0, -1]
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] > 1 a.. grid[i][j] != quarantine:
                    ___ k __ r..(4):
                        newRow = i+shiftX[k]
                        newCol = j+shiftY[k]
                        __ 0 <= newRow < m a.. 0 <= newCol < n a.. grid[newRow][newCol] __ 0:
                            grid[newRow][newCol] = 1
                    grid[i][j] = 1
                ____ grid[i][j] __ quarantine:
                    grid[i][j] = -1
    
    ___ test(self):
        testCases = [
            [
                [0,1,0,0,0,0,0,1],
                [0,1,0,1,0,0,0,1],
                [0,0,0,0,0,0,0,1],
            ],
            [
                [0,1,0,0,0,0,0,1],
                [0,1,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ],
            [
                [1,1,1,0,0,0,0,0,0],
                [1,0,1,0,1,1,1,1,1],
                [1,1,1,0,0,0,0,0,0]
            ],
        ]
        ___ grid __ testCases:
            result = self.containVirus(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
