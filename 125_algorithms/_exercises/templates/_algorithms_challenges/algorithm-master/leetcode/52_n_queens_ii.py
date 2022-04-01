c_ Solution:
    ___ totalNQueens  n):
        """
        :type n: int
        :rtype: int
        """
        Xs = s..()
        DLs = s..()  # left diagonal lines
        DRs = s..()  # right diagonal lines
        r.. divide_conquer(n, 0, 0, Xs, DLs, DRs)

    ___ divide_conquer  n, y, cnt, Xs, DLs, DRs):
        ___ x __ r..(n):
            __ x __ Xs:
                _____

            dl = x - y
            __ dl __ DLs:
                _____

            dr = x + y
            __ dr __ DRs:
                _____

            __ y __ n - 1:
                cnt += 1
                _____

            Xs.add(x)
            DLs.add(dl)
            DRs.add(dr)
            cnt = divide_conquer(n, y + 1, cnt, Xs, DLs, DRs)
            Xs.discard(x)
            DLs.discard(dl)
            DRs.discard(dr)

        r.. cnt
