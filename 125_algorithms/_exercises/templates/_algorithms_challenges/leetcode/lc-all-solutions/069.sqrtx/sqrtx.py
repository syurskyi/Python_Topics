c_ Solution(o..
  ___ mySqrt  x
    """
    :type x: int
    :rtype: int
    """
    lo = 0
    hi = x
    w.... lo <_ hi:
      mid = (hi + lo) // 2
      v = mid * mid
      __ v < x:
        lo = mid + 1
      ____ v > x:
        hi = mid - 1
      ____
        r.. mid
    r.. hi
