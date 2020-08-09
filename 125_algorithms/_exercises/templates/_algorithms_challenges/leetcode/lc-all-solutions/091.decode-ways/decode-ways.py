class Solution(object
  ___ numDecodings(self, s
    """
    :type s: str
    :rtype: int
    """
    __ le.(s) __ 0:
      r_ 0
    dp = [0] * (le.(s) + 1)
    dp[0] = 1
    dp[1] = 0 __ s[0] __ "0" else 1
    for i in range(1, le.(s)):
      pre = int(s[i - 1])
      cur = int(s[i])
      num = pre * 10 + cur
      __ cur != 0:
        dp[i + 1] += dp[i]
      __ pre != 0 and 0 < num <= 26:
        dp[i + 1] += dp[i - 1]

    r_ dp[-1]
