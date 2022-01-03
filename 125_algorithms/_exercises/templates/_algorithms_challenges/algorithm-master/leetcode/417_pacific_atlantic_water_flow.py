c_ Solution:
    """
    BFS

    1. for both p-side and a-side, init with queue and visit set
    2. add the edge and do bfs
    3. only add the cell which higher or equal the previous cell
    4. get the intersection in both set
    """
    ___ pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. []

        m, n = l..(matrix), l..(matrix[0])
        pqueue    # list
        aqueue    # list

        ___ x __ r..(m):
            pqueue.a..((x, 0))
            aqueue.a..((x, n - 1))

        ___ y __ r..(n):
            pqueue.a..((0, y))
            aqueue.a..((m - 1, y))

        pvisited = set(pqueue)
        avisited = set(aqueue)

        bfs(matrix, pqueue, pvisited)
        bfs(matrix, aqueue, avisited)

        r.. l..(pvisited & avisited)

    ___ bfs(self, matrix, queue, visited):
        m, n = l..(matrix), l..(matrix[0])

        ___ x, y __ queue:
            ___ dx, dy __ (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),
            ):
                _x = x + dx
                _y = y + dy

                __ n.. (0 <= _x < m a.. 0 <= _y < n):
                    continue
                __ (_x, _y) __ visited:
                    continue
                __ matrix[_x][_y] < matrix[x][y]:
                    continue

                queue.a..((_x, _y))
                visited.add((_x, _y))


c_ Solution:
    """
    DFS
    """
    ___ pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. []

        m, n = l..(matrix), l..(matrix[0])
        pvisited = set()
        avisited = set()

        ___ x __ r..(m):
            dfs(matrix, x, 0, pvisited)
            dfs(matrix, x, n - 1, avisited)

        ___ y __ r..(n):
            dfs(matrix, 0, y, pvisited)
            dfs(matrix, m - 1, y, avisited)

        r.. l..(pvisited & avisited)

    ___ dfs(self, matrix, x, y, visited):
        visited.add((x, y))

        ___ dx, dy __ (
            (0, -1), (0, 1),
            (-1, 0), (1, 0),
        ):
            _x = x + dx
            _y = y + dy

            __ n.. (
                0 <= _x < l..(matrix) a..
                0 <= _y < l..(matrix[0])
            ):
                continue
            __ (_x, _y) __ visited:
                continue
            __ matrix[_x][_y] < matrix[x][y]:
                continue

            dfs(matrix, _x, _y, visited)
