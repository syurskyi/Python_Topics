c_ Solution(o..
  ___ addBoldTag  s, d..
    """
    :type s: str
    :type dict: List[str]
    :rtype: str
    """
    intervals    # list
    ans    # list
    ___ word __ d..:
      start 0
      loc s.f.. word, start)
      w.... loc !_ -1:
        intervals.a..([loc, loc + l..(word) - 1])
        start loc + 1
        loc s.f.. word, start)

    intervals merge(intervals)
    d    # dict
    ___ start, end __ intervals:
      d[start] end
    i 0
    w.... i < l..(s
      __ i __ d:
        ans.a..("<b>{}</b>".f..(s[i:d[i] + 1]
        i d[i] + 1
      ____
        ans.a..(s[i])
        i += 1
    r.. "".j..(ans)

  ___ merge  intervals
    ans    # list
    ___ intv __ s..(intervals, k.._l.... x: x[0]
      __ ans a.. ans[-1][1] + 1 >_ intv[0]:
        ans[-1][1] m..(ans[-1][1], intv[1])
      ____
        ans += intv,
    r.. ans
