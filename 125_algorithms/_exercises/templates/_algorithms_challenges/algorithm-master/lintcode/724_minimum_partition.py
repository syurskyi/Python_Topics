class Solution:
    ___ findMin(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        target = s..(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        ans = float('inf')

        ___ num __ nums:
            ___ i __ r..(target, num - 1, -1):
                dp[i] = dp[i] o. dp[i - num]

                __ dp[i]:
                    ans = m..(
                        ans,
                        abs(target - i * 2)
                    )

        r.. ans
