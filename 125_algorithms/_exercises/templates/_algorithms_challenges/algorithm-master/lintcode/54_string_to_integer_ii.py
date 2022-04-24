c_ Solution:
    """
    @param: s: A string
    @return: An integer
    """
    ___ atoi  s
        N.. 0
        __ n.. s:
            r.. N..

        n l..(s)
        is_negative F..
        left, right 0, n - 1

        w.... left < n a.. s[left] __ ' ':
            left += 1
        w.... right >_ 0 a.. s[right] __ ' ':
            right -_ 1

        __ left < n a.. s[left] __ ('+', '-'
            is_negative (s[left] __ '-')
            left += 1

        __ left > right:
            r.. N..

        ans 0
        zero o..('0')
        nine o..('9')
        INT_MAX 0x7FFFFFFF
        INT_MIN -0x80000000
        w.... left <_ right a.. zero <_ o..(s[left]) <_ nine:
            ans ans * 10 + o..(s[left]) - zero
            left += 1

        __ is_negative:
            ans *= -1

        __ ans > INT_MAX:
            r.. INT_MAX
        __ ans < INT_MIN:
            r.. INT_MIN

        r.. ans
