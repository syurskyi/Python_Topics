#!/usr/bin/python3
"""
premium question
"""
____ t___ _______ L..
_______ heapq


dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


c_ Solution:
    ___ shortestDistance  maze: L..[L..[i..]], start: L..[i..], destination: L..[i..]) __ i..:
        """
        No friction rolling ball

        F[i][j][dir] = min distance given direction
        S[i][j] = whether stoppable

        Dijkstra's algorith, reduce to a graph problem
        """
        m, n = l..(maze), l..(maze[0])
        D = [[f__("inf") ___ _ __ r..(n)] ___ _ __ r..(m)]  # distance matrix
        i, j = start
        D[i][j] = 0
        q = [(0, i, j)]
        w.... q:
            dist, i, j = heapq.heappop(q)
            ___ di, dj __ dirs:
                cur_dist = 0
                I = i
                J = j
                # look ahead
                w.... 0 <= I + di < m a.. 0 <= J + dj < n a.. maze[I + di][J + dj] __ 0:
                    I += di
                    J += dj
                    cur_dist += 1

                __ dist + cur_dist < D[I][J]:
                    D[I][J] = dist + cur_dist
                    heapq.heappush(q, (D[I][J], I, J))

        i, j = destination
        r.. D[i][j] __ D[i][j] != f__("inf") ____ -1


__ _______ __ _______
    ... Solution().shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]) __ 12
