c_ Solution(o..):
  ___ isSubsequence  s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = c...defaultdict(l..)
    ___ i, c __ e..(t):
      d[c].a..(i)
    start = 0
    ___ c __ s:
      idx = bisect.bisect_left(d[c], start)
      __ l..(d[c]) __ 0 o. idx >= l..(d[c]):
        r.. F..
      start = d[c][idx] + 1
    r.. T..
