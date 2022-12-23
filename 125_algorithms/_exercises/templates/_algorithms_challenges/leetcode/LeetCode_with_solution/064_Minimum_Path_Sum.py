c_ Solution o..
    ___ minPathSum  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = l.. grid)
        __ height __ 0:
            r_ 0
        width = l.. grid[0])
        pathmap =    # list
        ___ i __ r.. height
            pathmap.a.. [100000000000] * width)
        pathmap[0][0] = grid[0][0]
        ___ i __ r.. height
            ___ j __ r.. width
                compare = [pathmap[i][j]]
                __ i - 1 >= 0:
                    compare.a.. pathmap[i - 1][j] + grid[i][j])
                __ j - 1 >= 0:
                    compare.a.. pathmap[i][j - 1] + grid[i][j])
                # min choice
                pathmap[i][j] = m.. compare)
        r_ pathmap[-1][-1]