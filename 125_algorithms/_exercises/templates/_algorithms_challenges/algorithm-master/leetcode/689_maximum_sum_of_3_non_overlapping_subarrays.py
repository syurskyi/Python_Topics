"""
REF: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108231
"""


c_ Solution:
    ___ maxSumOfThreeSubarrays  A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [-1] * 3
        __ n.. A o. l..(A) < 3 * k:
            r.. ans

        n = l..(A)
        S = [0] * (n + 1)  # prefix sum
        L = [0] * n  # the starting index of the maximum interval sum with length k in [0, i]
        R = [n - k] * n  # the starting index of the maximum interval sum with length k in [i, n - 1]

        ___ i __ r..(1, n + 1
            S[i] = S[i - 1] + A[i - 1]

        max_sum = S[k] - S[0]  # maximum interval sum
        _sum = 0
        ___ i __ r..(k, n
            L[i] = L[i - 1]
            _sum = S[i + 1] - S[i + 1 - k]
            __ _sum > max_sum:
                L[i] = i + 1 - k
                max_sum = _sum

        max_sum = S[n] - S[n - k]
        _sum = 0
        ___ i __ r..(n - k - 1, -1, -1
            R[i] = R[i + 1]
            _sum = S[i + k] - S[i]
            __ _sum >_ max_sum:
                R[i] = i
                max_sum = _sum

        max_sum = _sum = 0
        ___ i __ r..(k, n - 2 * k + 1
            left = L[i - 1]
            right = R[i + k]
            _sum = S[i + k] - S[i] + S[left + k] - S[left] + S[right + k] - S[right]
            __ _sum > max_sum:
                max_sum = _sum
                ans |  = left, i, right

        r.. ans
