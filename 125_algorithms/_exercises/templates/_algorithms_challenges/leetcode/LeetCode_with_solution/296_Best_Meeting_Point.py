c_ Solution o..
    # def minTotalDistance(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     # sort
    #     rows = []
    #     cols = []
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 1:
    #                 rows.append(i)
    #                 cols.append(j)
    #     row = rows[len(rows) / 2]
    #     cols.sort()
    #     col = cols[len(cols) / 2]
    #     return self.minDistance1D(rows, row) + self.minDistance1D(cols, col)

    # def minDistance1D(self, points, origin):
    #     distance = 0
    #     for point in points:
    #         distance += abs(point - origin)
    #     return distance

    ___ minDistance1D  points):
        # two points
        distance = 0
        i, j = 0, l.. points) - 1
        w.. i < j:
            distance += points[j] - points[i]
            i += 1
            j -= 1
        r_ distance

    ___ minTotalDistance  grid):
        rows = collectRows(grid)
        cols = collectCols(grid)
        row = rows[l.. rows) / 2]
        col = cols[l.. cols) / 2]
        r_ minDistance1D(rows) + minDistance1D(cols)

    ___ collectRows  grid):
        rows = []
        ___ i __ r.. l.. grid)):
            ___ j __ r.. l.. grid[0])):
                __ grid[i][j] __ 1:
                    rows.append(i)
        r_ rows

    ___ collectCols  grid):
        cols = []
        ___ j __ r.. l.. grid[0])):
            ___ i __ r.. l.. grid)):
                __ grid[i][j] __ 1:
                    cols.append(j)
        r_ cols
