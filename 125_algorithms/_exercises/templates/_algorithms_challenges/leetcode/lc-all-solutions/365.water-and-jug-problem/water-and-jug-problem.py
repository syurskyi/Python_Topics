class Solution(object
  ___ canMeasureWater(self, x, y, z
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    __ z > x + y:
      r_ False
    __ z __ 0:
      r_ True
    __ x __ z or y __ z or x + y __ z:
      r_ True
    __ min(x, y) __ 0:
      r_ True __ max(x, y) __ z else False
    n = min(x, y)
    w___ n > 1:
      __ x % n __ 0 and y % n __ 0:
        break
      n -= 1
    __ z % n __ 0:
      r_ True
    r_ False
