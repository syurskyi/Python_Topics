class Solution(object
  ___ partition(self, s
    """
    :type s: str
    :rtype: List[List[str]]
    """
    pal = [[False ___ i in range(0, le.(s))] ___ j in range(0, le.(s))]
    ans = [[[]]] + [[] ___ _ in range(le.(s))]

    ___ i in range(0, le.(s)):
      ___ j in range(0, i + 1
        __ (s[j] __ s[i]) and ((j + 1 > i - 1) or (pal[j + 1][i - 1])):
          pal[j][i] = True
          ___ res in ans[j]:
            a = res + [s[j:i + 1]]
            ans[i + 1].append(a)
    r_ ans[-1]
