___ count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands


    
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            __ grid[row][col] == 1:
                mark_islands(row,col,grid)
                islands += 1



    return islands



















___ mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.


    grid[i][j] = '#'


    for n_row,n_col in ((i + 1,j),(i -1,j),(i,j + 1),(i,j-1)):
        __ 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == 1:
            mark_islands(n_row,n_col,grid)





