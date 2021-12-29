class Solution:
    ___ myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        __ n.. s:
            r.. ans

        INT_MAX = 0x7FFFFFFF
        N = l..(s)
        ZERO = ord('0')

        sign = 1
        i = 0

        while i < N and s[i] __ ' ':
            i += 1

        __ i < N and s[i] __ ('+', '-'):
            sign = -1 __ s[i] __ '-' ____ 1
            i += 1

        while i < N and s[i].isdigit():
            val = ord(s[i]) - ZERO

            __ (ans > INT_MAX // 10 o.
                (ans __ INT_MAX // 10 and val > 7)):
                r.. INT_MAX __ sign __ 1 ____ ~INT_MAX

            ans = ans * 10 + val
            i += 1

        r.. sign * ans
