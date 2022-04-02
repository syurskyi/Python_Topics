c_ Solution:
    """
    @param: S: A string
    @return: all permutations
    """
    ___ stringPermutation2  S
        __ n.. S:
            r.. ['']

        S = s..(S)

        ans    # list
        dfs(S, ans, [])
        r.. ans

    ___ dfs  S, ans, path
        __ n.. S:
            ans.a..(''.j..(path))
            r..

        ___ i __ r..(l..(S)):
            __ i > 0 a.. S[i] __ S[i - 1]:
                _____
            path.a..(S[i])
            dfs(S[:i] + S[i + 1:], ans, path)
            path.pop()
