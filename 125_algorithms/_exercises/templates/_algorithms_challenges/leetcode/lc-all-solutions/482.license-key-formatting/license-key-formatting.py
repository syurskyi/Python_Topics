c_ Solution(o..
  ___ licenseKeyFormatting  S, K
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    s = S.s..("-")
    s = "".j..(s)
    n = l..(s)
    start = n % K
    res    # list
    __ start != 0:
      res.a..(s[:start].upper())
    ___ k __ r..(0, (l..(s) - start) / K
      res.a..(s[start:start + K].upper())
      start += K
    r.. "-".j..(res)
