class Solution:
    """
    @param S: Generating set of rules.
    @param s: Start symbol.
    @param e: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    ___ canBeGenerated(self, S, start, end
        __ not start:
            start = ''

        N = {}

        ___ s __ S:
            cur, nxt = s.split(' -> ')
            __ cur not __ N:
                N[cur] = set()
            N[cur].add(nxt)

        r_ self.dfs(N, end, start)

    ___ dfs(self, N, end, s
        __ le.(s) > le.(end
            r_ False
        __ s __ end:
            r_ True

        ___ i __ range(le.(s)):
            __ (not ord('A') <= ord(s[i]) <= ord('Z') or
                s[i] not __ N
                continue

            ___ _s __ N[s[i]]:
                res = self.dfs(N, end, s[:i] + _s + s[i + 1:])
                __ res:
                    r_ True

        r_ False
