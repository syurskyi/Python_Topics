class Solution(object
  ___ licenseKeyFormatting(self, S, K
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    s = S.split("-")
    s = "".join(s)
    n = le.(s)
    start = n % K
    res = []
    __ start != 0:
      res.append(s[:start].upper())
    ___ k in range(0, (le.(s) - start) / K
      res.append(s[start:start + K].upper())
      start += K
    r_ "-".join(res)
