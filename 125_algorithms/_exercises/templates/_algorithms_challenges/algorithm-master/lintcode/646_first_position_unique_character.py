c_ Solution:
    """
    @param: s: a string
    @return: it's index
    """
    ___ firstUniqChar  s
        __ n.. s:
            r.. -1

        D    # dict
        ___ c __ s:
            D[c] = D.g.. c, 0) + 1

        i = 0
        ___ c __ s:
            __ D[c] __ 1:
                r.. i
            i += 1

        r.. -1
