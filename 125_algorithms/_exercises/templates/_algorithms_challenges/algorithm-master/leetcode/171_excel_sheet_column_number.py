c_ Solution:
    ___ titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. 0

        s = s.u..

        ans = 0
        BASE = ord('A') - 1

        ___ char __ s:
            ans = ans * 26 + ord(char) - BASE

        r.. ans
