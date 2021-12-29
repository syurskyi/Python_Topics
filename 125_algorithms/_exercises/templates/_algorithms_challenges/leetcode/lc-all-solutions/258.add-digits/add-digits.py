class Solution(object):
  ___ addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    __ num < 10:
      return num
    return 1 + (num - 1) % 9
