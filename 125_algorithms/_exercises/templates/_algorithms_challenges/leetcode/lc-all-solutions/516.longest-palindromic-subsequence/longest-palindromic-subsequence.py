c_ Solution(object):
  ___ longestPalindromeSubseq(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = l..(s)
    dp = [1] * n
    ___ j __ r..(1, l..(s)):
      pre = dp[j]
      ___ i __ reversed(r..(0, j)):
        tmp = dp[i]
        __ s[i] __ s[j]:
          dp[i] = 2 + pre __ i + 1 <= j - 1 ____ 2
        ____:
          dp[i] = max(dp[i + 1], dp[i])
        pre = tmp
    r.. dp[0]
