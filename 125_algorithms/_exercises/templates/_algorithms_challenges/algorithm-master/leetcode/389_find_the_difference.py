c_ Solution:
    ___ findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = ord('a')
        ans = ord(t[-1]) - a

        ___ i __ r..(l..(s)):
            ans ^= ord(s[i]) - a
            ans ^= ord(t[i]) - a

        r.. chr(ans + a)


c_ Solution:
    ___ findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        __ n.. t:
            r.. ''

        freq    # dict

        ___ c __ s:
            __ c n.. __ freq:
                freq[c] = 0

            freq[c] += 1

        ___ c __ t:
            __ c n.. __ freq:
                r.. c

            freq[c] -= 1

        ___ c, cnt __ freq.i..:
            __ cnt:
                r.. c

        r.. ''
