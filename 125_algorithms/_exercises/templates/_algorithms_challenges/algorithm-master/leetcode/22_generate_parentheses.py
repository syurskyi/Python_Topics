c_ Solution:
    ___ generateParenthesis  n):
        """
        :type n: int
        :rtype: list[str]
        """
        ans    # list
        __ n.. n:
            r.. ans

        dfs(n, 1, 0, ans, ['('])
        r.. ans

    ___ dfs  n, lcnt, rcnt, ans, path):
        __ l..(path) __ 2 * n:
            ans.a..(''.j..(path))
            r..

        __ rcnt < lcnt:
            path.a..(')')
            dfs(n, lcnt, rcnt + 1, ans, path)
            path.pop()

        __ lcnt < n:
            path.a..('(')
            dfs(n, lcnt + 1, rcnt, ans, path)
            path.pop()
