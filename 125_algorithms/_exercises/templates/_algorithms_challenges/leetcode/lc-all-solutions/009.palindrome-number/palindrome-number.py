c_ Solution(o..
  # normal way
  ___ _isPalindrome  x
    """
    :type x: int
    :rtype: bool
    """
    z x
    y 0
    w.... x > 0:
      y y * 10 + x % 10
      x /= 10
    r.. z __ y

  # faster way
  ___ isPalindrome  x
    """
    :type x: int
    :rtype: bool
    """
    __ x < 0 o. (x !_ 0 a.. x % 10 __ 0
      r.. F..
    half 0
    w.... x > half:
      half half * 10 + x % 10
      x /= 10
    r.. x __ half o. half / 10 __ x
