class Solution(object
  ___ isMatch(self, s, p
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp = [[False] * (le.(p) + 1) ___ _ in range(le.(s) + 1)]
    dp[0][0] = True
    ___ j in range(1, le.(p) + 1
      __ p[j - 1] __ "*":
        dp[0][j] = dp[0][j - 2]

    ___ i in range(1, le.(s) + 1
      ___ j in range(1, le.(p) + 1
        __ p[j - 1] != "*":
          dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] __ p[j - 1] or p[j - 1] __ ".")
        ____
          dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (p[j - 2] __ s[i - 1] or p[j - 2] __ ".")
    r_ dp[-1][-1]
