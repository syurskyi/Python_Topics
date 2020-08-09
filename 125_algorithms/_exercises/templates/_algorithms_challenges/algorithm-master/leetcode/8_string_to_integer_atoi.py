class Solution:
    ___ myAtoi(self, s
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        __ not s:
            r_ ans

        INT_MAX = 0x7FFFFFFF
        N = le.(s)
        ZERO = ord('0')

        sign = 1
        i = 0

        w___ i < N and s[i] __ ' ':
            i += 1

        __ i < N and s[i] in ('+', '-'
            sign = -1 __ s[i] __ '-' else 1
            i += 1

        w___ i < N and s[i].isdigit(
            val = ord(s[i]) - ZERO

            __ (ans > INT_MAX // 10 or
                (ans __ INT_MAX // 10 and val > 7)):
                r_ INT_MAX __ sign __ 1 else ~INT_MAX

            ans = ans * 10 + val
            i += 1

        r_ sign * ans
