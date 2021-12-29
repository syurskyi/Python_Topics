def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0         # var. for the counts
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if grid[r][c] == 1:
                islands += 1
                mark_islands(r,c,grid)
            print(r, c, islands)
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    if (i>=0) and (j>=0) and (i<=len(grid)-1) and (j<=len(grid[i])-1):
        print(f'inside mark_islands row:{i} column:{j} value:{grid[i][j]}')
        if grid[i][j] == 1:
            grid[i][j] = '#'      # one way to mark visited ones - suggestion.
            mark_islands(i-1, j, grid)
            mark_islands(i+1, j, grid)
            mark_islands(i, j-1, grid)
            mark_islands(i, j+1, grid)


squares = [[1, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 0]]


print(count_islands(squares))
