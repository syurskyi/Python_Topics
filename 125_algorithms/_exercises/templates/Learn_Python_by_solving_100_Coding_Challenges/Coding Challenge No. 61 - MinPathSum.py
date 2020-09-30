# Minimum Path Sum
# Question: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Solutions:

c_ Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    ___ minPathSum(self, grid):
        __ le.(grid)__0 or le.(grid[0])__0:
            r_ 0
        ___ row __ ra..(0, le.(grid)):
            ___ col __ ra..(0, le.(grid[0])):
                __ row>0 an. col>0:
                    grid[row][col] +_ mi.(grid[row-1][col],grid[row][col-1])
                elif row>0:
                    grid[row][col] +_ grid[row-1][col]
                elif col>0:
                    grid[row][col] +_ grid[row][col-1]
        r_ grid[le.(grid)-1][le.(grid[0])-1]


grid _ [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
Solution().minPathSum(grid)