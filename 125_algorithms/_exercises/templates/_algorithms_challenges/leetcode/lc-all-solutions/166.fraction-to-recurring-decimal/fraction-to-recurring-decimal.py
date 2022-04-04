c_ Solution(o..
  ___ fractionToDecimal  numerator, denominator
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    ans = "-" __ numerator * denominator < 0 ____ ""
    numerator = abs(numerator)
    denominator = abs(denominator)
    ans += s..(numerator / denominator)
    __ numerator % denominator:
      ans += "."
    numerator = (numerator % denominator) * 10
    __ numerator __ 0:
      r.. ans
    d    # dict
    res    # list
    w... T...
      r = numerator % denominator
      v = numerator / denominator
      __ numerator __ d:
        idx = d[numerator]
        r.. ans + "".j..(res[:idx]) + "(" + "".j..(res[idx:]) + ")"
      res.a..(s..(v
      __ v __ 0:
        d[numerator] = l..(res) - 1
        numerator *= 10
        _____
      d[numerator] = l..(res) - 1
      numerator = r * 10
      __ r __ 0:
        r.. ans + "".j..(res)
    r.. ans + "".j..(res)
