___ count_islands(grid
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
    ___ row __ r..(l..(grid)):
        ___ col __ r..(l..(grid[0])):
            __ grid[row][col] __ 1:
                mark_islands(row,col,grid)
                islands += 1



    r.. islands



















___ mark_islands(i, j, grid
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.


    grid[i][j] = '#'


    ___ n_row,n_col __ ((i + 1,j),(i -1,j),(i,j + 1),(i,j-1)):
        __ 0 <= n_row < l..(grid) a.. 0 <= n_col < l..(grid[0]) a.. grid[n_row][n_col] __ 1:
            mark_islands(n_row,n_col,grid)





