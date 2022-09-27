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


MOD 10 ** 9 + 7


dirs [
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
]

nbrs {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: t..(),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}


____ c.. _______ d..


c_ Solution:
    ___ knightDialer  N: i.. __ i..
        """
        DP
        F[pos][step] = sum(F[nbr][step+1] for all nbr)
        """
        F d..(l....: d..(i..
        ___ pos __ r..(10
            F[pos][N-1] 1

        ___ n __ r..(N-2, -1, -1
            ___ pos __ r..(10
                ___ nbr __ nbrs[pos]:
                    F[pos][n] += F[nbr][n+1]
                    F[pos][n] %= MOD

        ret 0
        ___ i __ r..(10
            ret += F[i][0]
            ret %= MOD

        r.. ret


c_ SolutionTLE2:
    ___ -
        cache    # dict

    ___ knightDialer  N: i.. __ i..
        ret 0
        ___ i __ r..(10
            ret += dfs(i, N-1)
            ret %= MOD

        r.. ret

    ___ dfs  i, r
        __ (i, r) n.. __ cache:
            ret 0
            __ r __ 0:
                ret 1
            ____
                ___ nbr __ nbrs[i]:
                    ret += dfs(nbr, r-1)

            cache[i, r] ret

        r.. cache[i, r]


c_ SolutionTLE:
    ___ -
        # row, col size
        m 4
        n 3
        cache    # dict

    ___ knightDialer  N: i.. __ i..
        ret 0
        ___ i __ r..(m
            ___ j __ r..(n
                __ (i, j) !_ (3, 0) a.. (i, j) !_ (3, 2
                    ret += dfs(i, j, N-1)
                    ret %= MOD
        r.. ret

    ___ dfs  i, j, r
        __ (i, j, r) n.. __ cache:
            ret 0
            __ r __ 0:
                ret 1
            ____
                ___ di, dj __ dirs:
                    I i + di
                    J j + dj
                    __ 0 <_ I < m a.. 0 <_ J < n a.. (I, J) !_ (3, 0) a.. (I, J) !_ (3, 2
                        ret += dfs(I, J, r - 1)
                        ret %= MOD

            cache[i, j, r] ret

        r.. cache[i, j, r]


__ _______ __ _______
    ... Solution().knightDialer(1) __ 10
    ... Solution().knightDialer(2) __ 20
    ... Solution().knightDialer(3) __ 46
