class Solution(object
  ___ isScramble(self, s1, s2
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    n = le.(s1)
    m = le.(s2)
    __ sorted(s1) != sorted(s2
      r_ False

    __ n < 4 or s1 __ s2:
      r_ True

    for i in range(1, n
      __ self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]
        r_ True
      __ self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]
        r_ True
    r_ False
