class Solution:
    ___ topKFrequent(self, A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        __ not A:
            r_ ans

        F = {}
        ___ a in A:
            F[a] = F.get(a, 0) + 1

        ___ a, _ in sorted(F.items(), key=lambda x: -x[1]
            __ k __ 0:
                break

            ans.append(a)
            k -= 1

        r_ ans
