c_ Solution:
    """
    @param: s: A string
    @return: An integer
    """
    ___ atoi(self, s):
        NOT_FOUND = 0
        __ n.. s:
            r.. NOT_FOUND

        n = l..(s)
        is_negative = F..
        left, right = 0, n - 1

        w.... left < n a.. s[left] __ ' ':
            left += 1
        w.... right >= 0 a.. s[right] __ ' ':
            right -= 1

        __ left < n a.. s[left] __ ('+', '-'):
            is_negative = (s[left] __ '-')
            left += 1

        __ left > right:
            r.. NOT_FOUND

        ans = 0
        zero = ord('0')
        nine = ord('9')
        INT_MAX = 0x7FFFFFFF
        INT_MIN = -0x80000000
        w.... left <= right a.. zero <= ord(s[left]) <= nine:
            ans = ans * 10 + ord(s[left]) - zero
            left += 1

        __ is_negative:
            ans *= -1

        __ ans > INT_MAX:
            r.. INT_MAX
        __ ans < INT_MIN:
            r.. INT_MIN

        r.. ans
