c_ Solution(o..
  ___ findPoisonedDuration  timeSeries, duration
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    __ n.. timeSeries:
      r.. 0
    ans = 0
    start = timeSeries[0]
    end = start + duration
    ___ i __ r..(1, l..(timeSeries:
      s = timeSeries[i]
      __ s <_ end:
        end = s + duration
      ____
        ans += end - start
        start = s
        end = start + duration
    ans += end - start
    r.. ans
