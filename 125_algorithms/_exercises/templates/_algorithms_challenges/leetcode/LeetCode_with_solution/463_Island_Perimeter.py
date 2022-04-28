c_ Solution o..
    ___ islandPerimeter  grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution
        row_num = l.. grid)
        __ row_num __ 0 || l.. grid[0]) __ 0:
            r_ 0
        islands, overlaps = 0, 0
        col_num = l.. grid[0])
        ___ i __ r.. row_num):
            ___ j __ r.. col_num):
                __ (grid[i][j] __ 1):
                    islands += 1
                    # careful about right and down
                    __ (i < row_num - 1 && grid[i + 1][j] __ 1):
                        overlaps += 1
                    __ (j < col_num - 1 && grid[i][j + 1] __ 1):
                        overlaps += 1
        r_ islands * 4 - overlaps * 2
