c_ Solution:
    ___ strStr  haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        NOT_FOUND = -1
        __ haystack __ N.. o. needle __ N..
            r.. NOT_FOUND
        __ haystack __ needle:
            r.. 0

        m, n = l..(haystack), l..(needle)

        ___ i __ r..(m - n + 1):
            __ haystack[i:i + n] __ needle:
                r.. i

        r.. NOT_FOUND
