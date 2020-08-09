class Solution:
    ___ strStr(self, haystack, needle
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        NOT_FOUND = -1
        __ haystack is None or needle is None:
            r_ NOT_FOUND
        __ haystack __ needle:
            r_ 0

        m, n = le.(haystack), le.(needle)

        ___ i in range(m - n + 1
            __ haystack[i:i + n] __ needle:
                r_ i

        r_ NOT_FOUND
