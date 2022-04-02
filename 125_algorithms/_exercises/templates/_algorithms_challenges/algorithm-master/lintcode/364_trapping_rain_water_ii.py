____ heapq _______ heappush, heappop

c_ Solution:
    """
    @param: heights: a matrix of integers
    @return: an integer
    """
    ___ trapRainWater  heights
        __ n.. heights:
            r.. 0
        m, n = l..(heights), l..(heights[0])
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        ans = bound = x = y = i = 0
        bounds    # list
        visited = [[0 ___ _ __ r..(n)] ___ _ __ r..(m)]

        # Put the cells on the matrix boundaries into `bounds`
        ___ i __ r..(m
            heappush(bounds, (heights[i][0], i, 0))
            visited[i][0] = 1
            heappush(bounds, (heights[i][n - 1], i, n - 1))
            visited[i][n - 1] = 1
        ___ i __ r..(1, n - 1
            heappush(bounds, (heights[0][i], 0, i))
            visited[0][i] = 1
            heappush(bounds, (heights[m - 1][i], m - 1, i))
            visited[m - 1][i] = 1

        w.... bounds:
            # Find the min bound of any current boundary
            bound, x, y = heappop(bounds)
            # To keep the water in, keep finding the boundary
            ___ i __ r..(4
                _x = x + dx[i]
                _y = y + dy[i]
                __ 0 <= _x < m a.. 0 <= _y < n a.. n.. visited[_x][_y]:
                    visited[_x][_y] = 1
                    # Choosing the boundary of current cell
                    # if its lower than the bound outside
                    # than this cell will store water
                    # otherwise this cell will become the new boundary
                    _bound = m..(bound, heights[_x][_y])
                    heappush(bounds, (_bound, _x, _y))
                    __ _bound > heights[_x][_y]:
                        ans += _bound - heights[_x][_y]
        r.. ans
