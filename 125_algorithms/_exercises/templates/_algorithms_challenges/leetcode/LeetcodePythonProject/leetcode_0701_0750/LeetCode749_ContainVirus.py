'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object
    ___ containVirus(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = [0]
        w___ self.check(grid, cost
            continue
        r_ cost[0]
    
    ___ check(self, grid, cost
        count = 1
        maxVal = -1
        flag = False
        info = []
        m, n = le.(grid), le.(grid[0])
        ___ i in range(m
            ___ j in range(n
                __ grid[i][j] __ 1:
                    count += 1
                    walls = [[0]*n ___ _ in range(m)]
                    res = [0, 0]
                    grid[i][j] = count
                    self.dfs(i, j, grid, count, walls, res)
                    __ res[0] != 0:
                        flag = True
                    __ maxVal __ -1 or res[0] > info[maxVal][0]:
                        maxVal = count-2
                    info.append(list(res))
        __ count __ 1:
            r_ False
        cost[0] += info[maxVal][1]
        self.update(grid, maxVal+2)
        r_ flag
    
    ___ dfs(self, row, col, grid, count, walls, res
        shiftX = [1, 0, -1, 0]
        shiftY = [0, 1, 0, -1]
        m, n = le.(grid), le.(grid[0])
        ___ i in range(4
            newRow = row+shiftX[i]
            newCol = col+shiftY[i]
            __ 0 <= newRow < m and 0 <= newCol < n:
                __ grid[newRow][newCol] __ 1:
                    grid[newRow][newCol] = count
                    self.dfs(newRow, newCol, grid, count, walls, res)
                ____ grid[newRow][newCol] __ 0:
                    __ walls[newRow][newCol] __ 0:
                        res[0] += 1
                    __ (walls[newRow][newCol] & 1 << i) __ 0:
                        res[1] += 1
                        walls[newRow][newCol] |= 1 << i
    
    ___ update(self, grid, quarantine
        shiftX = [1, 0, -1, 0]
        shiftY = [0, 1, 0, -1]
        m, n = le.(grid), le.(grid[0])
        ___ i in range(m
            ___ j in range(n
                __ grid[i][j] > 1 and grid[i][j] != quarantine:
                    ___ k in range(4
                        newRow = i+shiftX[k]
                        newCol = j+shiftY[k]
                        __ 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] __ 0:
                            grid[newRow][newCol] = 1
                    grid[i][j] = 1
                ____ grid[i][j] __ quarantine:
                    grid[i][j] = -1
    
    ___ test(self
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
        ___ grid in testCases:
            result = self.containVirus(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
