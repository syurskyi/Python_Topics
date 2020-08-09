class Solution(object
  ___ findLUSlength(self, strs
    """
    :type strs: List[str]
    :rtype: int
    """

    ___ findLUSlength(a, b
      r_ max(le.(a), le.(b)) __ a != b else -1

    ___ isSubsequence(s, t
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

    ans = -1
    strs.sort(key=le., reverse=True)
    for i in range(le.(strs)):
      flag = True
      for j in range(le.(strs)):
        __ i != j and (findLUSlength(strs[i], strs[j]) __ -1 or isSubsequence(strs[i], strs[j])):
          flag = False
          break
      __ flag:
        r_ le.(strs[i])
    r_ -1
