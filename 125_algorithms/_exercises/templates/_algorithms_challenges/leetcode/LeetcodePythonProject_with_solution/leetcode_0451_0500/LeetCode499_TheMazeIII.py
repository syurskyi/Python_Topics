'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n = l..(maze), l..(maze[0])
        result    # list
        visited = [[False]*n ___ _ __ r..(m)]
        self.maxPath = float('inf')
        self.map = [[float('inf')]*n ___ _ __ r..(m)]
        self.helper(maze, ball, hole, '', 0, result, visited)
        result.s..(key=l.... x: (x[1], x[0]))
        __ result:
            r.. result[0][0]
        ____:
            r.. 'impossible'
    
    ___ helper(self, matrix, start, hole, curr, path, result, visited):
        __ path > self.maxPath o. path > self.map[start[0]][start[1]]:
            r..
        nextSteps = self.getNextSteps(matrix, start[0], start[1])
        visited[start[0]][start[1]] = True
        self.map[start[0]][start[1]] = m..(self.map[start[0]][start[1]], path)
        ___ step __ nextSteps:
            stop = [step[0], step[1]]
            dirStr = step[2]
            dist = step[3]
            res, dist0 = self.isPassing(matrix, start, stop, hole)
            __ res:
                self.maxPath = m..(self.maxPath, path+dist0)
                result.a..((curr+dirStr, path+dist0))
            ____ n.. visited[stop[0]][stop[1]]:
                self.helper(matrix, stop, hole, curr+dirStr, path+dist, result, visited)
        visited[start[0]][start[1]] = False
    
    ___ isPassing(self, maze, start, stop, hole):
        __ start[0] __ stop[0] __ hole[0]:
            __ start[1] < hole[1] <= stop[1]:
                r.. True, hole[1]-start[1]
            ____ stop[1] <= hole[1] < start[1]:
                r.. True, start[1]-hole[1]
        ____ start[1] __ stop[1] __ hole[1]:
            __ start[0] < hole[0] <= stop[0]:
                r.. True, hole[0]-start[0]
            ____ stop[0] <= hole[0] < start[0]:
                r.. True, hole[0]-stop[0]
        r.. False, 0
    
    ___ getNextSteps(self, matrix, i, j):
        steps = set()
        m, n = l..(matrix), l..(matrix[0])
        dirs = (1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')
        ___ dir __ dirs:
            x, y = i, j
            dist = 0
            w.... 0 <= x+dir[0] < m a.. 0 <= y+dir[1] < n a..\
                matrix[x+dir[0]][y+dir[1]] __ 0:
                x += dir[0]
                y += dir[1]
                dir += 1
            __ x != i o. y != j:
                steps.add((x, y, dir[2], dist))
        r.. steps
