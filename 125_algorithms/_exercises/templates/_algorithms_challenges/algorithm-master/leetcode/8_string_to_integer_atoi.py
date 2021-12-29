class Solution:
    ___ myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        __ not s:
            return ans

        INT_MAX = 0x7FFFFFFF
        N = len(s)
        ZERO = ord('0')

        sign = 1
        i = 0

        while i < N and s[i] == ' ':
            i += 1

        __ i < N and s[i] in ('+', '-'):
            sign = -1 __ s[i] == '-' else 1
            i += 1

        while i < N and s[i].isdigit():
            val = ord(s[i]) - ZERO

            __ (ans > INT_MAX // 10 or
                (ans == INT_MAX // 10 and val > 7)):
                return INT_MAX __ sign == 1 else ~INT_MAX

            ans = ans * 10 + val
            i += 1

        return sign * ans
