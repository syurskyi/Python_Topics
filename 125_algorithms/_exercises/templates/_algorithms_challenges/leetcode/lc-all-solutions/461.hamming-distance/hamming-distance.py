c_ Solution(o..
  ___ hammingDistance  x, y
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x x ^ y
    y 0
    w.... x:
      y += 1
      x x & (x - 1)
    r.. y
