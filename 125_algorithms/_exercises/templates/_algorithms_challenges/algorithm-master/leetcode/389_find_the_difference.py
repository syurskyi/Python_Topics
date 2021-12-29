class Solution:
    ___ findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = ord('a')
        ans = ord(t[-1]) - a

        for i in range(len(s)):
            ans ^= ord(s[i]) - a
            ans ^= ord(t[i]) - a

        return chr(ans + a)


class Solution:
    ___ findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        __ not t:
            return ''

        freq = {}

        for c in s:
            __ c not in freq:
                freq[c] = 0

            freq[c] += 1

        for c in t:
            __ c not in freq:
                return c

            freq[c] -= 1

        for c, cnt in freq.items():
            __ cnt:
                return c

        return ''
