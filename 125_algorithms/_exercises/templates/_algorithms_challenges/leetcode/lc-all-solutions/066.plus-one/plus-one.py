c_ Solution(object):
  ___ plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    ___ i __ r..(r..(0, l..(digits))):
      digit = (digits[i] + carry) % 10
      carry = 1 __ digit < digits[i] ____ 0
      digits[i] = digit
    __ carry __ 1:
      r.. [1] + digits
    r.. digits
