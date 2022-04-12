'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ findShortestWay  maze, ball, hole
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n l..(maze), l..(maze 0
        result    # list
        visited [[F..]*n ___ _ __ r..(m)]
        maxPath f__('inf')
        map [[f__('inf')]*n ___ _ __ r..(m)]
        helper(maze, ball, hole, '', 0, result, visited)
        result.s..(k.._l.... x: (x[1], x[0]
        __ result:
            r.. result 0 0 
        ____
            r.. 'impossible'
    
    ___ helper  matrix, start, hole, curr, p.., result, visited
        __ p.. > maxPath o. p.. > map[start[0]][start[1]]:
            r..
        nextSteps getNextSteps(matrix, start[0], start[1])
        visited[start[0]][start[1]] T..
        map[start[0]][start[1]] m.. m..[start[0]][start[1]], p..)
        ___ step __ nextSteps:
            stop [step[0], step[1]]
            dirStr step[2]
            dist step[3]
            res, dist0 isPassing(matrix, start, stop, hole)
            __ res:
                maxPath m..(maxPath, p..+dist0)
                result.a..((curr+dirStr, p..+dist0
            ____ n.. visited[stop[0]][stop[1]]:
                helper(matrix, stop, hole, curr+dirStr, p..+dist, result, visited)
        visited[start[0]][start[1]] F..
    
    ___ isPassing  maze, start, stop, hole
        __ start[0] __ stop[0] __ hole[0]:
            __ start[1] < hole[1] <_ stop[1]:
                r.. T.., hole[1]-start[1]
            ____ stop[1] <_ hole[1] < start[1]:
                r.. T.., start[1]-hole[1]
        ____ start[1] __ stop[1] __ hole[1]:
            __ start[0] < hole[0] <_ stop[0]:
                r.. T.., hole[0]-start[0]
            ____ stop[0] <_ hole[0] < start[0]:
                r.. T.., hole[0]-stop[0]
        r.. F.., 0
    
    ___ getNextSteps  matrix, i, j
        steps s..()
        m, n l..(matrix), l..(matrix 0
        dirs (1, 0, 'd'), (0, 1, _, (-1, 0, 'u'), (0, -1, 'l')
        ___ dir __ dirs:
            x, y i, j
            dist 0
            w.... 0 <_ x+dir[0] < m a.. 0 <_ y+dir[1] < n a..\
                matrix[x+dir[0]][y+dir[1]] __ 0:
                x += dir[0]
                y += dir[1]
                dir += 1
            __ x !_ i o. y !_ j:
                steps.add((x, y, dir[2], dist
        r.. steps
