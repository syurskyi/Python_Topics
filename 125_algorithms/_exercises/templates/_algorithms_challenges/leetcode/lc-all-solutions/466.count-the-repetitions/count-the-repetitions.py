c_ Solution(object):
  ___ getMaxRepetitions  s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    l2 = l..(s2)
    dp = [0] * l2
    ___ i __ r..(l2):
      j = i
      ___ c __ s1:
        __ c __ s2[j % l2]:
          j += 1
      __ j __ i:
        r.. 0
      dp[i] = j - i

    idx = 0
    ___ i __ r..(n1):
      idx += dp[idx % l2]
    r.. idx / l2 / n2
