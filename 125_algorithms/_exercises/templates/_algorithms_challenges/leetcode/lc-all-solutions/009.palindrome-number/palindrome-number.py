class Solution(object
  # normal way
  ___ _isPalindrome(self, x
    """
    :type x: int
    :rtype: bool
    """
    z = x
    y = 0
    w___ x > 0:
      y = y * 10 + x % 10
      x /= 10
    r_ z __ y

  # faster way
  ___ isPalindrome(self, x
    """
    :type x: int
    :rtype: bool
    """
    __ x < 0 or (x != 0 and x % 10 __ 0
      r_ False
    half = 0
    w___ x > half:
      half = half * 10 + x % 10
      x /= 10
    r_ x __ half or half / 10 __ x
