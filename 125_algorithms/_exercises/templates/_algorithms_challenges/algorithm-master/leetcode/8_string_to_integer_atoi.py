c_ Solution:
    ___ myAtoi  s
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        __ n.. s:
            r.. ans

        INT_MAX = 0x7FFFFFFF
        N = l..(s)
        ZERO = o..('0')

        sign = 1
        i = 0

        w.... i < N a.. s[i] __ ' ':
            i += 1

        __ i < N a.. s[i] __ ('+', '-'
            sign = -1 __ s[i] __ '-' ____ 1
            i += 1

        w.... i < N a.. s[i].i..
            val = o..(s[i]) - ZERO

            __ (ans > INT_MAX // 10 o.
                (ans __ INT_MAX // 10 a.. val > 7:
                r.. INT_MAX __ sign __ 1 ____ ~INT_MAX

            ans = ans * 10 + val
            i += 1

        r.. sign * ans
