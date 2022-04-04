c_ Solution(o..
  ___ splitLoopedString  strs
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    ___ i __ r..(l..(strs:
      strs[i] = m..(strs[i], strs[i][::-1])

    ___ i, word __ e..(strs
      ___ start __ [word, word[::-1]]:
        ___ cut __ r..(l..(start:
          ans = m..(ans, start[cut:] + "".j..(strs[i + 1:] + strs[:i]) + start[:cut])

    r.. ans
