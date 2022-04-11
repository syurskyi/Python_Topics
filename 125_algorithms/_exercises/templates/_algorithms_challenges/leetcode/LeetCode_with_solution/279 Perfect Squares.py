"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum
to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
_______ m__
_______ ___

__author__ 'Daniel'


c_ Solution(o..
    F [0]  # static dp for all test cases

    ___ numSquares  n
        """
        static dp
        F_i = min(F_{i - j^2}+1, \forall j)

        O(n), think it as a tree, cache tree O(m+n) = O(2n); rather than O(n sqrt(n))
        backward
        """
        w.... l..(Solution.F) <_ n:
            i l..(Solution.F)
            Solution.F.a..(___.maxint)
            j 1
            w.... i - j*j >_ 0:
                Solution.F[i] m..(Solution.F[i], Solution.F[i-j*j]+1)
                j += 1

        r.. Solution.F[n]

    ___ numSquares_bfs  n
        """
        bfs
        the q stores the intermediate result of sum of squares 
        :type n: int
        :rtype: int
        """
        q [0]
        visited [F.. ___ _ __ x..(n+1)]

        level 0
        w.... q:
            level += 1
            l l..(q)
            ___ i __ x..(l
                ___ j __ x..(1, i..(m__.sqrt(n+1
                    nxt q[i]+j*j
                    __ nxt <_ n a.. visited[nxt]:
                        _____
                    ____ nxt < n:
                        visited[nxt] T..
                        q.a..(nxt)
                    ____ nxt __ n:
                        r.. level
                    ____
                        _____
            q q[l:]

        r.. N..

    ___ numSquares_TLE  n
        """
        DP
        :type n: int
        :rtype: int
        """
        F [i ___ i __ x..(n+1)]
        ___ i __ x..(1, n+1
            ___ j __ x..(1, i..(m__.sqrt(i+1
                __ i-j*j >_ 0:
                    F[i] m..(F[i], F[i-j*j]+1)

        r.. F[n]


__ _______ __ _______
    ... Solution().numSquares(6) __ 3