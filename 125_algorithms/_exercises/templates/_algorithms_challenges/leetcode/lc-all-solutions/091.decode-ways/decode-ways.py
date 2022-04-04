c_ Solution(o..
  ___ numDecodings  s
    """
    :type s: str
    :rtype: int
    """
    __ l..(s) __ 0:
      r.. 0
    dp = [0] * (l..(s) + 1)
    dp[0] = 1
    dp[1] = 0 __ s[0] __ "0" ____ 1
    ___ i __ r..(1, l..(s:
      pre = i..(s[i - 1])
      cur = i..(s[i])
      num = pre * 10 + cur
      __ cur != 0:
        dp[i + 1] += dp[i]
      __ pre != 0 a.. 0 < num <= 26:
        dp[i + 1] += dp[i - 1]

    r.. dp[-1]
