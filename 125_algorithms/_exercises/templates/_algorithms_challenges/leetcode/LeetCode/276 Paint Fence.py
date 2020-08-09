"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ numWays_oneliner(self, n, k
        r_ 0 __ n < 1 else su.(reduce(lambda F, i: [(k-1)*(F[0]+F[1]), F[0]], xrange(1, n), [k, 0]))

    ___ numWays(self, n, k
        """
        You need to abstract number of colors to binary value (is different color)

        Let F1[i] be the number of ways for A[:i] with last two with different colors
            F2[i] be the number of ways for A[:i] with last two with same color

        F1[i] = (k-1)*(F1[i-1]+F2[i-1])
        F2[i] = F1[i-1]

        Optimize the space since only depends on i and i-1

        :type n: int
        :type k: int
        :rtype: int
        """
        __ n < 1:
            r_ 0

        num_diff = k
        num_same = 0
        ___ _ in xrange(1, n
            num_diff, num_same = (k-1)*(num_diff+num_same), num_diff

        r_ num_diff+num_same

    ___ numWays_MLE2(self, n, k
        """
        DP
        Let F[i][j][l] be the number of ways of painting for A[:i] with A[i-1] as color j and A[i-2] as color l
        :type n: int
        :type k: int
        :rtype: int
        """
        __ n < 1:
            r_ 0

        F = [[[0 ___ _ in xrange(k)] ___ _ in xrange(k)] ___ _ in xrange(2)]
        EMPTY = 0

        ___ j0 in xrange(k
            F[1][j0][EMPTY] = 1

        ___ i in xrange(2, n+1
            ___ j0 in xrange(k
                ___ j1 in xrange(k
                    F[i%2][j0][j1] = 0

            ___ j0 in xrange(k
                ___ j1 in xrange(k
                    ___ j2 in xrange(k
                        __ i __ 2:
                            F[i%2][j0][j1] = F[(i-1)%2][j1][EMPTY]

                        ____ j1 __ j2 and j0 != j1:
                            F[i%2][j0][j1] += F[(i-1)%2][j1][j2]
                        ____ j1 != j2:
                            F[i%2][j0][j1] += F[(i-1)%2][j1][j2]

        ret = 0
        ___ j0 in xrange(k
            ___ j1 in xrange(k
                ret += F[n%2][j0][j1]

        r_ ret

    ___ numWays_MLE(self, n, k
        """
        DP
        let F[i][j][l] be the number of ways of painting for A[:i] with A[i-1] as color j and A[i-2] as color l
        :type n: int
        :type k: int
        :rtype: int
        """
        __ n < 1:
            r_ 0

        F = [[[0 ___ _ in xrange(k)] ___ _ in xrange(k)] ___ _ in xrange(n+1)]
        EMPTY = 0

        ___ j0 in xrange(k
            F[1][j0][EMPTY] = 1

        ___ i in xrange(2, n+1
            ___ j0 in xrange(k
                ___ j1 in xrange(k
                    ___ j2 in xrange(k
                        __ i __ 2:
                            F[i][j0][j1] = F[i-1][j1][EMPTY]

                        ____ j1 __ j2 and j0 != j1:
                            F[i][j0][j1] += F[i-1][j1][j2]
                        ____ j1 != j2:
                            F[i][j0][j1] += F[i-1][j1][j2]

        ret = 0
        ___ j0 in xrange(k
            ___ j1 in xrange(k
                ret += F[n][j0][j1]

        r_ ret


__ __name__ __ "__main__":
    assert Solution().numWays(3, 2) __ 6


