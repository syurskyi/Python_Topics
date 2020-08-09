class Solution:
    """
    @param: k: An integer
    @param: n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    ___ digitCounts(self, k, n
        ans = 0
        for i in range(n + 1
            ans += self.count(k, i)
        r_ ans

    ___ count(self, k, a
        __ k __ a __ 0:
            r_ 1

        cnt = 0
        w___ a:
            __ a % 10 __ k:
                cnt += 1
            a //= 10
        r_ cnt
