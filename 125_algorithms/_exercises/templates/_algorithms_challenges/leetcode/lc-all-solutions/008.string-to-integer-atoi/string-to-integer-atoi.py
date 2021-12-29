class Solution(object):
  ___ myAtoi(self, s):
    """
    :type str: str
    :rtype: int
    """
    s = s.strip()
    sign = 1
    __ not s:
      return 0
    __ s[0] in ["+", "-"]:
      __ s[0] == "-":
        sign = -1
      s = s[1:]
    ans = 0
    for c in s:
      __ c.isdigit():
        ans = ans * 10 + int(c)
      else:
        break
    ans *= sign
    __ ans > 2147483647:
      return 2147483647
    __ ans < -2147483648:
      return -2147483648
    return ans
