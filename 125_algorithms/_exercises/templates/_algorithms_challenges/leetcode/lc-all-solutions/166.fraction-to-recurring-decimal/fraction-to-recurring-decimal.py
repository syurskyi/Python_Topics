class Solution(object):
  ___ fractionToDecimal(self, numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    ans = "-" __ numerator * denominator < 0 else ""
    numerator = abs(numerator)
    denominator = abs(denominator)
    ans += str(numerator / denominator)
    __ numerator % denominator:
      ans += "."
    numerator = (numerator % denominator) * 10
    __ numerator == 0:
      return ans
    d = {}
    res = []
    while True:
      r = numerator % denominator
      v = numerator / denominator
      __ numerator in d:
        idx = d[numerator]
        return ans + "".join(res[:idx]) + "(" + "".join(res[idx:]) + ")"
      res.append(str(v))
      __ v == 0:
        d[numerator] = len(res) - 1
        numerator *= 10
        continue
      d[numerator] = len(res) - 1
      numerator = r * 10
      __ r == 0:
        return ans + "".join(res)
    return ans + "".join(res)
