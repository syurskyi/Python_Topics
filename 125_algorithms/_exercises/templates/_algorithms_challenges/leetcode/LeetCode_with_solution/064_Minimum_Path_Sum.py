c_ Solution o..
    ___ minPathSum  grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = l.. grid)
        __ height __ 0:
            r_ 0
        width = l.. grid[0])
        pathmap = []
        ___ i __ r.. height):
            pathmap.append([100000000000] * width)
        pathmap[0][0] = grid[0][0]
        ___ i __ r.. height):
            ___ j __ r.. width):
                compare = [pathmap[i][j]]
                __ i - 1 >= 0:
                    compare.append(pathmap[i - 1][j] + grid[i][j])
                __ j - 1 >= 0:
                    compare.append(pathmap[i][j - 1] + grid[i][j])
                # min choice
                pathmap[i][j] = min(compare)
        r_ pathmap[-1][-1]