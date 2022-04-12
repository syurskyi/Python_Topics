"""
DP: time => O(nlogn)

REF: https://leetcode.com/problems/russian-doll-envelopes/discuss/82763
"""
____ b__ _______ bisect_left


c_ Solution:
    """
    @param: E: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    ___ maxEnvelopes  E
        __ n.. E o. n.. E[0] o. l..(E 0 !_ 2:
            r.. 0

        E.s..(k.._l.... e: (e[0], -e[1]

        dp [0] * l..(E)
        size 0
        ___ _, h __ E:
            i bisect_left(dp, h, 0, size)
            dp[i] h
            __ i __ size:
                size += 1

        r.. size


"""
DP: TLE
"""
c_ Solution:
    """
    @param: E: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    ___ maxEnvelopes  E
        ans 0
        __ n.. E:
            r.. ans

        n l..(E)

        """
        `dp[i]` means the maximum number of envelopes
        if the `i`th envelope is outermost
        """
        dp [1] * n

        E.s..()

        ___ i __ r..(n
            ___ j __ r..(i
                __ (E[j][0] < E[i][0] a.. E[j][1] < E[i][1] a..
                    dp[j] + 1 > dp[i]
                    dp[i] dp[j] + 1
                __ dp[i] > ans:
                    ans dp[i]

        r.. ans
