c_ Solution:
    """
    @param: S: A string
    @return: all permutations
    """
    ___ stringPermutation2  S
        __ n.. S:
            r.. ['']

        S s..(S)

        ans    # list
        dfs(S, ans,    # list)
        r.. ans

    ___ dfs  S, ans, p..
        __ n.. S:
            ans.a..(''.j..(p..
            r..

        ___ i __ r..(l..(S:
            __ i > 0 a.. S[i] __ S[i - 1]:
                _____
            p...a..(S[i])
            dfs(S[:i] + S[i + 1:], ans, p..)
            p...p.. )
