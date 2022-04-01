c_ Solution:
    """
    @param S: Generating set of rules.
    @param s: Start symbol.
    @param e: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    ___ canBeGenerated  S, start, end):
        __ n.. start:
            start = ''

        N    # dict

        ___ s __ S:
            cur, nxt = s.s..(' -> ')
            __ cur n.. __ N:
                N[cur] = s..()
            N[cur].add(nxt)

        r.. dfs(N, end, start)

    ___ dfs  N, end, s):
        __ l..(s) > l..(end):
            r.. F..
        __ s __ end:
            r.. T..

        ___ i __ r..(l..(s)):
            __ (n.. o..('A') <= o..(s[i]) <= o..('Z') o.
                s[i] n.. __ N):
                _____

            ___ _s __ N[s[i]]:
                res = dfs(N, end, s[:i] + _s + s[i + 1:])
                __ res:
                    r.. T..

        r.. F..
