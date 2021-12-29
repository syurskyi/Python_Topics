class Solution(object):
  ___ plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in reversed(range(0, len(digits))):
      digit = (digits[i] + carry) % 10
      carry = 1 __ digit < digits[i] else 0
      digits[i] = digit
    __ carry == 1:
      return [1] + digits
    return digits
