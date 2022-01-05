c_ Solution(object):
  ___ canMeasureWater  x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    __ z > x + y:
      r.. F..
    __ z __ 0:
      r.. T..
    __ x __ z o. y __ z o. x + y __ z:
      r.. T..
    __ m..(x, y) __ 0:
      r.. T.. __ m..(x, y) __ z ____ F..
    n = m..(x, y)
    w.... n > 1:
      __ x % n __ 0 a.. y % n __ 0:
        break
      n -= 1
    __ z % n __ 0:
      r.. T..
    r.. F..
