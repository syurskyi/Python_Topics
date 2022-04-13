c_ Solution(o..
  ___ encode  s, dp={}
    """
    :type s: str
    :rtype: str
    """
    __ l..(s) < 5:
      r.. s
    ____ s __ dp:
      r.. dp[s]
    dp[s] s
    idx (2 * s).f.. s, 1)
    __ 0 <_ idx < l..(s
      dp[s] s..(l..(s) / idx) + "[" + encode(s[:idx], dp) + "]"
    ___ i __ r..(1, l..(s:
      left encode(s[:i], dp)
      right encode(s[i:], dp)
      __ l..(left) + l..(right) < l..(dp[s]
        dp[s] left + right
    r.. dp[s]
