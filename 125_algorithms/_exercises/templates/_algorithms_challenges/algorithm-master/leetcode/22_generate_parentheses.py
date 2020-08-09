class Solution:
    ___ generateParenthesis(self, n
        """
        :type n: int
        :rtype: list[str]
        """
        ans = []
        __ not n:
            r_ ans

        self.dfs(n, 1, 0, ans, ['('])
        r_ ans

    ___ dfs(self, n, lcnt, rcnt, ans, path
        __ le.(path) __ 2 * n:
            ans.append(''.join(path))
            r_

        __ rcnt < lcnt:
            path.append(')')
            self.dfs(n, lcnt, rcnt + 1, ans, path)
            path.pop()

        __ lcnt < n:
            path.append('(')
            self.dfs(n, lcnt + 1, rcnt, ans, path)
            path.pop()
