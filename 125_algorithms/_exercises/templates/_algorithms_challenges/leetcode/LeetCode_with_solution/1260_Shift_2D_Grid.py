c_ Solution o..
    ___ shiftGrid  grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # m * n temp array
        new_grid = [[0] * l.. grid[0]) ___ _ __ r.. l.. grid))]
        m = l.. grid)
        n = l.. grid[0])
        # Compute final location
        true_k = k % (m * n)
        # row move
        move_i = true_k / n
        # col move
        move_j = true_k % n

        ___ i __ r.. m):
            ___ j __ r.. n):
                new_i = i + move_i
                # move one row if move_j + j >= n
                __ move_j + j >= n:
                    new_i += 1
                new_i %= m
                new_j = (j + move_j) % n
                new_grid[new_i][new_j] = grid[i][j]
        r_ new_grid
