'''
Created on Mar 7, 2017

@author: MT
'''

c_ Solution(o..
    ___ wallsAndGates  rooms
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        __ n.. rooms: r..
        m, n l..(rooms), l..(rooms[0])
        ___ i __ r..(m
            ___ j __ r..(n
                __ rooms[i][j] __ 0:
                    bfs(rooms, i, j)
    
    ___ bfs  rooms, i, j
        m, n l..(rooms), l..(rooms[0])
        queue [(i, j, 0)]
        w.... queue:
            i0, j0, dist queue.p.. 0)
            ___ x, y __ ((i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1:
                __ 0 <_ x < m a.. 0 <_ y < n a.. rooms[x][y] !_ -1:
                    newDist dist + 1
                    rooms[x][y] m..(rooms[x][y], newDist)
                    __ rooms[x][y] > rooms[i0][j0]:
                        queue.a..((x, y, newDist
    
    ___ test
        matrix [
            [f__('inf'), -1, 0, f__('inf')],
            [f__('inf'), f__('inf'), f__('inf'), -1],
            [f__('inf'), -1, f__('inf'), -1],
            [0, -1, f__('inf'), f__('inf')],
        ]
        print('before:')
        print('\n'.j..([s..(l) ___ l __ matrix]
        wallsAndGates(matrix)
        print('after:')
        print('\n'.j..([s..(l) ___ l __ matrix]
        print('-='*30+'-')

__ _____ __ _____
    Solution().test()
