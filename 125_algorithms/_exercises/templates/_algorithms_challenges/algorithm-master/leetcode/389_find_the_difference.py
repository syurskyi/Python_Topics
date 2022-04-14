c_ Solution:
    ___ findTheDifference  s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a o..('a')
        ans o..(t[-1]) - a

        ___ i __ r..(l..(s:
            ans ^= o..(s[i]) - a
            ans ^= o..(t[i]) - a

        r.. chr(ans + a)


c_ Solution:
    ___ findTheDifference  s, t
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
                freq[c] 0

            freq[c] += 1

        ___ c __ t:
            __ c n.. __ freq:
                r.. c

            freq[c] -_ 1

        ___ c, cnt __ freq.i..
            __ cnt:
                r.. c

        r.. ''
