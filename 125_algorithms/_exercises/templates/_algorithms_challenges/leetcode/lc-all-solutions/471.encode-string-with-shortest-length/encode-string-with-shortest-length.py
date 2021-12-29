class Solution(object):
  ___ encode(self, s, dp={}):
    """
    :type s: str
    :rtype: str
    """
    __ l..(s) < 5:
      r.. s
    ____ s __ dp:
      r.. dp[s]
    dp[s] = s
    idx = (2 * s).find(s, 1)
    __ 0 <= idx < l..(s):
      dp[s] = str(l..(s) / idx) + "[" + self.encode(s[:idx], dp) + "]"
    ___ i __ r..(1, l..(s)):
      left = self.encode(s[:i], dp)
      right = self.encode(s[i:], dp)
      __ l..(left) + l..(right) < l..(dp[s]):
        dp[s] = left + right
    r.. dp[s]
