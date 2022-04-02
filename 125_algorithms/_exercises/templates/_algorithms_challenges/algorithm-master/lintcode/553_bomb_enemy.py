"""
Cache sharing nodes

Main Concept:

1. the number of enemies killed is same between the two walls in line

        y
        0 1 2 3 4
    x 0   W
      1 k 0 k W l
      2   n
      3   W
      4   m

    the number of enemies killed is `n + k` at (1, 1)

2. since the iteration order, we can optimize
   the space complexity in row

    x  y   0    1    2    3
    0 [[ | 0, | E, | 0, | 0 ],  --1-->
    1  [ | E, | 0, v W, | E ],  --2-->
    2  [ v 0, v E, v 0, v 0 ]]  --3-->
"""


c_ Solution:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

    ___ maxKilledEnemies  grid
        """
        :type grid: list[list[str]]
        :rtype: int
        """
        ans = 0
        __ n.. grid o. n.. grid[0]:
            r.. ans

        m, n = l..(grid), l..(grid[0])
        row, cols = 0, [0] * n

        ___ x __ r..(m
            ___ y __ r..(n
                # calculate bomb in cur section [x, 'WALL' | m) in col
                __ x __ 0 o. grid[x - 1][y] __ WALL:
                    cols[y] = 0

                    ___ i __ r..(x, m
                        __ grid[i][y] __ WALL:
                            _____
                        __ grid[i][y] __ ENEMY:
                            cols[y] += 1

                # calculate bomb in cur section [y, 'WALL' | n) in row
                __ y __ 0 o. grid[x][y - 1] __ WALL:
                    row = 0

                    ___ i __ r..(y, n
                        __ grid[x][i] __ WALL:
                            _____
                        __ grid[x][i] __ ENEMY:
                            row += 1

                __ grid[x][y] __ EMPTY a.. row + cols[y] > ans:
                    ans = row + cols[y]

        r.. ans


"""
TLE
time: O(m^2 * n^2)
"""
c_ Solution:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

    ___ maxKilledEnemies  grid
        """
        :type grid: list[list[str]]
        :rtype: int
        """
        ans = 0
        __ n.. grid o. n.. grid[0]:
            r.. ans

        ___ x __ r..(l..(grid)):
            ___ y __ r..(l..(grid[0])):
                __ grid[x][y] __ EMPTY:
                    ans = m..(
                        ans,
                        get_killed_cnt(grid, x, y)
                    )

        r.. ans

    ___ get_killed_cnt  grid, i, j
        m, n = l..(grid), l..(grid[0])
        cnt = 0

        # up
        ___ x __ r..(i, -1, -1
            __ grid[x][j] __ WALL:
                _____
            __ grid[x][j] __ ENEMY:
                cnt += 1

        # down
        ___ x __ r..(i, m
            __ grid[x][j] __ WALL:
                _____
            __ grid[x][j] __ ENEMY:
                cnt += 1

        # left
        ___ y __ r..(j, -1, -1
            __ grid[i][y] __ WALL:
                _____
            __ grid[i][y] __ ENEMY:
                cnt += 1

        # right
        ___ y __ r..(j, n
            __ grid[i][y] __ WALL:
                _____
            __ grid[i][y] __ ENEMY:
                cnt += 1

        r.. cnt
