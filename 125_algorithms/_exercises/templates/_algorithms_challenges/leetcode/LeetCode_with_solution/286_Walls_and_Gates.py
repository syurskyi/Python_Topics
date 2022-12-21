c_ Solution o..
    ___ wallsAndGates  rooms
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # BFS with queue
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = l.. rooms)
        __ m __ 0:
            r_
        n = l.. rooms[0])
        q =    # list
        ___ row __ r.. m
            ___ col __ r.. n
                # gate
                __ rooms[row][col] __ 0:
                    q.append((row, col))

        w.. l.. q) > 0:
            point = q.pop(0)
            row, col = point[0], point[1]
            ___ d __ direction:
                r = row + d[0]
                c = col + d[1]
                # wall or out of rooms
                __ r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != 2147483647:
                    c_
                rooms[r][c] = rooms[row][col] + 1
                q.append((r, c))
