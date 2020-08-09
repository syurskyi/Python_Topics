class Solution:
    ___ firstUniqChar(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ -1

        freq = {}

        ___ c in s:
            freq[c] = freq.get(c, 0) + 1

        ___ i in range(le.(s)):
            __ freq[s[i]] __ 1:
                r_ i

        r_ -1
