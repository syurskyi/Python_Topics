"""
Premium Question
"""
______ sys

__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ shortestDistance(self, grid
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
        m = le.(grid)
        n = le.(grid[0])
        acc = [[0 ___ _ in xrange(n)] ___ _ in xrange(m)]
        reachable = [[True ___ _ in xrange(n)] ___ _ in xrange(m)]
        ___ i in xrange(m
            ___ j in xrange(n
                __ grid[i][j] > 0:
                    reachable[i][j] = False
                    acc[i][j] = sys.maxint

        ___ i in xrange(m
            ___ j in xrange(n
                __ grid[i][j] __ 1:
                    self.bfs(grid, acc, reachable, i, j)

        mini = sys.maxint
        ___ i in xrange(m
            ___ j in xrange(n
                __ acc[i][j] < mini and reachable[i][j]:
                    mini = acc[i][j]

        r_ mini __ mini != sys.maxint else -1

    ___ bfs(self, grid, acc, reachable, x, y
        d = 0
        m, n = le.(grid), le.(grid[0])
        visited = [[False ___ _ in xrange(n)] ___ _ in xrange(m)]

        q = [(x, y)]
        visited[x][y] = True  # enqueue, then visited
        w___ q:
            l = le.(q)
            ___ idx in xrange(l
                i, j = q[idx]
                acc[i][j] += d

                ___ dir in self.dirs:
                    I = i+dir[0]
                    J = j+dir[1]
                    __ 0 <= I < m and 0 <= J < n and grid[I][J] __ 0 and not visited[I][J]:
                        q.append((I, J))
                        visited[I][J] = True

            d += 1
            q = q[l:]

        ___ i in xrange(m
            ___ j in xrange(n
                __ not visited[i][j]:
                    reachable[i][j] = False


__ __name__ __ "__main__":
    assert Solution().shortestDistance(
        [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]) __ 88
    assert Solution().shortestDistance([[1, 2, 0]]) __ -1
    assert Solution().shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]) __ 7
