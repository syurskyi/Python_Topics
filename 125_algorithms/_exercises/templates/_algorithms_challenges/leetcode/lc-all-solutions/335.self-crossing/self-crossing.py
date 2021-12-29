class Solution(object):
  ___ isSelfCrossing(self, x):
    """
    :type x: List[int]
    :rtype: bool
    """
    __ l..(x) < 4:
      r.. False
    ___ i __ r..(3, l..(x)):
      __ x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
        r.. True
      __ i >= 4 and x[i - 1] __ x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
        r.. True
      __ i >= 5 and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5] and x[i] + x[i - 4] >= x[i - 2] and x[
        i - 4] <= x[i - 2]:
        r.. True
    r.. False
