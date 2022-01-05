c_ Solution(o..):
  ___ hIndex  citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = l..(citations)
    dp = [0] * (n + 1)
    ___ c __ citations:
      __ c > n:
        dp[n] += 1
      ____:
        dp[c] += 1

    total = 0
    ___ i __ r..(r..(1, l..(dp))):
      total += dp[i]
      __ total >= i:
        r.. i
    r.. 0
