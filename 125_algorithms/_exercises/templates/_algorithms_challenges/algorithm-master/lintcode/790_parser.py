class Solution:
    """
    @param S: Generating set of rules.
    @param s: Start symbol.
    @param e: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    ___ canBeGenerated(self, S, start, end):
        __ n.. start:
            start = ''

        N = {}

        ___ s __ S:
            cur, nxt = s.s..(' -> ')
            __ cur n.. __ N:
                N[cur] = set()
            N[cur].add(nxt)

        r.. self.dfs(N, end, start)

    ___ dfs(self, N, end, s):
        __ l..(s) > l..(end):
            r.. False
        __ s __ end:
            r.. True

        ___ i __ r..(l..(s)):
            __ (n.. ord('A') <= ord(s[i]) <= ord('Z') o.
                s[i] n.. __ N):
                continue

            ___ _s __ N[s[i]]:
                res = self.dfs(N, end, s[:i] + _s + s[i + 1:])
                __ res:
                    r.. True

        r.. False
