class Solution(object
  ___ isOneEditDistance(self, s, t
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    __ le.(s) >= le.(t
      i = 0
      w___ i < le.(t) and s[i] __ t[i]:
        i += 1
      r_ s != t and (s[i + 1:] __ t[i:] __ le.(s) != le.(t) else s[i + 1:] __ t[i + 1:])
    ____
      r_ self.isOneEditDistance(t, s)
