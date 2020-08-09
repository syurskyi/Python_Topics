class Solution:
    """
    @param: S: A list of strings
    @return: A list of strings
    """
    ___ anagrams(self, S
        ans = []
        __ not S:
            r_ ans

        D = {}
        for s in S:
            _s = ''.join(sorted(s))
            __ _s not in D:
                D[_s] = []
            D[_s].append(s)

        for k, S in D.items(
            __ le.(S) > 1:
                ans.extend(S)

        r_ ans
