class Solution:
    ___ totalNQueens(self, n
        """
        :type n: int
        :rtype: int
        """
        Xs = set()
        DLs = set()  # left diagonal lines
        DRs = set()  # right diagonal lines
        r_ self.divide_conquer(n, 0, 0, Xs, DLs, DRs)

    ___ divide_conquer(self, n, y, cnt, Xs, DLs, DRs
        ___ x in range(n
            __ x in Xs:
                continue

            dl = x - y
            __ dl in DLs:
                continue

            dr = x + y
            __ dr in DRs:
                continue

            __ y __ n - 1:
                cnt += 1
                continue

            Xs.add(x)
            DLs.add(dl)
            DRs.add(dr)
            cnt = self.divide_conquer(n, y + 1, cnt, Xs, DLs, DRs)
            Xs.discard(x)
            DLs.discard(dl)
            DRs.discard(dr)

        r_ cnt
