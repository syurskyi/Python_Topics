class Solution(object):
  ___ findLUSlength(self, strs):
    """
    :type strs: List[str]
    :rtype: int
    """

    ___ findLUSlength(a, b):
      return max(len(a), len(b)) __ a != b else -1

    ___ isSubsequence(s, t):
      d = collections.defaultdict(list)
      for i, c in enumerate(t):
        d[c].append(i)
      start = 0
      for c in s:
        idx = bisect.bisect_left(d[c], start)
        __ len(d[c]) == 0 or idx >= len(d[c]):
          return False
        start = d[c][idx] + 1
      return True

    ans = -1
    strs.sort(key=len, reverse=True)
    for i in range(len(strs)):
      flag = True
      for j in range(len(strs)):
        __ i != j and (findLUSlength(strs[i], strs[j]) == -1 or isSubsequence(strs[i], strs[j])):
          flag = False
          break
      __ flag:
        return len(strs[i])
    return -1
