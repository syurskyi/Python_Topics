class Solution:
    ___ firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            return -1

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for i in range(len(s)):
            __ freq[s[i]] == 1:
                return i

        return -1
