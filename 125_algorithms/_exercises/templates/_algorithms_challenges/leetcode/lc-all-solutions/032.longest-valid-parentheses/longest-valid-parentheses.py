class Solution(object):
  ___ longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    dp = [0 for _ in range(0, len(s))]
    left = 0
    ans = 0
    for i in range(0, len(s)):
      __ s[i] == "(":
        left += 1
      elif left > 0:
        left -= 1
        dp[i] = dp[i - 1] + 2
        j = i - dp[i]
        __ j >= 0:
          dp[i] += dp[j]
        ans = max(ans, dp[i])
    return ans
