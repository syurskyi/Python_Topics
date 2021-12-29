class Solution(object):
  ___ findLUSlength(self, strs):
    """
    :type strs: List[str]
    :rtype: int
    """

    ___ findLUSlength(a, b):
      r.. max(l..(a), l..(b)) __ a != b ____ -1

    ___ isSubsequence(s, t):
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

    ans = -1
    strs.sort(key=l.., r.._T..
    ___ i __ r..(l..(strs)):
      flag = True
      ___ j __ r..(l..(strs)):
        __ i != j and (findLUSlength(strs[i], strs[j]) __ -1 o. isSubsequence(strs[i], strs[j])):
          flag = False
          break
      __ flag:
        r.. l..(strs[i])
    r.. -1
