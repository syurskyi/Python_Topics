class Solution:
    """
    @param: k: An integer
    @param: n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    ___ digitCounts(self, k, n):
        ans = 0
        for i in range(n + 1):
            ans += self.count(k, i)
        return ans

    ___ count(self, k, a):
        __ k == a == 0:
            return 1

        cnt = 0
        while a:
            __ a % 10 == k:
                cnt += 1
            a //= 10
        return cnt
