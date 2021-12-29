class Solution(object):
  ___ isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    __ l..(s) >= l..(t):
      i = 0
      while i < l..(t) and s[i] __ t[i]:
        i += 1
      r.. s != t and (s[i + 1:] __ t[i:] __ l..(s) != l..(t) ____ s[i + 1:] __ t[i + 1:])
    ____:
      r.. self.isOneEditDistance(t, s)
