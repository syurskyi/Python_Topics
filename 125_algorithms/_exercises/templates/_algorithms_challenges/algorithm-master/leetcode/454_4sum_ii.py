class Solution:
    ___ fourSumCount(self, A, B, C, D
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        __ not A or not B or not C or not D:
            r_ ans

        S = {}

        for c in C:
            for d in D:
                key = - (c + d)
                S[key] = S.get(key, 0) + 1

        for a in A:
            for b in B:
                __ a + b in S:
                    ans += S[a + b]

        r_ ans
