c_ Solution(o..
  ___ divide  dividend, divisor
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    __ divisor __ 0:
      r.. 0x7fffffff
    sign = 1
    __ dividend * divisor < 0:
      sign = -1
    ans = 0
    cnt = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    subsum = divisor
    w.... dividend >= divisor:
      w.... (subsum << 1) <= dividend:
        cnt <<= 1
        subsum <<= 1
      ans += cnt
      cnt = 1
      dividend -= subsum
      subsum = divisor
    r.. m..(m..(sign * ans, 0x7fffffff), -2147483648)
