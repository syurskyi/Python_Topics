class Solution:
    """
    @param: s: A string
    @return: An integer
    """
    ___ atoi(self, s
        NOT_FOUND = 0
        __ not s:
            r_ NOT_FOUND

        n = le.(s)
        is_negative = False
        left, right = 0, n - 1

        w___ left < n and s[left] __ ' ':
            left += 1
        w___ right >= 0 and s[right] __ ' ':
            right -= 1

        __ left < n and s[left] in ('+', '-'
            is_negative = (s[left] __ '-')
            left += 1

        __ left > right:
            r_ NOT_FOUND

        ans = 0
        zero = ord('0')
        nine = ord('9')
        INT_MAX = 0x7FFFFFFF
        INT_MIN = -0x80000000
        w___ left <= right and zero <= ord(s[left]) <= nine:
            ans = ans * 10 + ord(s[left]) - zero
            left += 1

        __ is_negative:
            ans *= -1

        __ ans > INT_MAX:
            r_ INT_MAX
        __ ans < INT_MIN:
            r_ INT_MIN

        r_ ans
