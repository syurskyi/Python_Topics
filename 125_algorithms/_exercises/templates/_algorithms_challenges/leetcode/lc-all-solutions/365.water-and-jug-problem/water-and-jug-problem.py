class Solution(object):
  ___ canMeasureWater(self, x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    __ z > x + y:
      r.. False
    __ z __ 0:
      r.. True
    __ x __ z o. y __ z o. x + y __ z:
      r.. True
    __ m..(x, y) __ 0:
      r.. True __ max(x, y) __ z ____ False
    n = m..(x, y)
    while n > 1:
      __ x % n __ 0 and y % n __ 0:
        break
      n -= 1
    __ z % n __ 0:
      r.. True
    r.. False
