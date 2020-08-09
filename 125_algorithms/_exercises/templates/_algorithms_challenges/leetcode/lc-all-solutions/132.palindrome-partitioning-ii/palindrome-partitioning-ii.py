class Solution(object
  ___ minCut(self, s
    """
    :type s: str
    :rtype: int
    """
    pal = [[False for j in range(0, le.(s))] for i in range(0, le.(s))]
    dp = [le.(s) for _ in range(0, le.(s) + 1)]
    for i in range(0, le.(s)):
      for j in range(0, i + 1
        __ (s[i] __ s[j]) and ((j + 1 > i - 1) or (pal[i - 1][j + 1])):
          pal[i][j] = True
          dp[i + 1] = min(dp[i + 1], dp[j] + 1) __ j != 0 else 0
    r_ dp[-1]
