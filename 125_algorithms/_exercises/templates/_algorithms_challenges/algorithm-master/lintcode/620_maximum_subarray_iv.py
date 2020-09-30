class Solution:
    """
    @param: A: an array of integer
    @param: k: an integer
    @return: the largest sum
    """
    ___ maxSubarray4(self, A, k
        __ not A:
            r_ 0
        n = le.(A)
        __ n < k:
            r_ 0

        ans = float('-inf')
        Smin = 0
        S = [0] * (n + 1)

        ___ i __ range(1, n + 1
            S[i] = S[i - 1] + A[i - 1]

            """
            in prefix sum, `i` means the size,
            and ignoring that iteration if `i` < `k`
            """
            __ i < k:
                continue

            __ S[i] - Smin > ans:
                ans = S[i] - Smin

            """
            to get the segment sum of `k` children and ended at `i`
            => [i - k + 1, i]
            """
            __ S[i - k + 1] < Smin:
                Smin = S[i - k + 1]

        r_ ans
