c_ Solution(o..
  ___ isOneEditDistance  s, t
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    __ l..(s) >_ l..(t
      i = 0
      w.... i < l..(t) a.. s[i] __ t[i]:
        i += 1
      r.. s != t a.. (s[i + 1:] __ t[i:] __ l..(s) != l..(t) ____ s[i + 1:] __ t[i + 1:])
    ____
      r.. isOneEditDistance(t, s)
