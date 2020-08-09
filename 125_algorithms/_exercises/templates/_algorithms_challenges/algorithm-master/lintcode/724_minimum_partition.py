class Solution:
    ___ findMin(self, nums
        """
        :type nums: list[int]
        :rtype: int
        """
        __ not nums:
            r_ 0

        target = su.(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        ans = float('inf')

        ___ num in nums:
            ___ i in range(target, num - 1, -1
                dp[i] = dp[i] or dp[i - num]

                __ dp[i]:
                    ans = min(
                        ans,
                        abs(target - i * 2)
                    )

        r_ ans
