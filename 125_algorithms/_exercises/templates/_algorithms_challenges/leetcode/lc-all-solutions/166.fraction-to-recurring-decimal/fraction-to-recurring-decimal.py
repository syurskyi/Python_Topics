class Solution(object
  ___ fractionToDecimal(self, numerator, denominator
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
    __ numerator __ 0:
      r_ ans
    d = {}
    res =   # list
    w___ True:
      r = numerator % denominator
      v = numerator / denominator
      __ numerator __ d:
        idx = d[numerator]
        r_ ans + "".join(res[:idx]) + "(" + "".join(res[idx:]) + ")"
      res.append(str(v))
      __ v __ 0:
        d[numerator] = le.(res) - 1
        numerator *= 10
        continue
      d[numerator] = le.(res) - 1
      numerator = r * 10
      __ r __ 0:
        r_ ans + "".join(res)
    r_ ans + "".join(res)
