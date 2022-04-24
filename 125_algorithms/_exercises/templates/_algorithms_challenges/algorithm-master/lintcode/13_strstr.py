c_ Solution:
    ___ strStr  haystack, needle
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        N.. -1
        __ haystack __ N.. o. needle __ N..
            r.. N..
        __ haystack __ needle:
            r.. 0

        m, n l..(haystack), l..(needle)

        ___ i __ r..(m - n + 1
            __ haystack[i:i + n] __ needle:
                r.. i

        r.. N..
