___ spiral(size
    result = [[None] * size ___ _ in range(size)]
    row, col = 0, 0
    dr, dc = 0, 1
    ___ step in range(1, size * size + 1
        result[row][col] = step
        __ not ((0 <= col + dc < size) and (0 <= row + dr < size) and result[row + dr][col + dc] is None
            dr, dc = dc, -dr
        row, col = row + dr, col + dc
    r_ result
