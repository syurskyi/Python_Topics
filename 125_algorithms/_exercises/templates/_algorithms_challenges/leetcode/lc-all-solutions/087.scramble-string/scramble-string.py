c_ Solution(object):
  ___ isScramble  s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    n = l..(s1)
    m = l..(s2)
    __ s..(s1) != s..(s2):
      r.. F..

    __ n < 4 o. s1 __ s2:
      r.. T..

    ___ i __ r..(1, n):
      __ isScramble(s1[:i], s2[:i]) a.. isScramble(s1[i:], s2[i:]):
        r.. T..
      __ isScramble(s1[:i], s2[-i:]) a.. isScramble(s1[i:], s2[:-i]):
        r.. T..
    r.. F..
