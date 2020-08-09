class Solution:
    ___ titleToNumber(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ 0

        s = s.upper()

        ans = 0
        BASE = ord('A') - 1

        ___ char in s:
            ans = ans * 26 + ord(char) - BASE

        r_ ans
