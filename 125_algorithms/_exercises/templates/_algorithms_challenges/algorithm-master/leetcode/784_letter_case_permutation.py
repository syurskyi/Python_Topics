c_ Solution:
    ___ letterCasePermutation  s
        """
        :type s: str
        :rtype: List[str]
        """
        __ n.. s:
            r.. ['']
        ans    # list
        dfs(s, 0, ans, [])
        r.. ans

    ___ dfs  s, i, ans, path
        __ i __ l..(s
            ans.a..(''.j..(path))
            r..

        options = [s[i]] __ s[i].i.. ____ [s[i].l.., s[i].u..]

        ___ c __ options:
            path.a..(c)
            dfs(s, i + 1, ans, path)
            path.pop()
