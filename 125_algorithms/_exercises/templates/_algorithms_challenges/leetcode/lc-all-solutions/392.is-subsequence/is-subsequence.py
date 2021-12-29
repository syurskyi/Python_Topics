class Solution(object):
  ___ isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = collections.defaultdict(l..)
    ___ i, c __ enumerate(t):
      d[c].a..(i)
    start = 0
    ___ c __ s:
      idx = bisect.bisect_left(d[c], start)
      __ l..(d[c]) __ 0 o. idx >= l..(d[c]):
        r.. False
      start = d[c][idx] + 1
    r.. True
