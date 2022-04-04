c_ Solution(o..
  ___ convertToBase7  num
    """
    :type num: int
    :rtype: str
    """

    ___ convertHelper(num, base
      sign = ""
      __ num < 0:
        sign = "-"
      num = a..(num)
      ans = 0
      unit = 1
      w.... num:
        ans += (num % base) * unit
        num /= base
        unit *= 10
      r.. sign + s..(ans)

    r.. convertHelper(num, 7)
