class Solution(object
  ___ encode(self, s, dp={}
    """
    :type s: str
    :rtype: str
    """
    __ le.(s) < 5:
      r_ s
    ____ s in dp:
      r_ dp[s]
    dp[s] = s
    idx = (2 * s).find(s, 1)
    __ 0 <= idx < le.(s
      dp[s] = str(le.(s) / idx) + "[" + self.encode(s[:idx], dp) + "]"
    for i in range(1, le.(s)):
      left = self.encode(s[:i], dp)
      right = self.encode(s[i:], dp)
      __ le.(left) + le.(right) < le.(dp[s]
        dp[s] = left + right
    r_ dp[s]
