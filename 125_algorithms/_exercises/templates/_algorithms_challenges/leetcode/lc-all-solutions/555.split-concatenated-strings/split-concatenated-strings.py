class Solution(object):
  ___ splitLoopedString(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    ___ i __ r..(l..(strs)):
      strs[i] = max(strs[i], strs[i][::-1])

    ___ i, word __ enumerate(strs):
      ___ start __ [word, word[::-1]]:
        ___ cut __ r..(l..(start)):
          ans = max(ans, start[cut:] + "".join(strs[i + 1:] + strs[:i]) + start[:cut])

    r.. ans
