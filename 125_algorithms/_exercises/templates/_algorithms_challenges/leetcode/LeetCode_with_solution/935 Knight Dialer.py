#!/usr/bin/python3
"""
A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of a phone pad
(indicated above), and the knight makes N-1 hops.  Each hop must be from one key
to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it
presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.


Example 1:
Input: 1
Output: 10

Example 2:
Input: 2
Output: 20

Example 3:
Input: 3
Output: 46

Note:
1 <= N <= 5000
"""


MOD = 10 ** 9 + 7


dirs = [
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
]

nbrs = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}


____ collections _______ defaultdict


class Solution:
    ___ knightDialer(self, N: int) -> int:
        """
        DP
        F[pos][step] = sum(F[nbr][step+1] for all nbr)
        """
        F = defaultdict(l....: defaultdict(int))
        ___ pos __ r..(10):
            F[pos][N-1] = 1

        ___ n __ r..(N-2, -1, -1):
            ___ pos __ r..(10):
                ___ nbr __ nbrs[pos]:
                    F[pos][n] += F[nbr][n+1]
                    F[pos][n] %= MOD

        ret = 0
        ___ i __ r..(10):
            ret += F[i][0]
            ret %= MOD

        r.. ret


class SolutionTLE2:
    ___ __init__(self):
        self.cache = {}

    ___ knightDialer(self, N: int) -> int:
        ret = 0
        ___ i __ r..(10):
            ret += self.dfs(i, N-1)
            ret %= MOD

        r.. ret

    ___ dfs(self, i, r):
        __ (i, r) n.. __ self.cache:
            ret = 0
            __ r __ 0:
                ret = 1
            ____:
                ___ nbr __ nbrs[i]:
                    ret += self.dfs(nbr, r-1)

            self.cache[i, r] = ret

        r.. self.cache[i, r]


class SolutionTLE:
    ___ __init__(self):
        # row, col size
        self.m = 4
        self.n = 3
        self.cache = {}

    ___ knightDialer(self, N: int) -> int:
        ret = 0
        ___ i __ r..(self.m):
            ___ j __ r..(self.n):
                __ (i, j) != (3, 0) a.. (i, j) != (3, 2):
                    ret += self.dfs(i, j, N-1)
                    ret %= MOD
        r.. ret

    ___ dfs(self, i, j, r):
        __ (i, j, r) n.. __ self.cache:
            ret = 0
            __ r __ 0:
                ret = 1
            ____:
                ___ di, dj __ dirs:
                    I = i + di
                    J = j + dj
                    __ 0 <= I < self.m a.. 0 <= J < self.n a.. (I, J) != (3, 0) a.. (I, J) != (3, 2):
                        ret += self.dfs(I, J, r - 1)
                        ret %= MOD

            self.cache[i, j, r] = ret

        r.. self.cache[i, j, r]


__ __name__ __ "__main__":
    ... Solution().knightDialer(1) __ 10
    ... Solution().knightDialer(2) __ 20
    ... Solution().knightDialer(3) __ 46
