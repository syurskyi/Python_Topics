class Solution(object
  ___ longestPalindromeSubseq(self, s
    """
    :type s: str
    :rtype: int
    """
    n = le.(s)
    dp = [1] * n
    ___ j in range(1, le.(s)):
      pre = dp[j]
      ___ i in reversed(range(0, j)):
        tmp = dp[i]
        __ s[i] __ s[j]:
          dp[i] = 2 + pre __ i + 1 <= j - 1 else 2
        ____
          dp[i] = max(dp[i + 1], dp[i])
        pre = tmp
    r_ dp[0]
