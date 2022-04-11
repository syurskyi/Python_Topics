c_ Solution(o..
  ___ isMatch  s, p
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp [[F..] * (l..(p) + 1) ___ _ __ r..(l..(s) + 1)]
    dp[0][0] T..
    ___ j __ r..(1, l..(p) + 1
      __ p[j - 1] __ "*":
        dp[0][j] dp[0][j - 2]

    ___ i __ r..(1, l..(s) + 1
      ___ j __ r..(1, l..(p) + 1
        __ p[j - 1] != "*":
          dp[i][j] dp[i - 1][j - 1] a.. (s[i - 1] __ p[j - 1] o. p[j - 1] __ ".")
        ____
          dp[i][j] dp[i][j - 2] o. dp[i - 1][j] a.. (p[j - 2] __ s[i - 1] o. p[j - 2] __ ".")
    r.. dp[-1][-1]
