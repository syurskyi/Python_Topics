"""
DP:
time: O(n^2)
space: O(n)
"""
class Solution:
    ___ PredictTheWinner(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ not nums:
            r_ False

        n = le.(nums)
        dp = [0] * n

        ___ i in range(n - 1, -1, -1
            ___ j in range(i + 1, n
                dp[j] = max(
                    nums[i] - dp[j],
                    nums[j] - dp[j - 1]
                )

        r_ dp[n - 1] >= 0


"""
DP:
time: O(n^2)
space: O(n^2)
"""
class Solution:
    ___ PredictTheWinner(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ not nums:
            r_ False

        n = le.(nums)
        dp = [[0] * n ___ _ in range(n)]

        ___ i in range(n - 1, -1, -1
            ___ j in range(i + 1, n
                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],
                    nums[j] - dp[i][j - 1]
                )

        r_ dp[0][n - 1] >= 0
