class Solution(object):
  ___ fractionToDecimal(self, numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    ans = "-" __ numerator * denominator < 0 ____ ""
    numerator = abs(numerator)
    denominator = abs(denominator)
    ans += str(numerator / denominator)
    __ numerator % denominator:
      ans += "."
    numerator = (numerator % denominator) * 10
    __ numerator __ 0:
      r.. ans
    d = {}
    res    # list
    while True:
      r = numerator % denominator
      v = numerator / denominator
      __ numerator __ d:
        idx = d[numerator]
        r.. ans + "".join(res[:idx]) + "(" + "".join(res[idx:]) + ")"
      res.a..(str(v))
      __ v __ 0:
        d[numerator] = l..(res) - 1
        numerator *= 10
        continue
      d[numerator] = l..(res) - 1
      numerator = r * 10
      __ r __ 0:
        r.. ans + "".join(res)
    r.. ans + "".join(res)
