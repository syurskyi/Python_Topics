"""
DP:
time: O(n^2)
space: O(n)
"""
c_ Solution:
    ___ PredictTheWinner  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums:
            r.. F..

        n = l..(nums)
        dp = [0] * n

        ___ i __ r..(n - 1, -1, -1
            ___ j __ r..(i + 1, n
                dp[j] = m..(
                    nums[i] - dp[j],
                    nums[j] - dp[j - 1]
                )

        r.. dp[n - 1] >_ 0


"""
DP:
time: O(n^2)
space: O(n^2)
"""
c_ Solution:
    ___ PredictTheWinner  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        __ n.. nums:
            r.. F..

        n = l..(nums)
        dp = [[0] * n ___ _ __ r..(n)]

        ___ i __ r..(n - 1, -1, -1
            ___ j __ r..(i + 1, n
                dp[i][j] = m..(
                    nums[i] - dp[i + 1][j],
                    nums[j] - dp[i][j - 1]
                )

        r.. dp[0][n - 1] >_ 0
