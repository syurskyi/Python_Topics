'''
Created on May 8, 2017

@author: MT
'''

class Solution(object
    ___ hasPath(self, maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = le.(maze), le.(maze[0])
        queue= [start]
        visited = [[False]*n ___ _ in range(m)]
        visited[start[0]][start[1]] = True
        w___ queue:
            i, j = queue.pop(0)
            __ i __ destination[0] and j __ destination[1]:
                r_ True
            visited[i][j] = True
            ___ x, y in self.getNextSteps(maze, i, j
                __ not visited[x][y]:
                    queue.append((x, y))
        r_ False
    
    ___ getNextSteps(self, maze, i, j
        result = set()
        dirs = (1, 0), (0, 1), (-1, 0), (0, -1)
        m, n = le.(maze), le.(maze[0])
        ___ dir in dirs:
            x, y = i, j
            w___ 0 <= x+dir[0] < m and 0 <= y+dir[1] < n and\
                maze[x+dir[0]][y+dir[1]] != 1:
                x += dir[0]
                y += dir[1]
            result.add((x, y))
        result.discard((i, j))
        r_ list(result)
