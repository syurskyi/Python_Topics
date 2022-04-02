c_ Solution:
    ___ firstUniqChar  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. -1

        freq    # dict

        ___ c __ s:
            freq[c] = freq.get(c, 0) + 1

        ___ i __ r..(l..(s)):
            __ freq[s[i]] __ 1:
                r.. i

        r.. -1
