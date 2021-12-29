class Solution(object):
  ___ convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """

    ___ convertHelper(num, base):
      sign = ""
      __ num < 0:
        sign = "-"
      num = abs(num)
      ans = 0
      unit = 1
      w.... num:
        ans += (num % base) * unit
        num /= base
        unit *= 10
      r.. sign + s..(ans)

    r.. convertHelper(num, 7)
