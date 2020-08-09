class Solution(object
  ___ splitLoopedString(self, strs
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    for i in range(le.(strs)):
      strs[i] = max(strs[i], strs[i][::-1])

    for i, word in enumerate(strs
      for start in [word, word[::-1]]:
        for cut in range(le.(start)):
          ans = max(ans, start[cut:] + "".join(strs[i + 1:] + strs[:i]) + start[:cut])

    r_ ans
