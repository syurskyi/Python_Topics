#!/usr/bin/python3
"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and
attempts to make exactly K moves. The rows and columns are 0 indexed, so the
top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move
is two squares in a cardinal direction, then one square in an orthogonal
direction.

[Image]

Each time the knight is to move, it chooses one of eight possible moves
uniformly at random (even if the piece would go off the chessboard) and moves
there.

The knight continues moving until it has made exactly K moves or has moved off
the chessboard. Return the probability that the knight remains on the board
after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on
the board.
From each of those positions, there are also two moves that will keep the knight
on the board.
The total probability the knight stays on the board is 0.0625.
"""
dirs = (
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
)


class Solution:
    ___ knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """
        brute force K step

        with memory, it is considered dp
        """
        q = set([(r, c)])  # working que
        P = [[0 ___ _ __ range(N)] ___ _ __ range(N)]
        P[r][c] = 1  # optimize memory
        k = 0
        w___ k < K:
            k += 1
            cur_q = set()
            cur_P = [[0 ___ _ __ range(N)] ___ _ __ range(N)]
            ___ i, j __ q:
                ___ di, dj __ dirs:
                    I = i + di
                    J = j + dj
                    __ 0 <= I < N and 0 <= J < N:
                        cur_q.add((I, J))
                        cur_P[I][J] += P[i][j] * 1 / 8

            q = cur_q
            P = cur_P

        r_ su.([
            P[i][j]
            ___ i __ range(N)
            ___ j __ range(N)
        ])


    ___ knightProbability_error(self, N: int, K: int, r: int, c: int) -> float:
        """
        brute force K step
        """
        q = [(r, c)]  # working que
        P = [[0 ___ _ __ range(N)] ___ _ __ range(N)]
        P[r][c] = 1  # optimize memory
        k = 0
        w___ k < K:
            k += 1
            cur_q =   # list
            cur_P = [[0 ___ _ __ range(N)] ___ _ __ range(N)]
            ___ i, j __ q:
                ___ di, dj __ dirs:
                    I = i + di
                    J = j + dj
                    __ 0 <= I < N and 0 <= J < N:
                        cur_q.append((I, J))  # error, count multiple times
                        cur_P[I][J] += P[i][j] * 1 / 8

            q = cur_q
            P = cur_P

        r_ su.([
            P[i][j]
            ___ i __ range(N)
            ___ j __ range(N)
        ])


__  -n __ "__main__":
    assert Solution().knightProbability(3, 2, 0, 0)  __ 0.0625
    assert Solution().knightProbability(3, 3, 0, 0)  __ 0.015625
