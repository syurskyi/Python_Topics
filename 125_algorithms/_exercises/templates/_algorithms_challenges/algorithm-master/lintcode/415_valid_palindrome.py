c_ Solution:
    ___ isPalindrome  s
        """
        :type s: str
        :rtype: bool
        """
        __ n.. s:
            r.. T..

        s = s.l..
        n = l..(s)
        left, right = 0, n - 1

        w.... left < right:
            w.... left < right a.. n.. s[left].i..
                left += 1
            w.... left < right a.. n.. s[right].i..
                right -= 1

            __ s[left] != s[right]:
                r.. F..

            left += 1
            right -= 1

        r.. T..
