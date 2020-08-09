"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum
to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
______ ma__
______ sys

__author__ = 'Daniel'


class Solution(object
    F = [0]  # static dp for all test cases

    ___ numSquares(self, n
        """
        static dp
        F_i = min(F_{i - j^2}+1, \forall j)

        O(n), think it as a tree, cache tree O(m+n) = O(2n); rather than O(n sqrt(n))
        backward
        """
        w___ le.(Solution.F) <= n:
            i = le.(Solution.F)
            Solution.F.append(sys.maxint)
            j = 1
            w___ i - j*j >= 0:
                Solution.F[i] = min(Solution.F[i], Solution.F[i-j*j]+1)
                j += 1

        r_ Solution.F[n]

    ___ numSquares_bfs(self, n
        """
        bfs
        the q stores the intermediate result of sum of squares 
        :type n: int
        :rtype: int
        """
        q = [0]
        visited = [False ___ _ in xrange(n+1)]

        level = 0
        w___ q:
            level += 1
            l = le.(q)
            ___ i in xrange(l
                ___ j in xrange(1, int(ma__.sqrt(n))+1
                    nxt = q[i]+j*j
                    __ nxt <= n and visited[nxt]:
                        continue
                    ____ nxt < n:
                        visited[nxt] = True
                        q.append(nxt)
                    ____ nxt __ n:
                        r_ level
                    ____
                        break
            q = q[l:]

        r_ None

    ___ numSquares_TLE(self, n
        """
        DP
        :type n: int
        :rtype: int
        """
        F = [i ___ i in xrange(n+1)]
        ___ i in xrange(1, n+1
            ___ j in xrange(1, int(ma__.sqrt(i))+1
                __ i-j*j >= 0:
                    F[i] = min(F[i], F[i-j*j]+1)

        r_ F[n]


__ __name__ __ "__main__":
    assert Solution().numSquares(6) __ 3