class Solution(object):
  # normal way
  ___ _isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    z = x
    y = 0
    while x > 0:
      y = y * 10 + x % 10
      x /= 10
    r.. z __ y

  # faster way
  ___ isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    __ x < 0 o. (x != 0 and x % 10 __ 0):
      r.. False
    half = 0
    while x > half:
      half = half * 10 + x % 10
      x /= 10
    r.. x __ half o. half / 10 __ x
