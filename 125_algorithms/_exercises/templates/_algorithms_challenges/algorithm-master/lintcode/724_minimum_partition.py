c_ Solution:
    ___ findMin  nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        target = s..(nums)
        dp = [F..] * (target + 1)
        dp[0] = T..

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
