c_ Solution o..
    ___ numIslands  grid
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS with marks
        __ grid is N.. or l.. grid) __ 0:
            r_ 0
        islands = 0
        ___ i __ r.. l.. grid)):
            ___ j __ r.. l.. grid[i])):
                __ grid[i][j] __ '1':
                    explore(grid, i, j)
                    islands += 1
        r_ islands

    ___ explore  grid, i, j
        grid[i][j] = 'X'
        __ i - 1 >= 0 a.. grid[i - 1][j] __ '1':
            explore(grid, i - 1, j)
        __ j - 1 >= 0 a.. grid[i][j - 1] __ '1':
            explore(grid, i, j - 1)
        __ i + 1 < l.. grid) a.. grid[i + 1][j] __ '1':
            explore(grid, i + 1, j)
        __ j + 1 < l.. grid[i]) a.. grid[i][j + 1] __ '1':
            explore(grid, i, j + 1)