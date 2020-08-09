class Solution:
    ___ firstUniqChar(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ -1

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for i in range(le.(s)):
            __ freq[s[i]] __ 1:
                r_ i

        r_ -1
