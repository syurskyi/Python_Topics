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

    ___ dfs  s, i, ans, p..
        __ i __ l..(s
            ans.a..(''.j..(p..
            r..

        options = [s[i]] __ s[i].i.. ____ [s[i].l.., s[i].u..]

        ___ c __ options:
            p...a..(c)
            dfs(s, i + 1, ans, p..)
            p...p.. )
