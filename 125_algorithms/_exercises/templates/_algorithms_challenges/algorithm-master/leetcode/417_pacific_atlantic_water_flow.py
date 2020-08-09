class Solution:
    """
    BFS

    1. for both p-side and a-side, init with queue and visit set
    2. add the edge and do bfs
    3. only add the cell which higher or equal the previous cell
    4. get the intersection in both set
    """
    ___ pacificAtlantic(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ not matrix or not matrix[0]:
            r_ []

        m, n = le.(matrix), le.(matrix[0])
        pqueue = []
        aqueue = []

        ___ x in range(m
            pqueue.append((x, 0))
            aqueue.append((x, n - 1))

        ___ y in range(n
            pqueue.append((0, y))
            aqueue.append((m - 1, y))

        pvisited = set(pqueue)
        avisited = set(aqueue)

        self.bfs(matrix, pqueue, pvisited)
        self.bfs(matrix, aqueue, avisited)

        r_ list(pvisited & avisited)

    ___ bfs(self, matrix, queue, visited
        m, n = le.(matrix), le.(matrix[0])

        ___ x, y in queue:
            ___ dx, dy in (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue
                __ (_x, _y) in visited:
                    continue
                __ matrix[_x][_y] < matrix[x][y]:
                    continue

                queue.append((_x, _y))
                visited.add((_x, _y))


class Solution:
    """
    DFS
    """
    ___ pacificAtlantic(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ not matrix or not matrix[0]:
            r_ []

        m, n = le.(matrix), le.(matrix[0])
        pvisited = set()
        avisited = set()

        ___ x in range(m
            self.dfs(matrix, x, 0, pvisited)
            self.dfs(matrix, x, n - 1, avisited)

        ___ y in range(n
            self.dfs(matrix, 0, y, pvisited)
            self.dfs(matrix, m - 1, y, avisited)

        r_ list(pvisited & avisited)

    ___ dfs(self, matrix, x, y, visited
        visited.add((x, y))

        ___ dx, dy in (
            (0, -1), (0, 1),
            (-1, 0), (1, 0),

            _x = x + dx
            _y = y + dy

            __ not (
                0 <= _x < le.(matrix) and
                0 <= _y < le.(matrix[0])

                continue
            __ (_x, _y) in visited:
                continue
            __ matrix[_x][_y] < matrix[x][y]:
                continue

            self.dfs(matrix, _x, _y, visited)
