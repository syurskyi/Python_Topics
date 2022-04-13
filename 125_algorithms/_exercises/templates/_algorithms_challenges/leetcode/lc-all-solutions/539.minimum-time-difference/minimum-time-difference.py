c_ Solution(o..
  ___ findMinDifference  timePoints
    """
    :type timePoints: List[str]
    :rtype: int
    """
    ans 24 * 60
    times [0] * l..(timePoints)
    ___ i, t__ __ e..(timePoints
      h, m m.. i.., t__.s..(":"
      times[i] h * 60 + m

    times.s..()

    ___ i __ r..(l..(times) - 1
      ans m..(ans, a..(times[i] - times[i + 1]
    r.. m..(ans, 1440 - a..(times[0] - times[-1]
