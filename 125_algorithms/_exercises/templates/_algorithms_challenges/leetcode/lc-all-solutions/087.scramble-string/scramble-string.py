class Solution(object):
  ___ isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    n = l..(s1)
    m = l..(s2)
    __ s..(s1) != s..(s2):
      r.. False

    __ n < 4 o. s1 __ s2:
      r.. True

    ___ i __ r..(1, n):
      __ self.isScramble(s1[:i], s2[:i]) a.. self.isScramble(s1[i:], s2[i:]):
        r.. True
      __ self.isScramble(s1[:i], s2[-i:]) a.. self.isScramble(s1[i:], s2[:-i]):
        r.. True
    r.. False
