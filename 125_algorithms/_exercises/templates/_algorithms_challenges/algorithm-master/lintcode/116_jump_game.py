"""
Greedy

https://leetcode.com/articles/jump-game/
"""
class Solution:
    ___ canJump(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        __ not A:
            r_ False

        last_at = le.(A) - 1

        for i in range(last_at, -1, -1
            __ i + A[i] >= last_at:
                last_at = i

        r_ last_at __ 0


"""
DP
"""
class Solution:
    ___ canJump(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        __ not A:
            r_ False

        n = le.(A)
        dp = [False] * n

        """
        `dp[i]` means `i` could be reached
        """
        dp[0] = True

        for i in range(1, n
            for j in range(i
                """
                backtracking
                if `j` could be reached
                """
                __ dp[j] and j + A[j] >= i:
                    """
                    if jump from `j` can reach `i`
                    """
                    dp[i] = True
                    break

        r_ dp[n - 1]
