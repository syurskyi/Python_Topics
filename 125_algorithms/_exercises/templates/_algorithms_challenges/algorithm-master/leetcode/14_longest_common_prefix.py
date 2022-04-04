c_ Solution:
    ___ longestCommonPrefix  strs
        """
        :type strs: List[str]
        :rtype: str
        """
        __ n.. strs o. n.. strs[0]:
            r.. ''

        t = strs[0]
        ___ i __ r..(l..(t:
            ___ s __ strs:
                __ i >_ l..(s) o. s[i] != t[i]:
                    r.. t[:i]

        r.. t
