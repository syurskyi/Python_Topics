class Solution(object):
  ___ partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    pal = [[False for i in range(0, len(s))] for j in range(0, len(s))]
    ans = [[[]]] + [[] for _ in range(len(s))]

    for i in range(0, len(s)):
      for j in range(0, i + 1):
        __ (s[j] == s[i]) and ((j + 1 > i - 1) or (pal[j + 1][i - 1])):
          pal[j][i] = True
          for res in ans[j]:
            a = res + [s[j:i + 1]]
            ans[i + 1].append(a)
    return ans[-1]
