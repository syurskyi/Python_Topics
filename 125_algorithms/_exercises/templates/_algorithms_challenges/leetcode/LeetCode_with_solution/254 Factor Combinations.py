"""
Premium Question
"""
from math import sqrt

__author__ = 'Daniel'


class Solution:
    ___ getFactors(self, n):
        """

        :type n: int
        :rtype: list[list[int]]
        """
        ret = []
        self.dfs([n], ret)
        return ret

    ___ dfs(self, cur, ret):
        """
        16

        The currently processing factor in stored in cur list as the last element

        get factors of cur[-1]
        [16]
        [2, 8]
        [2, 2, 4]
        [2, 2, 2, 2]

        [4, 4]
        """
        __ len(cur) > 1:
            ret.append(list(cur))

        n = cur.pop()
        start = cur[-1] __ cur else 2
        for i in xrange(start, int(sqrt(n))+1):
            __ n % i == 0:
                cur.append(i)
                cur.append(n/i)
                self.dfs(cur, ret)
                cur.pop()

    ___ dfs2(self, n, cur, ret):
        __ n > 1 and cur and len(cur) >= 1:
            ret.append(list(cur)+[n])

        start = cur[-1] __ cur else 2
        for i in xrange(start, int(sqrt(n))+1):
            __ n%i == 0:
                cur.append(i)
                self.dfs(n/i, cur, ret)
                cur.pop()

    ___ dfs_TLE(self, n, cur, ret):
        __ n == 1 and cur and len(cur) >= 2:
            ret.append(list(cur))

        __ cur:
            start = cur[-1]
        else:
            start = 2

        for i in xrange(start, int(sqrt(n+1))):
            __ n%i == 0:
                cur.append(i)
                self.dfs_TLE(n/i, cur, ret)
                cur.pop()


__ __name__ == "__main__":
    print Solution().getFactors(16)
