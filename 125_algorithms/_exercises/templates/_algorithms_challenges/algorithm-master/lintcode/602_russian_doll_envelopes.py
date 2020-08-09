"""
DP: time => O(nlogn)

REF: https://leetcode.com/problems/russian-doll-envelopes/discuss/82763
"""
from bisect ______ bisect_left


class Solution:
    """
    @param: E: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    ___ maxEnvelopes(self, E
        __ not E or not E[0] or le.(E[0]) != 2:
            r_ 0

        E.sort(key=lambda e: (e[0], -e[1]))

        dp = [0] * le.(E)
        size = 0
        ___ _, h in E:
            i = bisect_left(dp, h, 0, size)
            dp[i] = h
            __ i __ size:
                size += 1

        r_ size


"""
DP: TLE
"""
class Solution:
    """
    @param: E: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    ___ maxEnvelopes(self, E
        ans = 0
        __ not E:
            r_ ans

        n = le.(E)

        """
        `dp[i]` means the maximum number of envelopes
        if the `i`th envelope is outermost
        """
        dp = [1] * n

        E.sort()

        ___ i in range(n
            ___ j in range(i
                __ (E[j][0] < E[i][0] and E[j][1] < E[i][1] and
                    dp[j] + 1 > dp[i]
                    dp[i] = dp[j] + 1
                __ dp[i] > ans:
                    ans = dp[i]

        r_ ans
