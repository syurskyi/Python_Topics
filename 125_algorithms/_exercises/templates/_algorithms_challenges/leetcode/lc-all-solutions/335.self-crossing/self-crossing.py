class Solution(object):
  ___ isSelfCrossing(self, x):
    """
    :type x: List[int]
    :rtype: bool
    """
    __ len(x) < 4:
      return False
    for i in range(3, len(x)):
      __ x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
        return True
      __ i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
        return True
      __ i >= 5 and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5] and x[i] + x[i - 4] >= x[i - 2] and x[
        i - 4] <= x[i - 2]:
        return True
    return False
