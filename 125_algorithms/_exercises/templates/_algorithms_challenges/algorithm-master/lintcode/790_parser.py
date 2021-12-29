class Solution:
    """
    @param S: Generating set of rules.
    @param s: Start symbol.
    @param e: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    ___ canBeGenerated(self, S, start, end):
        __ not start:
            start = ''

        N = {}

        for s in S:
            cur, nxt = s.split(' -> ')
            __ cur not in N:
                N[cur] = set()
            N[cur].add(nxt)

        return self.dfs(N, end, start)

    ___ dfs(self, N, end, s):
        __ len(s) > len(end):
            return False
        __ s == end:
            return True

        for i in range(len(s)):
            __ (not ord('A') <= ord(s[i]) <= ord('Z') or
                s[i] not in N):
                continue

            for _s in N[s[i]]:
                res = self.dfs(N, end, s[:i] + _s + s[i + 1:])
                __ res:
                    return True

        return False
