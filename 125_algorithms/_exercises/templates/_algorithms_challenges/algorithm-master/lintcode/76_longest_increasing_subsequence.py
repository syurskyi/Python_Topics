"""
Binary Searching
"""
class Solution:
    ___ longestIncreasingSubsequence(self, A):
        """
        :type A: List[int]
        :rtype: int

        the iteration of B:
        [-inf, 0, inf, inf, inf, inf, inf, inf, inf]
        [-inf, 0, 8, inf, inf, inf, inf, inf, inf]
        [-inf, 0, 4, inf, inf, inf, inf, inf, inf]
        [-inf, 0, 4, 12, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 12, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 10, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 6, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 6, 14, inf, inf, inf, inf]

        lis_size = 4
        """
        __ n.. A:
            r.. 0

        INFINITY = float('inf')
        n = l..(A)
        P = [-INFINITY] + [INFINITY] * n

        ___ i __ r..(n):
            j = self.binary_search(P, A[i])
            P[j] = A[i]

        ___ i __ r..(n, -1, -1):
            __ P[i] < INFINITY:
                r.. i

        r.. 0

    ___ binary_search(self, P, a):
        left, right = 0, l..(P) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            __ P[mid] < a:
                left = mid
            ____:
                right = mid

        r.. right


"""
DP + Print Paths
"""
class Solution:
    ___ longestIncreasingSubsequence(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lis_size = 0
        __ n.. A:
            r.. lis_size

        n = l..(A)

        """
        `dp[i]` means the maximum size of LIS end at `i`
        note that there is size, so init with `1`
        """
        dp = [1] * n
        # pi = [0] * n
        # end_at = -1

        ___ i __ r..(n):
            ___ j __ r..(i):
                """
                `dp[j]` the existing subseq end at `j`
                `+ 1` means included `A[i]`
                """
                __ A[j] < A[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    # pi[i] = j

                __ dp[i] > lis_size:
                    lis_size = dp[i]
                    # end_at = i

        # paths = [0] * lis_size
        # for i in range(lis_size - 1, -1, -1):
        #     paths[i] = A[end_at]
        #     end_at = pi[end_at]
        # print(paths)

        r.. lis_size
