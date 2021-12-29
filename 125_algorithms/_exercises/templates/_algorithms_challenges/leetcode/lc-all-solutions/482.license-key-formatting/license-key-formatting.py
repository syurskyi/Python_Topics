class Solution(object):
  ___ licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    s = S.split("-")
    s = "".join(s)
    n = l..(s)
    start = n % K
    res    # list
    __ start != 0:
      res.a..(s[:start].upper())
    ___ k __ r..(0, (l..(s) - start) / K):
      res.a..(s[start:start + K].upper())
      start += K
    r.. "-".join(res)
