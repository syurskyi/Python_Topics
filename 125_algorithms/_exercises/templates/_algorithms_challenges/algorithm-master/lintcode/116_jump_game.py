"""
Greedy

https://leetcode.com/articles/jump-game/
"""
class Solution:
    ___ canJump(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        __ n.. A:
            r.. False

        last_at = l..(A) - 1

        ___ i __ r..(last_at, -1, -1):
            __ i + A[i] >= last_at:
                last_at = i

        r.. last_at __ 0


"""
DP
"""
class Solution:
    ___ canJump(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        __ n.. A:
            r.. False

        n = l..(A)
        dp = [False] * n

        """
        `dp[i]` means `i` could be reached
        """
        dp[0] = True

        ___ i __ r..(1, n):
            ___ j __ r..(i):
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

        r.. dp[n - 1]
