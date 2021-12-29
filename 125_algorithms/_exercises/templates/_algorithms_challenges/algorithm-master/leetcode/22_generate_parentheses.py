class Solution:
    ___ generateParenthesis(self, n):
        """
        :type n: int
        :rtype: list[str]
        """
        ans    # list
        __ n.. n:
            r.. ans

        self.dfs(n, 1, 0, ans, ['('])
        r.. ans

    ___ dfs(self, n, lcnt, rcnt, ans, path):
        __ l..(path) __ 2 * n:
            ans.a..(''.join(path))
            r..

        __ rcnt < lcnt:
            path.a..(')')
            self.dfs(n, lcnt, rcnt + 1, ans, path)
            path.pop()

        __ lcnt < n:
            path.a..('(')
            self.dfs(n, lcnt + 1, rcnt, ans, path)
            path.pop()
