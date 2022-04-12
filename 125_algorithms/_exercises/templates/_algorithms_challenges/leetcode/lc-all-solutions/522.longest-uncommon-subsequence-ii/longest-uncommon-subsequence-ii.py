c_ Solution(o..
  ___ findLUSlength  strs
    """
    :type strs: List[str]
    :rtype: int
    """

    ___ findLUSlength(a, b
      r.. m..(l..(a), l..(b __ a !_ b ____ -1

    ___ isSubsequence(s, t
      d c...d..(l..)
      ___ i, c __ e..(t
        d[c].a..(i)
      start 0
      ___ c __ s:
        idx b__.bisect_left(d[c], start)
        __ l..(d[c]) __ 0 o. idx >_ l..(d[c]
          r.. F..
        start d[c][idx] + 1
      r.. T..

    ans -1
    strs.s..(key=l.., r.._T..
    ___ i __ r..(l..(strs:
      flag T..
      ___ j __ r..(l..(strs:
        __ i !_ j a.. (findLUSlength(strs[i], strs[j]) __ -1 o. isSubsequence(strs[i], strs[j]:
          flag F..
          _____
      __ flag:
        r.. l..(strs[i])
    r.. -1
