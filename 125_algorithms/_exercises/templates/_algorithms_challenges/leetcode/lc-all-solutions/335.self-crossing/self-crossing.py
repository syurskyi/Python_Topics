class Solution(object
  ___ isSelfCrossing(self, x
    """
    :type x: List[int]
    :rtype: bool
    """
    __ le.(x) < 4:
      r_ False
    ___ i in range(3, le.(x)):
      __ x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
        r_ True
      __ i >= 4 and x[i - 1] __ x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
        r_ True
      __ i >= 5 and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5] and x[i] + x[i - 4] >= x[i - 2] and x[
        i - 4] <= x[i - 2]:
        r_ True
    r_ False
