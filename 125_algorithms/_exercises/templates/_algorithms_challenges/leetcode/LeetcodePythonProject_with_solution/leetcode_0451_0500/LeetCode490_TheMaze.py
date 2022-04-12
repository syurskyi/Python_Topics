'''
Created on May 8, 2017

@author: MT
'''

c_ Solution(o..
    ___ hasPath  maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n l..(maze), l..(maze[0])
        queue= [start]
        visited [[F..]*n ___ _ __ r..(m)]
        visited[start[0]][start[1]] T..
        w.... queue:
            i, j queue.p.. 0)
            __ i __ destination[0] a.. j __ destination[1]:
                r.. T..
            visited[i][j] T..
            ___ x, y __ getNextSteps(maze, i, j
                __ n.. visited[x][y]:
                    queue.a..((x, y
        r.. F..
    
    ___ getNextSteps  maze, i, j
        result s..()
        dirs (1, 0), (0, 1), (-1, 0), (0, -1)
        m, n l..(maze), l..(maze[0])
        ___ dir __ dirs:
            x, y i, j
            w.... 0 <_ x+dir[0] < m a.. 0 <_ y+dir[1] < n a..\
                maze[x+dir[0]][y+dir[1]] !_ 1:
                x += dir[0]
                y += dir[1]
            result.add((x, y
        result.discard((i, j
        r.. l..(result)
