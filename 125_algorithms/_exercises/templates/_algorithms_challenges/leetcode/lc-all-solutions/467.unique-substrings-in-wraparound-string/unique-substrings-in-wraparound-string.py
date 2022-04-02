c_ Solution(o..
  ___ findSubstringInWraproundString  p
    """
    :type p: str
    :rtype: int
    """
    d    # dict
    cnt = 0
    ___ i __ r..(l..(p)):
      __ i > 0 a.. (o..(p[i]) - o..(p[i - 1]) __ 1 o. o..(p[i - 1]) - o..(p[i]) __ 25
        cnt += 1
      ____:
        cnt = 1
      d[o..(p[i])] = m..(d.get(o..(p[i]), 0), cnt)

    r.. s..(d.values())
