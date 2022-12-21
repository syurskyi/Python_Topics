c_ Solution o..
    ___ lengthOfLongestSubstringTwoDistinct  s
        """
        :type s: str
        :rtype: int
        """
        i, j, maxLen = 0, -1, 0
        # i for start, k for end, j for latest pos contains different character from k
        ___ k __ r.. 1, l.. s)):
            __ s[k] __ s[k - 1]:
                c_
            __ j >= 0 and s[j] != s[k]:
                maxLen = m..(k - i, maxLen)
                # update i
                i = j + 1
            # update
            j = k - 1
        r_ m..(l.. s) - i, maxLen)