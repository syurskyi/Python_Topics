___ count_islands(grid
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands 0         # var. for the counts
    ___ r, row __ e..(grid
        ___ c, val __ e..(row
            __ grid[r][c] __ 1:
                islands += 1
                mark_islands(r,c,grid)
            print(r, c, islands)
    r.. islands


___ mark_islands(i, j, grid
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    __ (i>_0) a.. (j>_0) a.. (i<_l..(grid)-1) a.. (j<_l..(grid[i])-1
        print _*inside mark_islands row:{i} column:{j} value:{grid[i][j]}')
        __ grid[i][j] __ 1:
            grid[i][j] '#'      # one way to mark visited ones - suggestion.
            mark_islands(i-1, j, grid)
            mark_islands(i+1, j, grid)
            mark_islands(i, j-1, grid)
            mark_islands(i, j+1, grid)


squares [[1, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 0]]


print(count_islands(squares
