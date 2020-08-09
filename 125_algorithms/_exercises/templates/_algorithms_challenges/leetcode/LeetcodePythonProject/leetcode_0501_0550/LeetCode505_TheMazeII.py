'''
Created on May 11, 2017

@author: MT
'''

class Solution(object
    ___ shortestDistance(self, maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        ______ heapq
        __ not maze or not maze[0]: r_ -1
        m, n = le.(maze), le.(maze[0])
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        visited = [[False]*n for _ in range(m)]
        w___ heap:
            currDist, i, j = heapq.heappop(heap)
            __ i __ destination[0] and j __ destination[1]:
                r_ currDist
            visited[i][j] = True
            for x, y, dist in self.getNextSteps(maze, i, j
                __ not visited[x][y]:
                    heapq.heappush(heap, (currDist+dist, x, y))
        r_ -1
    
    ___ getNextSteps(self, maze, i, j
        m, n = le.(maze), le.(maze[0])
        steps = set()
        dirs = (1, 0), (0, 1), (-1, 0), (0, -1)
        for dir in dirs:
            x, y = i, j
            dist = 0
            w___ 0 <= x+dir[0] < m and 0 <= y+dir[1] < n and\
                maze[x+dir[0]][y+dir[1]] != 1:
                x += dir[0]
                y += dir[1]
                dist += 1
            __ x != i or y != j:
                steps.add((x, y, dist))
        r_ list(steps)