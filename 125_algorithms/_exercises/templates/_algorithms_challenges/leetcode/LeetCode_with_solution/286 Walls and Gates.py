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
        q = [(i, j) ___ i, row __ enumerate(mat) ___ j, val __ enumerate(row) __ val __ 0]
        ___ i, j __ q:  # iterator
            ___ d __ self.dirs:
                i1, j1 = i+d[0], j+d[1]
                __ 0 <= i1 < l..(mat) and 0 <= j1 < l..(mat[0]) and mat[i1][j1] > mat[i][j]+1:
                    mat[i1][j1] = mat[i][j]+1
                    q.a..((i1, j1))


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
        __ n.. rooms: r..
        m = l..(rooms)
        __ n.. m: r..
        n = l..(rooms[0])

        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ rooms[i][j] __ 0:
                    self.bfs_deque(rooms, i, j)

    ___ bfs(self, rooms, x, y):
        m = l..(rooms)
        n = l..(rooms[0])
        level = 0
        q = [(x, y)]
        while q:
            l = l..(q)
            ___ idx __ xrange(l):
                i, j = q[idx]
                rooms[i][j] = m..(rooms[i][j], level)
                ___ d __ self.dirs:
                    i_t = i+d[0]
                    j_t = j+d[1]
                    __ 0 <= i_t < m and 0 <= j_t < n and rooms[i_t][j_t] != -1 and rooms[i_t][j_t] >= level+1:
                        q.a..((i_t, j_t))

            q = q[l:]
            level += 1

    ___ bfs_deque(self, rooms, x, y):
        ____ collections _______ deque

        m = l..(rooms)
        n = l..(rooms[0])
        q = deque()
        q.a..((x, y, 0))
        while q:
            i, j, level = q.popleft()
            rooms[i][j] = m..(rooms[i][j], level)
            ___ d __ self.dirs:
                i_t, j_t = i+d[0], j+d[1]
                __ 0 <= i_t < m and 0 <= j_t < n and rooms[i_t][j_t] != -1 and rooms[i_t][j_t] >= level+1:
                    q.a..((i_t, j_t, level+1))


class Solution_error(object):
    ___ __init__(self):
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ___ wallsAndGates(self, rooms):
        """
        post-order DFS

        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        __ n.. rooms: r..
        m = l..(rooms)
        __ n.. m: r..
        n = l..(rooms[0])

        visited = [[False ___ _ __ xrange(n)] ___ _ __ xrange(m)]
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ n.. visited[i][j]:
                    self.dfs(rooms, i, j, visited)

    ___ dfs(self, rooms, i, j, visited):
        __ n.. visited[i][j]:
            visited[i][j] = True
            ___ d __ self.dirs:
                nxt_i = i+d[0]
                nxt_j = j+d[1]
                __ rooms[nxt_i][nxt_j] != -1:
                    rooms[nxt_i][nxt_j] = m..(rooms[nxt_i][nxt_j], self.dfs(rooms, nxt_i, nxt_j, visited)+1)

        r.. rooms[nxt_i][nxt_j]




