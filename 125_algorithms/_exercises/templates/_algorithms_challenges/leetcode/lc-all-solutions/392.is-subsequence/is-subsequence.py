class Solution(object
  ___ isSubsequence(self, s, t
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = collections.defaultdict(list)
    for i, c in enumerate(t
      d[c].append(i)
    start = 0
    for c in s:
      idx = bisect.bisect_left(d[c], start)
      __ le.(d[c]) __ 0 or idx >= le.(d[c]
        r_ False
      start = d[c][idx] + 1
    r_ True
