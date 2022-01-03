c_ Solution:
    ___ totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        Xs = set()
        DLs = set()  # left diagonal lines
        DRs = set()  # right diagonal lines
        r.. divide_conquer(n, 0, 0, Xs, DLs, DRs)

    ___ divide_conquer(self, n, y, cnt, Xs, DLs, DRs):
        ___ x __ r..(n):
            __ x __ Xs:
                continue

            dl = x - y
            __ dl __ DLs:
                continue

            dr = x + y
            __ dr __ DRs:
                continue

            __ y __ n - 1:
                cnt += 1
                continue

            Xs.add(x)
            DLs.add(dl)
            DRs.add(dr)
            cnt = divide_conquer(n, y + 1, cnt, Xs, DLs, DRs)
            Xs.discard(x)
            DLs.discard(dl)
            DRs.discard(dr)

        r.. cnt
