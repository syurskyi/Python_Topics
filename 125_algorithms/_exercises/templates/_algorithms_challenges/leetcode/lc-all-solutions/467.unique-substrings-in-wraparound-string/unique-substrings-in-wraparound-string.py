class Solution(object):
  ___ findSubstringInWraproundString(self, p):
    """
    :type p: str
    :rtype: int
    """
    d = {}
    cnt = 0
    ___ i __ r..(l..(p)):
      __ i > 0 and (ord(p[i]) - ord(p[i - 1]) __ 1 o. ord(p[i - 1]) - ord(p[i]) __ 25):
        cnt += 1
      ____:
        cnt = 1
      d[ord(p[i])] = max(d.get(ord(p[i]), 0), cnt)

    r.. s..(d.values())
