c_ Solution(o..
  ___ findMinDifference  timePoints
    """
    :type timePoints: List[str]
    :rtype: int
    """
    ans = 24 * 60
    times = [0] * l..(timePoints)
    ___ i, time __ e..(timePoints
      h, m = map(i.., time.s..(":"
      times[i] = h * 60 + m

    times.s..()

    ___ i __ r..(l..(times) - 1
      ans = m..(ans, abs(times[i] - times[i + 1]
    r.. m..(ans, 1440 - abs(times[0] - times[-1]
