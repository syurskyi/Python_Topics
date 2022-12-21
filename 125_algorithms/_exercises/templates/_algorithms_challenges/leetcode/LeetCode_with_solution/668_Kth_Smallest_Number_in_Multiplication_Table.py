c_ Solution:
    ___ findKthNumber  m: i.., n: i.., k: i..   i..:
        # https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solution/
        ___ enough(x
            count = 0
            # ith row [i, 2*i, 3*i, ..., n*i]
            # for each column, k = x // i
            ___ i __ r.. 1, m+1
                count += min(x // i, n)
            r_ count >= k

        lo, hi = 1, m * n
        w.. lo < hi:
            mi = (lo + hi) // 2
            __ n.. enough(mi
                lo = mi + 1
            ____
                hi = mi
        r_ lo
