c_ Solution(o..
  ___ isSelfCrossing  x
    """
    :type x: List[int]
    :rtype: bool
    """
    __ l..(x) < 4:
      r.. F..
    ___ i __ r..(3, l..(x:
      __ x[i] >= x[i - 2] a.. x[i - 1] <= x[i - 3]:
        r.. T..
      __ i >= 4 a.. x[i - 1] __ x[i - 3] a.. x[i] + x[i - 4] >= x[i - 2]:
        r.. T..
      __ i >= 5 a.. x[i - 1] <= x[i - 3] a.. x[i - 3] <= x[i - 1] + x[i - 5] a.. x[i] + x[i - 4] >= x[i - 2] a.. x[
        i - 4] <= x[i - 2]:
        r.. T..
    r.. F..
