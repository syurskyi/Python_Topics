"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the
volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water are trapped between the blocks. The total volume of water trapped is 4.
"""
______ heapq

__author__ = 'Daniel'


class Cell:
    ___ __init__(self, i, j, h
        self.i = i
        self.j = j
        self.h = h

    ___ __cmp__(self, other
        r_ self.h - other.h


class Solution(object
    ___ __init__(self
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ trapRainWater(self, mat
        """
        Find the min height with no water that higher than the current height and keep it.
        Starting from the min height with no water
        Do BFS with heap (similar to Dijkstra's algorithm)

        :param mat: List[List[int]]
        :return: an integer
        """
        __ not mat: r_ 0

        m, n = le.(mat), le.(mat[0])
        visited = [[False ___ _ in xrange(n)] ___ _ in xrange(m)]
        h = []
        # add cells at the four edges
        ___ i in xrange(m
            visited[i][0] = True
            heapq.heappush(h, Cell(i, 0, mat[i][0]))
            visited[i][n-1] = True
            heapq.heappush(h, Cell(i, n-1, mat[i][n-1]))

        ___ j in xrange(1, n-1
            visited[0][j] = True
            heapq.heappush(h, Cell(0, j, mat[0][j]))
            visited[m-1][j] = True
            heapq.heappush(h, Cell(m-1, j, mat[m-1][j]))

        # BFS with heap
        trapped = 0
        w___ h:
            cur = heapq.heappop(h)
            ___ dir in self.dirs:
                I, J = cur.i+dir[0], cur.j+dir[1]
                __ 0 <= I < m and 0 <= J < n and not visited[I][J]:
                    nxt = Cell(I, J, mat[I][J])
                    __ nxt.h < cur.h:  # fill
                        trapped += cur.h - nxt.h
                        nxt.h = cur.h

                    visited[I][J] = True
                    heapq.heappush(h, nxt)

        r_ trapped


__ __name__ __ "__main__":
    assert Solution().trapRainWater([
        [12, 13, 0, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13]]
    ) __ 14
    assert Solution().trapRainWater([
        [9, 1, 10, 10],
        [9, 1, 2, 8],
        [2, 6, 5, 0],
        [6, 0, 9, 0]]
    ) __ 0
