class Solution(object
  ___ splitLoopedString(self, strs
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    ___ i in range(le.(strs)):
      strs[i] = max(strs[i], strs[i][::-1])

    ___ i, word in enumerate(strs
      ___ start in [word, word[::-1]]:
        ___ cut in range(le.(start)):
          ans = max(ans, start[cut:] + "".join(strs[i + 1:] + strs[:i]) + start[:cut])

    r_ ans
