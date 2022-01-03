c_ Solution(object):
  ___ intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    ans = ""
    values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    literals = ["M", "D", "C", "L", "X", "V", "I"]
    ___ idx __ [0, 2, 4]:
      k = num / values[literals[idx]]
      __ = (num % values[literals[idx]]) / values[literals[idx + 2]]
      ans += k * literals[idx]
      __ __ >= 9:
        ans += literals[idx + 2] + literals[idx]
      ____ __ >= 5:
        ans += literals[idx + 1] + (__ - 5) * literals[idx + 2]
      ____ __ __ 4:
        ans += literals[idx + 2] + literals[idx + 1]
      ____:
        ans += __ * literals[idx + 2]
      num %= values[literals[idx + 2]]
    r.. ans
