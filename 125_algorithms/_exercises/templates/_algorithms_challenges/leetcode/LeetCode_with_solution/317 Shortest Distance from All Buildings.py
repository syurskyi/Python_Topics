"""
Premium Question
"""
_______ sys

__author__ = 'Daniel'


c_ Solution(object):
    ___ - ):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ shortestDistance(self, grid):
        """
        BFS & collect all distance

        ideas:
        Pruning: don't use a fresh "visited" for each BFS. Instead, I walk only
        onto the cells that were reachable from all previous buildings. From the
        first building I only walk onto cells where grid is 0, and make them -1.
        From the second building I only walk onto cells where grid is -1, and I
        make them -2.
        -1
        -2
        -3
        :type grid: List[List[int]]
        :rtype: int
        """
        m = l..(grid)
        n = l..(grid[0])
        acc = [[0 ___ _ __ xrange(n)] ___ _ __ xrange(m)]
        reachable = [[T.. ___ _ __ xrange(n)] ___ _ __ xrange(m)]
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ grid[i][j] > 0:
                    reachable[i][j] = F..
                    acc[i][j] = sys.maxint

        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ grid[i][j] __ 1:
                    bfs(grid, acc, reachable, i, j)

        mini = sys.maxint
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ acc[i][j] < mini a.. reachable[i][j]:
                    mini = acc[i][j]

        r.. mini __ mini != sys.maxint ____ -1

    ___ bfs(self, grid, acc, reachable, x, y):
        d = 0
        m, n = l..(grid), l..(grid[0])
        visited = [[F.. ___ _ __ xrange(n)] ___ _ __ xrange(m)]

        q = [(x, y)]
        visited[x][y] = T..  # enqueue, then visited
        w.... q:
            l = l..(q)
            ___ idx __ xrange(l):
                i, j = q[idx]
                acc[i][j] += d

                ___ dir __ dirs:
                    I = i+dir[0]
                    J = j+dir[1]
                    __ 0 <= I < m a.. 0 <= J < n a.. grid[I][J] __ 0 a.. n.. visited[I][J]:
                        q.a..((I, J))
                        visited[I][J] = T..

            d += 1
            q = q[l:]

        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ n.. visited[i][j]:
                    reachable[i][j] = F..


__ _______ __ _______
    ... Solution().shortestDistance(
        [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]) __ 88
    ... Solution().shortestDistance([[1, 2, 0]]) __ -1
    ... Solution().shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]) __ 7
