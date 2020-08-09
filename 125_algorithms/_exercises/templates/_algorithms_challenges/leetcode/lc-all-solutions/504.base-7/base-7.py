class Solution(object
  ___ convertToBase7(self, num
    """
    :type num: int
    :rtype: str
    """

    ___ convertHelper(num, base
      sign = ""
      __ num < 0:
        sign = "-"
      num = abs(num)
      ans = 0
      unit = 1
      w___ num:
        ans += (num % base) * unit
        num /= base
        unit *= 10
      r_ sign + str(ans)

    r_ convertHelper(num, 7)
