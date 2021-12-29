"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies
you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall
is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""
__author__ = 'Daniel'


class Solution(object):
    ___ maxKilledEnemies(self, grid):
        """
        Brute force: O(n * n^2)
        Place the bomb around boundary
        The result of boundary bomb can be reused - dp

        The time complexity is O(m + n)
        :type grid: List[List[str]]
        :rtype: int
        """
        __ n.. grid: r.. 0

        m, n = l..(grid), l..(grid[0])
        rows = [0 ___ _ __ xrange(m)]
        cols = [0 ___ _ __ xrange(n)]
        gmax = 0
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ i __ 0 o. grid[i-1][j] __ 'W':
                    cols[j] = 0
                    ___ k __ xrange(i, m):
                        __ grid[k][j] __ 'E':
                            cols[j] += 1
                        ____ grid[k][j] __ 'W':
                            break

                __ j __ 0 o. grid[i][j-1] __ 'W':
                    rows[i] = 0
                    ___ k __ xrange(j, n):
                        __ grid[i][k] __ 'E':
                            rows[i] += 1
                        ____ grid[i][k] __ 'W':
                            break

                __ grid[i][j] __ '0':
                    gmax = max(gmax, rows[i] + cols[j])

        r.. gmax

__ __name__ __ "__main__":
    ... Solution().maxKilledEnemies(["0E00", "E0WE", "0E00"]) __ 3