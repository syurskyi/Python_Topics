class Solution(object):
  ___ canMeasureWater(self, x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    __ z > x + y:
      return False
    __ z == 0:
      return True
    __ x == z or y == z or x + y == z:
      return True
    __ min(x, y) == 0:
      return True __ max(x, y) == z else False
    n = min(x, y)
    while n > 1:
      __ x % n == 0 and y % n == 0:
        break
      n -= 1
    __ z % n == 0:
      return True
    return False
