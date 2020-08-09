#!/usr/bin/python3
"""
premium question
"""
from typing ______ List
______ heapq


dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    ___ shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        No friction rolling ball

        F[i][j][dir] = min distance given direction
        S[i][j] = whether stoppable

        Dijkstra's algorith, reduce to a graph problem
        """
        m, n = le.(maze), le.(maze[0])
        D = [[float("inf") for _ in range(n)] for _ in range(m)]  # distance matrix
        i, j = start
        D[i][j] = 0
        q = [(0, i, j)]
        w___ q:
            dist, i, j = heapq.heappop(q)
            for di, dj in dirs:
                cur_dist = 0
                I = i
                J = j
                # look ahead
                w___ 0 <= I + di < m and 0 <= J + dj < n and maze[I + di][J + dj] __ 0:
                    I += di
                    J += dj
                    cur_dist += 1

                __ dist + cur_dist < D[I][J]:
                    D[I][J] = dist + cur_dist
                    heapq.heappush(q, (D[I][J], I, J))

        i, j = destination
        r_ D[i][j] __ D[i][j] != float("inf") else -1


__ __name__ __ "__main__":
    assert Solution().shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]) __ 12
