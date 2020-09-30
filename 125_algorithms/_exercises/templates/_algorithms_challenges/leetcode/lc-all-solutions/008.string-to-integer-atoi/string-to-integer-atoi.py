class Solution(object
  ___ myAtoi(self, s
    """
    :type str: str
    :rtype: int
    """
    s = s.strip()
    sign = 1
    __ not s:
      r_ 0
    __ s[0] __ ["+", "-"]:
      __ s[0] __ "-":
        sign = -1
      s = s[1:]
    ans = 0
    ___ c __ s:
      __ c.isdigit(
        ans = ans * 10 + int(c)
      ____
        break
    ans *= sign
    __ ans > 2147483647:
      r_ 2147483647
    __ ans < -2147483648:
      r_ -2147483648
    r_ ans
