c_ Solution o..
    ___ numberOfPatterns  m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        used = [False] * 9
        res = 0
        ___ l __ r.. m, n + 1):
            res += calc_patterns(used, -1, l)
            used = [False] * 9
        r_ res

    ___ is_valid  used, index, last):
        # markded
        __ used[index]:
            r_ False
        # first digit
        __ last __ -1:
            r_ True
        # adjacent cells (in a row or in a column)
        __ (last + index) % 2 __ 1:
            r_ True
        mid = (last + index) / 2
        __ mid __ 4:
            r_ used[mid]
        # adjacent cells on diagonal
        __ (index % 3 != last % 3) and (index / 3 != last / 3):
            r_ True
        # all other cells which are not adjacent
        r_ used[mid]

    ___ calc_patterns  used, last, length):
        __ length __ 0:
            r_ 1
        res = 0
        ___ i __ r.. 9):
            __ is_valid(used, i, last):
                used[i] = True
                res += calc_patterns(used, i, length - 1)
                used[i] = False
        r_ res
