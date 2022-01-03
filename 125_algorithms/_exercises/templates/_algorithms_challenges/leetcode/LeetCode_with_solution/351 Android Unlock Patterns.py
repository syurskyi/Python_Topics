"""
Premium Question
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ - ):
        """
        Skip matrix
        Encode rule for 2, 4, 6, 8, 5
        """
        skip = [[N.. ___ _ __ xrange(10)] ___ _ __ xrange(10)]
        skip[1][3], skip[3][1] = 2, 2
        skip[1][7], skip[7][1] = 4, 4
        skip[3][9], skip[9][3] = 6, 6
        skip[7][9], skip[9][7] = 8, 8
        skip[4][6], skip[6][4] = 5, 5
        skip[2][8], skip[8][2] = 5, 5
        skip[1][9], skip[9][1] = 5, 5
        skip[3][7], skip[7][3] = 5, 5

    ___ numberOfPatterns(self, m, n):
        """
        NP - O(N!)
        dfs

        Maintain a skip matrix
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [F.. ___ _ __ xrange(10)]
        r.. s..(
            dfs(1, visited, remain) * 4 +
            dfs(2, visited, remain) * 4 +
            dfs(5, visited, remain)
            ___ remain __ xrange(m, n+1)
        )

    ___ dfs(self, cur, visited, remain):
        """
        Return the count of combination
        Optimization - memoization
        """
        __ remain __ 1:
            r.. 1

        visited[cur] = T..
        ret = 0
        ___ nxt __ xrange(1, 10):
            __ (
                n.. visited[nxt] a.. (
                    skip[cur][nxt] __ N.. o.
                    visited[skip[cur][nxt]]
                )
            ):
                ret += dfs(nxt, visited, remain - 1)

        visited[cur] = F..
        r.. ret


__ __name__ __ "__main__":
    ... Solution().numberOfPatterns(1, 2) __ 65
    ... Solution().numberOfPatterns(1, 3) __ 385
