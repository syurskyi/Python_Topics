'''
Created on Mar 7, 2017

@author: MT
'''

c_ Solution(object):
    ___ wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        __ n.. rooms: r..
        m, n = l..(rooms), l..(rooms[0])
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ rooms[i][j] __ 0:
                    bfs(rooms, i, j)
    
    ___ bfs(self, rooms, i, j):
        m, n = l..(rooms), l..(rooms[0])
        queue = [(i, j, 0)]
        w.... queue:
            i0, j0, dist = queue.pop(0)
            ___ x, y __ ((i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1)):
                __ 0 <= x < m a.. 0 <= y < n a.. rooms[x][y] != -1:
                    newDist = dist + 1
                    rooms[x][y] = m..(rooms[x][y], newDist)
                    __ rooms[x][y] > rooms[i0][j0]:
                        queue.a..((x, y, newDist))
    
    ___ test
        matrix = [
            [float('inf'), -1, 0, float('inf')],
            [float('inf'), float('inf'), float('inf'), -1],
            [float('inf'), -1, float('inf'), -1],
            [0, -1, float('inf'), float('inf')],
        ]
        print('before:')
        print('\n'.j..([s..(l) ___ l __ matrix]))
        wallsAndGates(matrix)
        print('after:')
        print('\n'.j..([s..(l) ___ l __ matrix]))
        print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
