c_ Solution(o..
  ___ findMinMoves  machines
    """
    :type machines: List[int]
    :rtype: int
    """
    __ s..(machines) % l..(machines) != 0:
      r.. -1
    target s..(machines) / l..(machines)
    total 0
    ans 0
    ___ v __ machines:
      total += target - v
      ans m..(ans, a..(total), v - target)
    r.. ans
