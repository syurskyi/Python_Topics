class Solution:
    ___ findTheDifference(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = ord('a')
        ans = ord(t[-1]) - a

        ___ i in range(le.(s)):
            ans ^= ord(s[i]) - a
            ans ^= ord(t[i]) - a

        r_ chr(ans + a)


class Solution:
    ___ findTheDifference(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        __ not t:
            r_ ''

        freq = {}

        ___ c in s:
            __ c not in freq:
                freq[c] = 0

            freq[c] += 1

        ___ c in t:
            __ c not in freq:
                r_ c

            freq[c] -= 1

        ___ c, cnt in freq.items(
            __ cnt:
                r_ c

        r_ ''
