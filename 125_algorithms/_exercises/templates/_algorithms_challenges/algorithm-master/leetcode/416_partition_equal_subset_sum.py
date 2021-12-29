"""
REF: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592


`dp[s]` means the specific sum `s` can be gotten from the sum of subset in `nums`
"""


class Solution:
    ___ canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums:
            r.. True

        target = s..(nums)

        __ target & 1 __ 1:
            r.. False

        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True

        ___ a __ nums:
            ___ s __ r..(target, a - 1, -1):
                __ dp[s]:
                    continue

                dp[s] = dp[s - a]

        r.. dp[target]
