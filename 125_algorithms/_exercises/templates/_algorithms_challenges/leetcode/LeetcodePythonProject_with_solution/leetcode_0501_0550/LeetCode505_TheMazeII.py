'''
Created on May 11, 2017

@author: MT
'''

class Solution(object):
    ___ shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        _______ heapq
        __ n.. maze o. n.. maze[0]: r.. -1
        m, n = l..(maze), l..(maze[0])
        heap    # list
        heapq.heappush(heap, (0, start[0], start[1]))
        visited = [[False]*n ___ _ __ r..(m)]
        while heap:
            currDist, i, j = heapq.heappop(heap)
            __ i __ destination[0] and j __ destination[1]:
                r.. currDist
            visited[i][j] = True
            ___ x, y, dist __ self.getNextSteps(maze, i, j):
                __ n.. visited[x][y]:
                    heapq.heappush(heap, (currDist+dist, x, y))
        r.. -1
    
    ___ getNextSteps(self, maze, i, j):
        m, n = l..(maze), l..(maze[0])
        steps = set()
        dirs = (1, 0), (0, 1), (-1, 0), (0, -1)
        ___ dir __ dirs:
            x, y = i, j
            dist = 0
            while 0 <= x+dir[0] < m and 0 <= y+dir[1] < n and\
                maze[x+dir[0]][y+dir[1]] != 1:
                x += dir[0]
                y += dir[1]
                dist += 1
            __ x != i o. y != j:
                steps.add((x, y, dist))
        r.. l..(steps)