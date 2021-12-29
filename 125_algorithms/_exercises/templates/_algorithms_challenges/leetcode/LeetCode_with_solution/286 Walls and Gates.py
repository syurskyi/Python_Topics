"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ___ wallsAndGates(self, mat):
        """
        bfs
        O(mn), abstract level

        reference: https://leetcode.com/discuss/60170/6-lines-o-mn-python-bfs
        :type mat: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = [(i, j) for i, row in enumerate(mat) for j, val in enumerate(row) __ val == 0]
        for i, j in q:  # iterator
            for d in self.dirs:
                i1, j1 = i+d[0], j+d[1]
                __ 0 <= i1 < len(mat) and 0 <= j1 < len(mat[0]) and mat[i1][j1] > mat[i][j]+1:
                    mat[i1][j1] = mat[i][j]+1
                    q.append((i1, j1))


class Solution_slow(object):
    ___ __init__(self):
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ___ wallsAndGates(self, rooms):
        """
        bfs
        O(kmn) where k is #0s
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        __ not rooms: return
        m = len(rooms)
        __ not m: return
        n = len(rooms[0])

        for i in xrange(m):
            for j in xrange(n):
                __ rooms[i][j] == 0:
                    self.bfs_deque(rooms, i, j)

    ___ bfs(self, rooms, x, y):
        m = len(rooms)
        n = len(rooms[0])
        level = 0
        q = [(x, y)]
        while q:
            l = len(q)
            for idx in xrange(l):
                i, j = q[idx]
                rooms[i][j] = min(rooms[i][j], level)
                for d in self.dirs:
                    i_t = i+d[0]
                    j_t = j+d[1]
                    __ 0 <= i_t < m and 0 <= j_t < n and rooms[i_t][j_t] != -1 and rooms[i_t][j_t] >= level+1:
                        q.append((i_t, j_t))

            q = q[l:]
            level += 1

    ___ bfs_deque(self, rooms, x, y):
        from collections import deque

        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        q.append((x, y, 0))
        while q:
            i, j, level = q.popleft()
            rooms[i][j] = min(rooms[i][j], level)
            for d in self.dirs:
                i_t, j_t = i+d[0], j+d[1]
                __ 0 <= i_t < m and 0 <= j_t < n and rooms[i_t][j_t] != -1 and rooms[i_t][j_t] >= level+1:
                    q.append((i_t, j_t, level+1))


class Solution_error(object):
    ___ __init__(self):
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ___ wallsAndGates(self, rooms):
        """
        post-order DFS

        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        __ not rooms: return
        m = len(rooms)
        __ not m: return
        n = len(rooms[0])

        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                __ not visited[i][j]:
                    self.dfs(rooms, i, j, visited)

    ___ dfs(self, rooms, i, j, visited):
        __ not visited[i][j]:
            visited[i][j] = True
            for d in self.dirs:
                nxt_i = i+d[0]
                nxt_j = j+d[1]
                __ rooms[nxt_i][nxt_j] != -1:
                    rooms[nxt_i][nxt_j] = min(rooms[nxt_i][nxt_j], self.dfs(rooms, nxt_i, nxt_j, visited)+1)

        return rooms[nxt_i][nxt_j]




