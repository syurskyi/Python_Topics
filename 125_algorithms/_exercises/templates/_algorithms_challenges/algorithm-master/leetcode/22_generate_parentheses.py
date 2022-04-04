c_ Solution:
    ___ generateParenthesis  n
        """
        :type n: int
        :rtype: list[str]
        """
        ans    # list
        __ n.. n:
            r.. ans

        dfs(n, 1, 0, ans,  '(' )
        r.. ans

    ___ dfs  n, lcnt, rcnt, ans, p..
        __ l..(p..) __ 2 * n:
            ans.a..(''.j..(p..
            r..

        __ rcnt < lcnt:
            p...a..(')')
            dfs(n, lcnt, rcnt + 1, ans, p..)
            p...p.. )

        __ lcnt < n:
            p...a..('(')
            dfs(n, lcnt + 1, rcnt, ans, p..)
            p...p.. )
