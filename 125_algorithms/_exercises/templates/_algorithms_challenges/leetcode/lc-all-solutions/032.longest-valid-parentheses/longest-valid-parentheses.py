class Solution(object
  ___ longestValidParentheses(self, s
    """
    :type s: str
    :rtype: int
    """
    dp = [0 ___ _ in range(0, le.(s))]
    left = 0
    ans = 0
    ___ i in range(0, le.(s)):
      __ s[i] __ "(":
        left += 1
      ____ left > 0:
        left -= 1
        dp[i] = dp[i - 1] + 2
        j = i - dp[i]
        __ j >= 0:
          dp[i] += dp[j]
        ans = max(ans, dp[i])
    r_ ans
