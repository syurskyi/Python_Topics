"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        """
        Skip matrix
        Encode rule for 2, 4, 6, 8, 5
        """
        self.skip = [[None ___ _ in xrange(10)] ___ _ in xrange(10)]
        self.skip[1][3], self.skip[3][1] = 2, 2
        self.skip[1][7], self.skip[7][1] = 4, 4
        self.skip[3][9], self.skip[9][3] = 6, 6
        self.skip[7][9], self.skip[9][7] = 8, 8
        self.skip[4][6], self.skip[6][4] = 5, 5
        self.skip[2][8], self.skip[8][2] = 5, 5
        self.skip[1][9], self.skip[9][1] = 5, 5
        self.skip[3][7], self.skip[7][3] = 5, 5

    ___ numberOfPatterns(self, m, n
        """
        NP - O(N!)
        dfs

        Maintain a skip matrix
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [False ___ _ in xrange(10)]
        r_ su.(
            self.dfs(1, visited, remain) * 4 +
            self.dfs(2, visited, remain) * 4 +
            self.dfs(5, visited, remain)
            ___ remain in xrange(m, n+1)
        )

    ___ dfs(self, cur, visited, remain
        """
        Return the count of combination
        Optimization - memoization
        """
        __ remain __ 1:
            r_ 1

        visited[cur] = True
        ret = 0
        ___ nxt in xrange(1, 10
            __ (
                not visited[nxt] and (
                    self.skip[cur][nxt] is None or
                    visited[self.skip[cur][nxt]]
                )

                ret += self.dfs(nxt, visited, remain - 1)

        visited[cur] = False
        r_ ret


__ __name__ __ "__main__":
    assert Solution().numberOfPatterns(1, 2) __ 65
    assert Solution().numberOfPatterns(1, 3) __ 385
