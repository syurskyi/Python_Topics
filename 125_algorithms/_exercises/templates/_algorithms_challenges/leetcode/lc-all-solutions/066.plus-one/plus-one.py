class Solution(object
  ___ plusOne(self, digits
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    ___ i in reversed(range(0, le.(digits))):
      digit = (digits[i] + carry) % 10
      carry = 1 __ digit < digits[i] else 0
      digits[i] = digit
    __ carry __ 1:
      r_ [1] + digits
    r_ digits
